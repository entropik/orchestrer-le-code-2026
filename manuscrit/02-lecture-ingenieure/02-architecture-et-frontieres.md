# B02 - Organiser l'architecture et les responsabilités

> Lecture ingénieure · Chapitre rédigé.

[Sommaire](../SOMMAIRE.md) · [Lire la version accessible](../01-lecture-accessible/02-architecture-et-frontieres.md) · [Fiche de rédaction](../../tranches/B02-architecture-et-frontieres.md)

## Ce que tu sauras faire

Concevoir des modules cohérents, des ports et des adaptateurs sans ritualiser l'architecture hexagonale.

---

## Première synthèse

### 1. La profondeur des modules selon John Ousterhout

Dans son ouvrage fondamental *A Philosophy of Software Design*[^1], le professeur John Ousterhout (Université de Stanford) formule le critère mathématique et conceptuel qui sépare une architecture logicielle pérenne d'un bourbier technique : la **profondeur des modules (*Deep Modules*)**.

Dans tout système informatique d'envergure, la complexité intrinsèque est inévitable. La différence entre une conception médiocre et une architecture d'excellence réside dans la manière dont cette complexité est distribuée :
- La **mauvaise conception** disperse la complexité à travers une myriade de **modules superficiels (*Shallow Modules*)**.
- La **bonne conception** concentre et encapsule une forte complexité interne derrière une **interface publique extrêmement étroite et minimale**.

```text
COMPARAISON DE PROFONDEUR ARCHITECTURALE :

       MODULE PROFOND (Idéal pour l'IA)               MODULE SUPERFICIEL (Anti-pattern)
    ┌─────────────────────────────────────┐        ┌─────────────────────────────────────┐
    │ INTERFACE MINIMALE : 2 MÉTHODES     │        │ INTERFACE LARGE : 12 MÉTHODES       │
    │ stocker(id, flux), lire(id)         │        │ init(), config(), setBuffer(),      │
    ├─────────────────────────────────────┤        │ auth(), lock(), flush(), verify()...│
    │                                     │        ├─────────────────────────────────────┤
    │ COMPLEXITÉ INTERNE FORTE (MASQUÉE)  │        │ COMPLEXITÉ INTERNE MINIME           │
    │ • Pool de descripteurs de fichiers  │        │ (Ne fait que relayer les paramètres │
    │ • Écriture atomique avec renommage  │        │  vers un autre sous-composant sans  │
    │ • Calcul SHA-256 à la volée         │        │  véritable transformation)          │
    │ • Retry exponentiel sur verrouillage│        │                                     │
    │ • Chiffrement au vol AES-256        │        └─────────────────────────────────────┘
    └─────────────────────────────────────┘
```

#### La métrique de valeur d'un module
Ousterhout modélise la valeur nette $V$ apportée par un composant comme le rapport entre la complexité fonctionnelle qu'il prend en charge ($C_{interne}$) et le coût cognitif imposé par son interface publique ($C_{interface}$) :

$$V = \frac{C_{interne}}{C_{interface}}$$

Un module profond maximise $V$ en offrant une interface $C_{interface}$ minuscule pour une puissance opérationnelle $C_{interne}$ maximale. À l'inverse, un module superficiel expose une interface presque aussi complexe que son code interne ($V \approx 1$) : il impose une taxe cognitive sans masquer aucun détail d'implémentation.

#### Pourquoi ce principe est vital face à un agent de code IA
Les modèles de langage (LLM) s'égarent dès qu'ils doivent naviguer dans des architectures « superficielles ». Lorsqu'un traitement élémentaire exige de traverser quinze micro-fichiers de dix lignes chacun (des contrôleurs passe-plats, des convertisseurs triviaux, des interfaces redondantes), l'agent sature rapidement sa fenêtre d'attention (*Context Dilution*), hallucine des signatures de fonctions et produit des erreurs d'assemblage en cascade.

En imposant des **modules profonds**, l'architecte fournit à l'agent un point d'appui inébranlable : le modèle peut remanier l'intégralité de la tuyauterie interne d'un module sans risquer de corrompre le reste du système, car la surface de contact publique demeure microscopique et inviolable.

[^1]: John Ousterhout, *A Philosophy of Software Design*, Yaknyam Press, 2018.

---

### 2. Anatomie d'une interface minimale

Pour qu'un module profond serve de rempart efficace au sein du [Harnais](../03-annexes/05-glossaire.md#harnais), son interface publique doit respecter quatre exigences formelles :

