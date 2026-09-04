{
  "title": "Transformer le besoin en contrat vérifiable",
  "description": "Relier invariants, schémas, validation à l'exécution et compatibilité des contrats.",
  "weight": 3,
  "chapter_id": "B03",
  "theme": "03",
  "status": "redaction",
  "source_path": "manuscrit/02-lecture-ingenieure/03-besoin-et-contrats.md",
  "mirror": "/accessible/03-besoin-et-contrats",
  "related": [
    "/ingenieure/02-architecture-et-frontieres",
    "/ingenieure/06-tests-et-preuves"
  ],
  "notions": [
    {
      "label": "Contrat",
      "anchor": "contrat"
    },
    {
      "label": "Invariant",
      "anchor": "invariant"
    },
    {
      "label": "API",
      "anchor": "api"
    }
  ],
  "previous": "/ingenieure/02-architecture-et-frontieres",
  "next": "/ingenieure/04-harnais-et-contexte"
}

## Ce que tu sauras faire

Relier invariants, schémas, validation à l'exécution et compatibilité des contrats.

---

## Première synthèse

### 1. L'illusion du typage statique pur aux frontières I/O

Dans l'ingénierie logicielle contemporaine, l'adoption du typage statique (TypeScript en configuration stricte, Rust, Go, Python avec Mypy) est souvent perçue comme un bouclier absolu contre les défaillances. En vertu de **l'isomorphisme de Curry-Howard**[^1], un type statique équivaut à une proposition logique formelle, et le corps de la fonction constitue la preuve constructive de cette proposition. Si le code compile, la preuve est mathématiquement valide.

Cependant, cette garantie s'effondre brutalement dès que le système franchit la frontière des entrées-sorties (I/O) :
- Les données transmises sur le réseau (requêtes HTTP, webhooks, messages MQTT) sont des flux d'octets bruts non typés (JSON, texte, binaire).
- En JavaScript / TypeScript, les types statiques sont totalement **effacés à la compilation (*Type Erasure*)** : à l'exécution dans le moteur V8, il ne subsiste aucun contrôle de type natif.
- En Python, les annotations de type (`typing`) sont de simples métadonnées ignorées par l'interpréteur CPython au moment de l'exécution.

```text
LE PIÈGE DE L'EFFACEMENT DE TYPE AUX FRONTIÈRES :

   [ Client Web / Tiers non maîtrisé ]
                   │  Payload JSON : {"taille_octets": "50000000"}  (une chaîne !)
                   ▼
       ┌───────────────────────┐
       │ Contrôleur applicatif │ ◄── TypeScript compile sans erreur :
       │ (interface Document)  │     "interface Document { taille_octets: number; }"
       └───────────┬───────────┘
                   │  Mais à l'exécution, 'taille_octets' est une STRING !
                   ▼
       [ Calcul de quota : taille_octets + 10 ]
                   │
                   ▼  En JS : "50000000" + 10 = "5000000010" octets !
       💥 CRASH SILENCIEUX OU CORRUPTION MÉTIER CRITIQUE
```

Faire confiance aux types statiques pour valider les frontières réseau est une faute d'ingénierie majeure. Pour immuniser un système contre les données corrompues ou malveillantes, l'architecture doit intégrer une **validation runtime hermétique aux frontières**.

[^1]: William Alvin Howard, *The formulae-as-types notion of construction*, 1969, formalisant la correspondance fondamentale entre logique intuitionniste et calcul des types.

---

### 2. Le paradigme Schema-First et la source unique de vérité

Pour éliminer toute divergence entre la documentation, le modèle statique du compilateur et la validation à l'exécution, l'ingénierie moderne adopte la discipline **Schema-First** :

