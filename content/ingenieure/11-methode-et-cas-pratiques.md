{
  "title": "Appliquer ORCHESTRE du besoin à la résolution",
  "description": "Raccorder la méthode de pilotage ORCHESTRE aux étapes techniques et aux compétences d'ingénierie sans construire un cycle en cascade.",
  "weight": 11,
  "chapter_id": "B11",
  "theme": "11",
  "status": "valide",
  "source_path": "manuscrit/02-lecture-ingenieure/11-methode-et-cas-pratiques.md",
  "mirror": "/accessible/11-methode-et-cas-pratiques",
  "related": [
    "/ingenieure/01-piloter-un-systeme",
    "/ingenieure/06-tests-et-preuves"
  ],
  "notions": [
    {
      "label": "ADR",
      "anchor": "adr"
    },
    {
      "label": "Tranche verticale",
      "anchor": "tranche-verticale"
    },
    {
      "label": "Idempotence",
      "anchor": "idempotence"
    }
  ],
  "previous": "/ingenieure/10-exploitation-et-evolution",
  "next": "/ingenieure/12-ecosysteme-et-independance"
}

## Ce que tu sauras faire

Raccorder la méthode de pilotage ORCHESTRE aux étapes techniques et aux compétences d'ingénierie sans construire un cycle en cascade.

---

## Première synthèse

### 1. Correspondance formelle : ORCHESTRE, méthode KISS et gouvernance agentique

Dans le développement logiciel assisté par agents autonomes, l'extrême vélocité de génération de code amplifie immédiatement les erreurs de cadrage. Sans une méthode de gouvernance stricte, un agent produit en quelques minutes une masse indéchiffrable de dette technique.

L'ingénierie moderne combine deux grilles complémentaires :
1. **La méthode KISS en 6 phases séquentielles** (KISS Software Engineering Framework)[^1] qui régit le cycle de vie industriel de chaque artefact.
2. **La méthode ORCHESTRE** qui organise le contrôle cognitif, les points d'arrêt et l'arbitrage humain.

```text
MATRICE D'ALIGNEMENT DES PROTOCOLES :

  ORCHESTRE        PHASE INDUSTRIELLE   OUTIL / COMMANDE      SAS DE CONTRÔLE HUMAIN
  ─────────        ──────────────────   ────────────────      ──────────────────────
  O (Observer)     1. SPÉCIFICATION     /grill-with-docs      Audit de l'existant, gel du glossaire.
  R (Résultat)     1. SPÉCIFICATION     /to-prd               Validation des User Stories et critères.
  C (Cartographier)2. CONTRATS          /to-issues            Découpage en tranches verticales.
  H (Hypothèse)    2. CONTRATS          ADR formel (docs/adr) Choix d'architecture minimale (KISS).
  ──────────────────────────────────────────────────────────────────────────────────
  ► POINT D'ARRÊT DÉCISIONNEL : Gel mémoire (/clear), purge du contexte et handoff.
  ──────────────────────────────────────────────────────────────────────────────────
  E (Expérimenter) 3. TESTS             /tdd (Preuve rouge)   Test d'intégration à la frontière.
  S (Sécuriser)    4. IMPLÉMENTATION    /implement (Code vert)Code minimal passant le test.
  T (Tracer)       4. IMPLÉMENTATION    Git commits atomiques Historique traçable sans fichier parasite.
  R (Relire)       5. INTÉGRATION       /review (Double audit)Standards (Axe 1) & Spécification (Axe 2).
  E (Exposer)      6. LIVRAISON         Staging / Blue-Green  Canary release, surveillance SLO.
```

#### La gouvernance de la mémoire cognitive (*Smart Zone*)
Un grand modèle de langage subit une dégradation mathématique de son attention et de sa rigueur logique lorsque sa fenêtre contextuelle s'alourdit (phénomène de *Lost in the Middle* et de dérive cognitive)[^2].
- **La règle de la Smart Zone (~100k-120k tokens)** : Dès que la phase de cadrage et de spécification est terminée, l'ingénieur ne doit jamais laisser l'agent coder dans la même session polluée par des centaines d'échanges d'exploration.
- **Le protocole de Handoff** : L'ingénieur purge la session (`/clear`), scelle les décisions dans un document immuable (`PRD.md` et `docs/adr/000X.md`), et ouvre une session d'implémentation vierge dédiée exclusivement à une unique tranche verticale.

