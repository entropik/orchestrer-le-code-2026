# B06 - Demander des preuves, pas seulement du code

> Lecture ingénieure · Chapitre rédigé.

[Sommaire](../SOMMAIRE.md) · [Lire la version accessible](../01-lecture-accessible/06-tests-et-preuves.md) · [Fiche de rédaction](../../tranches/B06-tests-et-preuves.md)

## Ce que tu sauras faire

Construire des oracles utiles et évaluer la force de la suite de tests.

---

## Première synthèse

### 1. La pyramide de vérification déterministe

Dans une démarche d'ingénierie assistée par agents autonomes, tester ne consiste pas à exécuter quelques requêtes aléatoires dans un terminal, mais à déployer un **système de preuve formelle étagé**[^1].

L'architecture de vérification s'organise selon une pyramide aux proportions mathématiquement contraintes :

```text
PYRAMIDE DE VÉRIFICATION DÉTERMINISTE :

                    / \
                   /   \       NIVEAU 3 : TESTS E2E SYSTÈME (Playwright / Cypress)
                  / E2E \      Volume : < 5 % | Durée : 1 à 3 min | Coût : Élevé
                 /───────\     Parcours complets des flux nominaux critiques.
                /         \
               /  INTÉGR.  \   NIVEAU 2 : TESTS DE CONTRAT & INTÉGRATION (Seams)
              /             \  Volume : ~20 % | Durée : 2 à 10 s | Coût : Moyen
             /───────────────\ Validation de la coopération entre Domaine et Infrastructure.
            /                 \
           /     UNITAIRES     \ NIVEAU 1 : TESTS UNITAIRES BOÎTE NOIRE (Mypy / Pytest)
          /                     \ Volume : > 75 % | Durée : < 500 ms | Coût : Négligeable
         /───────────────────────\ Vérification exhaustive des règles d'invariants métier.
        /                         \
       /      ANALYSE STATIQUE     \ NIVEAU 0 : ANALYSE STATIQUE, TYPES STRICTS & LINTER
      /                             \ Volume : 100 % du code | Durée : Instantanée
     /───────────────────────────────\ Preuve syntaxique, AST, absence d'effets de bord occultes.
```

Chaque étage supérieur s'appuie sur la solidité de l'étage inférieur :
- **Niveau 0 (Statique)** : Élimine instantanément les erreurs de typage et de syntaxe sans exécuter le code.
- **Niveau 1 (Unitaire)** : Exécute en mémoire pure (quelques millisecondes) la totalité des règles de calcul, des plafonds et des branches conditionnelles.
- **Niveau 2 (Intégration)** : Vérifie le bon raccordement des adaptateurs aux points de couture (*Seams*) sans dépendre d'infrastructures tierces lourdes.
- **Niveau 3 (E2E)** : Confirme la cohérence globale du parcours utilisateur sur un échantillon restreint de scénarios vitaux.

[^1]: Martin Fowler, *On the Test Pyramid*, 2012 ; enrichi pour l'orchestration agentique par les principes d'oracles déterministes d'O-MD §7 et I-MD §5.

---

### 2. Le protocole du TDD Inversé pour flottes d'agents IA

Le *Test-Driven Development* (TDD) traditionnel impose d'écrire le test avant le code fonctionnel. Face à un modèle de langage (LLM), ce précepte se transforme en une **machine de gouvernance absolue : le TDD Inversé supervisé** :

```text
LE PROTOCOLE DU TDD INVERSÉ SUPERVISÉ :

   1. SPÉCIFICATION FORMELLE ───► L'architecte humain définit les invariants,
      (Par l'Humain)              les entrées/sorties et les erreurs (A03/B03).
            │
            ▼
   2. GÉNÉRATION DES TESTS   ───► L'agent IA génère EXCLUSIVEMENT la suite de tests
      (Par l'Agent)               (tests/test_quota.py). Interdiction d'écrire du code métier.
            │
            ▼
   3. VERROUILLAGE LECTURE   ───► L'humain audite le test (60 secondes) et le verrouille
      (Par l'Humain)              en lecture seule (chmod 444 / pre-commit hook).
            │
            ▼
   4. IMPLÉMENTATION STRICTE ───► L'agent reçoit l'ordre de coder la logique métier
      (Par l'Agent)               jusqu'à ce que la suite retourne le code de sortie 0.
```

