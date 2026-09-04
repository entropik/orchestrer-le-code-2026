# B04 - Donner du contexte et des limites à l'agent

> Lecture ingénieure · Chapitre rédigé.

[Sommaire](../SOMMAIRE.md) · [Lire la version accessible](../01-lecture-accessible/04-harnais-et-contexte.md) · [Fiche de rédaction](../../tranches/B04-harnais-et-contexte.md)

## Ce que tu sauras faire

Construire un contexte progressif, une architecture de harnais en trois couches et des limites d'exécution agnostiques.

---

## Première synthèse

### 1. L'architecture de harnais en trois couches

Dans l'ingénierie assistée par agents autonomes, le [Harnais](../03-annexes/05-glossaire.md#harnais) (*Harness*) constitue le système d'exploitation cognitif encadrant l'activité des modèles d'IA. Considérer le harnais comme un simple ensemble de prompts disparates est une erreur conceptuelle qui condamne les équipes à la non-reproductibilité.

Le standard industriel éprouvé structure le harnais en **trois couches d'abstraction étanches**[^1] :

```text
ARCHITECTURE DU HARNAIS EN TROIS COUCHES :

  ┌────────────────────────────────────────────────────────────────────────┐
  │ COUCHE 1 : GLOBALE (Machine développeur : ~/.config/ ou ~/.gemini/)   │
  │ • Réflexes universels indépendants du code : /ask-matt, /wait-what     │
  │ • Métarègles cognitives, posture de dialogue, sécurité utilisateur     │
  └───────────────────────────────────┬────────────────────────────────────┘
                                      │
                                      ▼
  ┌────────────────────────────────────────────────────────────────────────┐
  │ COUCHE 2 : PROJET (Dépôt Git : .agents/skills/ & CONTEXT.md)          │
  │ • Repository-as-Code : 37 skills portables (/tdd, /review, /verify)   │
  │ • Règles d'architecture, commandes de build et oracles de test locaux  │
  └───────────────────────────────────┬────────────────────────────────────┘
                                      │
                                      ▼
  ┌────────────────────────────────────────────────────────────────────────┐
  │ COUCHE 3 : RUNTIME & MÉMOIRE ÉPHÉMÈRE (.scratch/ & Session courante)  │
  │ • Fiche de tranche du cycle (A04/B04), journal d'ADR temporaire        │
  │ • Snapshots d'inspection AST, journaux d'erreurs et compte rendu honnête│
  └────────────────────────────────────────────────────────────────────────┘
```

1. **La Couche Globale (Poste de travail : `~/.`)** : Elle héberge les capacités transversales qui accompagnent l'ingénieur sur tous ses projets. C'est le domicile des compétences méta-analytiques : l'aiguilleur de diagnostic (`/ask-matt`), le brainstorming contradictoire (`/grill-me`) ou le frein d'urgence anti-complexité (`/wait-what`).
2. **La Couche Projet (Dépôt Git : `.agents/skills/` à la racine)** : Incarnation rigoureuse du paradigme *Repository-as-Code*. Le dépôt Git embarque ses propres compétences exécutables, ses conventions de nommage et ses suites de tests. Grâce à cette couche, un développeur ou un agent qui clone le dépôt dispose instantanément de l'outillage complet sans aucune configuration préalable de son environnement hôte.
3. **La Couche Runtime et Mémoire Vive** : Elle rassemble les artefacts éphémères propres à la tâche en cours : le glossaire vivant (`CONTEXT.md`), les fiches de tranches actives et les données de travail transitoires stockées dans `.scratch/`.

[^1]: Voir la formalisation complète dans l'ADR fondateur du projet : `docs/adr/0001-harnais-agentique-en-trois-couches.md` ainsi que l'[Architecture du harnais](../03-annexes/03-architecture-du-harnais.md).

---

### 2. La règle de précédence formelle (*Shadowing*) et l'agnosticisme

L'un des défis majeurs d'un harnais distribué est la résolution des conflits entre directives globales et exigences locales. Le système applique la **règle de précédence stricte par masquage (*Shadowing*)** :

$$\text{Règle de résolution} : \text{Runtime} \succ \text{Couche Projet (.agents)} \succ \text{Couche Globale (~/)}$$

Si une compétence ou une règle porte le même nom au niveau global (`~/.agents/skills/tdd`) et au sein du projet (`./.agents/skills/tdd`), la version locale du projet s'impose immédiatement et totalement. 