[^1]: Martin Fowler, *Patterns of Enterprise Application Architecture*, Addison-Wesley, 2002.
[^2]: Nelson F. Liu et al., *Lost in the Middle: How Language Models Use Long Contexts*, Transactions of the Association for Computational Linguistics, 2024.

---

### 2. L'architecture par tranches verticales (*Tracer Bullets*)

L'un des anti-patterns les plus destructeurs consiste à découper un projet de manière horizontale par couches techniques :
*« Étape 1 : Créer toutes les tables de la base de données. Étape 2 : Créer tous les modèles ORM. Étape 3 : Créer toutes les routes API. Étape 4 : Créer toutes les interfaces web. »*

Ce découpage en couches horizontales est incompatible avec le développement agentique : il accumule des milliers de lignes de code mort non testables de bout en bout avant la fin du projet, rendant tout diagnostic d'intégration impossible.

L'ingénierie agile impose l'approche par **tranches verticales** (*Tracer Bullets*)[^3] :

```text
DÉCOUPAGE HORIZONTAL (DANGEREUX)      TRANCHE VERTICALE (ROBUSTE)
────────────────────────────────      ───────────────────────────
[ Interface Web Complète       ]            ┌───┐
[ Contrôleurs API Globaux      ]            │ T │  Chaque tranche traverse
[ Modèles Métier Abstraits     ]            │ R │  l'UI, l'API, le Domaine
[ Schéma Base de Données Total ]            │ A │  et la Base de Données
                                            │ N │  pour un unique parcours
(Rien ne fonctionne avant la fin)           │ C │  utilisateur testable.
                                            │ H │
                                            │ E │  ► Démonstrable en Staging.
                                            └───┘
```

Chaque tranche implémente un parcours utilisateur complet et autonome, validé par un test d'intégration de frontière, avant d'aborder la tranche suivante.

[^3]: David Thomas et Andrew Hunt, *The Pragmatic Programmer: Your Journey To Mastery*, 20e anniversaire, Addison-Wesley, 2019.

---

### 3. Dossier de réalisation 1 : Upload direct multipart avec reprise

