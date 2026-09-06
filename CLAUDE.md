# Mémoire du Projet : Orchestrer le code en 2026

Guide universel pour les agents IA (Claude Code, Cursor, Codex, Antigravity, Roo Code).
Ce document est la source unique de vérité pour la mémoire persistante du projet. Tout agent opérant dans ce dépôt doit lire et respecter ces directives à chaque session.

---

## 1. Identité & Règle d'Or Éditoriale

- **Auteur & Droits** : Marc Tallec, © 2026. Licence Creative Commons CC BY-NC-ND 4.0 (contenu) / MIT (code d'ingénierie). TDM Opt-Out actif (Directive UE 2019/790).
- **Projet** : *Orchestrer le code en 2026* (`savoirs.keredit.com`).
- **Structure** : 24 chapitres miroirs (12 accessibles A01-A12, 12 ingénieurs B01-B12) + 1 Avant-propos opérationnel (Chapitre 00) + Annexes communes.
- **Principe cardinal** : Modifier **exclusivement** les fichiers sources Markdown dans `manuscrit/` et `editorial/`. Ne **jamais** modifier directement les fichiers générés dans `content/` ou `dist/`.

---

## 2. Invariants Impératifs : Schémas & Rendu Graphique (Style des Tableaux)

Dans ce projet, aucun schéma ne doit être rendu sous forme de bloc de code brut illisible :

1. **Syntaxe ASCII standard** :
   - Tout schéma dans `manuscrit/**/*.md` doit obligatoirement utiliser les caractères de boîte déterministes : `┌`, `─`, `┐`, `│`, `└`, `┘`, `├`, `┼`, `▼`, `──►`.
   - Ne **jamais** utiliser des caractères de fortune (`+---+`, `|`, `-->`) qui contournent les tests et produisent un bloc noir disgracieux sur mobile.
2. **Transposition graphique obligatoire** :
   - Tout nouveau schéma ou modification de schéma doit être enregistré dans `data/diagrams/manuscrit.json` via le script `scripts/preparer_schemas_manuscrit.py`.
   - Si le parseur automatique ne suffit pas (par exemple pour une grille comparative côte à côte), ajouter un cas explicite dans `parse_custom()` dans `scripts/preparer_schemas_manuscrit.py`.
   - Hugo intercepte les blocs ```` ```text ```` via `layouts/_markup/render-codeblock-text.html` et les restitue sous forme de **planches graphiques responsive** (`layouts/partials/diagrams/plate.html`).
3. **Contrôle de conformité** :
   - Le test unitaire `test_all_manuscrit_ascii_diagrams_transposed` dans `tests/test_hugo.py` vérifie que 100 % des schémas du manuscrit sont transposés. Lors d'un ajout, ajuster le compteur attendu.

---

## 3. Chaîne d'Exécution & Commandes Déterministes

Toujours exécuter ces commandes avec `python3.11` et l'interpréteur Hugo étendu :

| Action | Commande exacte |
|---|---|
| **Transposition des schémas** | `python3.11 scripts/preparer_schemas_manuscrit.py` |
| **Génération du contenu Hugo** | `python3.11 scripts/preparer_hugo.py` |
| **Vérification structurelle** | `python3.11 scripts/verifier.py` |
| **Suite de tests unitaires** | `python3.11 -m unittest discover -s tests` |
| **Tests typographiques & recherche** | `node tests/test_typo.mjs && node tests/test_search.mjs` |
| **Compilation du site statique** | `/opt/homebrew/bin/hugo --panicOnWarning` |
| **Validation HTML & liens internes** | `python3.11 scripts/verifier_html.py public` |
| **Déploiement Cloudflare Pages** | `npx wrangler pages deploy public --project-name savoirs --branch main` |

---

## 4. Architecture du Harnais & Compétences (Skills de Matt)

Conformément à la doctrine en trois couches documentée dans `manuscrit/03-annexes/03-architecture-du-harnais.md` :

1. **Couche Globale** (`~/.`):
   - Réflexes universels d'aiguillage (`ask-matt`), contradiction socratique (`grill-me`), arrêt d'urgence (`wait-what`).
2. **Couche Projet** (`.agents/skills/`):
   - Compétences d'ingénierie et de rédaction : `writing-for-agents`, `code-review`, `diagnosing-bugs`, `tdd`, `domain-modeling`, `setup-pre-commit`, `scaffold-exercises`.
   - La version locale à la racine du projet surcharge toujours la version globale (*shadowing*).
3. **Couche Mémoire Vive / Artefacts** :
   - Modèle de domaine : `CONTEXT.md`
   - Décisions d'architecture : `docs/adr/`
   - Directives agents permanentes : `AGENTS.md` (ce fichier) et `CLAUDE.md`.