#### Agnosticisme technologique des agents
Un harnais robuste ne dépend d'aucun fournisseur de modèle propriétaire. La structure standardisée en répertoires `.agents/skills/<nom>/SKILL.md` (avec frontmatter YAML standardisé) assure une interopérabilité totale entre les moteurs d'orchestration modernes : Claude Code, Gemini CLI (agy), OpenAI Codex, Cursor Sidecars ou Kimi. Le clonage du dépôt suffit à armer n'importe quel moteur d'IA avec les exactes mêmes règles opérationnelles.

---

### 3. Inspection chirurgicale par AST versus lecture intégrale naïve

L'approche naïve du vibe coding consiste à exécuter des commandes `cat` ou `view_file` sur des fichiers entiers pour les injecter dans le prompt de l'agent. Cette pratique détruit l'efficacité du modèle :
- Elle consomme inutilement 80 % du budget de tokens.
- Elle noie l'information névralgique dans une masse de détails d'implémentation triviaux.
- Elle favorise le phénomène de *Context Dilution*.

L'ingénierie de contexte impose l'**inspection par Arbre Syntaxique Abstrait (AST - *Abstract Syntax Tree*)** :

```text
COMPARAISON D'INSPECTION DE CODE :

LECTURE NAÏVE (Textuelle brute) :        EXTRACTION PAR AST (Chirurgicale) :
┌────────────────────────────────┐         ┌────────────────────────────────┐
│ 650 lignes de code             │         │ 18 lignes d'index structurel   │
│ - Détails d'implémentation     │         │ • class GestionnaireSession    │
│ - Variables temporaires        │ ──────► │   - creer_session(id, taille)  │
│ - Algorithmes de parsing       │         │   - finaliser_session(id)      │
│ - Boucles et conditions        │         │ • class SessionStatus (Enum)   │
└────────────────────────────────┘         └────────────────────────────────┘
  ~4 500 tokens gaspillés                     ~140 tokens d'une clarté absolue
```

En fournissant à l'agent un condensé structurel (signatures de méthodes, types d'arguments, docstrings) généré par analyse syntaxique, le harnais lui offre une vue cartographique parfaite pour un coût en tokens divisé par trente. L'agent ne demandera la lecture complète du corps d'une fonction que lorsqu'il aura formellement identifié qu'elle doit être modifiée.

---

### 4. La Smart Zone et la gestion des frontières de phase

Les modèles d'attention des transformeurs présentent une courbe de performance en cloche. Si les fenêtres de contexte modernes dépassent le million de tokens, la **Smart Zone** (zone où le raisonnement logique, la précision d'instruction et la capacité de déduction restent optimaux) se situe entre **0 et 120 000 tokens**.

Au-delà de ce seuil, les capacités de raisonnement se dégradent exponentiellement :

```text
DÉGRADATION COGNITIVE AU-DELÀ DE LA SMART ZONE :

  Précision
  100% ┌──────────────────────┐
       │     SMART ZONE       │
   80% │ (0 - 120k tokens)    │\
       │                      │ \
   40% │ Raisonnement optimal │  \  Zone d'hallucinations et
       │ Rigueur de typage    │   \ de régressions silencieuses
    0% └──────────────────────┴────\──────────────────────────►
       0k                   120k   200k                    Tokens
```

Pour préserver cette vigilance, l'architecte pilote les **frontières de phase (*Phase Boundaries*)** grâce à cinq primitives d'hygiène cognitive :
- `/clear` : Réinitialisation intégrale de la mémoire vive après validation et commit d'une tranche.
- `/compact` : Résumé condensé automatique des décisions techniques sans perte d'invariants.
- `/handoff` : Génération d'une fiche de passation structurée transmise à une nouvelle session vierge.
- `invoke_subagent` : Délégation d'une sous-tâche d'exploration ou de recherche à un agent éphémère disposant de son propre contexte isolé.
- `git stash` / `.scratch/` : Sauvegarde externe des données intermédiaires sur le disque hôte plutôt que dans le fil de discussion.

---

### 5. Le protocole de session déterministe en sept étapes

Pour interdire toute régression, le déroulement d'une session agentique suit le cycle déterministe en sept étapes théorisé dans O-MD §4 :

