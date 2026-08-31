# A01 - Piloter un système, pas une génération de code

> Lecture accessible · Amorce de synthèse, chapitre à développer et à relire.

[Sommaire](../SOMMAIRE.md) · [Approfondir le même chapitre](../02-lecture-ingenieure/01-piloter-un-systeme.md) · [Fiche de rédaction](../../tranches/A01-piloter-un-systeme.md)

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

[O-MD §1, §4, §5](../../sources/originaux/manuel_orchestration_logicielle.md) ; [I-MD §1, §9.5](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](../../analyse/03-registre-critique.md). Les exemples techniques restent à développer et à tester dans la tranche.