1. **La Spécification Unique** : On définit le contrat sous forme de schéma déclaratif rigoureux (JSON Schema, OpenAPI 3.1, ou schéma programmatique via TypeBox, Zod ou Pydantic).
2. **La Dérivation Automatique** : Les types statiques du compilateur sont dérivés directement et exclusivement de ce schéma. Il est formellement interdit d'écrire manuellement une interface TypeScript ou une classe Python en doublon d'un schéma : le schéma est la *Single Source of Truth*.
3. **Le Rejet Précoce** : Toute charge utile ne respectant pas le schéma est interceptée et refoulée à la périphérie immédiate du système (code HTTP 400), avant même que le cœur de domaine ne soit sollicité.

```text
CYCLE SCHEMA-FIRST :

             ┌──────────────────────────────────────────────┐
             │         SCHÉMA RUNTIME UNIQUE                │
             │ (JSON Schema, OpenAPI, TypeBox, Pydantic)    │
             └──────┬────────────────────────────────┬──────┘
                    │                                │
      (Génération statique)             (Exécution dynamique)
                    ▼                                ▼
     ┌─────────────────────────────┐  ┌─────────────────────────────┐
     │ Types statiques compilateur │  │ Parseur de frontière        │
     │ (TypeScript, Mypy)          │  │ Rejet immédiat si non-conforme
     └─────────────────────────────┘  └─────────────────────────────┘
```

---

### 3. Le principe « Parse, Don't Validate »

Théorisé par Alexis King[^2], le principe **Parse, Don't Validate** enseigne qu'une fonction de vérification ne doit pas renvoyer un simple booléen `True/False` sur une donnée brute. 

#### Le piège de la validation classique
Lorsqu'un développeur écrit :
```python
def est_uuid_valide(valeur: str) -> bool: ...
```
Le reste du programme continue de manipuler une simple chaîne `str`. Dix lignes plus bas, une autre fonction recevant cette même chaîne ne peut pas savoir si elle a déjà été validée. Elle est contrainte soit de faire aveuglément confiance (risque de bug), soit de re-valider la donnée (gaspillage de cycles CPU).

#### La puissance du parsing de domaine
Le parsing consiste à consommer une donnée non structurée et à renvoyer soit une erreur explicite, soit un **type de domaine enrichi qui apporte la preuve intrinsèque de sa validité** :

$$\text{Parse} : \text{DonnéeBrute} \longrightarrow \text{Erreur} \lor \text{TypeProuvé}$$

Dès lors qu'une fonction de domaine reçoit une instance de `IdentifiantSession`, le compilateur et le système garantissent qu'il s'agit d'un UUIDv4 strictement conforme. Aucune vérification supplémentaire n'est nécessaire au sein du domaine.

[^2]: Alexis King, *Parse, don't validate*, 2019, essai de référence sur le système de types appliqué à la modélisation fonctionnelle.

---

### 4. Spécification formelle des erreurs : la norme RFC 9457

Dans une architecture distribuée opérée par des agents IA, renvoyer des erreurs informelles sous la forme `{"error": "Invalid file"}` est une cause majeure d'hallucinations et de boucles de correction infinies.

Le standard industriel moderne est la **RFC 9457** (*Problem Details for HTTP APIs*, remplaçant la RFC 7807)[^3]. Il standardise un format JSON prédictible pour décrire tout incident de manière univoque :

```json
{
  "type": "https://api.domaine.com/erreurs/quota-depasse",
  "title": "Quota de stockage dépassé",
  "status": 403,
  "detail": "Le fichier de 55 000 000 octets dépasse le plafond autorisé de 52 428 800 octets.",
  "instance": "/televersements/session-9874",
  "invalid_params": [
    {
      "name": "taille_octets",
      "reason": "La valeur 55000000 excède le maximum de 52428800 octets."
    }
  ]
}
```

Ce formalisme permet aux agents d'IA (ainsi qu'aux clients d'API) d'extraire programmatiquement le champ fautif (`invalid_params[0].name`) et d'appliquer une stratégie de compensation déterministe sans recourir au parsing heuristique de messages texte.