1. **Cadrage de l'intention** : Le pilote énonce la tranche sous forme de résultat observable et spécifie les contraintes de contexte.
2. **Inspection passive sans mutation** : L'agent explore l'arborescence, extrait les AST et localise les points de couture (*Seams*). Toute modification de fichier est formellement bloquée.
3. **Plan d'intervention borné** : L'agent liste les fichiers exacts à impacter et soumet son plan à l'arbitrage humain.
4. **Test d'échec initial (TDD Rouge)** : Écriture du test unitaire qui matérialise le besoin et prouve la défaillance actuelle du système.
5. **Implémentation minimale (TDD Vert)** : Écriture de la quantité minimale de code nécessaire pour faire passer le test à l'état vert.
6. **Refactoring & Vérification de non-régression** : Nettoyage du code, passage des linters, et exécution de l'intégralité de la suite de tests du dépôt.
7. **Synthèse et consignation d'ADR** : Rédaction du compte rendu honnête, consignation des choix structurants dans `docs/adr/`, et commit Git atomique.

---

## Mise en pratique

### Implémentation d'un extracteur de contexte AST avec contrôle de budget de tokens en Python 3.11

Le programme suivant implémente un analyseur syntaxique d'AST capable d'extraire la signature des classes et fonctions d'un module pour générer un contexte chirurgical sous contrainte stricte de budget de tokens :

```python
"""Module d'ingénierie de contexte : Extracteur d'AST et gestionnaire de budget.

Démontre la compression structurelle de fichiers de code pour l'alimentation
optimale du harnais agentique dans le respect de la Smart Zone.
"""
from dataclasses import dataclass
import ast
import unittest


@dataclass(frozen=True)
class SignatureSymbole:
    type_symbole: str  # "classe" ou "fonction"
    nom: str
    signature: str
    docstring: str


@dataclass(frozen=True)
class ResumeStructurelModule:
    chemin_fichier: str
    symboles: tuple[SignatureSymbole, ...]
    tokens_estimes: int


class InspecteurASTContexte:
    """Analyseur statique extrayant l'ossature d'un code source sans son corps."""

    RATIO_CARACTERES_PAR_TOKEN = 4.0

    @classmethod
    def estimer_tokens(cls, texte: str) -> int:
        return int(len(texte) / cls.RATIO_CARACTERES_PAR_TOKEN)

    @classmethod
    def analyser_source(cls, chemin_fichier: str, code_source: str) -> ResumeStructurelModule:
        arbre = ast.parse(code_source, filename=chemin_fichier)
        symboles: list[SignatureSymbole] = []

        for noeud in arbre.body:
            if isinstance(noeud, ast.ClassDef):
                doc = ast.get_docstring(noeud) or ""
                # Extraire les méthodes publiques de la classe
                methodes = [
                    m.name for m in noeud.body
                    if isinstance(m, (ast.FunctionDef, ast.AsyncFunctionDef))
                    and not m.name.startswith("_")
                ]
                signature = f"class {noeud.name}(méthodes: {', '.join(methodes) or 'aucune'})"
                symboles.append(SignatureSymbole("classe", noeud.name, signature, doc))

            elif isinstance(noeud, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if not noeud.name.startswith("_"):
                    doc = ast.get_docstring(noeud) or ""
                    args = [a.arg for a in noeud.args.args]
                    signature = f"def {noeud.name}({', '.join(args)})"
                    symboles.append(SignatureSymbole("fonction", noeud.name, signature, doc))

        # Génération de la représentation condensée
        lignes_resume = [f"=== MODULE : {chemin_fichier} ==="]
        for s in symboles:
            lignes_resume.append(f"[{s.type_symbole.upper()}] {s.signature}")
            if s.docstring:
                lignes_resume.append(f"  Documentation : {s.docstring.strip().splitlines()[0]}")

        texte_condense = "\n".join(lignes_resume)
        tokens = cls.estimer_tokens(texte_condense)

        return ResumeStructurelModule(
            chemin_fichier=chemin_fichier,
            symboles=tuple(symboles),
            tokens_estimes=tokens,
        )


class GenerateurDossierMission:
    """Assembleur de dossier de mission sous plafond strict de tokens."""

    def __init__(self, plafond_tokens: int = 1500) -> None:
        self.plafond_tokens = plafond_tokens

    def assembler(
        self,
        glossaire_context: str,
        fiche_tranche: str,
        resumes_ast: list[ResumeStructurelModule]
    ) -> str:
        parties = [
            "### 1. GLOSSAIRE DE RÉFÉRENCE",
            glossaire_context.strip(),
            "\n### 2. FICHE DE MISSION",
            fiche_tranche.strip(),
            "\n### 3. STRUCTURE DES MODULES IMPACTÉS (AST)",
        ]
        for r in resumes_ast:
            parties.append(f"--- Fichier : {r.chemin_fichier} ---")
            for s in r.symboles:
                parties.append(f"{s.signature} : {s.docstring}")

        dossier_complet = "\n".join(parties)
        tokens_totaux = InspecteurASTContexte.estimer_tokens(dossier_complet)

        if tokens_totaux > self.plafond_tokens:
            raise ValueError(
                f"Dépassement du budget cognitif : {tokens_totaux} tokens générés "
                f"(plafond fixé à {self.plafond_tokens})"
            )

        return dossier_complet
```

