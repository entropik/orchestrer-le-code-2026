{
  "title": "Protéger les données et faire évoluer leur structure",
  "description": "Choisir contraintes, transactions et migrations à partir des anomalies à empêcher.",
  "weight": 8,
  "chapter_id": "B08",
  "theme": "08",
  "status": "redaction",
  "source_path": "manuscrit/02-lecture-ingenieure/08-donnees-et-migrations.md",
  "mirror": "/accessible/08-donnees-et-migrations",
  "related": [
    "/ingenieure/07-asynchronisme-et-reprises",
    "/ingenieure/09-livraison-et-production"
  ],
  "notions": [
    {
      "label": "Migration",
      "anchor": "migration"
    },
    {
      "label": "RPO",
      "anchor": "rpo"
    },
    {
      "label": "RTO",
      "anchor": "rto"
    }
  ],
  "previous": "/ingenieure/07-asynchronisme-et-reprises",
  "next": "/ingenieure/09-livraison-et-production"
}

## Ce que tu sauras faire

Choisir contraintes, transactions et migrations à partir des anomalies à empêcher.

---

## Première synthèse

### 1. Niveaux d'isolation SQL et anomalies formelles de concurrence

Dans l'architecture de persistance, déléguer la gestion des données aux automatismes d'un ORM généré par un agent d'IA sans maîtriser la sémantique transactionnelle sous-jacente conduit inévitablement à des corruptions silencieuses.

Le standard ANSI SQL définit quatre niveaux d'isolation transactionnelle formels, arbitrés en fonction des anomalies mathématiques qu'ils autorisent ou interdisent[^1] :

```text
MATRICE D'ISOLATION ET D'ANOMALIES SQL :

  ┌───────────────────┬──────────────┬──────────────────────┬───────────────┬─────────────┐
  │ Niveau d'Isolation│ Dirty Reads  │ Non-Repeatable Reads │ Phantom Reads │ Write Skew  │
  ├───────────────────┼──────────────┼──────────────────────┼───────────────┼─────────────┤
  │ Read Uncommitted  │   TOLÉRÉ     │       TOLÉRÉ         │    TOLÉRÉ     │   TOLÉRÉ    │
  │ Read Committed    │   INTERDIT   │       TOLÉRÉ         │    TOLÉRÉ     │   TOLÉRÉ    │
  │ Repeatable Read   │   INTERDIT   │       INTERDIT       │   INTERDIT*   │   TOLÉRÉ    │
  │ Serializable      │   INTERDIT   │       INTERDIT       │   INTERDIT    │  INTERDIT   │
  └───────────────────┴──────────────┴──────────────────────┴───────────────┴─────────────┘
  * Note : Dans le moteur PostgreSQL, Repeatable Read utilise le MVCC (Multi-Version Concurrency
    Control) et élimine également les Phantom Reads par snapshot isolation.
```