#### A. Le modèle formel de signature d'URLs éphémères
Pour permettre le transfert résilient de fichiers volumineux (jusqu'à 500 Mo) sans saturer la bande passante ni la mémoire vive de l'API centrale, l'architecture délègue le flux binaire directement à un stockage objet (compatible S3 / Cloudflare R2) :

```text
SÉQUENCE D'UPLOAD DIRECT MULTIPART AVEC REPRISE :

  Navigateur Client                 Serveur API                   Stockage Objet (S3/R2)
         │                               │                                   │
         ├── 1. POST /uploads/sessions ──►│ (Vérifie droits & quota)          │
         │   (taille: 450 Mo, checksum)  ├── 2. InitiateMultipartUpload ────►│
         │                               │◄── 3. upload_id & clés signées ───┤
         │◄── 4. session_id & URLs parts ┼                                   │
         │                                                                   │
         ├── 5. PUT Part 1 (10 Mo) ─────────────────────────────────────────►│
         ├── 6. PUT Part 2 (10 Mo) ─────────────────────────────────────────►│
         │   [ Coupure Réseau ]                                              │
         ├── 7. GET /uploads/sessions/{id}/parts ──► (Interroge les parts)  │
         │◄── 8. Parts 1 & 2 reçues ─────────────────┼                       │
         ├── 9. PUT Part 3 (10 Mo) ─────────────────────────────────────────►│
         │                                                                   │
         ├── 10. POST /uploads/sessions/{id}/finaliser ──►                   │
         │                               ├── 11. CompleteMultipartUpload ───►│
         │                               ├── 12. Vérifie somme de contrôle   │
         │                               └── 13. Émet événement DOCUMENT_RECU│
         │◄── 14. Document prêt (201) ───┼                                   │
```

#### B. La machine d'états finis du document
Pour garantir qu'aucun fichier incomplet ou non vérifié ne parvienne à l'atelier d'impression, le cycle de vie du document obéit à une machine d'états finis stricte :

$$\text{États} = \{\text{PREPARE}, \; \text{EN\_COURS}, \; \text{RECU}, \; \text{EN\_VALIDATION}, \; \text{VALIDE}, \; \text{REJETE}, \; \text{EXPIRE}\}$$

- **Invariant fondamental** : Un document ne peut passer à l'état `VALIDE` que si :
  1. Le statut précédent est strictement `RECU`.
  2. Le contrôle de conformité géométrique prepresse (dimensions physiques et fond perdu minimal de 3 mm sur chaque bord) est exécuté avec succès.
  3. L'opérateur de l'atelier ne dispose d'un accès en lecture que sur les documents à l'état `VALIDE`.

---

### 4. Dossier de réalisation 2 : Résolution déterministe d'une course critique (Doublons)

#### A. Anatomie de la vulnérabilité *Check-Then-Act* (TOCTOU)
L'anomalie des doublons de commande provient d'une fenêtre de vulnérabilité temporelle (*Time-Of-Check to Time-Of-Use*) entre la vérification de l'existence d'une commande et son insertion :

```text
INTERLEAVING TEMPOREL CRÉANT LE DOUBLON :

  Thread A (Requête 1)                              Thread B (Requête 2)
  ────────────────────                              ────────────────────
  SELECT id FROM commandes WHERE panier_id = 42;    
  (Retourne NULL : aucune commande)
                                                    SELECT id FROM commandes WHERE panier_id = 42;
                                                    (Retourne NULL : aucune commande)
  INSERT INTO commandes (panier_id, montant) ...;
  (Commit réussi : Commande #1042 créée)
                                                    INSERT INTO commandes (panier_id, montant) ...;
                                                    (Commit réussi : Commande #1043 créée !)
```

#### B. La résolution mathématique par contrainte unique et clé d'idempotence
La seule barrière inviolable repose sur le moteur de base de données relationnelle :
1. **La clé d'idempotence (`cle_idempotence`)** : Générée de manière déterministe côté client (ou dérivée de façon cryptographique du `panier_id`).
2. **L'index d'unicité composite** :
   ```sql
   ALTER TABLE commandes 
   ADD CONSTRAINT uq_commandes_organisation_idempotence 
   UNIQUE (organisation_id, cle_idempotence);
   ```
3. **L'insertion atomique avec clause de conflit** :
   ```sql
   INSERT INTO commandes (organisation_id, panier_id, cle_idempotence, montant, statut)
   VALUES ($1, $2, $3, $4, 'CREEE')
   ON CONFLICT (organisation_id, cle_idempotence)
   DO UPDATE SET updated_at = NOW() -- Empêche l'échec et récupère l'identifiant existant
   RETURNING id, statut, created_at;
   ```

---

## Mise en pratique

Le code Python 3.11 ci-dessous implémente les deux moteurs critiques du chapitre :
1. Un **Moteur de Commandes avec Idempotence et Barrière Concurrente** démontrant la neutralisation absolue des courses critiques (TOCTOU).
2. Un **Moteur d'Upload Multipart et de Contrôle Prepresse** validant la machine d'états finis du document.
3. Une **Suite de tests unitaires `unittest`** complète validant la robustesse multithreadée.

```python
"""Module d'ingénierie ORCHESTRE : Upload multipart et résolution de concurrence.

Implémente la machine d'états finis d'upload direct et la protection atomique
contre les courses critiques de commandes par clé d'idempotence.
"""

from dataclasses import dataclass
from enum import Enum
import threading
from typing import Dict, List, Optional, Set
import unittest


# ===========================================================================
# 1. GESTION DES COMMANDES & IDEMPOTENCE (RÉSOLUTION DES DOUBLONS)
# ===========================================================================

class ConcurrenceConflitErreur(Exception):
    """Levée lorsqu'une collision d'unicité est interceptée sans idempotence."""


@dataclass
class Commande:
    id: int
    organisation_id: str
    panier_id: str
    cle_idempotence: str
    montant_centimes: int


class DepôtCommandesSecurise:
    """Simule un moteur relationnel avec contrainte d'unicité stricte."""

    def __init__(self) -> None:
        self._commandes: Dict[int, Commande] = {}
        self._index_unicite: Set[tuple[str, str]] = set()  # (org_id, cle_idempotence)
        self._compteur_id: int = 1000
        self._verrou_transactionnel = threading.Lock()

    def creer_commande(
        self,
        organisation_id: str,
        panier_id: str,
        cle_idempotence: str,
        montant_centimes: int,
        barriere_concurrence: Optional[threading.Barrier] = None,
    ) -> tuple[Commande, bool]:
        """Crée une commande ou retourne l'existante selon la clé d'idempotence.

        Retourne un tuple (Commande, est_nouvelle_creation).
        """
        # Synchronisation forcée pour prouver la résistance aux courses critiques
        if barriere_concurrence is not None:
            barriere_concurrence.wait()

        with self._verrou_transactionnel:
            cle_composite = (organisation_id, cle_idempotence)

            # 1. Vérification de la contrainte d'unicité (Atomic ON CONFLICT)
            if cle_composite in self._index_unicite:
                # Récupération de l'enregistrement existant (Idempotence)
                for cmd in self._commandes.values():
                    if (
                        cmd.organisation_id == organisation_id
                        and cmd.cle_idempotence == cle_idempotence
                    ):
                        return cmd, False

            # 2. Insertion de la nouvelle commande
            self._compteur_id += 1
            nouvelle_commande = Commande(
                id=self._compteur_id,
                organisation_id=organisation_id,
                panier_id=panier_id,
                cle_idempotence=cle_idempotence,
                montant_centimes=montant_centimes,
            )
            self._commandes[nouvelle_commande.id] = nouvelle_commande
            self._index_unicite.add(cle_composite)
            return nouvelle_commande, True


# ===========================================================================
# 2. UPLOAD DIRECT MULTIPART & CONTRÔLE PREPRESSE (MACHINE D'ÉTATS)
# ===========================================================================

class StatutDocument(str, Enum):
    PREPARE = "PREPARE"
    EN_COURS = "EN_COURS"
    RECU = "RECU"
    EN_VALIDATION = "EN_VALIDATION"
    VALIDE = "VALIDE"
    REJETE = "REJETE"


class TransitionEtatInvalideErreur(Exception):
    """Levée lorsqu'une transition d'état viole le contrat du document."""


@dataclass
class MorceauUpload:
    numero_partie: int
    taille_octets: int
    checksum_md5: str


class SessionUploadDocument:
    """Orchestre la réception multipart et le contrôle géométrique prepresse."""

    def __init__(
        self,
        document_id: str,
        organisation_id: str,
        taille_totale_prevue: int,
    ) -> None:
        self.document_id = document_id
        self.organisation_id = organisation_id
        self.taille_totale_prevue = taille_totale_prevue
        self.statut = StatutDocument.PREPARE
        self.parties_recues: Dict[int, MorceauUpload] = {}

    def enregistrer_partie(self, morceau: MorceauUpload) -> None:
        """Enregistre un fragment transféré directement au stockage objet."""
        if self.statut not in (StatutDocument.PREPARE, StatutDocument.EN_COURS):
            raise TransitionEtatInvalideErreur(
                f"Impossible d'ajouter une partie à un document en état {self.statut}."
            )
        self.parties_recues[morceau.numero_partie] = morceau
        self.statut = StatutDocument.EN_COURS

    def finaliser_transfert(self) -> None:
        """Valide l'intégrité de l'assemblage après la réception de toutes les parts."""
        if self.statut != StatutDocument.EN_COURS:
            raise TransitionEtatInvalideErreur(
                "Finalisation impossible : aucun transfert en cours."
            )

        octets_recus = sum(p.taille_octets for p in self.parties_recues.values())
        if octets_recus != self.taille_totale_prevue:
            self.statut = StatutDocument.REJETE
            raise ValueError(
                f"Intégrité compromise : attendu {self.taille_totale_prevue} o, "
                f"reçu {octets_recus} o."
            )

        self.statut = StatutDocument.RECU

    def valider_prepresse(self, largeur_mm: float, hauteur_mm: float, fond_perdu_mm: float) -> bool:
        """Vérifie les contraintes géométriques indispensables à la fabrication."""
        if self.statut != StatutDocument.RECU:
            raise TransitionEtatInvalideErreur(
                f"Validation prepresse impossible : le document est en statut {self.statut}."
            )

        self.statut = StatutDocument.EN_VALIDATION

        # Règle d'atelier : Fond perdu minimal de 3.0 mm requis sur tous les bords
        if fond_perdu_mm < 3.0 or largeur_mm <= 0 or hauteur_mm <= 0:
            self.statut = StatutDocument.REJETE
            return False

        self.statut = StatutDocument.VALIDE
        return True
```

---

### La suite de tests prouvant l'idempotence et les transitions d'états

```python
class TestOrchestreCasPratiques(unittest.TestCase):
    """Suite vérifiant l'anti-collision de commandes et le cycle d'upload."""

    def test_course_critique_neutralisee_par_idempotence(self) -> None:
        """Prouve que deux requêtes strictement simultanées ne créent qu'une seule commande."""
        depot = DepôtCommandesSecurise()
        barriere = threading.Barrier(2)
        resultats: List[tuple[Commande, bool]] = []

        def client_action() -> None:
            # Même panier, même clé d'idempotence envoyée par les deux threads
            res = depot.creer_commande(
                organisation_id="org_artisan_42",
                panier_id="panier_99",
                cle_idempotence="idemp_hash_panier_99",
                montant_centimes=14500,
                barriere_concurrence=barriere,
            )
            resultats.append(res)

        t1 = threading.Thread(target=client_action)
        t2 = threading.Thread(target=client_action)

        t1.start()
        t2.start()
        t1.join()
        t2.join()

        self.assertEqual(len(resultats), 2)
        cmd1, creee1 = resultats[0]
        cmd2, creee2 = resultats[1]

        # Les deux threads reçoivent rigoureusement la même commande (même identifiant)
        self.assertEqual(cmd1.id, cmd2.id)
        # Une seule et unique création a eu lieu ; la seconde est reconnue comme existante
        self.assertTrue(creee1 ^ creee2)  # XOR strict : un True et un False

    def test_cycle_vie_upload_et_controle_prepresse(self) -> None:
        """Vérifie la machine d'états de l'upload et le rejet en cas de fond perdu insuffisant."""
        session = SessionUploadDocument(
            document_id="doc_affiches_a3",
            organisation_id="org_artisan_42",
            taille_totale_prevue=20_000_000,  # 20 Mo
        )

        # 1. Enregistrement de 2 morceaux de 10 Mo
        session.enregistrer_partie(MorceauUpload(1, 10_000_000, "md5_part1"))
        session.enregistrer_partie(MorceauUpload(2, 10_000_000, "md5_part2"))
        self.assertEqual(session.statut, StatutDocument.EN_COURS)

        # 2. Finalisation du transfert
        session.finaliser_transfert()
        self.assertEqual(session.statut, StatutDocument.RECU)

        # 3. Test de rejet prepresse : fond perdu de 1.5 mm < 3.0 mm requis
        succes = session.valider_prepresse(largeur_mm=297.0, hauteur_mm=420.0, fond_perdu_mm=1.5)
        self.assertFalse(succes)
        self.assertEqual(session.statut, StatutDocument.REJETE)


if __name__ == "__main__":
    unittest.main()
```

---

## Exercice d'arbitrage & Corrigé commenté

### Le cas d'ingénierie : La migration de schéma bloquante sous forte charge

Pour résoudre le bug des doublons sur une table de commandes en production comptant 8 millions de lignes et recevant 150 écritures par seconde, un agent soumet la Pull Request suivante :

```sql
-- Migration proposée par l'agent :
ALTER TABLE commandes 
ADD COLUMN cle_idempotence VARCHAR(64) NOT NULL,
ADD CONSTRAINT uq_commandes_cle_idempotence UNIQUE (cle_idempotence);
```

### La grille d'audit de l'architecte

1. **Verrou exclusif destructeur (`ACCESS EXCLUSIVE LOCK`)** : Ajouter une colonne `NOT NULL` sans valeur par défaut sur une table de 8 millions de lignes nécessite la réécriture complète de la table ou un verrou exclusif bloquant toutes les transactions entrantes pendant plusieurs dizaines de secondes, provoquant l'écroulement des connexions applicatives.
2. **Création d'index synchrone bloquante** : La contrainte `UNIQUE` crée un index B-Tree en verrouillant la table en écriture pendant toute la durée de son calcul.
3. **Absence de rétrocompatibilité** : Le code de l'ancienne version active en production ne connaît pas la colonne `cle_idempotence` : tout déploiement provoque un crash immédiat des requêtes d'insertion antérieures.

### Le corrigé commenté

**Décision de l'architecte** : Rejet de la Pull Request avec exigence du patron **Expand-Migrate-Contract** sans coupure :

```sql
-- Étape 1 : Ajout de la colonne NULLABLE (Verrou instantané en sub-milliseconde)
ALTER TABLE commandes ADD COLUMN cle_idempotence VARCHAR(64);

-- Étape 2 : Création de l'index unique de manière non bloquante en arrière-plan
CREATE UNIQUE INDEX CONCURRENTLY idx_commandes_org_idemp 
ON commandes (organisation_id, cle_idempotence);

-- Étape 3 : Raccordement de la contrainte formelle adossée à l'index existant
ALTER TABLE commandes 
ADD CONSTRAINT uq_commandes_idempotence 
UNIQUE USING INDEX idx_commandes_org_idemp;
```

Ce protocole s'exécute avec une disponibilité de 100 % du service et un impact de latence strictement nul sur les clients actifs.

---

## Checklist réflexe du pilote

Avant d'autoriser la mise en œuvre d'une tranche verticale ou d'un correctif d'ingénierie, valide ces six exigences :

- [ ] **La tranche traverse toutes les couches** : Le livrable fournit une preuve démontrable de bout en bout (UI, API, Domaine, Base).
- [ ] **L'agent a opéré dans la Smart Zone** : La session de génération n'a pas dépassé 120k tokens et les contextes ont été purgés via un Handoff formel.
- [ ] **Le test concurrent est sous barrière** : Toute vulnérabilité de concurrence est reproduite de manière déterministe avant écriture du correctif.
- [ ] **L'idempotence est garantie par la persistance** : La protection repose sur une contrainte d'intégrité relationnelle atomique (`ON CONFLICT`).
- [ ] **La migration respecte l'Expand-Contract** : Les index sont créés `CONCURRENTLY` sans verrou exclusif bloquant.
- [ ] **Les états métier sont hermétiques** : Les composants en aval (atelier) ne consomment que des entités à l'état strictement validé.

---

## Sources et limites

Ce chapitre s'appuie sur les standards d'ingénierie logicielle et de découpage de projets :
- **O-MD §5, §11, §12, §13 et §14** ([Manuel d'Orchestration Logicielle](/projet/references/sources/o-md)) : La méthode ORCHESTRE, le point d'arrêt, la décomposition des cas pratiques et l'analyse de cause racine.
- **I-MD §9 et §10** ([Manuel d'Ingénierie Logicielle](/projet/references/sources/i-md)) : Le cadre KISS en six phases séquentielles, la bibliothèque opérationnelle de prompts et les matrices d'audit de Pull Requests.
- [Guide des workflows agentiques](/annexes/workflows) : Formalisation des protocoles d'exécution et outillage des agents.

Pour étudier les arbitrages de souveraineté technologique, la gestion des modèles ouverts versus propriétaires, les protocoles MCP et l'optimisation du coût total de possession (TCO), poursuis vers le chapitre final : **[B12 — Choisir ses outils et préserver son indépendance](/ingenieure/12-ecosysteme-et-independance)**. Pour réviser les principes sans code, consulte le miroir accessible : **[A11 — Appliquer ORCHESTRE du besoin à la résolution](/accessible/11-methode-et-cas-pratiques)**.

## Rédaction de ce chapitre

[Objectifs et critères de la tranche B11](/redaction/b11-methode-et-cas-pratiques).
