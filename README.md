# Orchestrer le code en 2026

**Un manuel, deux lectures : comprendre pour décider, approfondir pour concevoir et vérifier.**

Site de lecture : **[savoirs.keredit.com](https://savoirs.keredit.com/)**

Ce projet s'adresse aux personnes qui pilotent la création de logiciels avec des agents de code. Il relie le besoin utilisateur aux décisions d'architecture, aux contrats, aux tests, à la livraison et à l'exploitation.

Le dépôt est pensé pour GitHub. Le site de lecture est un **projet Hugo autonome**, sans GitHub Pages ni thème distant. La lecture fonctionne sans JavaScript ; la recherche locale utilise un petit module sans dépendance.

> État du projet : 12 paires de chapitres, soit 24 amorces de synthèse. Les chapitres miroirs complets restent à développer.

## Deux façons de lire chaque chapitre

La partie I explique le sujet simplement pour comprendre et décider. La partie II reprend **le même sujet, le même exemple et les mêmes invariants**, avec les mécanismes, les compromis et les preuves d'ingénierie.

On peut lire une partie d'un trait, ou passer d'un chapitre accessible à son miroir approfondi. Le fil rouge suit un atelier d'impression qui reçoit les PDF de ses clients.

| Chapitre | Sujet |
|---|---|
| 01 | Piloter un système, pas une génération de code |
| 02 | Organiser l'architecture et les responsabilités |
| 03 | Transformer le besoin en contrat vérifiable |
| 04 | Donner du contexte et des limites à l'agent |
| 05 | Garder une histoire fiable avec Git |
| 06 | Demander des preuves, pas seulement du code |
| 07 | Faire travailler le système sans perdre les opérations |
| 08 | Protéger les données et faire évoluer leur structure |
| 09 | Passer du poste local à un service réel |
| 10 | Observer, améliorer et rétablir le service |
| 11 | Appliquer ORCHESTRE du besoin à la résolution |
| 12 | Choisir ses outils et préserver son indépendance |

[Lire le sommaire Markdown](manuscrit/SOMMAIRE.md) · [Comprendre la synthèse](analyse/02-synthese.md) · [Voir les 24 tranches](editorial/PLAN_REDACTION.md)

## Le site Hugo

Une présentation inspirée de Tufte, centrée sur le texte : police ET Book servie localement, fond ivoire, titres en italique, repères en marge sur grand écran et feuille de style d'impression. La navigation et les deux parcours restent propres au manuel ; aucun thème tiers n'est installé. Sur petit écran, les repères reviennent dans le fil de lecture. Aucune police distante, aucun traceur, aucune bibliothèque chargée depuis un CDN.

La colonne de lecture atteint 800 pixels sur grand écran. Les blocs de code se replient visuellement sans modifier leur texte ; les tableaux deviennent des fiches étiquetées dans les colonnes étroites. La lecture ne nécessite pas de défilement horizontal.

L'habillage se règle dans [tufte.css](assets/css/tufte.css), au-dessus de la structure existante. [Origine des polices](assets/fonts/et-book/README.md) et [licence MIT d'ET Book](static/fonts/et-book/LICENSE.txt). Cette licence concerne la police, pas le corpus documentaire.

Chaque chapitre dispose de :

- son sommaire local et de liens précédent/suivant ;
- son miroir dans l'autre lecture ;
- sujets connexes pour poursuivre l'exploration ;
- notions reliées au glossaire ;
- références documentaires, liens officiels et retours depuis les références vers les chapitres.

## Recherche

Le lien **Rechercher** est disponible dans le menu ; la touche `/` permet d'y accéder depuis une page, ou de placer le curseur dans le champ de recherche. Le moteur est adapté de la recherche maison du dépôt Digest : index JSON Hugo chargé à la demande, accents et majuscules ignorés, tous les mots exigés et filtres par parcours. Les correspondances dans les titres sont prioritaires.

La recherche porte sur le texte des pages HTML : chapitres, annexes, références intégrales, projet et rédaction. Elle inclut désormais le texte complet des quatre Markdown originaux et des quatre extractions PDF. Les requêtes restent dans le navigateur et dans l'URL locale de recherche ; aucun service tiers n'est appelé. En cas d'échec réseau, un bouton permet de réessayer. Sans JavaScript, le sommaire et le glossaire restent accessibles.