#### Les quatre anomalies de concurrence
1. **Dirty Read (Lecture sale)** : La transaction T2 lit une modification effectuée par la transaction T1 alors que T1 n'a pas encore commité. Si T1 fait un `ROLLBACK`, T2 a fondé ses calculs sur des données imaginaires.
2. **Non-Repeatable Read (Lecture non répétable)** : La transaction T1 lit une ligne. La transaction T2 modifie cette ligne et commite. T1 relit la même ligne et constate que les valeurs ont changé au cours de sa propre transaction.
3. **Phantom Read (Lecture fantôme)** : La transaction T1 exécute une requête avec prédicat (ex: `WHERE montant > 100`). T2 insère une nouvelle ligne respectant ce critère et commite. T1 réexécute la requête et voit apparaître une ligne supplémentaire.
4. **Write Skew (Dérive d'écriture)** : Deux transactions concurrentes lisent des ensembles disjoints mais liés par un invariant global (ex: *« Au moins un médecin de garde par service »*). T1 retire le docteur A, T2 retire le docteur B. Les deux transactions committent avec succès, mais le service se retrouve sans aucun médecin de garde.

Pour contrer le Write Skew, le niveau **Serializable** ou un verrouillage applicatif explicite est strictement requis. Sous *Serializable*, le moteur SQL peut lever une exception d'échec de sérialisation (code SQLSTATE `40001`), imposant au harnais applicatif un mécanisme de réessai automatique déterministe.

[^1]: Berenson, Bernstein, Gray, Melton, O'Neil et O'Neil, *A Critique of ANSI SQL Isolation Levels*, ACM SIGMOD, 1995.

---

### 2. Verrouillage Optimiste (OCC) versus Verrouillage Pessimiste

Pour coordonner l'accès concurrentiel aux lignes sans pénaliser le débit du système, l'architecte arbitre entre deux stratégies fondamentales :

```text
COMPARAISON DES STRATÉGIES DE VERROUILLAGE :

  VERROUILLAGE OPTIMISTE (OCC)             VERROUILLAGE PESSIMISTE (Pessimistic Locking)
  Principe : Détection à la validation      Principe : Exclusion dès la lecture
  ┌─────────────────────────────────┐       ┌─────────────────────────────────┐
  │ 1. SELECT * FROM doc WHERE id=1 │       │ 1. SELECT * FROM doc WHERE id=1 │
  │    (Lit version = 4)            │       │    FOR UPDATE;                  │
  │ 2. Calculs en mémoire           │       │    (Verrou exclusif posé)       │
  │ 3. UPDATE doc SET data=...,     │       │ 2. Calculs métier               │
  │    version = 5                  │       │ 3. UPDATE doc SET data=...;     │
  │    WHERE id=1 AND version=4;    │       │ 4. COMMIT; (Verrou libéré)      │
  └─────────────────────────────────┘       └─────────────────────────────────┘
  ✓ Zéro verrouillage en lecture            ✓ Concurrence éliminée mécaniquement
  ✓ Idéal pour forte consultation           ✗ Risque de Deadlock sous charge
  ✗ Échec si modification concurrente       ✗ Sature le pool de connexions SQL
```

- **Le Verrouillage Optimiste** repose sur un numéro de version incrémental (`version: integer`). Si la clause `WHERE version = 4` ne met à jour aucune ligne (compteur de lignes affectées = 0), un conflit est détecté et l'application rejoue l'opération.
- **Le Verrouillage Pessimiste (`SELECT ... FOR UPDATE`)** bloque physiquement toute écriture concurrente jusqu'au commit. Il est strictement réservé aux sections critiques brèves (décrémentation d'un stock unitaire ou débit d'un solde bancaire).

---

### 3. Le Pattern Expand-Contract pour les migrations sans coupure

Modifier un schéma de base de données relationnelle en production sans interrompre le service (*Zero-Downtime Deployment*) interdit formellement toute modification destructive immédiate.

L'industrie applique le **Pattern Expand-Contract (Élargir - Transiter - Contracter)**[^2] en trois étapes ordonnées :

```text
SÉQUENCE COMPLÈTE DU PATTERN EXPAND-CONTRACT :

  PHASE 1 : ÉLARGISSEMENT (EXPAND)
  ├── Migration SQL : ALTER TABLE devis ADD COLUMN statut_code VARCHAR(30) NULL;
  └── Application V1 (Active) : Continue de lire et d'écrire sur l'ancienne colonne 'statut'.
  
  PHASE 2 : TRANSITION & DOUBLE ÉCRITURE (TRANSITION)
  ├── Déploiement Application V2 :
  │     • Écriture double : Écrit à la fois sur 'statut' ET 'statut_code'.
  │     • Lecture tolérante : Lit 'statut_code' avec fallback immédiat sur 'statut'.
  └── Script de Backfill (Par lots) :
        UPDATE devis SET statut_code = ... WHERE id BETWEEN 1 AND 1000 AND statut_code IS NULL;
        (Exécuté en tâches de fond cadencées pour ne pas saturer le journal WAL).

  PHASE 3 : CONTRACTION (CONTRACT)
  ├── Déploiement Application V3 : Lit et écrit exclusivement sur 'statut_code'.
  └── Migration SQL finale : ALTER TABLE devis DROP COLUMN statut;
```

Toute tentative de compresser ces trois phases en une seule transaction SQL unilatérale provoque un verrouillage de table (*AccessExclusiveLock*) et une coupure de service générale.

[^2]: Pramod Sadalage et Martin Fowler, *Refactoring Databases: Evolutionary Database Design*, Addison-Wesley, 2006.

---

### 4. Sauvegardes continues, Write-Ahead Logs et Point-in-Time Recovery

Se contenter d'un export quotidien nocturne (`pg_dump` à 02h00) constitue une faute de gouvernance majeure : si le disque subit une panne matérielle à 18h00, l'entreprise subit une **perte sèche de 16 heures de transactions (RPO = 16h)**.

L'ingénierie moderne de persistance impose l'archivage continu des journaux de transactions **Write-Ahead Logging (WAL)** vers un stockage objet chiffré et immuable (Cloudflare R2, AWS S3) via des outils industriels comme `pgBackRest` ou `WAL-G`[^3].

```text
ARCHITECTURE POINT-IN-TIME RECOVERY (PITR) :

  [ Base PostgreSQL ] ──── Écriture continue WAL ────► [ Coffre S3 / R2 distant ]
           │                                                    │
     (Crash à 14h32:15)                                         │
           ▼                                                    ▼
  [ Nouvelle Instance ] ◄── 1. Restauration Snapshot 02h00 ─────┤
           │            ◄── 2. Rejeu des segments WAL jusqu'à ──┘
           │                   la milliseconde exacte 14h32:14
           ▼
  ÉTAT DU SYSTÈME RESTAURÉ AVEC ZÉRO PERTE DE TRANSACTION (RPO ≈ 0s)
```

Cette architecture confère au système la capacité de **remonter le temps (Point-in-Time Recovery)** : en cas de corruption ou de suppression accidentelle d'une table à 14h32:15, l'ingénieur restaure la base à 14h32:14 avec une précision à la milliseconde près.

[^3]: PostgreSQL Global Development Group, *Continuous Archiving and Point-in-Time Recovery (PITR)*, Documentation officielle PostgreSQL v16, 2023.

---

## Mise en pratique

### Modélisation du Verrouillage Optimiste et Migration Expand-Contract en Python 3.11

Le programme suivant implémente un gestionnaire de persistance relationnelle démontrant le contrôle de concurrence optimiste et la compatibilité ascendante d'une migration en trois étapes :

```python
"""Module d'ingénierie de persistance : Concurrence optimiste et Expand-Contract.

Démontre la gestion des anomalies d'écriture concurrente et la coexistence
sans coupure de deux versions applicatives sur le même schéma.
"""
from dataclasses import dataclass
from typing import Optional
import unittest


# ============================================================================
# 1. MODÈLE AVEC CONTRÔLE DE CONCURRENCE OPTIMISTE (OCC)
# ============================================================================

class ConflitConcurrenceOptimisteErreur(Exception):
    """Émise lorsque la version d'un enregistrement a été modifiée par un tiers."""
    pass


@dataclass
class LigneDocumentSQL:
    id_document: str
    nom_fichier: str
    version: int
    # Phase 1 Expand : Ancienne colonne conservée, nouvelle colonne nullable
    statut_v1: str
    statut_code_v2: Optional[str] = None


class BaseDonneesDocumentSimulee:
    """Simulateur de moteur SQL gérant les transactions et l'OCC."""

    def __init__(self) -> None:
        self._tables: dict[str, LigneDocumentSQL] = {}

    def inserer(self, document: LigneDocumentSQL) -> None:
        self._tables[document.id_document] = document

    def lire(self, id_document: str) -> LigneDocumentSQL:
        if id_document not in self._tables:
            raise KeyError(f"Document {id_document} introuvable.")
        doc = self._tables[id_document]
        # Renvoie une copie pour simuler l'isolation mémoire d'un curseur SQL
        return LigneDocumentSQL(
            id_document=doc.id_document,
            nom_fichier=doc.nom_fichier,
            version=doc.version,
            statut_v1=doc.statut_v1,
            statut_code_v2=doc.statut_code_v2,
        )

    def mettre_a_jour_optimiste(
        self, id_document: str, nouveau_statut_v1: str, nouveau_code_v2: Optional[str], version_attendue: int
    ) -> None:
        """Simule : UPDATE doc SET ... version = version + 1 WHERE id = ? AND version = ?"""
        ligne_actuelle = self._tables.get(id_document)
        if not ligne_actuelle:
            raise KeyError("Document inexistant.")

        if ligne_actuelle.version != version_attendue:
            raise ConflitConcurrenceOptimisteErreur(
                f"Conflit de concurrence sur {id_document} : version attendue {version_attendue}, "
                f"version trouvée en base {ligne_actuelle.version}."
            )

        # Mise à jour atomique
        ligne_actuelle.statut_v1 = nouveau_statut_v1
        ligne_actuelle.statut_code_v2 = nouveau_code_v2
        ligne_actuelle.version += 1


# ============================================================================
# 2. ADAPTATEURS LOGICIELS COHABITANTS (V1 ET V2 EXPAND-CONTRACT)
# ============================================================================

class ServiceDocumentV1:
    """Ancienne version du logiciel en production : ne connaît que 'statut_v1'."""

    def __init__(self, db: BaseDonneesDocumentSimulee) -> None:
        self.db = db

    def valider(self, id_doc: str) -> None:
        doc = self.db.lire(id_doc)
        # Écrit uniquement sur v1, ignore totalement v2
        self.db.mettre_a_jour_optimiste(id_doc, "VALIDE", doc.statut_code_v2, doc.version)


class ServiceDocumentV2:
    """Nouvelle version : applique le Dual-Write et lit en priorité sur v2."""

    def __init__(self, db: BaseDonneesDocumentSimulee) -> None:
        self.db = db

    def valider(self, id_doc: str) -> None:
        doc = self.db.lire(id_doc)
        # Double écriture systématique : v1 pour rétro-compatibilité, v2 pour le futur
        self.db.mettre_a_jour_optimiste(id_doc, "VALIDE", "CODE_VALIDE_FABRICATION", doc.version)

    def obtenir_statut_unifie(self, id_doc: str) -> str:
        doc = self.db.lire(id_doc)
        # Lecture préférentielle sur v2 avec fallback sur v1
        return doc.statut_code_v2 or f"LEGACY_{doc.statut_v1}"
```

---

### La suite de tests prouvant l'intégrité transactionnelle et la migration sans coupure

```python
class TestPersistanceEtExpandContract(unittest.TestCase):
    """Suite vérifiant la détection de conflit OCC et la cohabitation V1/V2."""

    def test_detection_conflit_concurrence_optimiste(self) -> None:
        db = BaseDonneesDocumentSimulee()
        db.inserer(LigneDocumentSQL("doc-1", "devis.pdf", version=1, statut_v1="EN_ATTENTE"))

        # Deux travailleurs lisent la même ligne en version 1
        lecteur_a = db.lire("doc-1")
        lecteur_b = db.lire("doc-1")

        # Le travailleur A commite sa mise à jour avec succès (version passe à 2)
        db.mettre_a_jour_optimiste("doc-1", "VALIDE", None, version_attendue=lecteur_a.version)
        self.assertEqual(db.lire("doc-1").version, 2)

        # Le travailleur B tente de commiter avec son ancienne version 1 -> Conflit !
        with self.assertRaises(ConflitConcurrenceOptimisteErreur):
            db.mettre_a_jour_optimiste("doc-1", "REJETE", None, version_attendue=lecteur_b.version)

    def test_cohabitation_v1_et_v2_sans_coupure(self) -> None:
        db = BaseDonneesDocumentSimulee()
        # Enregistrement historique créé avant la migration
        db.inserer(LigneDocumentSQL("doc-legacy", "ancien.pdf", version=1, statut_v1="EN_ATTENTE"))

        v1 = ServiceDocumentV1(db)
        v2 = ServiceDocumentV2(db)

        # 1. La version V2 sait lire un document ancien (fallback sur V1)
        statut_lu = v2.obtenir_statut_unifie("doc-legacy")
        self.assertEqual(statut_lu, "LEGACY_EN_ATTENTE")

        # 2. La version V1 valide un document : le code V2 continue de le comprendre
        v1.valider("doc-legacy")
        self.assertEqual(v2.obtenir_statut_unifie("doc-legacy"), "LEGACY_VALIDE")

        # 3. La version V2 valide le document avec la double écriture
        v2.valider("doc-legacy")
        doc_final = db.lire("doc-legacy")
        self.assertEqual(doc_final.statut_v1, "VALIDE")
        self.assertEqual(doc_final.statut_code_v2, "CODE_VALIDE_FABRICATION")
        self.assertEqual(v2.obtenir_statut_unifie("doc-legacy"), "CODE_VALIDE_FABRICATION")


if __name__ == "__main__":
    unittest.main()
```

---

## Exercice d'arbitrage & Corrigé commenté

### Le cas d'ingénierie : L'indexation bloquante sur une table critique

Un agent de code propose la Pull Request suivante pour optimiser la recherche des factures impayées sur une base PostgreSQL de 8 millions de lignes :

```sql
-- Migration proposée par l'agent dans migrations/0042_index_impayes.sql :
ALTER TABLE factures ADD COLUMN est_impayee BOOLEAN NOT NULL DEFAULT FALSE;
CREATE INDEX idx_factures_impayees ON factures (client_id, date_emission) WHERE est_impayee = TRUE;
```

### La grille d'audit de l'architecte

1. **Verrouillage exclusif prolongé (*Table Lock Outage*)** : Exécuter `CREATE INDEX` sans l'option `CONCURRENTLY` sur une table de 8 millions de lignes pose un verrou de partage exclusif (*ShareLock*) qui interdit toute écriture pendant plusieurs dizaines de secondes.
2. **Saturation des entrées/sorties et de la mémoire WAL** : Mettre à jour 8 millions de lignes avec une valeur par défaut dans une transaction SQL classique génère une avalanche d'octets dans les journaux de transactions, ralentissant la réplication de production.

### Le corrigé commenté

**Décision de l'architecte** : Refus de la PR avec consigne de migration non-bloquante :

```text
CONSIGNE DE REFACTORING SQL INDUSTRIEL :
1. Bannir 'CREATE INDEX' direct en production.
2. Utiliser obligatoirement la directive non-bloquante :
   CREATE INDEX CONCURRENTLY idx_factures_impayees ON factures (client_id, date_emission)
   WHERE est_impayee = TRUE;
3. Exécuter cette instruction en dehors de tout bloc transactionnel unitaire
   (PostgreSQL interdit 'CONCURRENTLY' à l'intérieur d'un bloc BEGIN / COMMIT).
4. Ajouter la colonne comme nullable dans un premier temps pour éviter de réécrire
   physiquement les 8 millions de lignes sur le disque hôte.
```

---

## Checklist réflexe du pilote

Avant de valider une migration de schéma ou une refonte de persistance, contrôle ces six critères d'ingénierie :

- [ ] **Les migrations sont non-bloquantes** : Les index sont créés avec `CONCURRENTLY` et aucune instruction ne bloque l'écriture de production.
- [ ] **Le pattern Expand-Contract est respecté** : Les colonnes nouvelles sont d'abord optionnelles et la double écriture est assurée avant contraction.
- [ ] **L'isolation transactionnelle est appropriée** : Le niveau SQL (Read Committed vs Serializable) est choisi en fonction des anomalies réelles à prohiber.
- [ ] **Les courses critiques sont protégées** : Les modifications concurrentes sont arbitrées par verrouillage optimiste (`version`) ou pessimiste (`FOR UPDATE`).
- [ ] **Le RPO est garanti par les WAL** : Les segments de transactions sont continuellement répliqués vers un stockage objet chiffré indépendant.
- [ ] **Le PITR a été testé** : La procédure de restauration à la milliseconde a été validée lors d'un exercice d'incident programmé.

---

## Sources et limites

Ce chapitre approfondit les méthodologies d'ingénierie relationnelle et de haute disponibilité :
- **O-MD §2, §3, §8, §10 et §13** ([Manuel d'Orchestration Logicielle](/projet/references/sources/o-md)) : L'intégrité de schéma, l'idempotence des transactions, les migrations versionnées et la reprise d'activité.
- **I-MD §7** ([Manuel d'Ingénierie Logicielle](/projet/references/sources/i-md)) : Les anomalies transactionnelles ANSI SQL, le contrôle de concurrence optimiste, le cycle Expand-Contract et la réplication continue par WAL.

Pour maîtriser l'automatisation de la chaîne CI/CD, la conteneurisation déterministe et le déploiement sur infrastructure VPS, poursuis vers le chapitre suivant : **[B09 — Automatiser la livraison et la production](/ingenieure/09-livraison-et-production)**. Pour réviser les concepts sans code, consulte le miroir accessible : **[A08 — Protéger les données et faire évoluer leur structure](/accessible/08-donnees-et-migrations)**.

## Références pour approfondir

- [PostgreSQL — NOTIFY](https://www.postgresql.org/docs/current/sql-notify.html) — Notifications de sessions ; à distinguer d'une file durable de travaux. [Notice et chapitres associés](/projet/references#ref-notify).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche B08](/redaction/b08-donnees-et-migrations).
