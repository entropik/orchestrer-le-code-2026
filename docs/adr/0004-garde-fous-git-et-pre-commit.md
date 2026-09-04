# ADR 0004 : Garde-fous Git et crochets pré-commit pour agents et contributeurs

- **Statut** : Accepté
- **Date** : 2026-09-04
- **Contexte** : Le développement assisté par des agents d'intelligence artificielle (Claude Code, Gemini CLI, Codex, Kimi) comporte des risques de commandes destructrices (`git push --force`, `git reset --hard`, `git clean -fd`, `git checkout .`) ou de commits accidentels de fichiers sensibles (`.env`, clés) et de contenus désynchronisés.

## Décision

Nous mettons en place une double couche de garde-fous de sécurité au niveau du dépôt :

1. **Crochet d'interception agent (`.claude/hooks/block-dangerous-git.sh` & `.claude/settings.json`)** :
   - Intercepte tout appel d'outil Bash avant son exécution (*PreToolUse*).
   - Bloque sans appel les commandes à risque : `git push` (toutes variantes), `git reset --hard`, `git clean -f/-fd`, `git branch -D`, `git checkout .`, `git restore .`.
   - Renvoie un code d'erreur 2 et un message explicite à l'agent lui rappelant qu'il n'a pas l'autorisation d'exécuter ces commandes destructrices.

2. **Crochets Git natifs du dépôt (`.githooks/pre-commit`)** :
   - Configuré via `git config core.hooksPath .githooks`.
   - Bloque le commit de fichiers de secrets ou de variables d'environnement (`.env`, `.pem`, `.key`, `id_rsa`).
   - Exécute les vérifications structurelles de base (`python3.11 scripts/verifier.py`).
   - Vérifie la stricte synchronisation des contenus Hugo (`python3.11 scripts/preparer_hugo.py --check`).
   - Exécute la suite complète des 26 tests unitaires (`python3.11 -m unittest discover -s tests`).

## Options Considérées

- **Installer Husky et lint-staged via npm** : Rejetée car ce dépôt est strictement en Python 3.11 et Hugo sans dépendance Node.js au runtime. Imposer un `package.json` et `node_modules` alourdirait le socle sans valeur ajoutée.
- **Rien mettre et compter sur les prompts** : Rejetée car les modèles de langage peuvent oublier ou contourner les consignes текстоnelles lors de contextes longs ou de phases d'urgence.

## Conséquences

- **Intégrité absolue du dépôt** : Aucun agent ne peut forcer un push ou écraser l'arbre de travail local sans supervision humaine explicite.
- **Zéro désynchronisation committée** : Tout commit est garanti vert vis-à-vis des tests unitaires et de l'arborescence Hugo.
- **Zéro dépendance lourde** : Purement implémenté en Bash et scripts Python existants.