1. **L'omniprésence des valeurs par défaut sensées** : L'interface doit répondre à 95 % des cas d'usage nominaux sans obliger l'appelant à renseigner dix arguments optionnels de configuration.
2. **L'étanchéité des exceptions (Pas de fuite d'abstraction)** : Un module de stockage ne doit jamais laisser s'échapper une exception technique brute (comme un `sqlite3.OperationalError` ou un `FileNotFoundError`). Il capture les erreurs du sous-système et émet exclusivement des exceptions de domaine typées et documentées (ex. `DocumentIntrouvableErreur`, `QuotaStockageDepasseErreur`).
3. **L'absence d'état temporel occulte (*Statelessness*)** : Une méthode ne doit jamais exiger qu'une autre méthode ait été exécutée auparavant dans un ordre implicite non imposé par le système de types (proscription absolue du motif `module.initialiser()` puis `module.traiter()`).
4. **L'immutabilité des paramètres** : Les structures de données transmises en argument à une interface ne doivent jamais être modifiées sur place (*in-place mutation*). Tout effet de bord masqué détruit la testabilité déterministe.

---

### 3. Les Points de Couture (Seams) de Michael Feathers

Dans son traité classique *Working Effectively with Legacy Code*[^2], Michael Feathers définit un **Point de Couture (*Seam*)** comme :
> *« Un endroit d'un programme où l'on peut altérer un comportement sans avoir à modifier le code source situé à cet endroit. »*

Pour l'architecte supervisant des agents IA, les points de couture constituent les **charnières de testabilité et d'isolation** indispensables pour faire valider le code généré sans dépendre de l'infrastructure réelle :

```text
LES TROIS TYPES DE POINTS DE COUTURE :

1. OBJECT SEAM (Polymorphisme & Injection)
   Le domaine reçoit une interface abstraite (Protocol) au lieu d'instancier
   directement une classe concrète. Permet de substituer une base PostgreSQL
   par un stockage mémoire ultra-rapide pendant les tests de l'agent.

2. LINK SEAM (Résolution au moment du chargement)
   L'interception s'opère sur le résolveur de modules (sys.path en Python,
   module-alias en Node.js). Permet de court-circuiter un SDK tiers (Stripe,
   SendGrid) par un simulateur local sans toucher au code métier.

3. PREPROCESSING SEAM (Configuration & Drapeaux d'environnement)
   Activation conditionnelle de sondes télémétriques précises lors des phases
   autonomes de diagnostic d'incident (/diagnosing-bugs).
```

L'Object Seam est le fondement même du découpage propre : il permet au harnais d'exécuter l'oracle de test en un dixième de seconde sur la machine locale, sans réseau ni base de données active.

[^2]: Michael Feathers, *Working Effectively with Legacy Code*, Prentice Hall, 2004.

---

### 4. Domain-Driven Design : Entités, Objets-Valeurs et Agrégats

Le *Domain-Driven Design* (DDD), théorisé par Eric Evans[^3], fournit la grammaire formelle pour empêcher l'agent de dissoudre la logique métier dans des dictionnaires non typés :