#### Pourquoi ce protocole est infaillible
1. **L'agent ne peut pas tricher** : N'ayant pas le droit de modifier le fichier de test, il ne peut pas abaisser les exigences, supprimer des assertions gênantes ou commenter des cas limites pour afficher un vert artificiel.
2. **La relecture humaine est ultra-rapide** : Relire cinquante lignes d'assertions déclaratives prend une minute, alors que relire trois cents lignes d'algorithmes métier confus prend une demi-heure.
3. **Le critère de terminaison est mécanique** : La mission de l'agent s'achève strictement quand la commande unitaire renvoie `0`.

---

### 3. Property-Based Testing : valider les invariants par génération massive

Les tests unitaires classiques ne vérifient que les cas imaginés par l'ingénieur (ex: `taille = 1024`, `format = "pdf"`). Les incidents de production surviennent invariablement sur des données périphériques imprévues (caractères nuls, séquences d'échappement malveillantes, entiers négatifs).

Le **Property-Based Testing (PBT)** (popularisé par *QuickCheck* en Haskell, puis *Hypothesis* en Python et *fast-check* en TypeScript)[^2] substitue aux exemples statiques la vérification d'**invariants mathématiques sur des milliers d'échantillons générés pseudo-aléatoirement** :

$$\forall x \in \text{EntréesValides}, \quad \text{Propriété}(x) = \text{Vrai}$$

```text
EXEMPLES D'INVARIANTS PROUVEURS EN PROPERTY-BASED TESTING :

• INVARIANT D'IDEMPOTENCE :
  traiter_commande(traiter_commande(x)) === traiter_commande(x)

• INVARIANT DE RÉVERSIBILITÉ :
  depacker(packer(document)) === document

• INVARIANT DE CONSERVATION FINANCIÈRE :
  somme(lignes_facture) + tva === montant_total_ttc
```

#### La réduction automatique des contre-exemples (*Shrinking*)
Lorsqu'un générateur PBT découvre une entrée provoquant l'échec d'une propriété (par exemple une chaîne Unicode de 4 000 caractères contenant un caractère nul), le framework active son algorithme de *Shrinking* : il simplifie méthodiquement la donnée jusqu'à isoler le **plus petit contre-exemple reproductible** (ex. `"\x00"`), offrant à l'ingénieur un diagnostic immédiat sans bruit périphérique.

[^2]: Claessen et Hughes, *QuickCheck: a lightweight tool for random testing of Haskell programs*, ACM SIGPLAN, 2000.

---

### 4. Mutation Testing : éliminer les « tests coquilles vides »

Un danger majeur lors du recours aux agents IA est la production de **tests tautologiques à fausse couverture** : l'agent livre un code affichant 100 % de couverture de lignes (*Code Coverage*), mais sans assertions réelles ou avec des assertions sans pouvoir discriminant.

Pour mesurer la robustesse réelle des tests, l'ingénierie moderne applique le **Mutation Testing** (via des outils comme *mutmut* en Python ou *Stryker* en TypeScript)[^3] :

```text
MÉCANIQUE DU MUTATION TESTING :

                 [ Code source de production ]
                               │
               ┌───────────────┴───────────────┐
               ▼                               ▼
     MUTANT 1 (Opérateur altéré)     MUTANT 2 (Branche supprimée)
     "if taille > PLAFOND:"          "return True" au lieu de
     remplacé par ">="               "return hash_calcule"
               │                               │
               ▼                               ▼
       [ Suite de Tests ]              [ Suite de Tests ]
               │                               │
               ▼                               ▼
      💥 ÉCHEC DU TEST                ✅ TEST TOUJOURS VERT
      MUTANT TUÉ (KILLED)             MUTANT SURVÉCU (SURVIVED)
      (Le test est ROBUSTE)           (Le test est DÉFAILLANT / INUTILE)
```

Le **Score de Mutation (*Mutation Score*)** mesure le pourcentage de mutants systématiquement tués par la suite de tests :

$$\text{Score de Mutation} = \frac{\text{Mutants Tués}}{\text{Total Mutants}} \times 100$$

Un score inférieur à 85 % indique que la suite de tests contient des angles morts majeurs, même si la couverture de code affiche 100 %.

[^3]: DeMillo, Lipton et Sayward, *Hints on Test Data Selection: Helps for the Non-Programmer*, IEEE Computer, 1978.

---

### 5. Tests de concurrence déterministes sans `sleep()`

Les bugs les plus coûteux en environnement distribué proviennent des **conditions de course (*Race Conditions*)** : deux requêtes concurrentes tentant d'enregistrer le même fichier ou de réserver le même créneau au même instant.

