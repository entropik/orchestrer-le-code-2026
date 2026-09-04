# B05 - Garder une histoire fiable avec Git

> Lecture ingénieure · Chapitre rédigé.

[Sommaire](../SOMMAIRE.md) · [Lire la version accessible](../01-lecture-accessible/05-git-et-collaboration.md) · [Fiche de rédaction](../../tranches/B05-git-et-collaboration.md)

## Ce que tu sauras faire

Organiser branches, worktrees et revue sans confondre séparation de travail et sécurité.

---

## Première synthèse

### 1. La topologie interne de Git : un graphe orienté acyclique d'objets immuables

Pour l'ingénieur logiciel, Git n'est pas un ensemble de commandes utilitaires, mais un **système de fichiers adressable par le contenu adossé à un Graphe Orienté Acyclique (*Directed Acyclic Graph* ou DAG)**[^1].

Toute la persistance de Git repose sur quatre types d'objets primitifs, identifiés par leur empreinte cryptographique (SHA-1 ou SHA-256) et stockés dans le répertoire `.git/objects/` :
- **Le Blob** : Les octets bruts d'un fichier, dénués de métadonnées (ni nom de fichier, ni droits d'accès). Deux fichiers au contenu identique partagent le même blob.
- **Le Tree** : L'équivalent d'un répertoire. Il associe des noms de fichiers, des permissions POSIX et des empreintes de blobs ou de sous-arbres.
- **Le Commit** : Un instantané pointant vers un arbre racine (`tree`), avec une liste de commits parents (zéro pour le commit racine, un pour un commit standard, deux ou plus pour une fusion), un auteur, un committer, un horodatage et un message textuel.
- **Le Tag annoté** : Une référence immuable pointant vers un commit précis, signée cryptographiquement (GPG/SSH).

```text
LE GRAPHE D'OBJETS GIT (DAG) :

  [ Commit: feat(upload) ] ───► [ Parent Commit ]
          │
          ▼
    [ Root Tree ]
          │
    ┌─────┴─────────────────────┐
    ▼                           ▼
[ Tree: /app ]             [ Blob: CONTEXT.md ]
    │                      (SHA: 4a2b1c...)
    ▼
[ Blob: parseur.py ]
(SHA: e89f02...)
```

Cette architecture confère à l'historique une **propriété d'immutabilité mathématique** : modifier un seul octet d'un fichier vieux de trois ans altère son hash, ce qui altère le hash de son arbre, puis celui de son commit, invalidant toute la descendance du DAG.

[^1]: Scott Chacon et Ben Straub, *Pro Git*, Apress, 2e édition, 2014.

---

### 2. Git Worktrees : exécution multi-agents sans collision de disque

Dans l'ingénierie traditionnelle, un développeur bascule entre branches via `git checkout` ou `git switch`. Cette approche séquentielle est rigoureusement incompatible avec l'orchestration de flottes d'agents autonomes.

Si deux agents travaillent simultanément sur deux tâches (par exemple, l'un sur le parseur de devis, l'autre sur la tuyauterie de stockage), l'exécution conjointe de `checkout` dans le même dossier de travail provoque des collisions destructrices : fichiers écrasés en cours d'édition, tests perturbés et blocages d'IDE.

La solution industrielle standard repose sur les **Git Worktrees** (`git worktree`)[^2] :

```text
TOPOLOGIE MULTI-AGENTS AVEC GIT WORKTREES :

                        DÉPÔT CENTRAL (.git)
                   [ Base d'objets, Refs, Index ]
                                  │
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
   WORKTREE MAIN          WORKTREE AGENT-01        WORKTREE AGENT-02
   ~/src/projet-main      ~/src/projet-wt-pdf      ~/src/projet-wt-auth
   Branche: main          Branche: feat/pdf        Branche: fix/auth-token
   (Supervision lead)     (Agent Tâche A)          (Agent Tâche B)
   Port test : 8000       Port test : 8001         Port test : 8002
   DB test   : test_0.db  DB test   : test_1.db    DB test   : test_2.db
```

#### Les limites critiques de l'isolation par Worktree
Un Git Worktree sépare les répertoires physiques sur le disque hôte, mais **ne constitue en aucun cas une sandbox de sécurité ou d'exécution** :
- **Partage des ports réseau** : Si l'agent 01 et l'agent 02 lancent simultanément leur serveur de test sur le port standard `8080`, le second s'effondre avec une erreur `EADDRINUSE`.
- **Partage des bases locales** : Si les deux worktrees pointent vers le même fichier SQLite local (`db.sqlite3`), des verrous d'écriture concurrents corrompent les données.
- **Ressources globales de machine** : Un agent malveillant ou halluciné exécutant `rm -rf /` ou modifiant `~/.ssh/` impacte l'ensemble de la machine hôte.

