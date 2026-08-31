# B02 - Organiser l'architecture et les responsabilités

> Lecture ingénieure · Amorce de synthèse, chapitre à développer et à relire.

[Sommaire](../SOMMAIRE.md) · [Lire la version accessible](../01-lecture-accessible/02-architecture-et-frontieres.md) · [Fiche de rédaction](../../tranches/B02-architecture-et-frontieres.md)

## Ce que tu sauras faire

Concevoir des modules cohérents, des ports et des adaptateurs sans ritualiser l'architecture hexagonale.

## Première synthèse

Une frontière architecturale est utile lorsqu'elle encapsule une décision susceptible d'évoluer. Un port de stockage peut exprimer les capacités nécessaires au cas d'usage sans exposer le SDK d'un fournisseur. L'adaptateur traduit ces capacités, y compris leurs erreurs, dans le protocole concret.

Cette séparation n'annule pas les différences de comportement entre fournisseurs. Taille maximale, visibilité des écritures, expiration et garanties de reprise doivent rester explicites dans le contrat. Une substitution de technologie se démontre par des tests contractuels ; elle ne se déduit pas de l'existence d'une interface.

La profondeur d'un module décrit le service rendu derrière son interface, non un quotient scientifique à maximiser. Une grande implémentation n'est pas vertueuse en soi. On évalue plutôt le nombre de décisions que ses utilisateurs doivent connaître et le coût d'une modification locale.

## Déroulé prévu

1. Cohésion, couplage et profondeur des modules.
2. Entités, objets-valeurs et frontières d'agrégats.
3. Ports, adaptateurs et direction des dépendances.
4. Points de substitution pour le test et l'évolution.

## Mise en pratique

Définir un port de stockage et deux adaptateurs conceptuels avec leurs différences de garanties.

## Critère de réussite

Le domaine ne dépend pas du transport ; les limites de substitution sont documentées.

## Sources et limites

[O-MD §1, §2](../../sources/originaux/manuel_orchestration_logicielle.md) ; [I-MD §2](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](../../analyse/03-registre-critique.md). Les exemples techniques restent à développer et à tester dans la tranche.
