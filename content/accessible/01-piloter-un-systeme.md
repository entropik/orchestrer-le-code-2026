{
  "title": "Piloter un système, pas une génération de code",
  "description": "Savoir ce que l'on délègue à un agent et ce que l'on doit décider soi-même.",
  "weight": 1,
  "chapter_id": "A01",
  "theme": "01",
  "status": "amorce",
  "source_path": "manuscrit/01-lecture-accessible/01-piloter-un-systeme.md",
  "mirror": "/ingenieure/01-piloter-un-systeme",
  "related": [
    "/accessible/04-harnais-et-contexte",
    "/accessible/11-methode-et-cas-pratiques"
  ],
  "notions": [
    {
      "label": "Agent",
      "anchor": "agent"
    },
    {
      "label": "Harnais",
      "anchor": "harnais"
    },
    {
      "label": "Invariant",
      "anchor": "invariant"
    }
  ],
  "next": "/accessible/02-architecture-et-frontieres"
}

> Nouveau dans cette édition : [évaluer ou acquérir le socle de programmation](/commencer) avant de poursuivre. Ce passage reste facultatif pour un lecteur déjà autonome.

## Ce que tu sauras faire

Savoir ce que l'on délègue à un agent et ce que l'on doit décider soi-même.

## Première synthèse

Tu demandes un bouton pour déposer un fichier. L'agent peut dessiner ce bouton en quelques instants. Pourtant, le travail important commence avec les questions que le bouton ne montre pas : à qui appartient le fichier, qui peut l'ouvrir et que devient-il si le transfert s'interrompt ? Piloter du logiciel, c'est rendre ces questions visibles avant de déclarer le travail terminé.

Tu n'as pas besoin de comprendre chaque ligne pour prendre une bonne décision. Tu dois pouvoir nommer le résultat attendu, les erreurs coûteuses et les preuves à demander. Dans notre atelier d'impression, voir un nom de fichier à l'écran ne suffit pas : il faut vérifier que le fichier reçu est complet et disponible uniquement aux bonnes personnes.

Une mission utile précise aussi les limites de l'action. Demander une analyse ne signifie pas autoriser une modification, et demander une modification locale ne signifie pas autoriser une publication. Cette séparation protège les données et rend la collaboration plus claire.

## Déroulé prévu

1. Le logiciel comme atelier : entrées, règles, données et résultat.
2. Le rôle de l'orchestrateur : intention, limites et preuve.
3. Prototype visible et service fiable : deux étapes différentes.
4. Décider quand continuer et quand demander un arbitrage.

## Mise en pratique

Rédiger une mission pour analyser le dépôt de fichiers, sans modification ni publication.

## Critère de réussite

La mission distingue résultat, données concernées, preuve et autorisation.

## Sources et limites

[O-MD §1, §4, §5](/references/sources/o-md#section-1) ; [I-MD §1, §9.5](/references/sources/i-md#section-1).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A01](/redaction/a01-piloter-un-systeme).