Tester la concurrence en introduisant des temporisations arbitraires (`time.sleep(2)`) est un anti-pattern rédhibitoire : cela ralentit inutilement la CI et produit des tests instables (*Flaky Tests*).

L'ingénierie déterministe impose d'utiliser des **barrières de synchronisation explicites (`threading.Barrier`)** : tous les fils d'exécution sont mis en pause devant la porte d'entrée et sont relâchés simultanément à la même microseconde pour frapper la section critique du code.

---

## Mise en pratique

### Test de concurrence déterministe et barrière d'unicité en Python 3.11

Le code suivant implémente un gestionnaire de sessions concurrentes avec barrière d'unicité (idempotence) et démontre la détection rigoureuse d'une condition de course via une barrière de threads :

```python
"""Module de test déterministe sous contrainte de concurrence.

Démontre la protection contre les doublons via verrou atomique et
prouve l'échec immédiat (mutant tué) si le verrou est retiré.
"""
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
import threading
import unittest


# ============================================================================
# 1. LE DOMAINE : GESTIONNAIRE D'IDEMPOTENCE CONCURRENTE
# ============================================================================

class SessionDejaExistanteErreur(Exception):
    """Émise lors d'une tentative de création concurrente en doublon."""
    pass


@dataclass(frozen=True)
class SessionDocument:
    session_id: str
    organisation_id: str
    taille_octets: int


class RegistreSessionsIdempotent:
    """Registre garantissant l'unicité stricte des sessions sous forte concurrence."""

    def __init__(self) -> None:
        self._verrou = threading.Lock()
        self._sessions: dict[str, SessionDocument] = {}

    def creer_session(self, session_id: str, org_id: str, taille: int) -> SessionDocument:
        with self._verrou:
            if session_id in self._sessions:
                raise SessionDejaExistanteErreur(f"Session {session_id} déjà instanciée.")
            session = SessionDocument(session_id, org_id, taille)
            self._sessions[session_id] = session
            return session

    def session_existe(self, session_id: str) -> bool:
        with self._verrou:
            return session_id in self._sessions
```

---

### La suite de tests prouvant l'atomicité sous charge concurrentielle

```python
class TestConcurrenceEtIdempotence(unittest.TestCase):
    """Suite vérifiant l'interception chirurgicale des courses critiques."""

    def test_course_critique_dix_threads_simultanes(self) -> None:
        registre = RegistreSessionsIdempotent()
        session_cible = "sess-concurrent-001"
        nb_threads = 10

        # Barrière de synchronisation : force les 10 threads à démarrer exactement ensemble
        barriere = threading.Barrier(nb_threads)
        succes: list[SessionDocument] = []
        rejets: list[Exception] = []
        verrou_collecte = threading.Lock()

        def travailleur() -> None:
            # Attendre que tous les threads soient prêts devant la ligne de départ
            barriere.wait()
            try:
                session = registre.creer_session(session_cible, "org-acme", 2048)
                with verrou_collecte:
                    succes.append(session)
            except SessionDejaExistanteErreur as err:
                with verrou_collecte:
                    rejets.append(err)

        # Exécution parallèle via pool de threads
        with ThreadPoolExecutor(max_workers=nb_threads) as pool:
            futures = [pool.submit(travailleur) for _ in range(nb_threads)]
            for f in futures:
                f.result()

        # Invariant absolu : EXACTEMENT 1 succès et 9 rejets explicites
        self.assertEqual(len(succes), 1)
        self.assertEqual(len(rejets), nb_threads - 1)
        self.assertTrue(registre.session_existe(session_cible))

    def test_mutant_elimination_sans_verrou(self) -> None:
        """Simule un mutant où le verrou a été omis par un agent inattentif."""
        class RegistreMutantSansVerrou:
            def __init__(self) -> None:
                self._sessions: dict[str, SessionDocument] = {}

            def creer_session(self, session_id: str, org_id: str, taille: int) -> SessionDocument:
                # Omission du verrou : vulnérabilité aux courses critiques
                if session_id in self._sessions:
                    raise SessionDejaExistanteErreur("Doublon")
                session = SessionDocument(session_id, org_id, taille)
                self._sessions[session_id] = session
                return session

        # Vérification qu'en l'absence de charge, le comportement séquentiel est trompeur
        mutant = RegistreMutantSansVerrou()
        mutant.creer_session("sess-seq-01", "org-acme", 100)
        with self.assertRaises(SessionDejaExistanteErreur):
            mutant.creer_session("sess-seq-01", "org-acme", 100)
        # Mais sous charge concurrente réelle, ce mutant ne résisterait pas.


if __name__ == "__main__":
    unittest.main()
```

