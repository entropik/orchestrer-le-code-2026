# Orchestrer le code en 2026

Manuel de pratique et plateforme de savoirs partagés pour apprendre à comprendre, décider, concevoir et vérifier le code assisté par des agents d'intelligence artificielle.

## Language

**Lecture Miroir**:
Deux parcours de lecture parallèles (Partie I Accessible et Partie II Ingénieure) abordant exactement les douze mêmes sujets dans le même ordre, interconnectés par des liens bidirectionnels.
_Avoid_: Version vulgarisée, version technique, niveau débutant, niveau avancé.

**Atelier d'Impression**:
Le domaine métier applicatif fil rouge servant d'exemple continu à travers l'ensemble des chapitres du manuel (devis, analyse PDF, contrôle prépresse, massicotage, bon à tirer).
_Avoid_: Projet démo, cas fictif, application d'exemple.

**Bon à Tirer (BAT)**:
Épreuve contractuelle formelle validée par le client avant l'engagement des machines d'impression, verrouillant l'état de la commande de façon irréversible.
_Avoid_: Validation client, signature, confirmation de commande.

**Fond Perdu (Bleed)**:
Zone d'au moins 3 mm extérieure à la boîte de découpe (TrimBox) indispensable pour éviter les liserés blancs lors du massicotage du papier.
_Avoid_: Marge de sécurité, débord, marge d'impression.

**Boîte de Découpe (TrimBox)**:
Rectangle définissant les dimensions réelles du document final après coupe mécanique.
_Avoid_: Format fini, dimensions utiles, zone de page.

**Tranche Verticale (Tracer Bullet)**:
Unité minimale de travail traversant toutes les couches nécessaires (modèle de données, règles métier, interface, tests e2e) pour livrer un comportement observable autonome.
_Avoid_: Couche technique, ticket backend, ticket frontend, module horizontal.

**Smart Zone**:
Fenêtre de lucidité cognitive du modèle de langage (~100k à 120k tokens) au-delà de laquelle la mémoire de travail s'érode et les hallucinations augmentent.
_Avoid_: Contexte infini, taille de fenêtre, budget de prompt.

**Harnais d'Orchestration**:
Ensemble des contraintes exécutables, compétences outillées (`.agents/skills/`), linters, et suites de tests automatisées imposés à l'agent pour forcer des preuves déterministes.
_Avoid_: Prompt système, persona d'agent, instructions libres.

**Preuve Observable**:
Artefact d'ingénierie vérifiable de façon autonome (test unitaire rouge puis vert à la frontière publique, rapport de linter, statut HTTP 200) sans vérification manuelle humaine.
_Avoid_: Validation visuelle, revue informelle, test manuel.

**ADR (Architecture Decision Record)**:
Notice de décision d'architecture consignant un choix difficile à inverser, surprenant sans contexte, et issu d'un arbitrage réel, stocké dans `docs/adr/`.
_Avoid_: Spécification technique, note de réunion, documentation d'implémentation.

**Icônes Lucide**:
Bibliothèque vectorielle minimale et épurée (tracé 24×24, stroke 1.5–2px) utilisée exclusivement pour l'ensemble des repères visuels, boutons et actions du site (`assets/icons/`, `layouts/partials/icon.html`, `layouts/shortcodes/icon.html`).
_Avoid_: Émojis système (🎯, 🐞, 🔗, 🛑, 👥, etc.), icônes raster, polices d'icônes, scripts CDN tiers.

## Invariants Techniques

- **Environnement Python** : Python 3.11 (`python3.11 -m unittest discover -s tests`).
- **Générateur de site statique** : Hugo Extended v0.158+ (`hugo --minify`).
- **Déploiement cible** : Cloudflare Pages (`npx wrangler pages deploy public --project-name savoirs --branch main`).
- **Standard des compétences** : `.agents/skills/<name>/SKILL.md` à la racine du dépôt Git.
- **Iconographie** : Lucide Icons exclusivement en SVG inline (zero-runtime, pas de CDN, zéro layout shift). Les émojis système sont formellement proscrits de l'interface et des fiches documentaires (voir ADR-0003).
- **Garde-fous Git** : Protection active via `.githooks/pre-commit` (contrôle des tests, structure des sources, refus des secrets) et `.claude/hooks/block-dangerous-git.sh` (interception des commandes destructrices pour agents, voir ADR-0004).
- **Design Responsive & Mobile** : En-tête avec navigation tactile accessible (`aria-expanded`), mini-sommaire mobile interactif en tête d'article (`.mobile-reader-menu`), typographie fluide (`clamp()`) et `overflow-x: clip` sur le body (voir ADR-0005).