Le harnais d'orchestration doit donc dynamiquement attribuer des ports distincts et des bases de test éphémères à chaque worktree instancié.

[^2]: Documentation officielle Git : `git-worktree(1)`, introduit dans Git v2.5 (juillet 2015).

---

### 3. Stacked Pull Requests & stratégies de réconciliation

Face à un grand chantier logiciel, confier à un agent la réalisation d'une branche de 800 lignes touchant à 25 fichiers est un anti-pattern fatal :
- Le coût cognitif de revue humaine explose (*Review Fatigue*).
- Les régressions subtiles deviennent indétectables dans la masse.
- Le moindre rejet oblige à jeter l'intégralité du travail.

L'architecte impose le paradigme des **Stacked Pull Requests (PRs empilées)** :

```text
CHAÎNE LINÉAIRE DE STACKED PULL REQUESTS (< 150 LIGNES CHACUNE) :

  [ main ] (Production stable)
     ▲
     │  PR 1 : feat(schema): Contrats et objets-valeurs purs (60 lignes)
     ├────────────────────────────────────────────────────────────────
     │  PR 2 : feat(parseur): Parseur aux frontières et erreurs RFC 9457 (85 lignes)
     ├────────────────────────────────────────────────────────────────
     │  PR 3 : feat(api): Raccordement HTTP Fastify et tests d'intégration (75 lignes)
```

Chaque PR est atomique, testable de manière autonome et fusionnable indépendamment dès validation.

#### Comparatif des stratégies de fusion

| Stratégie de Fusion | Structure du DAG résultant | Traçabilité | Recommandation pour Flottes d'Agents |
|---|---|---|---|
| **Rebase & Fast-Forward** | Histoire strictement linéaire sans commits de merge. | Très haute lisibilité, bisect trivial. | **Idéal** pour les PR individuelles bien découpées. |
| **Squash & Merge** | Tous les commits de la branche sont condensés en un seul. | Histoire propre, mais perte des étapes intermédiaires. | **Recommandé par défaut** : masque les micro-itérations désordonnées de l'agent. |
| **Explicit Merge Commit (`--no-ff`)** | Crée un nœud de fusion explicite à deux parents. | Préserve la topologie de branche, mais alourdit le graphe. | Réservé aux fusions de sous-systèmes majeurs. |

---

### 4. Diagnostic de régression automatisé par `git bisect run`

Lorsqu'un comportement fonctionnel se dégrade en production sans cause évidente, Git offre l'outil de diagnostic algorithmique le plus puissant qui soit : la recherche binaire déterministe via `git bisect`[^3].

Au lieu de faire inspecter des centaines de commits à l'aveugle par un agent, l'architecte rédige un **script d'oracle binaire** et laisse Git converger en complexité logarithmique :

