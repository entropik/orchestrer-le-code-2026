{
  "title": "Donner du contexte et des limites à l'agent",
  "description": "Construire un contexte progressif, une architecture de harnais en trois couches et des limites d'exécution agnostiques.",
  "weight": 4,
  "chapter_id": "B04",
  "theme": "04",
  "status": "amorce",
  "source_path": "manuscrit/02-lecture-ingenieure/04-harnais-et-contexte.md",
  "mirror": "/accessible/04-harnais-et-contexte",
  "related": [
    "/ingenieure/01-piloter-un-systeme",
    "/ingenieure/12-ecosysteme-et-independance"
  ],
  "notions": [
    {
      "label": "Agent",
      "anchor": "agent"
    },
    {
      "label": "Harnais",
      "anchor": "harnais"
    },
    {
      "label": "MCP",
      "anchor": "mcp"
    }
  ],
  "previous": "/ingenieure/03-besoin-et-contrats",
  "next": "/ingenieure/05-git-et-collaboration"
}

## Ce que tu sauras faire

Construire un contexte progressif, une architecture de harnais en trois couches et des limites d'exécution agnostiques.

## Première synthèse

La sélection du contexte est un arbitrage rigoureux entre information manquante et bruit saturant. Une carte de symboles facilite la navigation, mais ne remplace pas la lecture des implémentations qui portent les invariants. Interdire l'accès à tout fichier voisin peut masquer précisément la dépendance responsable d'un bogue.

En ingénierie assistée par agents, le harnais d'orchestration ne doit jamais être conçu comme un bloc monolithique ou lié à un fournisseur unique (Claude, OpenAI Codex, Google Gemini, Kimi, ou Cursor). Il s'organise selon une **architecture en trois couches distinctes** (*Layered Architecture*) :

1. **La Couche Globale (Poste développeur : `~/.`)** : Héberge les réflexes cognitifs universels de l'ingénieur, indépendants de tout projet. On y retrouve l'aiguilleur universel (`/ask-matt`), le brainstorming exploratoire sans état (`/grill-me`), le bouton d'arrêt d'urgence anti-jargon (`/wait-what`) et l'apprentissage guidé (`/teach`).
2. **La Couche Projet (Dépôt Git : `.agents/skills/` à la racine)** : Incarnation du paradigme *Repository-as-Code*. Le dépôt embarque ses propres compétences exécutables (`/grill-with-docs`, `/to-prd`, `/to-issues`, `/implement`, `/tdd`, `/review`), ses règles de nommage et ses commandes de test réelles (`python3.11 -m unittest`, `pnpm test`). Un simple `git clone` transmet immédiatement le même harnais à tous les développeurs et apprenants, éradiquant le syndrome « *Ça marche sur ma machine* ».
3. **La Couche Runtime et Mémoire Vive** : Matérialisée par le glossaire vivant (`CONTEXT.md`), le registre des décisions engageantes (`docs/adr/`) et les espaces de travail éphémères de cycle (`.scratch/`).

Les moteurs d'agents appliquent une **règle de précédence stricte** : **le local surcharge toujours le global (*shadowing*)**. Si une compétence porte le même nom au niveau global et dans le dépôt, la version de la couche projet s'impose immédiatement avec ses invariants et ses commandes spécifiques. Cette structure garantit une portabilité totale : le même dossier `.agents/` guide indifféremment Codex, Claude Code, Gemini CLI, Kimi ou les sidecars de Cursor.

La gestion de la mémoire impose enfin une hygiène stricte de la **Smart Zone** (~100k à 120k tokens) : franchir ce seuil de contexte dégrade le raisonnement du modèle. Aux frontières de phases (*Phase boundaries*), l'ingénieur arbitre explicitement entre la continuité, le vidage intégral (`/clear`), la passerelle portative hors dépôt (`/handoff`), la délégation à un sous-agent ou la compression ciblée (`/compact`) (voir la modélisation complète dans la [Matrice des 37 skills et workflows](/annexes/workflows-agentiques)).

## Déroulé prévu

1. Contexte stable, domaine, tâche et observations dynamiques.
2. L'architecture de harnais en trois couches : poste global, dépôt partagé (`.agents/`), mémoire vive (`CONTEXT.md`).
3. Précédence (*shadowing*) et neutralité d'exécution agnostique (Codex, Claude, Gemini, Kimi, Cursor).
4. Carte du dépôt, symboles et inspection AST.
5. Mémoire durable : provenance, fraîcheur, ADRs et résolution des contradictions.
6. Isolation, budgets de tokens (*Smart Zone*), quotas et collecte des résultats.

## Mise en pratique

Spécifier un manifeste de contexte avec source, date, rôle et règle de mise à jour de chaque entrée, adossé à l'arborescence `.agents/skills/` et `CONTEXT.md`.

## Critère de réussite

Une source périmée ou une instruction embarquée ne peut pas devenir silencieusement une règle du projet, et le clonage du dépôt suffit à répliquer l'intégralité du harnais opérationnel sans configuration machine préalable.

## Sources et limites

[O-MD §4, §5](/references/sources/o-md#section-4) ; [I-MD §1.2 à §1.5, §10, §11.5](/references/sources/i-md#section-1-2) ; [Guide des workflows agentiques](/annexes/workflows-agentiques).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Rédaction de ce chapitre

[Objectifs et critères de la tranche B04](/redaction/b04-harnais-et-contexte).
