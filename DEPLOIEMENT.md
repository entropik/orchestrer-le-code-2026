# Déployer `savoirs.keredit.com`

Le site Hugo est publié sur Cloudflare Pages et son code source est conservé dans le dépôt GitHub `entropik/orchestrer-le-code-2026`. GitHub Pages n'est pas utilisé.

## Configuration actuelle

Le projet Pages a été créé en mode **Direct Upload** avec ces valeurs :

| Réglage | Valeur |
|---|---|
| Nom du projet | `savoirs` |
| Branche indiquée au déploiement | `main` |
| Commande de construction locale | `hugo --panicOnWarning` |
| Dossier envoyé | `public` |

Le contenu Hugo étant versionné, aucun générateur Python n'est requis sur l'hébergeur. La CI GitHub contrôle séparément que le contenu est synchronisé avec le manuscrit.

Après validation de la CI :

```sh
hugo --panicOnWarning
npx wrangler pages deploy public --project-name savoirs --branch main
```

Wrangler utilise uniquement l'autorisation OAuth locale. Aucun secret Cloudflare n'est enregistré dans GitHub. Un déploiement automatique pourra être ajouté plus tard avec un jeton dédié et limité à Pages.

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