| Concept DDD | Définition Sémantique | Règle d'or d'implémentation pour l'Agent |
|---|---|---|
| **Objet-Valeur (*Value Object*)** | Objet immuable défini strictement par la totalité de ses attributs. Ne possède aucun identifiant propre. Deux objets avec les mêmes attributs sont strictement égaux. | Instancié par une méthode de fabrique qui valide les [Invariants](../03-annexes/05-glossaire.md#invariant) (ex. `Email.creer("test@domaine.com")`, `MontantTTC.de_centimes(1200)`). Champs gelés (`frozen=True`). |
| **Entité (*Entity*)** | Objet défini par une identité continue qui traverse le temps, indépendamment des mutations de ses attributs. | Possède un identifiant immuable unique (UUIDv7, NanoID). Ses mutations s'effectuent par des méthodes explicites (`commande.marquer_payee()`), jamais par assignation directe de champs publics. |
| **Agrégat (*Aggregate*)** | Grappe d'entités et d'objets-valeurs traitée comme une unité cohérente pour toute modification d'état. Délimite une frontière transactionnelle étanche. | Accessible exclusivement via sa **Racine d'Agrégat (*Aggregate Root*)**. Aucun composant extérieur n'a le droit de modifier directement un élément intérieur sans passer par la racine. |

[^3]: Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*, Addison-Wesley, 2003.

---

### 5. L'Architecture Hexagonale sans dogmatisme

Conçue par Alistair Cockburn, l'architecture hexagonale (dite *Ports & Adaptateurs*) protège le domaine souverain contre l'obsolescence et la volatilité des technologies extérieures :

```text
                        TOPOLOGIE HEXAGONALE DU SYSTÈME :

     [ REQUÊTE HTTP ]          [ APPEL CLI ]          [ WEBHOOK TIERS ]
            │                        │                        │
            ▼                        ▼                        ▼
     ┌────────────────────────────────────────────────────────────────┐
     │ ADAPTATEURS PRIMAIRES (Driving Adapters)                       │
     │ Fastify, Flask, CLI Parser : Traduisent le transport en appel. │
     └───────────────────────────────┬────────────────────────────────┘
                                     │
                                     ▼
     ┌────────────────────────────────────────────────────────────────┐
     │ PORTS D'ENTRÉE (Inbound Ports / Use Cases)                     │
     │ Contrat formel du scénario métier (ex. TraiterDocumentUseCase) │
     └───────────────────────────────┬────────────────────────────────┘
                                     │
                                     ▼
     ┌────────────────────────────────────────────────────────────────┐
     │ CŒUR DE DOMAINE (Domain Core)                                  │
     │ Entités, Objets-Valeurs, Invariants : RÈGLES PURES             │
     │ (Zéro import vers SQL, Flask, AWS ou le disque)                │
     └───────────────────────────────┬────────────────────────────────┘
                                     │
                                     ▼
     ┌────────────────────────────────────────────────────────────────┐
     │ PORTS DE SORTIE (Outbound Ports)                               │
     │ Interfaces abstraites (Protocol) : IStockageFichiers, IHorloge │
     └───────────────────────────────┬────────────────────────────────┘
                                     │
                     ┌───────────────┴───────────────┐
                     ▼                               ▼
     ┌──────────────────────────────┐ ┌──────────────────────────────┐
     │ ADAPTATEUR CONCRET DISQUE    │ │ ADAPTATEUR MÉMOIRE (TEST)    │
     │ (Production : Système hôte)  │ │ (CI & Harnais d'agent : 2ms) │
     └──────────────────────────────┘ └──────────────────────────────┘
```

#### La règle absolue des dépendances
Toutes les flèches de dépendance pointent vers le centre :
- Le Domaine ne dépend d'aucun paquet tiers, d'aucun moteur de base de données, d'aucun framework web.
- L'Infrastructure dépend du Domaine (elle implémente les interfaces définies par les [Ports](../03-annexes/05-glossaire.md#port)).
- Un changement de technologie (passer de fichiers locaux à un bucket S3, ou de SQLite à PostgreSQL) se cantonne à écrire un nouvel adaptateur sans toucher à une seule ligne du Domaine.

---

## Mise en pratique

### Définir un Port de stockage et deux adaptateurs substituables en Python 3.11

Voici l'implémentation de référence démontrant l'usage des `Protocol` de Python pour définir un point de couture pur. Le domaine ignore totalement la manière dont les octets sont enregistrés :

```python
"""Module de domaine & infrastructure : Démonstration Ports & Adaptateurs.

Illustre la substitution complète d'un adaptateur de production (fichiers)
par un adaptateur de test en mémoire (in-memory) sans altérer le domaine.
"""
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol
import hashlib


# ============================================================================
# 1. LE DOMAINE (Objets-Valeurs, Exceptions et Port de Sortie)
# ============================================================================

class ErreurStockage(Exception):
    """Exception de domaine racine pour les pannes de persistance."""
    pass


class DocumentIntrouvable(ErreurStockage):
    """Émise lorsqu'un document requis n'existe pas dans le référentiel."""
    pass


@dataclass(frozen=True)
class EmpreinteDocument:
    identifiant: str
    sha256: str
    taille_octets: int


class PortStockage(Protocol):
    """Le Port de sortie : Contrat abstrait d'infrastructure."""

    def enregistrer(self, identifiant: str, donnees: bytes) -> EmpreinteDocument:
        """Enregistre le document de manière atomique et renvoie son empreinte."""
        ...

    def lire(self, identifiant: str) -> bytes:
        """Récupère le contenu binaire brut ou lève DocumentIntrouvable."""
        ...


# ============================================================================
# 2. ADAPTATEUR DE PRODUCTION (Infrastructure réelle sur système de fichiers)
# ============================================================================

class AdaptateurDisqueFichiers:
    """Adaptateur de production : persistance physique sur disque local."""

    def __init__(self, repertoire_racine: Path) -> None:
        self._racine = repertoire_racine
        self._racine.mkdir(parents=True, exist_ok=True)

    def _chemin(self, identifiant: str) -> Path:
        # Assainissement strict du chemin pour empêcher toute traversée de répertoire
        nom_nettoye = Path(identifiant).name
        return self._racine / nom_nettoye

    def enregistrer(self, identifiant: str, donnees: bytes) -> EmpreinteDocument:
        cible = self._chemin(identifiant)
        # Écriture atomique via fichier temporaire
        fichier_tmp = cible.with_suffix(".tmp")
        try:
            fichier_tmp.write_bytes(donnees)
            fichier_tmp.replace(cible)
        except OSError as err:
            raise ErreurStockage(f"Échec d'écriture physique : {err}") from err

        hash_calcul = hashlib.sha256(donnees).hexdigest()
        return EmpreinteDocument(
            identifiant=identifiant,
            sha256=hash_calcul,
            taille_octets=len(donnees),
        )

    def lire(self, identifiant: str) -> bytes:
        cible = self._chemin(identifiant)
        if not cible.is_file():
            raise DocumentIntrouvable(f"Document absent : {identifiant}")
        try:
            return cible.read_bytes()
        except OSError as err:
            raise ErreurStockage(f"Erreur d'accès I/O : {err}") from err


# ============================================================================
# 3. ADAPTATEUR DE TEST (Harnais de test in-memory ultra-rapide)
# ============================================================================

class AdaptateurMemoireTest:
    """Adaptateur éphémère pour le harnais de l'agent : ZÉRO accès disque."""

    def __init__(self) -> None:
        self._stockage: dict[str, bytes] = {}

    def enregistrer(self, identifiant: str, donnees: bytes) -> EmpreinteDocument:
        self._stockage[identifiant] = bytes(donnees)
        return EmpreinteDocument(
            identifiant=identifiant,
            sha256=hashlib.sha256(donnees).hexdigest(),
            taille_octets=len(donnees),
        )

    def lire(self, identifiant: str) -> bytes:
        if identifiant not in self._stockage:
            raise DocumentIntrouvable(f"Document absent du mock : {identifiant}")
        return self._stockage[identifiant]
```

### La suite de tests prouvant l'interchangeabilité parfaite

Cette suite unitaire vérifie que n'importe quelle brique applicative peut s'exécuter indifféremment sur l'un ou l'autre adaptateur, respectant le principe de substitution de Liskov :

```python
import tempfile
import unittest


class TestContratPortStockage(unittest.TestCase):
    """Test paramétrique vérifiant le respect strict du Port."""

    def verifier_cycle_de_vie_port(self, stockage: PortStockage) -> None:
        identifiant = "doc-contrat-001.pdf"
        contenu = b"%PDF-1.7 Contenu de preuve certifiee."

        # 1. Enregistrement
        empreinte = stockage.enregistrer(identifiant, contenu)
        self.assertEqual(empreinte.identifiant, identifiant)
        self.assertEqual(empreinte.taille_octets, len(contenu))
        self.assertNotEqual(empreinte.sha256, "")

        # 2. Lecture nominale
        lu = stockage.lire(identifiant)
        self.assertEqual(lu, contenu)

        # 3. Rejet d'un document introuvable
        with self.assertRaises(DocumentIntrouvable):
            stockage.lire("document-inexistant.pdf")

    def test_adaptateur_memoire(self) -> None:
        """Vérifie l'adaptateur de test utilisé par le harnais agentique."""
        stockage_memoire = AdaptateurMemoireTest()
        self.verifier_cycle_de_vie_port(stockage_memoire)

    def test_adaptateur_disque_physique(self) -> None:
        """Vérifie l'adaptateur de production avec isolation en répertoire temporaire."""
        with tempfile.TemporaryDirectory() as dossier_tmp:
            stockage_disque = AdaptateurDisqueFichiers(Path(dossier_tmp))
            self.verifier_cycle_de_vie_port(stockage_disque)


if __name__ == "__main__":
    unittest.main()
```

---

## Exercice d'arbitrage & Corrigé commenté

### Le cas d'ingénierie : La fuite d'abstraction dans le contrôleur

Un agent de code propose de raccorder un nouveau moyen de paiement par carte bancaire. Dans sa Pull Request, il livre le contrôleur web suivant :

```python
# Code soumis par l'agent (Anti-pattern de couplage fort) :
import stripe
from app.config import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY

def encaisser_commande_api(commande_id: str, montant_centimes: int, token_carte: str):
    try:
        charge = stripe.Charge.create(
            amount=montant_centimes,
            currency="eur",
            source=token_carte,
            description=f"Commande {commande_id}",
        )
        return {"statut": "SUCCES", "transaction": charge.id}
    except stripe.error.CardError as err:
        return {"statut": "REFUS", "code": err.code}
```

### La grille d'audit de l'architecte

1. **Où réside la dépendance ?** : Le contrôleur d'entrée dépend directement du SDK tiers `stripe`. Impossible de tester ce contrôleur sans disposer d'une clé API Stripe valide ou de dépendre de leur serveur sandbox externe.
2. **Quid de la portabilité ?** : Si l'entreprise décide demain de router 30 % des flux vers un opérateur local ou un terminal bancaire alternatif, tout le contrôleur doit être réécrit.
3. **Absence de module profond** : Le composant ne masque rien. C'est une coquille superficielle autour d'un appel réseau tiers.

### Le corrigé commenté

**Décision de l'architecte** : Refus de la PR avec instruction de refactoring selon le modèle [Port](../03-annexes/05-glossaire.md#port) / Adaptateur :

```text
CONSIGNE DE REFACTORING ARCHITECTURAL :
1. Définir un Port de domaine pur :
   class PortPasserellePaiement(Protocol):
       def debiter(self, montant: MontantEuros, jeton: JetonPaiement) -> ResultatPaiement: ...

2. Isoler le SDK Stripe dans un Adaptateur d'infrastructure dédié :
   infrastructure/paiement/adaptateur_stripe.py

3. Créer immédiatement l'adaptateur de test en mémoire :
   infrastructure/paiement/adaptateur_paiement_simulation.py

4. Réécrire le cas d'usage applicatif pour qu'il reçoive le PortPasserellePaiement
   par injection de dépendances. Aucun import de 'stripe' n'est toléré hors du dossier infrastructure/.
```

---

## Checklist réflexe du pilote

Avant de valider une refonte architecturale proposée par un agent, contrôle ces six critères d'ingénierie :

- [ ] **Les modules sont profonds** : Chaque composant résout une complexité substantielle derrière une interface de contact réduite à son strict minimum.
- [ ] **Le domaine est agnostique** : Le répertoire de logique métier ne contient aucun import d'infrastructure (pas de SQL, pas de pilote AWS, pas de client HTTP).
- [ ] **Les points de couture existent** : Tous les services externes (disque, base, courriel, passerelle de paiement) sont modélisés par des [Ports](../03-annexes/05-glossaire.md#port) abstraits (`Protocol`).
- [ ] **Les tests tournent hors ligne** : L'intégralité de la suite de tests unitaires peut s'exécuter en mode déconnecté sur une machine vierge en moins de deux secondes grâce aux adaptateurs mémoire.
- [ ] **Les erreurs sont typées** : Aucune exception brute de bibliothèque externe ne franchit la frontière du domaine sans être traduite en erreur métier compréhensible.
- [ ] **La structure est un monolithe modulaire** : Les responsabilités sont séparées par des répertoires étanches, sans éclatement artificiel en micro-services distribués.

---

## Sources et limites

Ce chapitre approfondit les principes majeurs de l'architecture logicielle moderne :
- **O-MD §1 et §2** ([Manuel d'Orchestration Logicielle](../../sources/originaux/manuel_orchestration_logicielle.md)) : Les quatre couches applicatives, la doctrine du monolithe modulaire et l'inversion des dépendances.
- **I-MD §2** ([Manuel d'Ingénierie Logicielle](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md)) : La métrique de profondeur des modules de John Ousterhout, les points de couture (*Seams*) de Michael Feathers et les agrégats du Domain-Driven Design d'Eric Evans.

Pour concevoir la formalisation des schémas d'entrée-sortie et le typage invariant avant l'écriture algorithmique, poursuis vers le chapitre suivant : **[B03 — Transformer le besoin en contrat vérifiable](../02-lecture-ingenieure/03-besoin-et-contrats.md)**. Pour réviser les concepts sans syntaxe de programmation, consulte le miroir accessible : **[A02 — Organiser l'architecture et les responsabilités](../01-lecture-accessible/02-architecture-et-frontieres.md)**.
