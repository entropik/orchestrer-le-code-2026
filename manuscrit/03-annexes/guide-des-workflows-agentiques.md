# Matrice des 37 skills agentiques

Ce document constitue l'index de référence des 37 compétences (*skills*) de l'écosystème d'ingénierie de Matt Pocock, adaptées pour une pratique agnostique et rigoureuse du code assisté par agents (Antigravity, Claude Code, Cursor, Codex, OpenCode).

Pour dissiper la charge mentale et rendre la pratique prévisible, ces compétences s'organisent en **six entrées thématiques**, précédées du routeur d'aiguillage universel. Chaque compétence fait l'objet d'un **billet d'ingénierie** précisant son rôle, son mode d'invocation, son déclencheur, ses flux et sa règle d'or.

---

{{< ask_matt_simulator >}}

---

## 0. Le Routeur Universel : ask-matt

### [ask-matt](https://github.com/mattpocock/skills/tree/main/skills/engineering/ask-matt)

- **Rôle & Intention** : Aiguilleur universel de session. C'est le système d'exploitation mental de toute la collection. Face à une intention, une anomalie ou un doute, il diagnostique votre situation immédiate, détermine le flux à emprunter et formule la commande exacte à exécuter.
- **Invocation** : `user-invoked` (`disable-model-invocation: true`). Il n'encombre pas le contexte de manière automatique : c'est vous qui l'invoquez explicitement (`/ask-matt [votre situation]`).
- **Quand l'invoquer** : Dès l'ouverture d'une session, au moindre doute méthodologique, ou avant de taper une commande d'agent au hasard.
- **Entrées / Sorties** : Lit votre situation formulée en langage naturel ; produit l'enchaînement ordonné des compétences à mobiliser, la commande immédiate et l'alerte sur le piège à éviter.
- **Règle d'or** : Ne commencez jamais une session dans le flou. Invoquez `/ask-matt` plutôt que de tenter du code ou des prompts improvisés.

---

### La Doctrine d'ask-matt : Dépasser le Vibe Coding

L'erreur la plus coûteuse avec les agents de code consiste à demander directement l'écriture d'une fonctionnalité dans une invite libre. L'agent produit du code plausible, mais sans contrat clair, sans frontières de modules et sans tests à l'interface publique. Dès que la base grandit, cette approche produit de l'entropie, des régressions croisées et une saturation du contexte.

La doctrine d'**`ask-matt`** repose sur un principe cardinal : **toute tâche d'ingénierie emprunte un chemin formel balisé**. La quasi-totalité du travail suit un **ruban principal** (*The Main Flow*), alimenté par **trois voies d'insertion** (*On-ramps*), arbitré par **cinq choix aux frontières de phases** (*Phase boundaries*), et sécurisé par des **outils de déblocage d'urgence**.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        LE RUBAN PRINCIPAL (Main Flow)                  │
│                                                                        │
│   Idée brute ───► /grill-with-docs ───┬───► /to-prd ───► /to-issues    │
│                         │             │                     │          │
│                         │ (Doute UI   │                     ▼          │
│                         │  ou état)   │                  /clear        │
│                         ▼             │                     │          │
│                    /prototype ────────┘                     ▼          │
│                                                     /implement + /tdd  │
│                                                             │          │
│                                                             ▼          │
│                                                          /review       │
└─────────────────────────────────────────────────────────────┼──────────┘
                                                              │
   VOIES D'INSERTION (On-Ramps) :                             ▼
   - Bugs & retours externes ───► /triage ───────────► Ticket prêt (merge)
   - Bug dur ou régression   ───► /diagnosing-bugs ──► Fix + Test rouge
   - Brouillard complet      ───► /wayfinder ────────► Décisions ──► /to-prd
```

#### 1. Le Ruban Principal : De l'Idée à la Production (*Idea → Ship*)

1. **Cadrage amont (`/grill-with-docs`)** : Point d'entrée systématique dans un dépôt Git. L'agent conduit une interview contradictoire, **une question à la fois** avec sa recommandation, après avoir inspecté le code existant. Il met à jour le vocabulaire dans `CONTEXT.md` et consigne les choix structurants dans `docs/adr/`.
2. **Embranchement Prototype (si doute exécutable)** : Si une question ergonomique (UI) ou logique (automate d'états) ne peut être tranchée sur le papier, bifurcation immédiate :
   - `/handoff` vers une session isolée.
   - `/prototype` sur une branche éphémère `prototype/<nom>` pour répondre à la question par du code jetable lancé en une commande.
   - `/handoff` retour pour consigner les acquis dans le fil de discussion principal.
3. **Embranchement Granularité** :
   - **Multi-sessions** : `/to-prd` (synthèse formelle sans ré-interviewer) → `/to-issues` (tranches verticales étanches avec graphe de blocage) → `/clear` pour vider le contexte → session neuve par ticket avec `/implement`.
   - **Mono-session** : `/implement` directement dans la même fenêtre de contexte si la tâche est unitaire et tient largement sous la limite de saturation.
4. **Implémentation sous preuve & Péage** : `/implement` pilote en interne `/tdd` (cycle rouge à la frontière publique → vert → refactor), puis déclenche la revue automatisée `/review` (axe standards + axe respect de la spécification) avant le commit.

#### 2. Les Trois Voies d'Insertion (*On-Ramps*)

Ces flux prennent naissance lors d'événements imprévus et rejoignent ensuite le ruban principal :

- **Bugs et retours non sollicités (`/triage`)** : Utilisé **uniquement** pour les tickets créés par des tiers (utilisateurs, support, alertes). Il contrôle l'antériorité contre `.out-of-scope/`, tente une reproduction minimale et attribue le rôle (`ready-for-agent`, `needs-info`, `wontfix`).
  > **Règle absolue** : Ne triez **jamais** les tickets issus de `/to-issues`. Vos propres tickets sont déjà prêts pour l'agent (*agent-ready*).
- **Bug dur, régression ou test intermittent (`/diagnosing-bugs`)** : Interdiction formelle d'émettre des théories ou de toucher au code avant d'avoir isolé une **commande unique déterministe** qui échoue à 100% sur le bug. L'agent minimise le cas, pose des hypothèses falsifiables, injecte des sondes étiquetées `[DEBUG-xxxx]`, rédige un test de non-régression, corrige à la frontière publique, et passe la main à `/improve-codebase-architecture` si aucune couture (*seam*) n'existait pour isoler le bug.
- **Brouillard complet sur chantier massif (`/wayfinder` / `decision-mapping`)** : Quand l'horizon est trop vaste pour une session, l'agent dresse `DECISION_MAP.md` avec des tickets de décisions (`Research`, `Prototype`, `Grilling`). On résout un ticket par session, clôturé par `/handoff`. Une fois le terrain dégagé, on rejoint le ruban principal à `/to-prd`.

#### 3. L'Arbitrage aux Frontières de Phases (*Phase Boundaries*) & Hygiène de la Smart Zone

La mémoire d'un agent n'est pas infinie. Au-delà de ~100k à 120k tokens (la **Smart Zone**), la précision de raisonnement du modèle s'érode. À la fin de chaque étape, l'ingénieur doit arbitrer entre 5 postures :

| Arbitrage | Quand l'utiliser | Ce qu'il produit |
| :--- | :--- | :--- |
| **Continue** | La tâche courante est modeste et la session reste sous les ~40k-50k tokens. | Zéro friction, continuité immédiate. |
| **`/clear`** | L'étape précédente est archivée dans un artefact pérenne (ex: PRD validé, tickets créés). | Contexte vidé à 100 %, session vierge prête pour `/implement`. |
| **`/handoff`** | Changement de répertoire, de harnais d'agent, ou transmission à un collègue. | Note Markdown temporaire dans `/tmp/` résumant l'état exact et les compétences à appeler. |
| **Sous-agent** | Recherche documentaire ou exploration de code isolée en arrière-plan. | Rapport synthétique injecté dans la session principale sans charger le contexte de tokens inutiles. |
| **`/compact`** | La session approche des 100k tokens avant la fin du cadrage. | Résumé condensé de l'historique pour poursuivre sans dégradation cognitive. |

---

### Exemple Transcript : ask-matt en situation sur le Fil Rouge

Voici une illustration concrète simulant l'aiguillage d'`ask-matt` au sein du domaine de ce manuel (l'atelier d'impression et son moteur de contrôle PDF) :

```text
> UTILISATEUR :
/ask-matt Je veux ajouter un contrôle prépresse automatique des marges de découpe
(bleed de 3 mm) avant de valider un devis d'impression. Par quoi je commence ?

