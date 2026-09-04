# Guide des workflows agentiques & Cas pratiques

Ce guide détaille la mécanique opératoire pour piloter des agents de code avec rigueur et prévisibilité. Il formalise le passage de l'intention floue à la livraison validée sans improvisation.

---

## 1. Le Ruban Principal : De l'Idée à la Production (Idea → Ship)

La quasi-totalité du travail d'ingénierie suit un ruban nominal continu, alimenté par trois voies d'insertion et arbitré par des barrières de péage qualité.

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

### Les 4 étapes clés du flux nominal :

1. **Cadrage amont (`/grill-with-docs`)** : Point d'entrée obligatoire dans un dépôt Git. L'agent mène une interview contradictoire sans complaisance, **une question à la fois** avec sa recommandation, après avoir inspecté le code existant. Il alimente en direct `CONTEXT.md` (glossaire métier) et formalise les choix structurants dans `docs/adr/`.
2. **Embranchement Prototype (si doute exécutable)** : Si une question ergonomique (interface utilisateur) ou un automate d'états ne peut être tranché sur le papier :
   - `/handoff` vers une session isolée.
   - `/prototype` sur une branche éphémère `prototype/<nom>` pour répondre à la question par du code jetable lancé en une seule commande.
   - `/handoff` retour pour consigner les apprentissages dans le fil de discussion principal.
3. **Spécification et Découpage en Tranches** :
   - `/to-prd` : Synthèse formelle des acquis de l'interview en document de spécification (User Stories, invariants, hors périmètre), sans relancer de questions.
   - `/to-issues` : Découpage du PRD en tranches verticales indépendantes (*tracer bullets* : schéma, logique, API, UI et test de bout en bout) avec graphe de dépendances bloquantes.
   - `/clear` : Vidage complet de la mémoire pour démarrer la fabrication dans un contexte vierge de tokens résiduels.
4. **Fabrication sous preuve & Barrière de péage** :
   - Pour chaque ticket : `/implement` pilote en interne `/tdd` (cycle rouge à la frontière publique → vert minimal → refactor).
   - Clôture impérative par `/review` : audit automatisé sur deux axes indépendants (Axe 1 : Standards de code du dépôt ; Axe 2 : Respect strict du contrat du ticket).

---

## 2. Les Trois Voies d'Insertion (On-Ramps)

Des situations initiales imprévues génèrent du travail avant de fusionner sur le ruban principal :

- **Bugs et retours non sollicités (`/triage`)** : Utilisé **exclusivement** pour les signalements créés par des tiers (clients, support, tickets bruts). Il vérifie l'antériorité contre `.out-of-scope/`, reproduit la panne et attribue le rôle (`ready-for-agent`, `needs-info`, `wontfix`).
  > **Règle d'or** : Ne triez **jamais** les tickets issus de `/to-issues` : vos propres tickets sont déjà prêts pour l'agent.
- **Bug dur, régression ou test intermittent (`/diagnosing-bugs`)** : Interdiction formelle de théoriser ou de modifier du code avant d'avoir isolé une **commande unique déterministe** qui reproduit l'échec à 100 %. L'agent minimise le scénario, pose 3 à 5 hypothèses falsifiables, trace avec des sondes `[DEBUG-xxxx]`, écrit le test de non-régression à la frontière publique, et passe la main à `/improve-codebase-architecture` si aucune couture n'existait.
- **Brouillard complet sur grand chantier (`/wayfinder` / `/decision-mapping`)** : Face à une initiative vaste ou incertaine, l'agent dresse `DECISION_MAP.md` découpé en tickets d'investigation (`Research`, `Prototype`, `Grilling`). Une session = un seul ticket résolu, clôturé impérativement par `/handoff`. Une fois le terrain dégagé, on rejoint le ruban principal à `/to-prd`.

---

## 3. Arbre d'Aiguillage Décisionnel