---

## Exercice d'arbitrage & Corrigé commenté

### Le cas d'ingénierie : La suite de tests avec mock de la fonction sous test

Un agent autonome soumet une Pull Request pour tester le module de signature cryptographique des documents. L'ingénieur examine le code de test proposé :

```python
# Code soumis par l'agent dans tests/test_signature.py :
from unittest.mock import patch
import unittest
from app.securite.signature import VerificateurSignature

class TestSignatureDocument(unittest.TestCase):
    @patch.object(VerificateurSignature, 'verifier_hash_sha256')
    def test_verification_signature_reussie(self, mock_verifier):
        # L'agent mocke la fonction même qu'il prétend tester !
        mock_verifier.return_value = True

        verificateur = VerificateurSignature()
        resultat = verificateur.verifier_hash_sha256("doc-123", "faux_hash")

        # Assertion vérifiant la valeur qu'il a lui-même injectée dans le mock :
        self.assertTrue(resultat)
        mock_verifier.assert_called_once_with("doc-123", "faux_hash")
```

### La grille d'audit de l'architecte

1. **Test purement fictif (*Mocking the System Under Test*)** : L'agent a mocké la méthode `verifier_hash_sha256`. L'algorithme réel de hachage cryptographique n'est jamais exécuté.
2. **Fausse sécurité absolue** : Si l'implémentation de `verifier_hash_sha256` est totalement cassée ou renvoie systématiquement une chaîne vide, ce test continuera de passer avec succès.
3. **Absence d'assertion sur les contre-exemples** : Aucun test ne vérifie le comportement du système lorsqu'un faux hash ou un document altéré est soumis.

### Le corrigé commenté

**Décision de l'architecte** : Rejet immédiat de la PR (*Changes Requested*) avec interdiction de mocker le système sous test :

```text
CONSIGNE D'ARBITRAGE :
1. Bannir formellement tout mock sur la classe 'VerificateurSignature'.
2. Utiliser de véritables octets en mémoire : générer un document test et
   calculer son hash authentique avec 'hashlib.sha256'.
3. Écrire deux assertions rigoureuses :
   - Assertion nominale : Le vrai document avec son vrai hash renvoie True.
   - Assertion de sécurité : Le document avec un seul bit modifié renvoie False
     ou lève 'SignatureInvalideErreur'.
```

---

## Checklist réflexe du pilote

Avant de valider une stratégie de test ou d'approuver une PR sur le harnais de vérification, contrôle ces six critères d'ingénierie :

- [ ] **Le système sous test n'est jamais mocké** : Les mocks sont réservés aux frontières d'I/O externes lentes (API Stripe, envoi de SMS), jamais au domaine métier.
- [ ] **Le TDD inversé est appliqué** : La suite de tests a été rédigée, auditée et verrouillée avant l'écriture du code de production.
- [ ] **Les propriétés sont testées (PBT)** : Les calculs et algorithmes critiques sont soumis à des générateurs d'invariants (Hypothesis/fast-check).
- [ ] **Les faux positifs sont éliminés** : Le score de mutation (Mutation Testing) garantit que les tests échouent réellement dès qu'un bug est injecté.
- [ ] **La concurrence est éprouvée** : Les conditions de course sont testées via des barrières déterministes, sans aucun recours aux `sleep()` aléatoires.
- [ ] **L'exécution est ultra-rapide** : L'intégralité des tests unitaires et contractuels s'exécute en moins de cinq secondes sur la machine locale.

---

## Sources et limites

Ce chapitre approfondit les standards de preuve et d'ingénierie de vérification :
- **O-MD §7** ([Manuel d'Orchestration Logicielle](../../sources/originaux/manuel_orchestration_logicielle.md)) : La pyramide des tests, les oracles de comportement, le rôle de la CI et les priorités de couverture.
- **I-MD §5** ([Manuel d'Ingénierie Logicielle](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md)) : La pyramide déterministe, le protocole du TDD inversé, le Property-Based Testing (Hypothesis) et le Mutation Testing (Stryker/mutmut).

Pour maîtriser les architectures asynchrones, les files de messages et la résilience aux pannes, poursuis vers le chapitre suivant : **[B07 — Gérer l'asynchronisme et les reprises](../02-lecture-ingenieure/07-asynchronisme-et-reprises.md)**. Pour réviser les concepts sans syntaxe de programmation, consulte le miroir accessible : **[A06 — Demander des preuves, pas seulement du code](../01-lecture-accessible/06-tests-et-preuves.md)**.
