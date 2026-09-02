# Projet d’exercice — Partie zéro

Ce projet local accompagne « Prendre la main ». Il ne lit aucun document personnel et ne contacte aucun service.

Prérequis : Node.js 24 LTS. Depuis ce dossier :

```sh
npm install
npm run start -- fixtures/commande-valide.json
npm test
npm run check
npm run build
```

Le programme retourne `0` pour un document valide, `1` pour un rejet métier et `2` pour un usage incorrect ou une erreur technique. Les fichiers de `fixtures/` sont fictifs.

Les instantanés exécutables de P01 à P04 se trouvent dans `etapes/`. `npm test` les exécute avant de construire et tester la version TypeScript finale.
