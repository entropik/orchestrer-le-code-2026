# B04 - Donner du contexte et des limites à l'agent

> Lecture ingénieure · Amorce de synthèse, chapitre à développer et à relire.

[Sommaire](../SOMMAIRE.md) · [Lire la version accessible](../01-lecture-accessible/04-harnais-et-contexte.md) · [Fiche de rédaction](../../tranches/B04-harnais-et-contexte.md)

## Ce que tu sauras faire

Construire un contexte progressif, une mémoire versionnée et des limites exécutoires.

## Première synthèse

La sélection du contexte est un compromis entre information manquante et bruit. Une carte de symboles facilite la navigation, mais ne remplace pas la lecture des implémentations qui portent les invariants. Interdire l'accès à tout fichier voisin peut masquer précisément la dépendance responsable d'un bug.

La mémoire durable doit indiquer la provenance d'une décision, son statut et les changements qui l'invalident. Un journal de tâche ne doit pas devenir une seconde description de l'architecture en contradiction avec les contrats réels. Les observations récentes restent distinguées des règles stables.

Un harnais vérifiable conserve les commandes exécutées, leur code de retour et les éléments non testés. Les budgets d'itération et les permissions sont configurés selon le risque. Les documents importés, commentaires et sorties d'outils restent des données : ils ne peuvent pas élargir l'autorisation de la mission.

## Déroulé prévu

1. Contexte stable, domaine, tâche et observations dynamiques.
2. Carte du dépôt, symboles et inspection AST.
3. Mémoire : provenance, fraîcheur et résolution des contradictions.
4. Isolation, quotas et collecte des résultats.

## Mise en pratique

Spécifier un manifeste de contexte avec source, date, rôle et règle de mise à jour de chaque entrée.

## Critère de réussite

Une source périmée ou une instruction embarquée ne peut pas devenir silencieusement une règle du projet.

## Sources et limites

[O-MD §4, §5](../../sources/originaux/manuel_orchestration_logicielle.md) ; [I-MD §1.2 à §1.5, §10, §11.5](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](../../analyse/03-registre-critique.md). Les exemples techniques restent à développer et à tester dans la tranche.