[^3]: RFC 9457, *Problem Details for HTTP APIs*, IETF, Standard de référence publié en juin 2023.

---

### 5. Évolution additive et compatibilité des consommateurs

Un contrat logiciel n'est pas figé dans le marbre éternel, mais ses évolutions doivent respecter les lois de **compatibilité ascendante** (dites aussi de la robustesse, dérivées de la loi de Postel[^4]) :

```text
RÈGLES D'OR DE L'ÉVOLUTION D'UN CONTRAT SANS RUPTURE :

1. EXTENSION ADDITIVE EXCLUSIVE :
   ✓ Tout nouveau champ ajouté dans une requête doit être OPTIONNEL ou disposer d'une valeur par défaut.
   ✗ Ajouter un champ obligatoire brise immédiatement tous les clients existants.

2. TOLÉRANCE AUX CHAMPS SUPERFLUS :
   ✓ Le parseur aux frontières ignore les champs inconnus non sollicités (sauf mode d'audit strict).
   ✗ Bloquer une requête sous prétexte qu'elle contient un champ inattendu interdit toute migration douce.

3. DÉPRÉCIATION PROGRAMMÉE (DEPRECATION CYCLE) :
   ✓ Un champ à supprimer doit être marqué "deprecated" dans le schéma, documenté avec sa date d'extinction,
     et conservé pendant au moins deux versions mineures avant retrait physique.
   ✗ Renommer brutalement un champ (ex. 'userId' renommé en 'customerId') brise la production.
```

[^4]: Jon Postel, *Transmission Control Protocol*, RFC 793, 1981 : *« Be liberal in what you accept, and conservative in what you send »*.

---

## Mise en pratique

### Modélisation complète d'un contrat Schema-First avec validation RFC 9457 en Python 3.11

Le code suivant implémente l'architecture complète d'un parseur de frontière pour la création de session de téléversement :
- Modélisation du domaine par des objets-valeurs immutables (`frozen=True`).
- Parseur étanche validant les types, les motifs regex et les bornes mathématiques.
- Émission d'erreurs conformes à la RFC 9457.
- Suite de tests unitaires exécutable et rigoureuse.

