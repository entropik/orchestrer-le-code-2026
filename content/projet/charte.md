{
  "title": "Charte éditoriale",
  "source_path": "editorial/CHARTE.md"
}

## Intention

Permettre à un décideur de piloter la fabrication d'un logiciel, puis d'accéder aux mécanismes d'ingénierie qui justifient ses décisions. Le manuel n'est ni une collection de prompts magiques ni une défense d'un fournisseur.

## Deux lectures pour chaque chapitre

La partie I contient A01 à A12 ; la partie II, B01 à B12. Axx et Bxx portent le même sujet, dans le même ordre et avec le même exemple. La première lecture ne réserve pas sa conclusion à la seconde. La seconde rappelle brièvement le problème pour être lisible indépendamment.

| Accessible | Ingénieure |
|---|---|
| Comprendre le problème et choisir une action. | Expliquer les mécanismes, concevoir et vérifier. |
| Situations concrètes et mots expliqués au premier usage. | Contrats, états, limites, modes de panne et preuves. |
| Peu de code ; exemples lisibles sans langage particulier. | Extraits exécutables lorsque utiles, environnement et version précisés. |
| Questions à poser et signaux d'alerte. | Compromis, tests, contre-exemples et procédures de reprise. |
| Exercice de décision avec corrigé. | Exercice de conception ou de diagnostic avec corrigé. |

## Ton

Tutoiement clair, précis et non condescendant. Expliquer avant de nommer. Ne pas remplacer une justification par « industriel », « absolu », « souverain » ou « déterministe ». Une métaphore aide à comprendre mais ne constitue pas un théorème.

## Modèle de chapitre final

Situation concrète ; objectif ; raisonnement ; exemple du fil rouge ; limites et erreurs fréquentes ; exercice ; corrigé ; checklist ; sources et renvoi miroir. Les amorces livrées sont le point de départ, pas ce format final entièrement rempli.

## Règles de preuve

- Distinguer constat dans les sources, synthèse éditoriale et validation externe.
- Indiquer chapitre ou section source ; préférer les textes Markdown aux extractions PDF pour les détails.
- Dater les éléments variables : versions, licences, API, prix, capacités et compatibilité.
- Une configuration copiée d'une source n'est pas réputée testée.
- Ne pas promettre sécurité totale, absence de panne ou correction universelle.
- Les noms de modèles et bibliothèques sont des exemples à vérifier, pas un classement permanent.

## Publication

Valider les droits sur les textes fournis et choisir une licence explicitement. Aucune attribution d'auteur ou autorisation de republication n'est déduite du simple dépôt local.

## Colophon de fabrication : le harnais de l'artisan

Ce manuel et son site web ne sont pas le produit d'un chatbot solitaire interrogé au fil de l'eau, mais d'un atelier logiciel orchestré selon les principes mêmes enseignés dans ces pages (*dogfooding* intégral). La chaîne de production combine quatre couches complémentaires :

1. **L'environnement de développement agentique (ADE)** : **Orca**. Les agents s'exécutent en parallèle, chacun dans un Git worktree strictement cloisonné doté de son propre terminal et d'un navigateur d'inspection dédié. Cette isolation garantit l'absence totale de collisions sur l'arbre Git et permet d'explorer des hypothèses concurrentes sans pollution du tronc principal.
2. **Le tandem des modèles d'inférence** :
   - **Google Gemini** : mobilisé pour la maïeutique, l'analyse synoptique du corpus volumineux, la cohérence trans-chapitres et la dialectique contradictoire.
   - **OpenAI Codex** : sollicité pour la précision syntaxique, l'implémentation fine des algorithmes de transposition, les scripts déterministes et la génération de tests unitaires rigoureux.
3. **La gouvernance et les compétences de Matt Pocock** : Le harnais de pilotage applique la doctrine en trois couches (réflexes universels d'aiguillage, compétences locales de dépôt sous `.agents/skills/` telles que `writing-for-agents`, `diagnosing-bugs`, `tdd`, `code-review`, `domain-modeling`, et mémoire vive persistante via `AGENTS.md`).
4. **La chaîne de compilation et les oracles déterministes** :
   - Génération de contenu Hugo sans dépendance externe tierce (`python3.11`).
   - Moteur de rendu typographique respectant les normes de l'Imprimerie nationale (espaces insécables, anti-solitaires, ligatures).
   - Validation géométrique intégrale des schémas ASCII déterministes transposés en planches vectorielles responsive (`tests/test_hugo.py`).
   - Compilation statique stricte avec Hugo étendu (`--panicOnWarning`), audit de tous les hyperliens internes (`scripts/verifier_html.py`), et distribution mondiale sur Cloudflare Pages à latence minimale, sans traceurs ni cookies.