```text
Vous démarrez une session : quelle est la situation ?
 │
 ├── "J'ai une idée ou une nouvelle fonctionnalité"
 │    └── Y a-t-il une base de code Git locale ?
 │         ├── OUI  ──> /grill-with-docs      (interview avec paper trail CONTEXT.md)
 │         └── NON  ──> /grill-me             (interview purement réflexive sans repo)
 │
 ├── "Je ne sais pas par où commencer ou quel outil choisir"
 │    └── /ask-matt                           (l'aiguilleur universel de session)
 │
 ├── "L'agent part dans du jargon ou devient confus"
 │    └── /wait-what                          (arrêt d'urgence et recadrage sans jargon)
 │
 ├── "Le bloqueur dépend d'un client ou d'un collègue"
 │    └── /to-questionnaire                   (génération d'un questionnaire ciblé)
 │
 ├── "Une action humaine sensible est requise (OAuth, secrets, AWS)"
 │    └── /wizard                             (script Bash interactif guidant l'humain)
 │
 ├── "Le chantier est immense et plein d'inconnues (brouillard)"
 │    └── /wayfinder                          (carte de tickets de décision)
 │
 ├── "Quelque chose est cassé, intermittent ou trop lent"
 │    └── /diagnosing-bugs                    (boucle rouge déterministe obligatoire)
 │
 ├── "Le code devient rigide ou superficiel"
 │    └── /improve-codebase-architecture      (audit HTML & modules profonds)
 │
 ├── "Des signalements ou PRs de tiers arrivent"
 │    └── /triage                             (qualification & briefs d'agents)
 │
 └── "J'ai un conflit de fusion Git"
      └── /resolving-merge-conflicts          (analyse des intentions des 2 branches)
```

---

## 4. Les 7 Trames d'Exécution Pas à Pas

### Cas 1 : Nouvelle Fonctionnalité (Flux nominal complet)

1. **Cadrage amont (`/grill-with-docs`)** : L'agent pose une question à la fois avec sa recommandation. Il aligne le glossaire dans `CONTEXT.md` et crée un ADR pour tout arbitrage difficilement réversible.
2. **Détour Prototype optionnel (`/prototype`)** : Code jetable sans tests, lancé en une commande pour trancher un doute UI ou d'automate d'états. Seul l'apprentissage est conservé.
3. **Spécification formelle (`/to-prd`)** : Synthèse sans ré-interview des acquis de l'interview en User Stories exhaustives, invariants et hors périmètre.
4. **Découpage en tranches verticales (`/to-issues`)** : Découpage en *tracer bullets* autonomes avec liens de blocage stricts.
5. **Implémentation sous preuve (`/implement` + `/tdd`)** : Session vierge par ticket dans un worktree dédié. Cycle TDD strict à l'interface publique.
6. **Audit au péage (`/review`)** : Relecture automatisée par deux sous-agents indépendants (Standards et Spécification).

### Cas 2 : Gros Chantier & Brouillard de Guerre

1. **Entrée : `/wayfinder`** : Génération de `DECISION_MAP.md` matérialisant la frontière du brouillard par des tickets typés (`Research`, `Prototype`, `Grilling`).
2. **Exécution unitaire** : Une session = un seul ticket résolu (*« decisions, not deliverables »*). Clôture systématique par `/handoff` pour forker vers une session fraîche.
3. **Sortie du brouillard** : Dès que l'horizon est dégagé, fusion vers `/to-prd` puis `/to-issues`.

### Cas 3 : Débogage Dur ou Régression de Performance