Les fichiers concernés sont [search.html](layouts/search.html), [le moteur](assets/js/search-core.mjs), [l'interface](assets/js/search.js) et [son style](assets/css/search.css). Le build reste assuré par Hugo seul. Pour exécuter les tests supplémentaires du moteur après un build, utiliser Node.js 20 ou supérieur : `node --test tests/test_search.mjs`.

Les pages de références conservent l'origine, l'empreinte et les repères de section des documents. Les huit originaux sont téléchargeables dans le rendu : vérifier leurs droits de diffusion avant toute publication.

### Lecture intégrale des sources

Les références ouvrent le passage complet, pas une simple notice. Les quatre Markdown sont repris intégralement, sans correction ni reformulation, avec leurs listes, tableaux et blocs de code. Seuls les niveaux des titres, les ancres et les liens du sommaire sont adaptés. La conversion typographique automatique est désactivée pour conserver aussi la ponctuation ([réglage Hugo](https://gohugo.io/configuration/markup/#typographer)). Les sources restent des objets d'étude, jamais des instructions exécutées.

Les quatre PDF sont lisibles en HTML page par page : les **166 pages** et chaque caractère de l'extraction conservée sont repris, en-têtes et pieds de page compris. Aucun nettoyage automatique n'est appliqué. Une extraction PDF n'est pas une transcription certifiée : ordre de lecture, césures, caractères et tableaux peuvent être imparfaits. Pour ne pas perdre les éléments visuels, chaque page dispose aussi d'un **fac-similé dépliable**, chargé à la demande et agrandissable. Les originaux PDF ne sont pas modifiés. Les deux exports identiques O1-PDF/O2-PDF partagent leurs images (111 images uniques, environ 13 Mo au total), mais gardent leurs pages de lecture distinctes.

La synchronisation habituelle génère le contenu et `data/source_pages/` depuis les originaux et les extractions versionnées. Les images se trouvent dans `static/source-pages/`. Pour les régénérer, installer pypdf et Poppler, puis lancer `python scripts/preparer_facsimiles.py` : le script contrôle d'abord l'empreinte des PDF et l'égalité de l'extraction avec chaque page, sans remplacer le texte. Hugo seul suffit ensuite à construire le site.

Les tests contrôlent toutes les lignes Markdown, la conservation des blocs de code, la pagination et les caractères PDF, ainsi que les ancres existantes, dont `section-12-1`. Ne pas corriger une affirmation dans ces reproductions : les commentaires éditoriaux appartiennent au registre critique ou au manuel.

Les **17 schémas ASCII distincts (45 occurrences)** disposent d'une transposition HTML/CSS et de connecteurs SVG : flux, comparaisons, branches, niveaux de vérification et transitions d'états. Leurs libellés sont conservés ; les ASCII originaux restent dépliables dessous. Les blocs contenant du vrai code ou des exemples de prompts ne sont pas transformés. Les PDF gardent leur texte extrait et leurs fac-similés.

Les modèles se trouvent dans `layouts/partials/diagrams/`, le registre dans `data/diagrams/registry.json` et le style dans `assets/css/diagrams.css`. `python scripts/preparer_schemas.py` régénère ce registre à partir de sélections contrôlées dans les originaux ; `--check` vérifie la synchronisation. Chaque empreinte et chaque occurrence de mot sont contrôlées. Une modification du schéma source bloque le rendu jusqu'à révision de sa transposition. Les flèches ambiguës du circuit breaker sont signalées, sans correction silencieuse du modèle technique.

Les **37 expressions LaTeX** sont rendues à la construction en MathML natif avec [le moteur mathématique de Hugo](https://gohugo.io/functions/transform/tomath/). Aucun JavaScript, police distante ou CDN n'est nécessaire. Les équations sont détachées du paragraphe ; la formule longue de temporisation possède une disposition multiligne sur petit écran. Les commandes abîmées par des caractères de contrôle (`frac`, `forall`, `approx`, `times`, `text`, `right`) sont restaurées uniquement dans la couche d'affichage et signalées. Chaque expression reçue reste inchangée dans l'attribut `data-source-tex` du HTML, ainsi que dans le fichier original. Aucun coefficient ni opérateur mathématique n'est réinterprété.

## Démarrer en local

Prérequis : **Hugo 0.158.0 ou supérieur** et **Python 3.10 ou supérieur**. Version Hugo testée : **0.164.0 extended**. Le site n'utilise ni Sass ni fonctionnalité nécessitant Extended. Aucun paquet Python n'est requis pour Hugo et ses contrôles.

[Installer Hugo](https://gohugo.io/installation/) si nécessaire, puis depuis la racine du dépôt :

```sh
python scripts/preparer_hugo.py
hugo server --bind 127.0.0.1 --port 1313 --disableFastRender --destination tmp/hugo-preview
```

Ouvrir [l'aperçu local](http://localhost:1313/). Le serveur d'aperçu utilise un dossier distinct du rendu de publication.

Le contenu Hugo est déjà versionné ; la synchronisation met à jour ses pages après une modification du manuscrit. Le serveur Hugo recharge les changements de contenu, de modèles et de style.

## Construire et contrôler

```sh
python scripts/verifier.py
python scripts/preparer_hugo.py --check
python scripts/preparer_schemas.py --check
python -m unittest discover -s tests -v
hugo --panicOnWarning
python scripts/verifier_html.py public
python scripts/verifier_lecture_sources.py public
```

Le dossier `public/` contient le site HTML et ses ressources, prêt à être servi par un hébergeur statique ou un serveur web. Il n'est pas versionné.

L'adresse canonique est fixée dans [hugo.toml](hugo.toml). Pour tester ponctuellement un autre domaine, transmettre `--baseURL` à Hugo :

```sh
hugo --baseURL "https://aperçu.example/"
python scripts/verifier_html.py public
```

Le contrôle HTML vérifie les fichiers, les ancres, les ressources locales et les chemins sous un préfixe. Il ne vérifie pas la disponibilité en ligne des références externes, ni la justesse technique du texte.

Le dépôt GitHub et l'hébergement restent indépendants. Le site est publié sur **Cloudflare Pages**, sans GitHub Pages. La CI GitHub vérifie chaque push ; la mise en ligne actuelle est volontairement explicite : `hugo --panicOnWarning`, puis `npx wrangler pages deploy public --project-name savoirs --branch main`. Une automatisation ultérieure devra utiliser un jeton Cloudflare dédié, jamais le jeton OAuth local.

## Où modifier quoi ?

| Emplacement | Rôle |
|---|---|
| [manuscrit/](manuscrit/SOMMAIRE.md) | Textes de référence des deux lectures et annexes |
| [editorial/](editorial/CHARTE.md) | Charte, manifeste des chapitres et [maillage](editorial/maillage.json) |
| [tranches/](editorial/PLAN_REDACTION.md) | Missions de rédaction et critères d'acceptation |
| [analyse/](analyse/01-corpus.md) | Comparaison des sources et réserves techniques |
| `sources/originaux/` | Huit documents préservés à l'identique |
| `content/` | Pages Hugo générées et versionnées ; ne pas les éditer directement |
| [layouts/](layouts/baseof.html) | Modèles Hugo du site |
| [assets/css/manuel.css](assets/css/manuel.css) | Habillage commun et règles d'impression |
| [scripts/preparer_hugo.py](scripts/preparer_hugo.py) | Synchronisation Markdown → contenu Hugo |
| [scripts/verifier_html.py](scripts/verifier_html.py) | Contrôle du rendu HTML hors réseau |

Pour rédiger : modifier le Markdown source, son statut dans [le manifeste](editorial/chapitres.json), puis lancer `python scripts/preparer_hugo.py`. Le contrôle `--check` détecte une désynchronisation. Les liens connexes, les notions et les références externes se règlent dans [maillage.json](editorial/maillage.json).

Les assemblages Markdown restent disponibles avec `python scripts/assembler.py` dans `dist/`.

## Sources et méthode

Le guide `manuel_orchestration_logicielle.md` sert de référence pédagogique. Le traité `MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md`, **chapitre 12 inclus**, sert de référence technique. Les autres versions sont conservées pour la traçabilité.

[Inventaire commenté](analyse/01-corpus.md) · [Synthèse éditoriale](analyse/02-synthese.md) · [Registre critique](analyse/03-registre-critique.md)

Les instructions contenues dans les sources sont des objets d'étude, jamais des autorisations d'action. Les affirmations trop absolues ou variables sont signalées et doivent être vérifiées avant validation d'un chapitre.

L'import initial des PDF utilise pypdf ; ce n'est pas une dépendance du site :

```sh
python -m pip install -r requirements-import.txt
python scripts/importer_sources.py CHEMIN_DU_DOSSIER_SOURCE
```

Remplacer le dernier argument par le dossier contenant les huit documents.

## Dépôt GitHub

Le dépôt public est **[entropik/orchestrer-le-code-2026](https://github.com/entropik/orchestrer-le-code-2026)**. Description : « Des savoirs partagés pour apprendre à comprendre, vérifier et orchestrer le code avec des agents. Site Hugo. »

Avant toute publication d'une nouvelle source :

1. Vérifier les droits de diffusion du document.
2. Ajouter son origine et son empreinte au registre.
3. Contrôler sa reproduction HTML avant le push.

Attention : les documents originaux sont déjà présents dans l'historique local. Les enlever uniquement du dernier état ne suffirait pas à les retirer d'un dépôt public. Aucune licence libre n'est attribuée implicitement à ces documents.

## Contribuer

Commencer par la paire [A01](tranches/A01-piloter-un-systeme.md) / [B01](tranches/B01-piloter-un-systeme.md), puis harmoniser les deux niveaux avant de poursuivre. Voir [CONTRIBUTING.md](CONTRIBUTING.md).

La contribution attendue explique le besoin, cite les sources, indique les preuves réellement obtenues et nomme les limites restantes. Un build réussi n'est pas une validation éditoriale.