> AGENT (ask-matt) :
Votre intention introduit une nouvelle règle métier bloquante sur un flux existant.
Vous êtes dans un dépôt Git structuré. Vous devez rejoindre le Ruban Principal.

1. PROCHAINE COMMANDE À EXÉCUTER :
   /grill-with-docs "Contrôle prépresse des marges de découpe (bleed 3 mm) au devis"

2. CE QUI VA SE PASSER :
   - L'agent va inspecter votre domaine de devis actuel et vos entités de commande.
   - Il va vous interroger UNE question à la fois : Que faire si le PDF n'a pas de zone
     de fond perdu déclarée (TrimBox/BleedBox) ? Est-ce un rejet strict ou un avertissement
     avec surcoût de massicotage ?
   - Les réponses enrichiront CONTEXT.md (glossaire 'Fond perdu', 'Zone de découpe').
   - Si la règle modifie le calcul du devis de façon irréversible, un ADR sera rédigé
     dans docs/adr/.

3. PIPELINE COMPLET DE VOTRE TÂCHE :
   /grill-with-docs ──► /to-prd ──► /to-issues ──► /clear ──► /implement ──► /review

4. PIÈGE MORTEL À ÉVITER :
   Ne commencez pas à modifier le parseur PDF ni le calcul de devis maintenant.
   Tant que la règle de rejet (strict vs warning) n'est pas tranchée dans l'interview,
   toute implémentation sera contestée par le client.