1. **Phase 1 — Boucle rouge déterministe** : Obligation d'obtenir une commande qui échoue de façon nette sur le symptôme à 100 % avant toute modification de code.
2. **Phase 2 — Minimiser le scénario** : Réduire le scénario à la plus petite charge utile provoquant la panne.
3. **Phase 3 — 3 à 5 hypothèses falsifiables** : *« Si X est la cause, alors changer Y fera disparaître l'erreur »*.
4. **Phase 4 — Sondes étiquetées** : Logs tracés sous la forme `[DEBUG-xxxx]` (zéro log orphelin).
5. **Phase 5 — Fix + Test de non-régression** : Test placé sur la couture publique, correction minimale, passage au vert.
6. **Phase 6 — Nettoyage & Bilan** : Suppression des sondes via `grep`. Si le bogue a révélé un manque de couture, passage de relais à `/improve-codebase-architecture`.

### Cas 4 : Amélioration Continue & Architecture Profonde

1. **Entrée : `/improve-codebase-architecture`** : Audit automatique repérant les modules superficiels ; génération d'un rapport HTML visuel dans `/tmp/` avec diagrammes Mermaid.
2. **Sélection et Cadrage** : Choix d'un candidat et lancement de `/grilling` adossé à `/codebase-design`. Application du **test de suppression** : supprimer le module concentre-t-il la complexité ou la disperse-t-il chez les appelants ?
3. **Enregistrement** : Mise à jour de `CONTEXT.md` et formalisation d'un ADR via `/domain-modeling`.

### Cas 5 : Gestion des Flux Entrants

1. **Triage automatique d'issues et PRs : `/triage`** : Vérifie l'antériorité contre `.out-of-scope/`, reproduit l'anomalie ou teste la PR, et attribue le rôle (`needs-info`, `ready-for-agent`, `wontfix`).
2. **Résolution de conflits Git : `/resolving-merge-conflicts`** : Analyse les intentions des deux branches, préserve les contrats et valide par la suite de tests avant le commit de fusion.

### Cas 6 : Pédagogie & Rédaction Technique (Pour *savoirs.keredit.com*)

1. **Ateliers et cours** : `/scaffold-exercises` pour les arborescences d'exercices et `/teach` pour la guidance interactive.
2. **Chaîne de publication** : `/writing-fragments` (matériau brut) → `/writing-beats` (progression rythmique) → `/writing-shape` (façonnage des paragraphes) → `/edit-article` (ciselage éditorial).

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

1. **Le Diagnostic Initial (`/ask-matt`)** : Constat du besoin de cadre documentaire. Invocation immédiate des compétences de gouvernance amont : `setup-matt-pocock-skills` et `domain-modeling`. Règle d'or : aucune écriture de code tant que le lexique partagé et l'arborescence ne sont pas scellés.
2. **Établir le Modèle de Domaine (`CONTEXT.md`)** : Rédaction du fichier racine respectant le format strict de Matt Pocock. Définition resserrée de ce que les termes *sont*, clauses d'évitement `_Avoid_` (*Bon à Tirer*, *Fond Perdu*, *Tranche Verticale*, *Lecture Miroir*), et invariants techniques intouchables.
3. **Acter la Première Décision Irréversible (`ADR 0001`)** : Création de `docs/adr/0001-harnais-agentique-en-trois-couches.md` validant les 3 critères (difficile à inverser, surprenant sans contexte, fruit d'un arbitrage réel).
4. **Déploiement Local & Synchronisation Agnostique (`.agents/skills/`)** : Copie des 37 compétences sous `.agents/skills/<nom>/SKILL.md` pour le *Repository-as-Code*, et exécution de `scripts/install_skills.py` pour synchroniser Claude Code, Codex, Gemini, Kimi et Cursor.
5. **Administration des Preuves Observables** : Validation par 26 tests unitaires au vert, compilation Hugo sans erreur et déploiement Cloudflare Pages vérifié en direct.

---

*Pour approfondir la doctrine du harnais et la gestion de la Smart Zone, consulter l'[Architecture du harnais](03-architecture-du-harnais.md). Pour parcourir les fiches détaillées des compétences, consulter le [Catalogue des 37 skills](04-catalogue-des-skills.md).*