---

### La suite de tests prouvant l'extraction AST et le contrôle budgétaire

```python
class TestInspecteurASTEtBudget(unittest.TestCase):
    """Vérifie la compression AST et l'herméticité du budget de tokens."""

    CODE_EXEMPLE = '''
class ServicePaiement:
    """Gestionnaire souverain des encaissements clients."""
    
    def __init__(self, cle_api: str):
        self._cle = cle_api
        self._compteur = 0

    def debiter_carte(self, montant_centimes: int, jeton: str) -> bool:
        """Débite la carte bancaire via le port configuré."""
        # 50 lignes de code interne d'orchestration complexe
        return True

    def rembourser(self, transaction_id: str) -> bool:
        """Rembourse une transaction clôturée."""
        return True

    def _methode_privee_interne(self):
        pass

def utilitaire_verification_sha(donnees: bytes) -> str:
    """Calcule l'empreinte sécurisée."""
    return "hash"
'''

    def test_compression_ast_efficace(self) -> None:
        resume = InspecteurASTContexte.analyser_source("paiement.py", self.CODE_EXEMPLE)
        
        # Vérification de l'extraction des classes et fonctions publiques
        noms_symboles = [s.nom for s in resume.symboles]
        self.assertIn("ServicePaiement", noms_symboles)
        self.assertIn("utilitaire_verification_sha", noms_symboles)
        self.assertNotIn("_methode_privee_interne", noms_symboles)

        # Vérification du gain de compression
        tokens_bruts = InspecteurASTContexte.estimer_tokens(self.CODE_EXEMPLE)
        self.assertLess(resume.tokens_estimes, tokens_bruts)

    def test_assemblage_dossier_mission_dans_le_budget(self) -> None:
        inspecteur = InspecteurASTContexte()
        resume = inspecteur.analyser_source("paiement.py", self.CODE_EXEMPLE)
        
        generateur = GenerateurDossierMission(plafond_tokens=500)
        dossier = generateur.assembler(
            glossaire_context="Termes : Débit, Remboursement, Jeton.",
            fiche_tranche="Mission : Ajouter le support de la devise USD.",
            resumes_ast=[resume]
        )
        self.assertIn("ServicePaiement", dossier)
        self.assertIn("USD", dossier)

    def test_rejet_depassement_budget(self) -> None:
        inspecteur = InspecteurASTContexte()
        resume = inspecteur.analyser_source("paiement.py", self.CODE_EXEMPLE)
        
        # Plafond volontairement trop bas pour vérifier l'interception
        generateur_trop_strict = GenerateurDossierMission(plafond_tokens=20)
        with self.assertRaises(ValueError) as ctx:
            generateur_trop_strict.assembler(
                glossaire_context="Glossaire lourd...",
                fiche_tranche="Mission...",
                resumes_ast=[resume]
            )
        self.assertIn("Dépassement du budget cognitif", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
```

---

## Exercice d'arbitrage & Corrigé commenté

### Le cas d'ingénierie : L'injection de contexte monolithique et chaotique

Un lead developer débutant sur l'outillage agentique configure le fichier de contexte partagé de son équipe (`AGENTS.md`) pour un microservice de gestion des abonnements. Il propose le contenu suivant :

