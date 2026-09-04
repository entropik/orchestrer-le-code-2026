# B06 - Demander des preuves, pas seulement du code

> Lecture ingénieure · Amorce de synthèse, chapitre à développer et à relire.

[Sommaire](../SOMMAIRE.md) · [Lire la version accessible](../01-lecture-accessible/06-tests-et-preuves.md) · [Fiche de rédaction](../../tranches/B06-tests-et-preuves.md)

## Ce que tu sauras faire

Construire des oracles utiles et évaluer la force de la suite de tests.

## Première synthèse

Le protocole appelé TDD inversé dans la source organise la séparation entre construction des tests et implémentation. Sa valeur tient à la revue des oracles, non au nom de la méthode. Des tests mal spécifiés peuvent parfaitement verrouiller un comportement incorrect.

Une propriété générative étend la diversité des entrées, sans établir une preuve pour toutes les valeurs possibles. Une campagne de mutation renseigne sur la capacité des tests à détecter certaines altérations ; les mutants équivalents et les limites des opérateurs demandent une interprétation. Les métriques complètent le raisonnement au lieu de le remplacer.

Pour les courses critiques, préférer un dispositif qui force l'interleaving pertinent à une attente arbitraire ou à cent répétitions chanceuses. Les modifications de tests sont acceptables lorsqu'elles suivent une évolution explicite du contrat ; elles doivent être relues séparément pour empêcher un affaiblissement silencieux.

## Déroulé prévu

1. Tests unitaires, contractuels, intégration et parcours.
2. TDD supervisé et revue des oracles (protocole détaillé dans le [Guide des workflows](../03-annexes/02-guide-des-workflows.md)).
3. Tests de propriétés, réduction des contre-exemples et mutations.
4. Horloge, hasard, concurrence et reproductibilité.

## Mise en pratique

Définir un test concurrent de création et montrer comment détecter le retrait de la barrière d'unicité.

## Critère de réussite

Le test échoue pour le mécanisme visé avant correction et passe après, sans masquer les erreurs de préparation.

## Sources et limites

[O-MD §7](../../sources/originaux/manuel_orchestration_logicielle.md) ; [I-MD §5](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](../../analyse/03-registre-critique.md). Les exemples techniques restent à développer et à tester dans la tranche.
