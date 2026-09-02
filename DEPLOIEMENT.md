# Déployer `savoirs.keredit.com`

Le site Hugo est publié par Cloudflare Pages depuis le dépôt GitHub `entropik/orchestrer-le-code-2026`. GitHub Pages n'est pas utilisé.

## Configuration Cloudflare Pages

Créer un projet Pages relié au dépôt avec ces valeurs :

| Réglage | Valeur |
|---|---|
| Nom du projet | `savoirs` |
| Branche de production | `main` |
| Commande de construction | `hugo --panicOnWarning` |
| Dossier de sortie | `public` |
| Variable de production et d'aperçu | `HUGO_VERSION=0.164.0` |

Le contenu Hugo étant versionné, aucun générateur Python n'est requis sur l'hébergeur. La CI contrôle séparément que le contenu est synchronisé avec le manuscrit.

## Domaine

Après le premier déploiement réussi, ouvrir **Custom domains** dans le projet Pages et associer `savoirs.keredit.com`. La zone `keredit.com` étant déjà gérée par Cloudflare, le CNAME et le certificat TLS doivent être créés automatiquement. Ne pas créer le CNAME manuellement avant cette association.

## Contrôle avant publication

```sh
python scripts/verifier.py
python scripts/preparer_hugo.py --check
python scripts/preparer_schemas.py --check
python -m unittest discover -s tests -v
hugo --panicOnWarning
python scripts/verifier_html.py public
python scripts/verifier_lecture_sources.py public
node --test tests/test_search.mjs
```

Après déploiement, vérifier la page d'accueil, la recherche, un chapitre de chaque lecture, une référence Markdown, une référence PDF et l'absence de défilement horizontal sur mobile.