```markdown
# Instructions pour les agents IA
1. Voici l'intégralité du schéma SQL de production (350 tables collées en texte brut).
2. Voici l'historique complet de nos 400 derniers commits Git.
3. Tu as accès en écriture root à l'ensemble du dépôt et aux serveurs de staging.
4. Si une dépendance manque, installe la dernière version disponible depuis npm.
5. Fais de ton mieux pour corriger les bugs signalés dans les issues GitHub.
```

### La grille d'audit de l'architecte

1. **Saturation immédiate du contexte (*Context Flooding*)** : Coller 350 tables SQL et 400 commits consomme 90 000 tokens avant même la première question, propulsant instantanément l'agent hors de sa Smart Zone.
2. **Absence de frontières d'autorisation** : L'octroi d'accès root et la liberté d'installer des paquets tiers non audités violent les règles d'isolation et exposent la chaîne logistique à des attaques par empoisonnement de paquets (*Dependency Confusion*).
3. **Impossibilité de test local déterministe** : Aucune commande d'oracle de test n'est fournie. L'agent navigue à l'aveugle sans savoir comment prouver la validité de ses modifications.

### Le corrigé commenté

**Décision de l'architecte** : Révocation immédiate et restructuration selon l'architecture en trois couches :

```text
CONSIGNE DE REFACTORING DU HARNAIS :
1. Purger AGENTS.md / CONTEXT.md : Conserver uniquement les 5 invariants du produit,
   le glossaire métier (10 termes) et la commande officielle de test ('pytest tests/unit').
2. Supprimer le dump des 350 tables : Le remplacer par des extracteurs AST ciblés
   activés uniquement sur les modèles concernés par la tranche.
3. Verrouiller les droits d'écriture : Isoler l'agent dans un Git Worktree éphémère
   avec interdiction absolue d'exécuter des commandes réseau ou d'installer des dépendances.
4. Instaurer le protocole d'enquête préalable : L'agent doit fournir un plan borné
   avant toute modification de code.
```

---

## Checklist réflexe du pilote

Avant de déléguer une tranche de développement à un agent, assure-toi de vérifier ces six invariants de harnais :

- [ ] **L'architecture en 3 couches est active** : Les réflexes globaux, les compétences du projet (`.agents/skills/`) et le contexte de runtime sont clairement découplés.
- [ ] **Le masquage (*Shadowing*) est respecté** : Les directives locales du dépôt surchargent prioritairement les configurations globales du poste.
- [ ] **Le budget de tokens est sous contrôle** : La session démarre dans la Smart Zone (< 120k tokens) sans injection massive de fichiers superflus.
- [ ] **L'inspection passe par les AST** : Les structures de code sont résumées par analyse syntaxique avant d'envisager la lecture du code d'implémentation.
- [ ] **Les commandes de test sont fournies** : L'agent dispose d'une commande unique, déterministe et locale pour vérifier son travail.
- [ ] **L'hygiène de fin de session est appliquée** : Les résultats sont consignés dans un ADR ou un commit atomique, et la session est réinitialisée (`/clear`).

---

## Sources et limites

Ce chapitre s'appuie sur les standards d'ingénierie de harnais et d'orchestration agentique :
- **O-MD §4 et §5** ([Manuel d'Orchestration Logicielle](../../sources/originaux/manuel_orchestration_logicielle.md)) : La structure du harnais, les prompts de cadrage, les rôles opérationnels et le protocole en sept messages.
- **I-MD §1.2 à §1.5, §10 et §11.5** ([Manuel d'Ingénierie Logicielle](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md)) : L'architecture en trois couches, la préservation de la Smart Zone, l'analyse statique par AST et la gouvernance par ADR.
- **[Architecture du harnais](../03-annexes/03-architecture-du-harnais.md)** et **[Catalogue des 37 skills](../03-annexes/04-catalogue-des-skills.md)** : Le catalogue d'outillage complet et la politique de précédence.

Pour maîtriser les flux de branches Git, les Git Worktrees pour flottes d'agents et les Pull Requests empilées, poursuis vers le chapitre suivant : **[B05 — Git sans folklore et collaboration agentique](../02-lecture-ingenieure/05-git-et-collaboration.md)**. Pour réviser les concepts fondamentaux sans outillage de programmation, consulte le miroir accessible : **[A04 — Donner du contexte et des limites à l'agent](../01-lecture-accessible/04-harnais-et-contexte.md)**.