```python
"""Module de validation contractuelle et de parsing aux frontières.

Implémente le principe 'Parse, Don't Validate' et la RFC 9457 pour la
création d'une session de téléversement de document (50 Mo max, PDF pur).
"""
from dataclasses import dataclass
from typing import Any, Optional
import re
import unittest


# ============================================================================
# 1. LE FORMAT D'ERREUR STRUCTURÉ (RFC 9457)
# ============================================================================

@dataclass(frozen=True)
class ParametreInvalide:
    nom: str
    motif: str


@dataclass(frozen=True)
class ErreurProblemDetails:
    type_uri: str
    titre: str
    statut_http: int
    detail: str
    instance_uri: str
    parametres_invalides: tuple[ParametreInvalide, ...]

    def en_dictionnaire(self) -> dict[str, Any]:
        return {
            "type": self.type_uri,
            "title": self.titre,
            "status": self.statut_http,
            "detail": self.detail,
            "instance": self.instance_uri,
            "invalid_params": [
                {"name": p.nom, "reason": p.motif}
                for p in self.parametres_invalides
            ],
        }


class ContratViolationException(Exception):
    """Exception levée en frontière lorsqu'une payload viole le contrat."""
    def __init__(self, problem: ErreurProblemDetails) -> None:
        super().__init__(problem.detail)
        self.problem = problem


# ============================================================================
# 2. LES OBJETS-VALEURS DU DOMAINE (Validés et Invariants)
# ============================================================================

@dataclass(frozen=True)
class OrganisationId:
    valeur: str

    def __post_init__(self) -> None:
        if not re.match(r"^org-[a-z0-9]{8}$", self.valeur):
            raise ValueError(f"Identifiant organisation non conforme : {self.valeur}")


@dataclass(frozen=True)
class NomFichierPDF:
    valeur: str

    def __post_init__(self) -> None:
        if not self.valeur.lower().endswith(".pdf"):
            raise ValueError("Le fichier doit obligatoirement avoir l'extension .pdf")
        if len(self.valeur) > 255:
            raise ValueError("Nom de fichier trop long (max 255 caractères)")


@dataclass(frozen=True)
class TailleFichier:
    octets: int
    PLAFOND_OCTETS: int = 50 * 1024 * 1024  # 50 Mo = 52 428 800 octets

    def __post_init__(self) -> None:
        if self.octets <= 0:
            raise ValueError("La taille doit être strictement positive")
        if self.octets > self.PLAFOND_OCTETS:
            raise ValueError(
                f"Taille {self.octets} octets supérieure au plafond de {self.PLAFOND_OCTETS} octets"
            )


@dataclass(frozen=True)
class CommandeCreationSession:
    """Contrat de domaine interne prouvé conforme par construction."""
    organisation: OrganisationId
    nom_fichier: NomFichierPDF
    taille: TailleFichier


# ============================================================================
# 3. LE PARSEUR DE FRONTIÈRE (Parse, Don't Validate)
# ============================================================================

class ParseurContratSession:
    """Parseur runtime aux frontières : transforme une charge JSON brute en Commande."""

    @classmethod
    def parser(cls, payload_brute: Any, instance_uri: str) -> CommandeCreationSession:
        if not isinstance(payload_brute, dict):
            probleme = ErreurProblemDetails(
                type_uri="https://api.domaine.com/erreurs/format-corrompu",
                titre="Payload non JSON",
                statut_http=400,
                detail="Le corps de la requête doit être un objet JSON valide.",
                instance_uri=instance_uri,
                parametres_invalides=(),
            )
            raise ContratViolationException(probleme)

        erreurs: list[ParametreInvalide] = []

        # 1. Extraction et validation Organisation
        org_raw = payload_brute.get("organisation_id")
        org_obj: Optional[OrganisationId] = None
        if not isinstance(org_raw, str):
            erreurs.append(ParametreInvalide("organisation_id", "Champ manquant ou non chaîne"))
        else:
            try:
                org_obj = OrganisationId(org_raw)
            except ValueError as e:
                erreurs.append(ParametreInvalide("organisation_id", str(e)))

        # 2. Extraction et validation Nom de Fichier
        nom_raw = payload_brute.get("nom_fichier")
        nom_obj: Optional[NomFichierPDF] = None
        if not isinstance(nom_raw, str):
            erreurs.append(ParametreInvalide("nom_fichier", "Champ manquant ou non chaîne"))
        else:
            try:
                nom_obj = NomFichierPDF(nom_raw)
            except ValueError as e:
                erreurs.append(ParametreInvalide("nom_fichier", str(e)))

        # 3. Extraction et validation Taille en octets
        taille_raw = payload_brute.get("taille_octets")
        taille_obj: Optional[TailleFichier] = None
        # Attention : interdiction stricte de convertir implicitement une chaîne en entier !
        if not isinstance(taille_raw, int) or isinstance(taille_raw, bool):
            erreurs.append(ParametreInvalide("taille_octets", "Doit être un entier strict (pas de string ni float)"))
        else:
            try:
                taille_obj = TailleFichier(taille_raw)
            except ValueError as e:
                erreurs.append(ParametreInvalide("taille_octets", str(e)))

        if erreurs or org_obj is None or nom_obj is None or taille_obj is None:
            probleme = ErreurProblemDetails(
                type_uri="https://api.domaine.com/erreurs/contrat-invalide",
                titre="Données d'entrée non conformes au contrat",
                statut_http=400,
                detail=f"{len(erreurs)} champ(s) violent le schéma de session.",
                instance_uri=instance_uri,
                parametres_invalides=tuple(erreurs),
            )
            raise ContratViolationException(probleme)

        # Tout est prouvé : instanciation de la commande de domaine
        return CommandeCreationSession(
            organisation=org_obj,
            nom_fichier=nom_obj,
            taille=taille_obj,
        )
```