```

---

## Déploiement : Racine de Projet (.agents/) ou Configuration Globale (~/.) ?

Une interrogation récurrente lors de l'adoption de ces 37 compétences concerne leur point d'ancrage physique : **faut-il installer les skills à la racine de chaque projet Git (sous `.agents/skills/` ou `.claude/`), ou globalement sur sa machine de travail (sous `~/.gemini/` ou `~/.claude/`) ?**

En ingénierie logicielle appliquée aux agents, il ne s'agit pas d'opposer ces deux approches, mais de mettre en œuvre une **architecture hybride en couches** (*Layered Architecture*).

### Tableau comparatif synthétique

| Critère d'évaluation | À la racine du projet (`.agents/skills/`) | Globalement sur la machine (`~/.`) |
| :--- | :--- | :--- |
| **Partage en équipe & Étudiants** | **Immédiat** : un `git clone` suffit pour que tout le monde dispose exactement des mêmes skills. | **Nul** : chaque collaborateur ou apprenant doit installer et configurer sa machine à la main. |
| **Reproductibilité & Versioning Git** | **Parfait** : les compétences évoluent avec les commits du projet et restent calées sur sa version. | **Risque de dérive** : une mise à jour globale non rétrocompatible peut casser un ancien projet. |
| **Spécialisation au contexte** | **Totale** : les skills intègrent les commandes exactes du projet (`pytest`, `vitest`, Hugo, conventions d'ADR). | **Générique** : obligé de rester abstrait pour ne pas créer d'effets de bord sur d'autres projets. |
| **Disponibilité sur nouveaux projets** | Nécessite d'initialiser le dossier `.agents/` sur chaque nouveau dépôt. | **Omniprésent** : disponible instantanément sur n'importe quel scratchpad ou dépôt tiers. |
| **Maintenance multi-dépôts** | Demande un effort de synchronisation si vous gérez 20 dépôts distincts. | **Centralisée** : une seule mise à jour profite instantanément à tous vos terminaux locaux. |
| **CI/CD & Agents autonomes** | Les runners distants (GitHub Actions) et conteneurs Docker y ont accès immédiatement. | Inexistant sur les machines distantes ou les serveurs d'intégration continue. |

---

### 1. Pourquoi l'installation à la racine (`.agents/`) est indispensable pour les équipes et les formations

Dans le cadre d'un enseignement technique, de formations partagées (comme sur *savoirs.keredit.com*) ou d'un travail en équipe :

1. **L'élimination radicale du syndrome « Ça marche sur ma machine »** :
   Si vos compétences résident uniquement dans votre répertoire personnel `~/`, vous faites une démonstration fluide de `/grill-with-docs` en session. Mais dès qu'un apprenant ou un collègue clone le dépôt et tente la même instruction, son agent échoue : soit il ignore la commande, soit il improvise du code non encadré.
2. **Le concept de « Repository-as-Code »** :
   En 2026, un dépôt Git moderne ne se limite plus à héberger du code source passif : il embarque son propre **harnais d'orchestration** (`.agents/skills/`, `.agents/rules/`, `CONTEXT.md`). Quiconque rejoint le dépôt hérite instantanément de la discipline, des garde-fous et des rituels méthodologiques de l'équipe.
3. **L'alignement sur les outils réels du projet** :
   Chaque projet possède ses propres invariants techniques. Sur ce manuel, la validation repose sur `python3.11 -m unittest` et la compilation sur Hugo. Un skill local `/implement` sait précisément quelles commandes de test exécuter pour administrer la preuve, alors qu'un skill global devrait deviner ou interroger l'utilisateur.

---

### 2. Pourquoi la configuration globale (`~/.`) reste utile au quotidien

Sur votre propre poste de développement personnel :

1. **L'ancrage des réflexes cognitifs universels** :
   Certaines compétences sont purement méthodologiques et indépendantes de tout langage ou framework :
   - `/ask-matt` (l'aiguilleur réflexe pour choisir la bonne voie),
   - `/grill-me` (l'interview exploratoire avant même la création d'un répertoire Git),
   - `/wait-what` (le bouton d'arrêt d'urgence anti-jargon en cas d'égarement de l'agent),
   - `/teach` (l'assistant interactif d'apprentissage personnel).
2. **Le confort immédiat sur les projets ponctuels** :
   Dès que vous ouvrez un terminal dans `/tmp/` pour tester une idée rapide ou que vous clonez une bibliothèque open-source tierce pour inspecter son code, vous conservez vos habitudes sans devoir initialiser une configuration locale.

---

### 3. La bonne pratique : Le Modèle Hybride en 3 Couches

Les moteurs d'agents contemporains (Antigravity, Claude Code, Cursor, Codex) appliquent une **règle de précédence stricte** : **le local surcharge toujours le global (*shadowing*)**.

Si une compétence `/ask-matt` est définie dans votre `~/.` mais qu'un fichier `.agents/skills/ask-matt/SKILL.md` est présent à la racine du dépôt actif, c'est la version locale du projet qui prend le dessus.

```text
┌────────────────────────────────────────────────────────────────────────┐
│ 1. COUCHE GLOBALE (Machine développeur : ~/.gemini/ ou ~/.claude/)    │
│    - Rôle : Vos réflexes personnels, navigation et apprentissage      │
│    - Exemples : ask-matt, grill-me, wait-what, teach, obsidian-vault  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼ (Surcharge locale prioritaire)
┌────────────────────────────────────────────────────────────────────────┐
│ 2. COUCHE PROJET (Dépôt Git : .agents/skills/ à la racine)             │
│    - Rôle : Gouvernance d'équipe, contrats et preuves de fabrication  │
│    - Exemples : setup-skills, grill-with-docs, to-prd, to-issues,     │
│                 implement, tdd, review, diagnosing-bugs, wizard       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 3. COUCHE RUNTIME / MÉMOIRE VIVE (CONTEXT.md, docs/adr/, tickets)     │
│    - Rôle : Les artefacts vivants produits par les agents et l'équipe │
│    - Exemples : Modèle de domaine, ADRs actés, backlog d'issues       │
└────────────────────────────────────────────────────────────────────────┘
```

#### En résumé pour votre pratique :

- **Pour vos dépôts partagés, vos projets clients et vos formations** : Déposez systématiquement les compétences clés sous **`.agents/skills/` à la racine** du projet, versionnées dans Git.
- **Pour votre poste individuel** : Installez la collection complète en global (`claude plugins install mattpocock-skills` ou dans votre dossier utilisateur). Vous profiterez du filet de sécurité partout, tout en laissant vos projets spécialiser leurs propres règles.

---

## Entrée 1 : Gouvernance du Dépôt & Cadrage Amont

Cette entrée rassemble les compétences qui posent le cadre du projet, vérifient l'existant avant toute création de code, et tiennent à jour la modélisation métier vivante.

### [setup-matt-pocock-skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/setup-matt-pocock-skills)

- **Rôle & Intention** : Configure le dépôt pour l'ensemble des compétences d'ingénierie. À exécuter une seule fois lors de la prise en main d'un projet.
- **Invocation** : `user-invoked`.
- **Quand l'invoquer** : À l'initialisation d'un nouveau dépôt ou avant d'utiliser les compétences d'ingénierie sur une base existante.
- **Entrées / Sorties** : Explore le gestionnaire de tickets (GitHub, GitLab, ou Markdown local sous `.scratch/`), configure les étiquettes de triage canoniques (`needs-triage`, `ready-for-agent`, etc.) et pose l'arborescence documentaire (`CONTEXT.md`, `docs/adr/`, `docs/agents/`).
- **Règle d'or** : Les compétences aval dépendent de cette convention pour savoir où lire et publier leurs artefacts. Ne la sautez jamais.

### [grill-with-docs](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)

- **Rôle & Intention** : Le point d'entrée par excellence pour toute nouvelle fonctionnalité dans une base de code existante. Combine une interview contradictoire sans complaisance avec la tenue continue du modèle de domaine.
- **Invocation** : `user-invoked` (`/grill-with-docs [votre intention]`).
- **Quand l'invoquer** : Dès qu'une idée émerge et que vous disposez d'un dépôt Git.
- **Entrées / Sorties** : Lit le code existant et `CONTEXT.md`. Met à jour `CONTEXT.md` au fil des clarifications. Rédige un ADR dans `docs/adr/` lorsqu'une décision lourde et difficilement réversible est actée.
- **Règle d'or** : L'agent pose ses questions **une par une**, avec sa réponse recommandée, après avoir fouillé le code. Aucun code de production n'est écrit durant cette phase.

### [grill-me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me)

- **Rôle & Intention** : Interview de cadrage sans état (*stateless*).
- **Invocation** : `user-invoked` (`/grill-me`).
- **Quand l'invoquer** : Lorsque vous voulez challenger un concept, une idée de startup ou un plan abstrait **sans base de code**.
- **Entrées / Sorties** : Aucun fichier local n'est modifié ; l'exploration se déroule intégralement dans le fil de conversation.
- **Règle d'or** : Si un dépôt existe, utilisez toujours `grill-with-docs`. Réservez `grill-me` aux réflexions préliminaires hors dépôt.

### [grilling](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)

- **Rôle & Intention** : Le moteur unitaire d'interview contradictoire qui anime les compétences de cadrage.
- **Invocation** : `model-invoked` (appelé par `grill-with-docs`, `decision-mapping`, `triage`).
- **Quand l'invoquer** : Invoqué par d'autres compétences pour traquer les ambiguïtés et lever les non-dits.
- **Règle d'or** : Interdiction de soumettre une liste de cinq questions simultanées (effet de sidération). Une seule question à la fois, avec réponse recommandée, en attendant la réponse avant d'enchaîner.

### [domain-modeling](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)

- **Rôle & Intention** : Discipline active de Domain-Driven Design (DDD). Aligne le vocabulaire du code sur les concepts métier réels.
- **Invocation** : `model-invoked`.
- **Quand l'invoquer** : Dès qu'un terme imprécis ou surchargé apparaît, ou qu'une décision architecturale est arrêtée.
- **Entrées / Sorties** : Entretient `CONTEXT.md` (glossaire strict sans code ni spec) et `docs/adr/`.
- **Règle d'or** : Un ADR n'est rédigé que s'il réunit trois critères stricts : difficile à inverser, surprenant sans contexte, et issu d'un compromis réel.

### [decision-mapping / wayfinder](https://github.com/mattpocock/skills/tree/main/skills/in-progress/decision-mapping)

- **Rôle & Intention** : Exploration méthodique du « brouillard de guerre » pour les chantiers complexes dépassant le cadre d'une seule session de cadrage.
- **Invocation** : `user-invoked`.
- **Quand l'invoquer** : Face à une initiative vaste, incertaine ou comportant de multiples inconnues architecturales.
- **Entrées / Sorties** : Crée et maintient `DECISION_MAP.md` découpé en tickets d'investigation typés (`Research`, `Prototype`, `Grilling`).
- **Règle d'or** : Une session = un seul ticket résolu. Chaque session se clôture obligatoirement par `/handoff` pour repartir sur une session neuve.

### [loop-me](https://github.com/mattpocock/skills/tree/main/skills/in-progress/loop-me)

- **Rôle & Intention** : Cadrage et spécification de boucles d'automatisation récurrentes.
- **Invocation** : `user-invoked`.
- **Quand l'invoquer** : Pour automatiser une tâche périodique ou récurrente dans votre quotidien de développeur.
- **Entrées / Sorties** : Produit une spécification dans `workflows/*.md` avec déclencheur (*trigger*), brief et points de contrôle (*checkpoints*).
- **Règle d'or** : Principe du « Push right » : différer l'intervention humaine le plus loin possible pour ne lui soumettre qu'une décision finale synthétique.

---

## Entrée 2 : Étude & Spécification

Cette entrée regroupe les compétences qui convertissent la réflexion issue du cadrage en artefacts techniques formels, sans recommencer d'interview.

### [prototype](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype)

- **Rôle & Intention** : Fabrication de code jetable destiné exclusivement à répondre à une question de conception précise.
- **Invocation** : `model-invoked` ou `user-invoked` (`/prototype`).
- **Quand l'invoquer** : Doute sur l'ergonomie d'une interface (branche *UI*) ou incertitude sur la viabilité d'une machine d'états (branche *Logic*).
- **Entrées / Sorties** : Produit un mini-programme jetable lancé en une seule commande, sans persistance réelle ni suite de tests.
- **Règle d'or** : Seule la réponse apprise est conservée (dans un ADR ou une note). Le code du prototype est immédiatement détruit ou absorbé, jamais conservé tel quel.

### [to-prd](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-prd)

- **Rôle & Intention** : Synthétise le fil de discussion issu du grilling en document formel de spécification (PRD).
- **Invocation** : `user-invoked` (`/to-prd`).
- **Quand l'invoquer** : Dès que l'interview `/grill-with-docs` a épuisé toutes les zones d'ombre.
- **Entrées / Sorties** : Rédige et publie le PRD : problème, solution, User Stories numérotées, décisions d'implémentation, frontières de tests et hors périmètre (*out of scope*).
- **Règle d'or** : **Pas de ré-interview**. L'agent synthétise les acquis sans relancer de questions.

### [to-issues](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-issues)

- **Rôle & Intention** : Découpe un PRD ou une spécification en tickets unitaires indépendants.
- **Invocation** : `user-invoked` (`/to-issues`).
- **Quand l'invoquer** : Immédiatement après `/to-prd`.
- **Entrées / Sorties** : Publie les tickets sur l'issue tracker configuré (GitHub, GitLab, ou Markdown local).
- **Règle d'or** : Chaque ticket est une **tranche verticale** (*tracer bullet* : traverse schéma, logique, API, UI et test de bout en bout), jamais une tranche horizontale par couche. Ordonnancement strict par dépendances bloquantes.

### [to-questionnaire](https://github.com/mattpocock/skills/tree/main/skills/productivity/to-questionnaire)

- **Rôle & Intention** : Lève les blocages d'exigences lorsque l'information n'est ni dans le code ni dans la tête du développeur, mais chez un tiers extérieur (client, expert métier, collègue).
- **Invocation** : `user-invoked` (`/to-questionnaire`).
- **Quand l'invoquer** : Dès qu'une question du grilling fait apparaître une zone d'ombre commerciale, juridique ou organisationnelle insoluble en interne.
- **Entrées / Sorties** : L'agent vous interroge brièvement sur le destinataire et le besoin d'arbitrage, puis génère un questionnaire Markdown prêt à être transmis.
- **Règle d'or** : Ne supposez jamais la réponse d'un tiers dans le code. Envoyez le questionnaire et attendez le retour pour réinjecter les faits dans `/grill-with-docs`.

---

## Entrée 3 : Fabrication & Preuves d'Ingénierie

Cette entrée gouverne la phase de production du code, sous la contrainte exclusive de preuves observables et d'une architecture modulaire profonde.

### [implement](https://github.com/mattpocock/skills/tree/main/skills/engineering/implement)

- **Rôle & Intention** : Réalisation bornée et étanche d'un ticket spécifique.
- **Invocation** : `user-invoked` (`/implement`).
- **Quand l'invoquer** : À l'ouverture d'une session neuve dédiée à un ticket unitaire issu de `/to-issues`.
- **Entrées / Sorties** : Travaille dans un arbre de travail Git dédié (*worktree*). Lit le ticket et le PRD.
- **Règle d'or** : Chaque ligne modifiée doit tracer directement à la spécification. Ne pousse jamais sur le dépôt distant et n'ouvre pas de PR sans autorisation explicite.

### [tdd](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)

- **Rôle & Intention** : Développement piloté par les tests, un comportement vertical à la fois.
- **Invocation** : `model-invoked` (appelé par `implement`) ou `user-invoked` (`/tdd`).
- **Quand l'invoquer** : Pour chaque comportement métier observable à implémenter.
- **Entrées / Sorties** : Cycle Rouge (test échouant pour la bonne raison à la frontière publique) $	o$ Vert (code minimal pour passer) $	o$ Refactor (nettoyage sous protection du test).
- **Règle d'or** : L'assertion doit porter sur l'interface publique stable, jamais sur les détails privés d'implémentation ou des mocks artificiels.

### [codebase-design](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design)

- **Rôle & Intention** : Référentiel de conception des **modules profonds** (*deep modules*).
- **Invocation** : `model-invoked`.
- **Notions clés** : Module, Interface, Profondeur (*depth*), Couture (*seam*), Adaptateur, Levier (*leverage*), Localité.
- **Règle d'or** : Appliquer le **test de suppression** : si supprimer le module fait disparaître la complexité, c'était un passe-plat superficiel. Si la complexité réapparaît chez $N$ appelants, le module est légitime.

### [migrate-to-shoehorn](https://github.com/mattpocock/skills/tree/main/skills/misc/migrate-to-shoehorn)

- **Rôle & Intention** : Assainissement des suites de tests TypeScript.
- **Invocation** : `user-invoked` ou `model-invoked`.
- **Quand l'invoquer** : Détection d'assertions de type risquées (`as MyType`) dans les fixtures de test.
- **Règle d'or** : Remplace les castings aveugles par des données partielles sûres via `@total-typescript/shoehorn`.

---

## Entrée 4 : Contrôle, Diagnostic & Santé du Code

Cette entrée réunit les barrières de péage qualité, le protocole de diagnostic scientifique des anomalies et l'entretien préventif de l'architecture.

### [review](https://github.com/mattpocock/skills/tree/main/skills/in-progress/review)

- **Rôle & Intention** : La barrière de péage avant toute intégration ou ouverture de PR.
- **Invocation** : `user-invoked` (`/review`).
- **Quand l'invoquer** : À la fin de l'implémentation d'un ticket, avant de committer ou de fusionner.
- **Entrées / Sorties** : Lance deux sous-agents indépendants en parallèle :
  - *Axe Standards* : conformité aux règles `AGENTS.md` du dépôt, style et modularité.
  - *Axe Spec* : stricte réponse au besoin sans aucun ajout superflu.
- **Règle d'or** : Les sous-agents sont strictement en lecture seule. Ils ne corrigent pas le code, ils fournissent un rapport précis avec références de lignes.

### [diagnosing-bugs](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)

- **Rôle & Intention** : Protocole d'investigation scientifique en 6 phases pour les bogues ardus et régressions de performance.
- **Invocation** : `model-invoked` ou `user-invoked` (`/diagnosing-bugs`).
- **Quand l'invoquer** : « Ça plante », « Comportement anormal », « Régression de vitesse ».
- **Les 6 phases** :
  1. *Boucle de rétroaction rouge déterministe* (test, curl, trace rejouée).
  2. *Minimisation* du scénario à la charge utile minimale.
  3. *3 à 5 hypothèses falsifiables* classées avant toute retouche.
  4. *Sondes ciblées* taguées `[DEBUG-xxxx]`.
  5. *Test de non-régression* à la bonne couture, puis correction.
  6. *Nettoyage* des sondes et bilan d'architecture.
- **Règle d'or absolue** : **Interdiction de lire le code pour formuler des hypothèses tant qu'une commande ne reproduit pas le bogue en rouge de façon nette.**

### [improve-codebase-architecture](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture)

- **Rôle & Intention** : Audit proactif de la dette technique et recherche d'opportunités d'épaississement de modules.
- **Invocation** : `user-invoked` (`/improve-codebase-architecture`).
- **Quand l'invoquer** : Lors des temps calmes ou quand l'ajout de fonctionnalités devient fastidieux.
- **Entrées / Sorties** : Génère un rapport HTML interactif autonome dans `/tmp/` (Mermaid + Tailwind) illustrant les refactorings recommandés avant/après, puis lance un grilling sur le candidat choisi.
- **Règle d'or** : Regroupe la logique éparpillée pour maximiser la localité et rendre le code naturellement navigable pour les agents.

### [resolving-merge-conflicts](https://github.com/mattpocock/skills/tree/main/skills/engineering/resolving-merge-conflicts)

- **Rôle & Intention** : Résolution causale des conflits de fusion et de rebase Git.
- **Invocation** : `model-invoked` lors d'un conflit Git en cours.
- **Quand l'invoquer** : Dès qu'un rebase ou un merge s'arrête sur un conflit.
- **Règle d'or** : Remonter aux sources primaires (commits, PRs d'origine) pour comprendre l'intention des deux branches. Ne jamais résoudre en aveugle ; valider par la suite de tests complète avant de clore.

### [triage](https://github.com/mattpocock/skills/tree/main/skills/engineering/triage)

- **Rôle & Intention** : Qualification des signalements et PRs externes via une machine à états stricte.
- **Invocation** : `user-invoked` (`/triage`).
- **Quand l'invoquer** : Pour traiter le flux d'issues et de contributions extérieures.
- **Entrées / Sorties** : Vérifie la non-redondance dans `.out-of-scope/`, reproduit l'anomalie ou exécute la PR, et attribue le rôle (`needs-info`, `ready-for-agent`, `wontfix`).
- **Règle d'or** : Ne pas trier les issues issues de `/to-issues` (elles sont déjà prêtes pour l'agent). Réserver le triage aux flux non filtrés arrivant de l'extérieur.

---

## Entrée 5 : Outillage Opérationnel & Sécurité

Cette entrée rassemble les garde-fous de sécurité, les assistants guidés pour les démarches manuelles délicates, le recadrage anti-jargon et l'outillage de contexte.

### [wait-what](https://github.com/mattpocock/skills/tree/main/skills/productivity/wait-what)

- **Rôle & Intention** : Arrêt d'urgence et recadrage immédiat lorsque l'agent part dans du jargon, dérive ou produit une réponse incompréhensible.
- **Invocation** : `user-invoked` (`/wait-what`).
- **Quand l'invoquer** : En cours de session, à l'intérieur de n'importe quel autre skill, dès que vous perdez le fil de l'explication de l'agent.
- **Entrées / Sorties** : L'agent s'arrête instantanément, examine ce qui a causé l'incompréhension, et ré-explique sa position en français simple et direct, en s'appuyant uniquement sur le vocabulaire validé dans `CONTEXT.md`.
- **Règle d'or** : Ne débattez jamais avec un agent qui a commencé à halluciner ou à jargonner. Invoquez `/wait-what` pour rétablir une base saine avant de continuer.

### [wizard](https://github.com/mattpocock/skills/tree/main/skills/in-progress/wizard)

- **Rôle & Intention** : Générateur de scripts bash interactifs guidant un opérateur humain dans des procédures manuelles fastidieuses.
- **Invocation** : `user-invoked`.
- **Quand l'invoquer** : Configurations de services tiers (Stripe, Cloudflare, secrets GitHub), migrations sensibles de données, bascules d'état irréversibles.
- **Entrées / Sorties** : Génère un script bash soigné (barre de progression, saisie masquée des clés secrètes, ouverture automatique des URLs, écriture dans `.env`).
- **Règle d'or** : Éphémère par défaut, détruit une fois la procédure validée, sauf demande explicite d'archivage dans `scripts/`.

### [git-guardrails-claude-code](https://github.com/mattpocock/skills/tree/main/skills/misc/git-guardrails-claude-code)

- **Rôle & Intention** : Crochets de sécurité interceptant les commandes Git destructrices d'un agent autonome.
- **Invocation** : Installation de hooks.
- **Règle d'or** : Bloque impitoyablement `push --force`, `reset --hard`, `clean -fd` et suppressions brutales de branches.

### [setup-pre-commit](https://github.com/mattpocock/skills/tree/main/skills/misc/setup-pre-commit)

- **Rôle & Intention** : Mise en place de contrôles automatisés rapides avant chaque commit Git.
- **Invocation** : `user-invoked`.
- **Entrées / Sorties** : Configure Husky, lint-staged, le formatage Prettier, le typage et les tests ciblés.
- **Règle d'or** : Empêche l'introduction de code mal formaté ou cassé dans l'historique local.

### [handoff](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff)

- **Rôle & Intention** : Passerelle inter-sessions pour vider le contexte conversationnel sans perdre les acquis.
- **Invocation** : `user-invoked` (`/handoff`).
- **Quand l'invoquer** : Dès qu'une session approche des 100k tokens ou lors d'une bifurcation vers un prototype.
- **Entrées / Sorties** : Compacte la conversation dans un fichier Markdown temporaire dans `/tmp/` (hors dépôt), avec liste des compétences recommandées pour la session suivante.
- **Règle d'or** : Ne stockez jamais de handoff dans le dépôt Git ; utilisez `/tmp/`.

### [writing-great-skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-great-skills)

- **Rôle & Intention** : Le traité d'ingénierie des compétences d'agents.
- **Invocation** : Document de référence.
- **Principes clés** : Hiérarchie d'information (étapes directes vs références externalisées), divulgation progressive, élimination sans pitié des phrases creuses (*no-ops*), mots directeurs (*leading words*).
- **Règle d'or** : Une compétence sert à arracher du déterminisme à un système stochastique. Sa prévisibilité prime sur tout.

### [find-skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)

- **Rôle & Intention** : Outil de découverte et d'installation de compétences d'agents issues de la communauté.
- **Invocation** : `user-invoked`.

---

## Entrée 6 : Pédagogie, Rédaction & Gestion des Savoirs

Cette entrée outille l'enseignement technique, la génération d'exercices et la chaîne complète de publication éditoriale (utilisée pour ce manuel et *savoirs.keredit.com*).

### [teach](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach)

- **Rôle & Intention** : Enseignement interactif d'un concept technique où le workspace sert d'atelier d'expérimentation.
- **Invocation** : `user-invoked`.

### [scaffold-exercises](https://github.com/mattpocock/skills/tree/main/skills/misc/scaffold-exercises)

- **Rôle & Intention** : Générateur de structures d'exercices de cours (énoncé, indices, solution, suite de tests de validation).
- **Invocation** : `user-invoked`.

### [writing-fragments](https://github.com/mattpocock/skills/tree/main/skills/in-progress/writing-fragments)

- **Rôle & Intention** : Première phase de la chaîne de rédaction : collecte brute d'intuitions, de faits et d'exemples sans souci de plan ni de style.
- **Invocation** : `user-invoked`.

### [writing-beats](https://github.com/mattpocock/skills/tree/main/skills/in-progress/writing-beats)

- **Rôle & Intention** : Deuxième phase : assemblage du matériau brut en pulsations logiques (*beats*).
- **Invocation** : `user-invoked`.
- **Règle d'or** : Chaque notion doit être posée et définie avant qu'une pulsation suivante ne s'appuie dessus.

### [writing-shape](https://github.com/mattpocock/skills/tree/main/skills/in-progress/writing-shape)

- **Rôle & Intention** : Troisième phase : façonnage rédigé, paragraphe par paragraphe, à partir des pulsations validées.
- **Invocation** : `user-invoked`.

### [edit-article](https://github.com/mattpocock/skills/tree/main/skills/personal/edit-article)

- **Rôle & Intention** : Quatrième phase : ciselage éditorial, resserrement de la prose et élimination des tournures passives.
- **Invocation** : `user-invoked`.

### [obsidian-vault](https://github.com/mattpocock/skills/tree/main/skills/personal/obsidian-vault)

- **Rôle & Intention** : Organisation et maillage de la base de connaissances personnelle en Markdown (liens wiki, notes d'index).
- **Invocation** : `user-invoked`.

---

## Compétences Absorbées ou Dépréciées

- **design-an-interface** : absorbé par [`codebase-design`](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design) et son patron de conception parallèle *design-it-twice*.
- **request-refactor-plan** : remplacé par le binôme [`improve-codebase-architecture`](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture) (diagnostic visuel) et [`to-issues`](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-issues) (découpage unitaire).
- **ubiquitous-language** : absorbé par [`domain-modeling`](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling) et la tenue de `CONTEXT.md`.
- **qa** : remplacé par l'usage conjoint de [`triage`](https://github.com/mattpocock/skills/tree/main/skills/engineering/triage) et [`diagnosing-bugs`](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs).

---

## Arbre d'Aiguillage des Workflows

```text
Situation de départ ?
 │
 ├── "J'ai une idée de fonctionnalité"
 │    └── Brouillard ou incertitudes majeures ?
 │         ├── Oui  ──> /decision-mapping  (lever le brouillard)
 │         └── Non  ──> /grill-with-docs   (flux nominal)
 │
 ├── "Quelque chose est cassé ou trop lent"
 │    └── /diagnosing-bugs                (boucle rouge obligatoire)
 │
 ├── "Le code devient rigide ou superficiel"
 │    └── /improve-codebase-architecture  (audit HTML & modules profonds)
 │
 ├── "Des signalements ou PRs arrivent"
 │    └── /triage                         (qualification & briefs d'agents)
 │
 ├── "J'ai un conflit de fusion Git"
 │    └── /resolving-merge-conflicts      (comprendre les deux intentions)
 │
 └── "Je prépare un cours ou un article"
      ├── Cours / Exercices ──> /scaffold-exercises puis /teach
      └── Article / Manuel  ──> /writing-fragments -> beats -> shape -> edit
```

---

## Les Trames d'Exécution par Cas d'Usage

### Cas 1 : Nouvelle Fonctionnalité (Flux nominal complet)

```text
┌────────────────────────────────────┐
│             Idée brute             │
└──────────────────┬─────────────────┘
                   │
                   ▼
┌────────────────────────────────────┐
│          /grill-with-docs          ├◄──Accord─complet─────┐
└──────────────────┬─────────────────┘        │             │
     Doute ergonomique ou d'état              │             │
                   ▼                          │             ▼
┌────────────────────────────────────┐        │        ┌─────────┐
│        /prototype (jetable)        ├────────┘        │ /to-prd │
└────────────────────────────────────┘                 └────┬────┘
                                                            │
┌────────────────────────────────────┐                      │
│    /to-issues (Tracer bullets)     │◄─────────────────────┘
└──────────────────┬─────────────────┘
                   │
                   ▼
┌────────────────────────────────────┐
│  Reset Contexte / Session fraîche  │
└──────────────────┬─────────────────┘
                   │
                   ▼
┌────────────────────────────────────┐
│       /implement (Ticket N)        │
└──────────────────┬─────────────────┘
                   │
                   ▼
┌────────────────────────────────────┐
│  /tdd (Rouge -> Vert -> Refactor)  │
└──────────────────┬─────────────────┘
                   │
                   ▼
┌────────────────────────────────────┐
│ /review (Axe Standards + Axe Spec) │
└──────────────────┬─────────────────┘
                Validé
                   ▼
┌────────────────────────────────────┐
│         Merge du ticket N          │
└────────────────────────────────────┘
```

1. **Étape 1 : Cadrer par l'interview (`/grill-with-docs`)** : L'agent pose une question à la fois avec sa réponse recommandée. Il aligne les termes sur `CONTEXT.md` et crée un ADR pour tout choix difficilement réversible.
2. **Étape 2 (Optionnelle) : Lever un doute ponctuel (`/prototype`)** : Code jetable sans persistance, démarré en une commande pour lever un doute UI ou d'état. Seule la réponse est conservée.
3. **Étape 3 : Spécifier sans ré-interviewer (`/to-prd`)** : Synthèse sans ré-interview en PRD formel (User Stories exhaustives, invariants, frontières de test).
4. **Étape 4 : Découper en tranches verticales (`/to-issues`)** : Découpage en *tracer bullets* (traversant schéma, logique, API, UI et test).
5. **Étape 5 : Implémenter sous preuve (`/implement` + `/tdd`)** : Session vierge par ticket dans un worktree dédié. Cycle TDD strict à l'interface publique.
6. **Étape 6 : Contrôler à la barrière de péage (`/review`)** : Relecture automatisée par deux sous-agents indépendants (Standards et Spécification).

### Cas 2 : Gros Chantier & Brouillard de Guerre

1. **Entrée : `/decision-mapping`** : Génération d'un `DECISION_MAP.md` matérialisant la frontière du brouillard avec des tickets typés (`Research`, `Prototype`, `Grilling`).
2. **Exécution unitaire** : Une session = un seul ticket résolu. Clôture systématique par `/handoff` pour forker vers une session fraîche.
3. **Sortie du brouillard** : Quand la trajectoire est dégagée, bascule vers le flux nominal : `/to-prd` puis `/to-issues`.

### Cas 3 : Débogage Dur ou Régression de Performance

```text
┌────────────────┐     ┌────────────────┐     ┌────────────────┐
│ 1. Boucle      │     │ 2. Minimiser   │     │ 3. 3-5         │
│    rouge       ├───> │    le cas      ├───> │    hypothèses  │
│    déterministe│     │    reproductible│    │    falsifiables│
└────────────────┘     └────────────────┘     └───────┬────────┘
                                                      │
┌────────────────┐     ┌────────────────┐             │
│ 6. Nettoyage   │     │ 5. Fix +       │             ▼
│    & retour    │<─── │    test de     │<────┌────────────────┐
│    architecture│     │    régression  │     │ 4. Sondes      │
└────────────────┘     └────────────────┘     │    étiquetées  │
                                              └────────────────┘
```

1. **Phase 1 — Boucle de rétroaction rouge étanche** : Obligation d'obtenir une commande qui échoue de façon nette sur le symptôme avant toute analyse de code.
2. **Phase 2 — Minimiser** : Réduire le scénario à la plus petite charge utile provoquant la panne.
3. **Phase 3 — 3 à 5 hypothèses falsifiables** : *"Si X est la cause, alors changer Y fera disparaître l'erreur"*.
4. **Phase 4 — Sondes étiquetées** : Logs tracés sous la forme `[DEBUG-xxxx]` (zéro log orphelin).
5. **Phase 5 — Test de non-régression + Fix** : Test placé sur la couture publique, correction minimale, passage au vert.
6. **Phase 6 — Nettoyage & Bilan** : Suppression des sondes via `grep`. Si le bogue a révélé une faiblesse d'architecture, passage de relais à `/improve-codebase-architecture`.

### Cas 4 : Amélioration Continue & Architecture Profonde

1. **Entrée : `/improve-codebase-architecture`** : Audit automatique repérant les modules superficiels et le manque de localité ; génération d'un rapport HTML visuel dans `/tmp/` avec diagrammes Mermaid.
2. **Sélection et Cadrage** : Choix d'un candidat et lancement de `/grilling` adossé à `/codebase-design`. Application du **test de suppression** : supprimer le module concentre-t-il la complexité ou la disperse-t-il chez les appelants ?
3. **Enregistrement** : Mise à jour de `CONTEXT.md` et formalisation d'un ADR via `/domain-modeling`.

### Cas 5 : Gestion des Flux Entrants

1. **Triage automatique d'issues et PRs : `/triage`** : Vérifie l'antériorité contre `.out-of-scope/`, reproduit l'anomalie ou teste la PR, et attribue le rôle (`needs-info`, `ready-for-agent`, `wontfix`).
2. **Résolution de conflits Git : `/resolving-merge-conflicts`** : Analyse les intentions des deux branches, préserve les contrats et valide par la suite de tests avant le commit de fusion.

### Cas 6 : Pédagogie & Rédaction Technique (Pour *savoirs.keredit.com*)

1. **Ateliers et cours** : `/scaffold-exercises` pour les arborescences d'exercices et `/teach` pour la guidance interactive.
2. **Chaîne de publication** : `/writing-fragments` (matériau brut) $	o$ `/writing-beats` (progression rythmique) $	o$ `/writing-shape` (façonnage des paragraphes) $	o$ `/edit-article` (ciselage éditorial).

### Cas 7 : Initialisation & Gouvernance Réelle d'un Dépôt (Le Jalon 1 Pas à Pas)

Ce cas concret retrace l'exécution réelle du **Jalon 1** menée sur ce dépôt même (*dogfooding* d'ingénierie). Il illustre chronologiquement comment poser une gouvernance irréprochable avant de créer la moindre ligne de code de production.

```text
┌────────────────────────────────────────────────────────────────────────┐
│               LE JALON 1 EN ACTION SUR CE DÉPÔT                        │
│                                                                        │
│ 1. Aiguillage initial ──────► /ask-matt (Constat : besoin de cadre)    │
│                                       │                                │
│ 2. Modélisation de domaine ─► CONTEXT.md (Glossaire strict & _Avoid_) │
│                                       │                                │
│ 3. Arbitrage engageant ─────► docs/adr/0001-harnais-en-trois-couches.md│
│                                       │                                │
│ 4. Outillage opérationnel ──► .agents/skills/ (37 skills déployés)     │
│                                       │                                │
│ 5. Preuves observables ─────► 26 tests unitaires OK + Build Hugo       │
│                                       │                                │
│ 6. Publication & Traçabilité► Git commit, push, Cloudflare Pages HTTP 200
└────────────────────────────────────────────────────────────────────────┘
```

#### Étape 1 : Le Diagnostic Initial (`/ask-matt`)

- **Constat** : Un dépôt sans cadre documentaire ni invariants explicites incite les agents à inventer leur propre vocabulaire, à mélanger les couches d'abstraction et à disperser les scripts dans des dossiers arbitraires.
- **Orientation de l'aiguilleur** : Invocation immédiate des compétences de gouvernance amont : `setup-matt-pocock-skills` et `domain-modeling`.
- **Règle d'or appliquée** : Aucune écriture de code tant que le lexique partagé et l'arborescence documentaire ne sont pas scellés.

#### Étape 2 : Établir le Modèle de Domaine (`CONTEXT.md`)

- **Principe DDD** : Rédaction du fichier racine `CONTEXT.md` respectant le format strict de Matt Pocock.
- **Règles d'écriture** :
  - Définir uniquement ce que le terme **est** (une à deux phrases maximum), jamais ce qu'il fait.
  - Bannir impitoyablement les synonymes ambigus sous la clause `_Avoid_` :
    - *Bon à Tirer (BAT)* : Épreuve contractuelle formelle validée par le client avant l'engagement des machines. `_Avoid_ : Validation client, signature, confirmation.`
    - *Fond Perdu (Bleed)* : Zone de 3 mm extérieure à la boîte de découpe. `_Avoid_ : Marge de sécurité, débord, marge d'impression.`
    - *Tranche Verticale (Tracer Bullet)* : Unité minimale traversant toutes les strates nécessaires. `_Avoid_ : Couche technique, ticket backend/frontend, module horizontal.`
    - *Lecture Miroir* : Deux parcours parallèles interconnectés. `_Avoid_ : Version vulgarisée, version technique, niveau débutant/avancé.`
  - Consigner les invariants techniques intouchables : Python 3.11 (`unittest`), Hugo Extended (`hugo --minify`), Cloudflare Pages (`wrangler`).
  - **Interdiction absolue** : Zéro extrait de code, zéro spécification de ticket dans `CONTEXT.md`.

#### Étape 3 : Acter la Première Décision Irréversible (`ADR 0001`)

- **Création du répertoire** : `docs/adr/`.
- **Notice formelle** : `docs/adr/0001-harnais-agentique-en-trois-couches.md`.
- **Validation des 3 critères de Matt Pocock** :
  1. *Difficile à inverser* : Revenir plus tard sur la structure du harnais ou sur le choix de l'emplacement des skills briserait l'autonomie des collaborateurs et apprenants.
  2. *Surprenant sans contexte* : Un observateur externe pourrait se demander pourquoi le dépôt embarque 37 skills dans Git au lieu de laisser chaque développeur utiliser ses plugins locaux.
  3. *Issu d'un arbitrage réel* : Choix d'une architecture hybride à trois couches avec standard agnostique `.agents/` et règle de précédence stricte (*shadowing* : le local à la racine du projet surcharge le global sur le poste).

#### Étape 4 : Déploiement Local & Synchronisation Agnostique (`.agents/skills/`)

- **Installation locale dans le dépôt** : Copie des 37 compétences sous `.agents/skills/<nom>/SKILL.md`. Le dépôt devient un *Repository-as-Code* immédiatement opérationnel après un simple `git clone`.
- **Synchronisation multi-moteurs** : Exécution de `scripts/install_skills.py` pour connecter le même catalogue aux répertoires des différents agents du poste (`~/.claude/skills/`, `~/.gemini/skills/`, `~/.codex/skills/`). Claude Code, OpenAI Codex, Google Gemini/Antigravity, Cursor et Kimi partagent exactement le même référentiel.

#### Étape 5 : Administration des Preuves Observables

- **Épreuve 1 — Suite de tests** : Exécution de `python3.11 -m unittest discover -s tests` → 26 tests unitaires au vert en 0.15 s.
- **Épreuve 2 — Compilation SSG** : Compilation Hugo avec minification → 76 pages rendues sans erreur de lien ni warning (175 ms).
- **Épreuve 3 — Déploiement Cloud** : Publication Cloudflare Pages validée par inspection d'en-tête HTTP 200 en production.

#### Bilan d'Ingénierie pour vos Projets :
En réalisant ce Jalon 1 en une seule passe disciplinée, le projet ne repose plus sur la chance ou la mémoire volatile du développeur. N'importe quel agent démarré demain sur ce dépôt lira `CONTEXT.md`, consultera l'ADR 0001, appliquera les 37 skills locaux et produira du code directement conforme aux attentes.

---

## Les 3 Règles d'Or de l'Ingénierie Agnostique

1. **L'hygiène de la *Smart Zone*** :
   - Au-delà de ~100k-120k tokens, les modèles dégradent leur raisonnement.
   - Les phases de cadrage (`/grill-with-docs` $	o$ `/to-prd` $	o$ `/to-issues`) se tiennent en une seule session.
   - Dès l'émission des tickets, **on vide le contexte** (ou on utilise `/handoff`). Chaque `/implement` s'exécute dans une session vierge dédiée à son ticket.
2. **La pyramide des artefacts** :
   - **Pérenne** : `CONTEXT.md` (glossaire métier) et `docs/adr/` (décisions engageantes).
   - **Éphémère de cycle** : PRD et tickets d'issues (vivent le temps du chantier).
   - **Jetable instantané** : prototypes (`/prototype`) et rapports HTML (`/tmp/*.html`).
3. **La primauté des preuves observables** :
   - L'agent ne livre pas du code : il livre une **preuve vérifiable** (test unitaire/d'intégration passant à l'interface publique d'un module profond).