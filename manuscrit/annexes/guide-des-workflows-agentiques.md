# Guide pratique des workflows agentiques

Ce guide formalise l'usage opérationnel des compétences agentiques (*skills*) issues des travaux de Matt Pocock, adaptées pour une pratique agnostique du développement assisté par agents (Antigravity, Claude Code, Cursor, Codex, OpenCode).

Il fait le pont entre la méthode **ORCHESTRE** du manuel et l'outillage quotidien : comment structurer une session, quelle commande appeler selon la situation, et comment garantir que l'agent produit des preuves vérifiables plutôt que du code spéculatif.

---

## 1. Cartographie complète des 37 skills

Les compétences s'organisent en **six familles opérationnelles**, chapeautées par un routeur d'aiguillage.

### 0. Le Routeur

- [**ask-matt**](https://github.com/mattpocock/skills/tree/main/skills/engineering/ask-matt) : Routeur conversationnel universel. À appeler dès que l'on hésite sur le bon enchaînement ou la compétence adaptée à la situation.

### 1. Gouvernance du dépôt & Cadrage amont

- [**setup-matt-pocock-skills**](https://github.com/mattpocock/skills/tree/main/skills/engineering/setup-matt-pocock-skills) : Configuration initiale du dépôt (gestionnaire d'issues, étiquettes de triage, emplacement de `CONTEXT.md` et des ADRs).
- [**grill-with-docs**](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs) : Interview sans complaisance adossée au code existant. Clarifie l'idée, met à jour le glossaire métier et acte les choix lourds en ADR.
- [**grill-me**](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) : Version sans état (*stateless*) du grilling, utile hors dépôt ou sur une idée abstraite sans base de code.
- [**grilling**](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) : Moteur élémentaire d'interview : pose les questions une par une, avec une recommandation argumentée, après avoir vérifié le code.
- [**domain-modeling**](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling) : Discipline active de modélisation du domaine (DDD). Entretient `CONTEXT.md` et documente les décisions irréversibles dans `docs/adr/`.
- [**decision-mapping**](https://github.com/mattpocock/skills/tree/main/skills/in-progress/decision-mapping) : Cartographie du « brouillard de guerre » pour les chantiers complexes. Découpe l'exploration en tickets d'investigation (Recherche, Prototype, Grilling).
- [**loop-me**](https://github.com/mattpocock/skills/tree/main/skills/in-progress/loop-me) : Cadrage et spécification de boucles d'automatisation récurrentes dans l'espace de travail.

### 2. Étude & Spécification

- [**prototype**](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype) : Fabrication de code jetable pour trancher une incertitude : branche *Logic* (machine à états) ou branche *UI* (ergonomie visuelle).
- [**to-prd**](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-prd) : Synthétise la discussion issue du grilling en document de spécification formelle (User Stories exhaustives, invariants, frontières de test). Sans ré-interview.
- [**to-issues**](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-issues) : Découpe le PRD en tranches verticales indépendantes (*tracer bullets*), ordonnées par dépendances bloquantes.

### 3. Fabrication & Preuves d'ingénierie

- [**implement**](https://github.com/mattpocock/skills/tree/main/skills/engineering/implement) : Implémentation bornée d'un ticket unitaire dans un arbre de travail (*worktree*) dédié, sans dérive ni extrapolation.
- [**tdd**](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) : Cycle Test-Driven Development strict : test rouge à l'interface publique, code minimal pour le vert, refactoring sous contrôle.
- [**codebase-design**](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design) : Référentiel des modules profonds (*deep modules*) : petite interface, forte valeur cachée, coutures franches (*seams*), adaptateurs et test de suppression.
- [**migrate-to-shoehorn**](https://github.com/mattpocock/skills/tree/main/skills/misc/migrate-to-shoehorn) : Assainissement des tests TypeScript en substituant les assertions artificielles `as` par des jeux de données partiels fiables.

### 4. Contrôle, Diagnostic & Santé du code

- [**review**](https://github.com/mattpocock/skills/tree/main/skills/in-progress/review) : Barrière de péage avant intégration. Deux sous-agents inspectent la diff en parallèle : Axe *Standards* (`AGENTS.md`) et Axe *Spec* (conformité au ticket).
- [**diagnosing-bugs**](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs) : Discipline en 6 phases pour traquer les anomalies dures : boucle de rétroaction rouge obligatoire avant toute hypothèse, réduction minimale, sondes étiquetées.
- [**improve-codebase-architecture**](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture) : Audit visuel de la dette architecturale sous forme de rapport HTML interactif pour transformer les modules superficiels en modules profonds.
- [**resolving-merge-conflicts**](https://github.com/mattpocock/skills/tree/main/skills/engineering/resolving-merge-conflicts) : Résolution méthodique de conflits Git : compréhension des deux intentions historiques, préservation des contrats et validation par les tests.
- [**triage**](https://github.com/mattpocock/skills/tree/main/skills/engineering/triage) : Machine à états pour qualifier les signalements et PRs externes : vérification, reproduction, étiquetage (`ready-for-agent`, `needs-info`, `wontfix`).

### 5. Outillage opérationnel & Sécurité

- [**wizard**](https://github.com/mattpocock/skills/tree/main/skills/in-progress/wizard) : Générateur de scripts bash interactifs guidant pas à pas un humain lors d'opérations manuelles ou de migrations sensibles.
- [**git-guardrails-claude-code**](https://github.com/mattpocock/skills/tree/main/skills/misc/git-guardrails-claude-code) : Crochets de sécurité interceptant les commandes Git destructrices (`push --force`, `reset --hard`).
- [**setup-pre-commit**](https://github.com/mattpocock/skills/tree/main/skills/misc/setup-pre-commit) : Mise en place des contrôles de pré-validation (Husky, lint-staged, typage et tests rapides).
- [**handoff**](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff) : Passerelle inter-sessions : résume le contexte courant dans un fichier temporaire hors dépôt pour redémarrer une session neuve sans pollution.
- [**writing-great-skills**](https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-great-skills) : Guide d'ingénierie des compétences : hiérarchie d'information, élimination du superflu (*pruning*), mots directeurs (*leading words*).
- [**find-skills**](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) : Recherche et intégration de compétences communautaires complémentaires.

### 6. Pédagogie, Rédaction & Connaissance

- [**teach**](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach) : Apprentissage interactif pas à pas dans l'espace de travail.
- [**scaffold-exercises**](https://github.com/mattpocock/skills/tree/main/skills/misc/scaffold-exercises) : Génération de répertoires d'exercices structurés (énoncé, indices, solution, suite de tests).
- [**writing-fragments**](https://github.com/mattpocock/skills/tree/main/skills/in-progress/writing-fragments) : Phase d'exploration rédactionnelle : collecte brute d'intuitions, faits et fragments sans contrainte de plan.
- [**writing-beats**](https://github.com/mattpocock/skills/tree/main/skills/in-progress/writing-beats) : Phase d'agencement : ordonnancement des pulsations logiques pour que chaque notion soit définie avant d'être utilisée.
- [**writing-shape**](https://github.com/mattpocock/skills/tree/main/skills/in-progress/writing-shape) : Phase de façonnage : développement paragraphe par paragraphe à partir des pulsations validées.
- [**edit-article**](https://github.com/mattpocock/skills/tree/main/skills/personal/edit-article) : Polissage stylistique : clarté, suppression du remplissage, rythme et lisibilité.
- [**obsidian-vault**](https://github.com/mattpocock/skills/tree/main/skills/personal/obsidian-vault) : Organisation et maillage de la base de connaissances personnelle en Markdown.

### Compétences absorbées ou dépréciées

- *design-an-interface* : absorbé par [`codebase-design`](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design).
- *request-refactor-plan* : absorbé par le binôme [`improve-codebase-architecture`](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture) + [`to-issues`](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-issues).
- *ubiquitous-language* : absorbé par [`domain-modeling`](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling).
- *qa* : remplacé par l'usage conjoint de [`triage`](https://github.com/mattpocock/skills/tree/main/skills/engineering/triage) et [`diagnosing-bugs`](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs).

---

## 2. Arbre de décision : Quel workflow invoquer ?

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

## 3. Les Trames d'Exécution Pas à Pas

### Trame 1 : Nouvelle Fonctionnalité (Flux nominal complet)

```text
┌──────────────┐
│  Idée brute  │
└──────┬───────┘
       ▼
┌──────────────────┐       Doute levé       ┌─────────────┐
│ /grill-with-docs ├───────────────────────>│   /to-prd   │
└──────┬───────────┘                        └──────┬──────┘
       │ Doute ergonomique                         │
       ▼ ou logique                                ▼
┌──────────────────┐                        ┌─────────────┐
│    /prototype    ├───────────────────────>│ /to-issues  │
│    (jetable)     │                        └──────┬──────┘
└──────────────────┘                               │
                                                   ▼
┌──────────────────┐    Chaque ticket       ┌─────────────┐
│     /review      │<───────────────────────┤ /implement  │
│ (Standards/Spec) │    dans un worktree    │ (avec /tdd) │
└──────┬───────────┘    et session neuve    └─────────────┘
       ▼
┌──────────────────┐
│   Merge ticket   │
└──────────────────┘
```

1. **Étape 1 : Cadrer par l'interview (`/grill-with-docs`)**
   - L'agent pose une question à la fois, avec sa réponse recommandée.
   - Il vérifie l'existant dans le code avant d'interroger l'humain.
   - Il aligne le vocabulaire sur `CONTEXT.md`.
   - Si une décision structurelle et difficilement réversible émerge, il rédige un ADR dans `docs/adr/`.
2. **Étape 2 (Optionnelle) : Lever un doute ponctuel (`/prototype`)**
   - Code jetable, sans persistance, lancé en une seule commande.
   - Branche *UI* pour le rendu visuel ou branche *Logic* pour valider un état.
   - Seule la réponse apprise est conservée ; le code du prototype est supprimé.
3. **Étape 3 : Spécifier sans ré-interviewer (`/to-prd`)**
   - L'agent synthétise les échanges en un PRD complet : problème, solution, User Stories détaillées, invariants, décisions techniques et frontières de test.
4. **Étape 4 : Découper en tranches verticales (`/to-issues`)**
   - Découpage en *tracer bullets* (traversant schéma, logique, interface et tests).
   - Pas de découpage horizontal par couche technique.
   - Ordonnancement strict par dépendances bloquantes.
5. **Étape 5 : Implémenter sous preuve (`/implement` + `/tdd`)**
   - **Règle d'hygiène** : Réinitialiser le contexte conversationnel (session neuve) pour chaque ticket.
   - Travailler dans un arbre Git dédié (*worktree*).
   - Cycle TDD : test rouge sur la couture publique, implémentation minimale, refactoring vers un module profond.
6. **Étape 6 : Contrôler à la barrière de péage (`/review`)**
   - Exécution de deux sous-agents en parallèle :
     - *Axe Standards* : conventions du dépôt, `AGENTS.md`, modularité.
     - *Axe Spec* : stricte conformité au besoin du ticket, sans ajout superflu.

---

### Trame 2 : Gros Chantier & Brouillard de Guerre (`/decision-mapping`)

Quand une idée est trop vaste pour être spécifiée en une seule passe :

1. **Cartographier le front pionnier :**
   - L'agent initialise un fichier `DECISION_MAP.md`.
   - Les questions ouvertes deviennent des tickets typés : `Research`, `Prototype` ou `Grilling`.
2. **Une session = Un ticket résolu :**
   - Une session n'aborde qu'un seul sujet à la fois pour préserver la qualité de raisonnement.
   - Clôture systématique par `/handoff` pour transmettre les acquis à la session suivante.
3. **Bascule vers le flux nominal :**
   - Lorsque les tickets bloquants sont levés, la route est dégagée : lancement de `/to-prd` puis `/to-issues`.

---

### Trame 3 : Débogage Dur & Régression de Performance (`/diagnosing-bugs`)

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

1. **Phase 1 — Construire la boucle de rétroaction :**
   - Interdiction formelle de lire le code pour formuler des intuitions tant qu'une commande unitaire (test ciblé, script curl, rejeu de trace) n'échoue pas de façon nette et reproductible sur le symptôme exact.
2. **Phase 2 — Minimiser le cas :**
   - Élaguer entrées, dépendances et étapes pour ne conserver que la charge utile minimale provoquant l'échec.
3. **Phase 3 — Formuler 3 à 5 hypothèses falsifiables :**
   - Modèle : *"Si X est la cause, alors modifier Y fera disparaître le problème"*.
4. **Phase 4 — Poser des sondes ciblées :**
   - Étiqueter chaque sonde de débogage avec un identifiant unique (ex: `[DEBUG-42a1]`). Jamais d'affichage sauvage sans étiquette.
5. **Phase 5 — Test de non-régression et correction :**
   - Poser le test de non-régression à la bonne couture, appliquer le correctif, constater le passage au vert.
6. **Phase 6 — Nettoyage et bilan d'architecture :**
   - Éliminer toutes les sondes via `grep "[DEBUG-"`.
   - Si le bug a révélé une absence de couture franche dans le code, basculer sur `/improve-codebase-architecture`.

---

### Trame 4 : Architecture Profonde & Résorption de Dette (`/improve-codebase-architecture`)

1. **Audit passif et rapport HTML :**
   - L'agent inspecte le dépôt pour repérer les modules superficiels (interfaces compliquées masquant peu de logique) et le manque de localité.
   - Génération d'un rapport visuel autonome dans `/tmp/` (diagrammes Mermaid, comparatifs avant/après).
2. **Sélection et approfondissement :**
   - Choix d'un candidat avec l'humain.
   - Interview `/grilling` adossée au vocabulaire de `codebase-design` :
     - Application du **test de suppression** : supprimer ce module élimine-t-il la complexité (passe-plat inutile) ou la disperse-t-il chez tous les appelants (module à forte valeur) ?
     - Définition d'une interface minimale cachant un maximum de complexité.
3. **Formalisation :**
   - Mise à jour de `CONTEXT.md` et création éventuelle d'un ADR via `/domain-modeling`.

---

### Trame 5 : Triage & Conflits de Synchronisation

1. **Triage entrant (`/triage`) :**
   - Analyse d'un ticket ou d'une PR externe.
   - Vérification contre `.out-of-scope/` pour éviter de réétudier des propositions déjà refusées.
   - Reproduction du bug ou exécution de la PR.
   - Attribution du statut (`needs-info`, `ready-for-agent`, `wontfix`).
2. **Résolution de conflits Git (`/resolving-merge-conflicts`) :**
   - Inspection de l'historique pour comprendre l'intention initiale des deux branches.
   - Préservation des deux intentions ou arbitrage explicite selon l'objectif de la branche courante.
   - Validation systématique par la suite de tests avant validation du commit.

---

### Trame 6 : Pédagogie & Rédaction Technique (Pour *savoirs.keredit.com*)

1. **Conception de formations :**
   - `/scaffold-exercises` prépare l'arborescence pédagogique (énoncé, solution, tests automatisés).
   - `/teach` anime l'apprentissage interactif avec l'apprenant.
2. **Chaîne de publication en 4 temps :**
   - `/writing-fragments` : collecte désordonnée d'idées et d'exemples.
   - `/writing-beats` : mise en séquence logique (chaque notion est assise avant d'être mobilisée).
   - `/writing-shape` : développement paragraphe par paragraphe.
   - `/edit-article` : chasse aux tournures passives, élagage du superflu.

---

## 4. Les 3 Règles d'Or de l'Ingénierie Agnostique

Quel que soit l'outil hôte (Antigravity, Claude Code, Cursor, Codex, OpenCode) :

1. **L'hygiène de la *Smart Zone* (Gestion du contexte)** :
   - Les modèles perdent en discernement au-delà de ~100k tokens.
   - Cadrage et spécification (`/grill-with-docs` -> `/to-prd` -> `/to-issues`) se font dans un même contexte.
   - Dès que les tickets sont émis, **on ouvre une session vierge par ticket** (ou on utilise `/handoff`). L'implémentation d'un ticket ne doit pas traîner l'historique verbeux de la conception.
2. **La pyramide des artefacts** :
   - **Pérenne** : `CONTEXT.md` (termes métier universels) et `docs/adr/` (décisions d'architecture engageantes).
   - **Éphémère de cycle** : PRD et tickets d'issues (vivent le temps du chantier puis s'archivent).
   - **Jetable instantané** : prototypes (`/prototype`) et rapports d'audit HTML (`/tmp/*.html`).
3. **La primauté des preuves observables** :
   - L'agent ne livre pas du code : il livre une **preuve vérifiable** (un test passant à l'interface publique d'un module profond). Aucun code n'est accepté sans son mécanisme de vérification.

---

## 5. Atelier Pratique : Le Fil Rouge « Variantes de Template »

Pour vos formations, cet atelier met en pratique la chaîne complète en 5 exercices :

- **Exercice 1 (Cadrage)** : Invoquer `/grill-with-docs` sur l'intention : *« Permettre à l'utilisateur de choisir entre 3 variantes de mise en page pour un gabarit d'impression »*. Observer comment l'agent refuse les termes ambigus et met à jour `CONTEXT.md`.
- **Exercice 2 (Prototype)** : Face au doute sur le sélecteur d'interface, lancer `/prototype` pour générer une route jetable avec variantes interchangeables en URL.
- **Exercice 3 (Spécification)** : Exécuter `/to-prd` puis `/to-issues` pour obtenir 3 tranches verticales (*tracer bullets*).
- **Exercice 4 (Implémentation)** : Ouvrir une session fraîche dans un worktree dédié, lancer `/implement` sur la tranche 1 en cycle TDD strict.
- **Exercice 5 (Péage)** : Lancer `/review` pour observer l'inspection simultanée sur l'Axe Standards et l'Axe Spec avant intégration finale.