---

### La suite de tests prouvant l'étanchéité absolue du parseur

```python
class TestContratParseurFrontiere(unittest.TestCase):
    """Suite de vérification garantissant le respect de la RFC 9457 et du typage."""

    def test_parsing_nominal_succes(self) -> None:
        payload_valide = {
            "organisation_id": "org-acme1234",
            "nom_fichier": "devis-plomberie-2026.pdf",
            "taille_octets": 2_450_000,
            "champ_futur_ignore": "compatibilite_ascendante",
        }
        commande = ParseurContratSession.parser(payload_valide, "/sessions/req-001")
        self.assertEqual(commande.organisation.valeur, "org-acme1234")
        self.assertEqual(commande.nom_fichier.valeur, "devis-plomberie-2026.pdf")
        self.assertEqual(commande.taille.octets, 2_450_000)

    def test_rejet_depassement_plafond_50mo(self) -> None:
        # 55 Mo = 57 671 680 octets
        payload_trop_lourde = {
            "organisation_id": "org-acme1234",
            "nom_fichier": "catalogue-lourd.pdf",
            "taille_octets": 57_671_680,
        }
        with self.assertRaises(ContratViolationException) as ctx:
            ParseurContratSession.parser(payload_trop_lourde, "/sessions/req-002")

        pb = ctx.exception.problem
        self.assertEqual(pb.statut_http, 400)
        self.assertEqual(len(pb.parametres_invalides), 1)
        self.assertEqual(pb.parametres_invalides[0].nom, "taille_octets")
        self.assertIn("supérieure au plafond", pb.parametres_invalides[0].motif)

    def test_rejet_type_coercitif_dangereux(self) -> None:
        """Vérifie qu'une taille sous forme de chaîne '1000' est strictement rejetée."""
        payload_string_int = {
            "organisation_id": "org-acme1234",
            "nom_fichier": "rapport.pdf",
            "taille_octets": "2500000",  # String au lieu d'int
        }
        with self.assertRaises(ContratViolationException) as ctx:
            ParseurContratSession.parser(payload_string_int, "/sessions/req-003")

        pb = ctx.exception.problem
        self.assertEqual(pb.parametres_invalides[0].nom, "taille_octets")

    def test_rejet_format_non_pdf(self) -> None:
        payload_faux_format = {
            "organisation_id": "org-acme1234",
            "nom_fichier": "script_malveillant.exe",
            "taille_octets": 1024,
        }
        with self.assertRaises(ContratViolationException) as ctx:
            ParseurContratSession.parser(payload_faux_format, "/sessions/req-004")

        pb = ctx.exception.problem
        self.assertEqual(pb.parametres_invalides[0].nom, "nom_fichier")
        self.assertIn(".pdf", pb.parametres_invalides[0].motif)


if __name__ == "__main__":
    unittest.main()
```

---

## Exercice d'arbitrage & Corrigé commenté

### Le cas d'ingénierie : L'assertion de type TypeScript sur un webhook externe

Un agent de code propose la Pull Request suivante pour intégrer les webhooks de notification de signature électronique d'un tiers :

```typescript
// Code soumis par l'agent dans la PR (Anti-pattern de sécurité critique) :
import { Request, Response } from 'express';

interface SignatureWebhookPayload {
  documentId: string;
  signatureStatus: 'SIGNED' | 'REJECTED';
  timestamp: number;
}

export function handleSignatureWebhook(req: Request, res: Response) {
  // L'agent utilise une assertion de type directe :
  const payload = req.body as SignatureWebhookPayload;

  if (payload.signatureStatus === 'SIGNED') {
    marquerDocumentSigne(payload.documentId);
  }
  return res.status(200).send({ received: true });
}
```

