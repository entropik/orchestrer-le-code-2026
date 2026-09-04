{
  "title": "Demander des preuves, pas seulement du code",
  "description": "Construire des oracles utiles et évaluer la force de la suite de tests.",
  "weight": 6,
  "chapter_id": "B06",
  "theme": "06",
  "status": "amorce",
  "source_path": "manuscrit/02-lecture-ingenieure/06-tests-et-preuves.md",
  "mirror": "/accessible/06-tests-et-preuves",
  "related": [
    "/ingenieure/03-besoin-et-contrats",
    "/ingenieure/11-methode-et-cas-pratiques"
  ],
  "notions": [
    {
      "label": "CI",
      "anchor": "ci"
    },
    {
      "label": "Invariant",
      "anchor": "invariant"
    },
    {
      "label": "Contrat",
      "anchor": "contrat"
    }
  ],
  "previous": "/ingenieure/05-git-et-collaboration",
  "next": "/ingenieure/07-asynchronisme-et-reprises"
}

## Ce que tu sauras faire

Construire des oracles utiles et évaluer la force de la suite de tests.

## Première synthèse

Le protocole appelé TDD inversé dans la source organise la séparation entre construction des tests et implémentation. Sa valeur tient à la revue des oracles, non au nom de la méthode. Des tests mal spécifiés peuvent parfaitement verrouiller un comportement incorrect.

Une propriété générative étend la diversité des entrées, sans établir une preuve pour toutes les valeurs possibles. Une campagne de mutation renseigne sur la capacité des tests à détecter certaines altérations ; les mutants équivalents et les limites des opérateurs demandent une interprétation. Les métriques complètent le raisonnement au lieu de le remplacer.

Pour les courses critiques, préférer un dispositif qui force l'interleaving pertinent à une attente arbitraire ou à cent répétitions chanceuses. Les modifications de tests sont acceptables lorsqu'elles suivent une évolution explicite du contrat ; elles doivent être relues séparément pour empêcher un affaiblissement silencieux.

## Déroulé prévu

1. Tests unitaires, contractuels, intégration et parcours.
2. TDD supervisé et revue des oracles (protocole détaillé dans le [Guide des workflows agentiques](/annexes/workflows-agentiques)).
3. Tests de propriétés, réduction des contre-exemples et mutations.
4. Horloge, hasard, concurrence et reproductibilité.

## Mise en pratique

Définir un test concurrent de création et montrer comment détecter le retrait de la barrière d'unicité.

## Critère de réussite

Le test échoue pour le mécanisme visé avant correction et passe après, sans masquer les erreurs de préparation.

## Sources et limites

[O-MD §7](/references/sources/o-md#section-7) ; [I-MD §5](/references/sources/i-md#section-5).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Rédaction de ce chapitre

[Objectifs et critères de la tranche B06](/redaction/b06-tests-et-preuves).
