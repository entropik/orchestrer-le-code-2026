# Orchestrer le code en 2026

**Un manuel, deux lectures : comprendre pour décider, approfondir pour concevoir et vérifier.**

Ce projet s'adresse aux personnes qui pilotent la création de logiciels avec des agents de code. Il relie le besoin utilisateur aux décisions d'architecture, aux contrats, aux tests, à la livraison et à l'exploitation.

Le dépôt est pensé pour GitHub. Le site de lecture est un **projet Hugo autonome**, sans GitHub Pages, sans thème distant et sans JavaScript applicatif.

> État du projet : 12 paires de chapitres, soit 24 amorces de synthèse. Le plan et les fiches de rédaction sont prêts ; le manuel complet et ses exercices corrigés restent à développer.

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

Une présentation sobre, centrée sur le texte : typographie de lecture, fond clair, navigation adaptée aux petits écrans et feuille de style d'impression. Aucune police distante, aucun traceur, aucune bibliothèque chargée depuis un CDN.

Chaque chapitre dispose de :

- son sommaire local et de liens précédent/suivant ;
- son miroir dans l'autre lecture ;
- sujets connexes pour poursuivre l'exploration ;
- notions reliées au glossaire ;
- références documentaires, liens officiels et retours depuis les références vers les chapitres.

Les pages de références conservent l'origine, l'empreinte et les repères de section des documents. Les huit originaux sont téléchargeables dans le rendu : vérifier leurs droits de diffusion avant toute publication.

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
python -m unittest discover -s tests -v
hugo --panicOnWarning
python scripts/verifier_html.py public
```

Le dossier `public/` contient le site HTML et ses ressources, prêt à être servi par un hébergeur statique ou un serveur web. Il n'est pas versionné.

Pour une future mise en ligne, fixer l'adresse réelle dans [hugo.toml](hugo.toml), ou transmettre `--baseURL` à Hugo. Exemple fictif :

```sh
hugo --baseURL "https://exemple.org/manuel/"
python scripts/verifier_html.py public --base-path /manuel/
```

Le contrôle HTML vérifie les fichiers, les ancres, les ressources locales et les chemins sous un préfixe. Il ne vérifie pas la disponibilité en ligne des références externes, ni la justesse technique du texte.

Aucune configuration GitHub Pages ni automatisation de déploiement n'est incluse. Le dépôt GitHub et l'hébergement Hugo sont deux choix indépendants.

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

## Préparer le dépôt GitHub

Nom suggéré : `orchestrer-le-code-2026`. Description : « Un manuel à deux niveaux pour piloter le code avec des agents : architecture, Git, tests et production. Site Hugo. »

Avant le premier push :

1. Choisir le compte propriétaire et la visibilité du dépôt.
2. Vérifier les droits de diffusion du corpus, du manuscrit et de l'historique Git.
3. Ajouter l'URL réelle du dépôt dans `params.repositoryURL` de [hugo.toml](hugo.toml) pour afficher le lien sur le site.
4. Créer le dépôt distant puis y pousser les sources, sans publier automatiquement le site.

Attention : les documents originaux sont déjà présents dans l'historique local. Les enlever uniquement du dernier état ne suffirait pas à les retirer d'un dépôt public. Aucune licence libre n'est attribuée implicitement à ces documents.

## Contribuer

Commencer par la paire [A01](tranches/A01-piloter-un-systeme.md) / [B01](tranches/B01-piloter-un-systeme.md), puis harmoniser les deux niveaux avant de poursuivre. Voir [CONTRIBUTING.md](CONTRIBUTING.md).

La contribution attendue explique le besoin, cite les sources, indique les preuves réellement obtenues et nomme les limites restantes. Un build réussi n'est pas une validation éditoriale.