### La grille d'audit de l'architecte

1. **L'assertion de type `as` est un mensonge pour le compilateur** : Le mot-clé `as SignatureWebhookPayload` force le compilateur TypeScript à se taire, sans exécuter la moindre vérification d'octets.
2. **Vulnérabilité aux payloads nulles ou forgées** : Si le payload reçu ne contient pas `signatureStatus` (ou contient une chaîne arbitraire `"SIGNED"` injectée par un attaquant sans validation cryptographique), l'état du document sera altéré sans contrôle.
3. **Absence de parsing d'erreur** : Si le payload est malformé, le serveur ne renvoie aucune erreur structurée permettant au prestataire d'identifier le dysfonctionnement.

### Le corrigé commenté

**Décision de l'architecte** : Rejet immédiat de la PR avec interdiction des assertions `as` sur les entrées réseau :

```text
CONSIGNE D'ARBITRAGE :
1. Bannir formellement 'as SignatureWebhookPayload'.
2. Remplacer l'interface manuelle par un schéma runtime (ex: TypeBox ou Zod).
3. Parser la charge avec 'WebhookSchema.parse(req.body)'.
4. Capturer les erreurs de parsing pour émettre une réponse HTTP 400 documentée
   avec le format RFC 9457.
5. Valider la signature cryptographique HMAC du webhook avant tout parsing de contenu.
```

---

## Checklist réflexe du pilote

Avant de valider une spécification ou une PR touchant aux contrats d'échange, contrôle ces six critères d'ingénierie :

- [ ] **Pas d'assertion aveugle (`as`)** : Aucune donnée provenant de l'extérieur n'est convertie par simple forçage de type du compilateur.
- [ ] **Validation runtime hermétique** : Toutes les entrées réseau traversent un parseur de frontière qui applique le principe *Parse, Don't Validate*.
- [ ] **Dérivation Schema-First** : Les types statiques dérivent automatiquement de schémas déclaratifs uniques servant de source de vérité.
- [ ] **Erreurs structurées RFC 9457** : Les réponses d'erreur HTTP intègrent `type`, `title`, `status`, `detail` et la liste des paramètres invalides.
- [ ] **Unités et plafonds explicites** : Les tailles sont exprimées en octets entiers stricts (pas de virgules flottantes, pas de conversion implicite de chaînes).
- [ ] **Compatibilité ascendante** : Les nouveaux champs dans les contrats existants sont strictement optionnels et les champs inconnus sont tolérés sans crash.

---

## Sources et limites

Ce chapitre approfondit les fondements du typage et de la conception de contrats aux frontières :
- **O-MD §3 et §12** ([Manuel d'Orchestration Logicielle](/references/sources/o-md)) : L'ingénierie des tranches verticales, l'expression formelle des invariants et la traçabilité des ADR.
- **I-MD §3, §9.3 et §10.2** ([Manuel d'Ingénierie Logicielle](/references/sources/i-md)) : L'échec du langage naturel, l'isomorphisme de Curry-Howard, le parsing runtime aux frontières réseau et la formalisation des erreurs selon la RFC 9457.

Pour étudier la mise en place du harnais agentique, l'isolation des contextes et la configuration des rôles de pilotage, poursuis vers le chapitre suivant : **[B04 — Structurer le contexte et le harnais d'agent](/ingenieure/04-harnais-et-contexte)**. Pour réviser la démarche sans code, consulte le miroir accessible : **[A03 — Transformer le besoin en contrat vérifiable](/accessible/03-besoin-et-contrats)**.

## Références pour approfondir

- [TypeScript — assertions de type](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions) — Les assertions de type ne vérifient pas les données à l'exécution. [Notice et chapitres associés](/references#ref-typescript).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche B03](/redaction/b03-besoin-et-contrats).
