# Orchestrer le code en 2026

Comprendre pour décider. Approfondir pour concevoir et vérifier.

## Commencer ici

- [Sommaire des deux lectures](manuscrit/SOMMAIRE.md) : 12 chapitres accessibles et leurs 12 miroirs ingénieurs.
- [Synthèse des deux approches](analyse/02-synthese.md) : ce que le nouveau manuel conserve, combine et corrige.
- [Plan des 24 tranches](editorial/PLAN_REDACTION.md) : missions de rédaction par chapitre.
- [Analyse du corpus](analyse/01-corpus.md) : huit fichiers, versions et doublons.
- [Registre critique](analyse/03-registre-critique.md) : erreurs, nuances et vérifications restant à faire.

## Ce qui est livré

Le dépôt contient le projet éditorial, l'analyse des sources, 24 amorces de chapitre et 24 fiches de rédaction. **Le livre complet n'est pas encore rédigé.** La première partie est autonome et accessible ; la seconde reprend les mêmes sujets avec les mécanismes, compromis et preuves techniques. Les renvois fonctionnent dans les deux sens, chapitre par chapitre.

Le document `MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md`, chapitre 12 inclus, est la référence technique principale. Le guide `manuel_orchestration_logicielle.md` est la référence pédagogique. Les autres versions sont conservées pour la traçabilité.

## Organisation

- `analyse/` : inventaire commenté, synthèse, réserves techniques.
- `editorial/` : charte, fil rouge, manifeste et plan de rédaction.
- `manuscrit/` : deux parcours miroirs et annexes.
- `tranches/` : une mission autonome par chapitre et par niveau.
- `sources/originaux/` : copies exactes des huit documents, jamais modifiées.
- `sources/extraits/` : texte extrait, avec repères de pages pour les PDF.
- `scripts/` et `tests/` : import, contrôle et assemblage Markdown.
- `dist/` : compilations générées, ignorées par Git.

## Vérifier et assembler

Python 3.10 ou supérieur suffit pour vérifier le dépôt et assembler le manuscrit :

```powershell
python scripts/verifier.py
python -m unittest discover -s tests -v
python scripts/assembler.py
```

L'assemblage produit trois fichiers : `dist/orchestrer-le-code-2026.md`, `dist/lecture-accessible.md` et `dist/lecture-ingenieure.md`. Ils portent le statut d'amorces tant que tous leurs chapitres ne sont pas validés. Aucun PDF final n'est produit à ce stade.

L'import des PDF demande en plus pypdf :

```powershell
python -m pip install -r requirements-import.txt
python scripts/importer_sources.py "C:/Users/marct/Documents"
```

Le chemin ci-dessus est celui des sources fournies pour ce projet ; ailleurs, le remplacer par le dossier contenant les huit fichiers. L'import refuse d'écraser un original différent.

## Rédiger la suite

Commencer par [A01](tranches/A01-piloter-un-systeme.md), puis [B01](tranches/B01-piloter-un-systeme.md), et relire la paire. La [charte](editorial/CHARTE.md) précise les attentes de chaque lecture. Le [manifeste](editorial/chapitres.json) suit l'état réel des chapitres.

Dépôt local : aucun dépôt distant, push ou publication n'est nécessaire à son utilisation. Les droits de diffusion des sources et la licence du futur livre restent à décider avant publication. Aucune licence libre n'est attribuée implicitement aux documents fournis.