$$\text{Nombre d'itérations} = \lceil \log_2(N) \rceil$$

Pour un historique de 1 024 commits, 10 itérations de test suffisent pour isoler le commit exact responsable de la régression.

```text
CONTRAT DE CODE RETOUR POUR L'ORACLE DE BISECT :

  Code retour = 0   ──► Le commit est SAIN (Good / Old).
  Code retour = 1   ──► Le commit est DÉFAILLANT (Bad / New). La régression est présente.
  Code retour = 125 ──► Le commit est INÉVALUABLE (Skip). Dépendance cassée, code non compilable.
```

[^3]: Christian Couder, *Fully automated bisecting with git bisect run*, Git User Manual, 2007.

---

## Mise en pratique

### Gestionnaire de Worktree avec allocation de ports et Oracle de Bisect en Python 3.11

Le programme suivant implémente deux composants fondamentaux d'ingénierie collaborative :
1. Un gestionnaire d'isolation d'arbres de travail qui génère des configurations de ports réseau et de stockage SQLite uniques par branche pour éradiquer les collisions.
2. Un simulateur déterministe d'oracle de recherche binaire (`bisect`) prouvant l'isolation du commit fautif.

```python
"""Module d'ingénierie collaborative : Worktrees isolés et Oracle de Bisect.

Démontre la gestion des ressources partagées lors d'exécutions d'agents concurrents
et l'identification algorithmique de régressions dans un historique de commits.
"""
from dataclasses import dataclass
from typing import Callable, Optional
import hashlib
import unittest


# ============================================================================
# 1. GESTIONNAIRE DE WORKTREE ET D'ISOLATION DE RESSOURCES
# ============================================================================

@dataclass(frozen=True)
class ConfigurationEnvironnementAgent:
    nom_branche: str
    port_ecoute_test: int
    chemin_base_sqlite: str
    repertoire_worktree: str


class GestionnaireWorktreeAgent:
    """Garantit l'absence de collision entre agents exécutés en parallèle."""

    PORT_BASE_TEST = 8100
    PLAGE_PORTS = 500

    @classmethod
    def calculer_configuration(cls, nom_branche: str, racine_depot: str) -> ConfigurationEnvironnementAgent:
        # Hachage déterministe du nom de branche pour dériver un port unique
        hash_val = int(hashlib.sha256(nom_branche.encode("utf-8")).hexdigest()[:8], 16)
        port_attribue = cls.PORT_BASE_TEST + (hash_val % cls.PLAGE_PORTS)

        nom_nettoye = "".join(c if c.isalnum() or c in "-_" else "_" for c in nom_branche)
        chemin_db = f"{racine_depot}/.scratch/db_test_{nom_nettoye}.sqlite3"
        chemin_wt = f"{racine_depot}/../wt_{nom_nettoye}"

        return ConfigurationEnvironnementAgent(
            nom_branche=nom_branche,
            port_ecoute_test=port_attribue,
            chemin_base_sqlite=chemin_db,
            repertoire_worktree=chemin_wt,
        )


# ============================================================================
# 2. ORACLE ET MOTEUR DE RECHERCHE BINAIRE (BISECT) DÉTERMINISTE
# ============================================================================

@dataclass(frozen=True)
class CommitHistorique:
    sha: str
    message: str
    charge_utile: int  # Donnée métier simulée (ex: taille max autorisée)


class MoteurBisectDeterministique:
    """Algorithme de recherche binaire dans un historique de commits en O(log N)."""

    @classmethod
    def localiser_premier_commit_faillible(
        cls,
        historique_commits: list[CommitHistorique],
        oracle: Callable[[CommitHistorique], int]
    ) -> Optional[CommitHistorique]:
        """Localise le commit exact qui a fait basculer l'oracle de 0 à 1."""
        if not historique_commits:
            return None

        # Vérifier que le début est sain (0) et la fin en échec (1)
        if oracle(historique_commits[0]) != 0 or oracle(historique_commits[-1]) != 1:
            return None

        bas = 0
        haut = len(historique_commits) - 1
        premier_faillible: Optional[CommitHistorique] = None

        while bas <= haut:
            milieu = (bas + haut) // 2
            commit_courant = historique_commits[milieu]
            resultat = oracle(commit_courant)

            if resultat == 1:
                premier_faillible = commit_courant
                # Chercher plus tôt dans l'histoire
                haut = milieu - 1
            else:
                # Chercher plus tard
                bas = milieu + 1

        return premier_faillible
```

---

### La suite de tests prouvant l'isolation des worktrees et la précision du bisect

```python
class TestGitCollaborationEtBisect(unittest.TestCase):
    """Vérifie l'allocation des ports et l'isolation logarithmique du bisect."""

    def test_allocation_ports_sans_collision(self) -> None:
        cfg_agent1 = GestionnaireWorktreeAgent.calculer_configuration("feat/pdf-engine", "/home/repo")
        cfg_agent2 = GestionnaireWorktreeAgent.calculer_configuration("feat/auth-token", "/home/repo")

        # Les deux agents doivent obtenir des ports et des bases distincts
        self.assertNotEqual(cfg_agent1.port_ecoute_test, cfg_agent2.port_ecoute_test)
        self.assertNotEqual(cfg_agent1.chemin_base_sqlite, cfg_agent2.chemin_base_sqlite)
        self.assertIn(".scratch", cfg_agent1.chemin_base_sqlite)

    def test_bisect_sur_changement_de_regle_de_quota(self) -> None:
        """Simule 100 commits où le commit 42 a abaissé par erreur le quota à 10 Mo."""
        historique: list[CommitHistorique] = []
        for i in range(100):
            # Avant le commit 42, quota = 50 Mo ; à partir du commit 42, quota = 10 Mo (régression)
            quota = 50 if i < 42 else 10
            historique.append(CommitHistorique(
                sha=f"commit-{i:03d}",
                message=f"Évolution {i}",
                charge_utile=quota
            ))

        # Oracle vérifiant si un fichier de 30 Mo est accepté
        # Si accepté -> 0 (bon) ; si rejeté par erreur -> 1 (régression)
        def oracle_test_30mo(commit: CommitHistorique) -> int:
            taille_test = 30
            # Le comportement attendu est d'accepter jusqu'à 50 Mo
            return 0 if commit.charge_utile >= taille_test else 1

        coupable = MoteurBisectDeterministique.localiser_premier_commit_faillible(
            historique,
            oracle_test_30mo
        )

        self.assertIsNotNone(coupable)
        self.assertEqual(coupable.sha, "commit-042")
        self.assertEqual(coupable.charge_utile, 10)


if __name__ == "__main__":
    unittest.main()
```

---

## Exercice d'arbitrage & Corrigé commenté

### Le cas d'ingénierie : La Pull Request « Big Bang » générée par un agent

Un agent autonome soumet une Pull Request unique intitulée :  
`feat: refonte complète du système de documents et passage à PostgreSQL`.  

L'audit de la PR révèle les éléments suivants :
- 48 fichiers modifiés, 2 840 lignes ajoutées, 1 120 lignes supprimées.
- Le schéma de la base de données a été modifié sans script de migration.
- 4 tests unitaires préexistants ont été désactivés avec le commentaire `// TODO: fix later`.
- L'agent demande une validation immédiate pour « débloquer les autres fonctionnalités ».

### La grille d'audit de l'architecte

1. **Rayon d'explosion incontrôlable** : Il est humainement impossible d'attester de la non-régression d'un tel volume en une seule relecture.
2. **Violation de l'intégrité des tests** : Désactiver des tests rouges pour afficher une CI verte est une fraude méthodologique inacceptable.
3. **Absence de réversibilité** : Si cette PR est fusionnée et qu'un incident survient en production, il sera impossible de séparer la régression liée à PostgreSQL de celle liée aux documents.

### Le corrigé commenté

**Décision de l'architecte** : Fermeture immédiate de la PR (*Closed / Rejected*) avec ordre de décomposition en Stacked PRs :

```text
CONSIGNE DE FRACTIONNEMENT EN 3 STACKED PRS :
1. PR 1 (Contrats purs, max 100 lignes) :
   Définition des nouvelles interfaces et schémas sans changer la base active.
2. PR 2 (Migration de schéma isolée) :
   Script de migration SQL réversible (up/down) avec tests d'intégrité de données.
3. PR 3 (Adaptateur PostgreSQL) :
   Implémentation du nouvel adaptateur sous le port existant, avec réactivation
   stricte de l'intégralité de la suite de tests sans aucun commentaire d'exclusion.
```

---

## Checklist réflexe du pilote

Avant de valider une opération Git ou d'autoriser une fusion dans la branche principale, contrôle ces six critères d'ingénierie :

- [ ] **Pas de commits destructeurs** : Les commandes à risque (`push --force`, `reset --hard`) sont interceptées par des garde-fous locaux et des règles distantes.
- [ ] **Les Worktrees sont isolés** : Chaque agent concurrent dispose de ports de test dédiés et d'une base de données locale éphémère distincte.
- [ ] **Les PRs sont empilées et concises** : Aucune Pull Request ne dépasse une taille raisonnable (< 200 lignes) et chaque changement est unitaire.
- [ ] **La CI est verte sans exclusion** : Aucun test n'a été court-circuité, ignoré ou supprimé pour forcer le succès de la validation.
- [ ] **L'historique est propre** : Les messages de commit respectent les conventions sémantiques et expliquent la raison d'être des modifications.
- [ ] **La réversibilité est testée** : L'équipe est capable de revenir en arrière (*revert*) sans perte de données ni corruption transactionnelle.

---

## Sources et limites

Ce chapitre approfondit les pratiques industrielles de gestion de versions et de revue de code :
- **O-MD §6** ([Manuel d'Orchestration Logicielle](../../sources/originaux/manuel_orchestration_logicielle.md)) : Le modèle mental de Git, les verbes essentiels, la séquence Commit-Push-PR-Merge et la résolution sémantique des conflits.
- **I-MD §4** ([Manuel d'Ingénierie Logicielle](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md)) : La structure du DAG Git, les Git Worktrees pour flottes d'agents, les Stacked Pull Requests et l'automatisation de `git bisect run`.

Pour concevoir la pyramide des tests, l'ingénierie TDD et les oracles de preuve formelle, poursuis vers le chapitre suivant : **[B06 — Tester et prouver le comportement](../02-lecture-ingenieure/06-tests-et-preuves.md)**. Pour réviser les concepts fondamentaux sans outillage de programmation, consulte le miroir accessible : **[A05 — Garder une histoire fiable avec Git](../01-lecture-accessible/05-git-et-collaboration.md)**.
