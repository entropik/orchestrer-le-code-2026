# B12 - Choisir ses outils et préserver son indépendance

> Lecture ingénieure · Amorce de synthèse, chapitre à développer et à relire.

[Sommaire](../SOMMAIRE.md) · [Lire la version accessible](../01-lecture-accessible/12-ecosysteme-et-independance.md) · [Fiche de rédaction](../../tranches/B12-ecosysteme-et-independance.md)

## Ce que tu sauras faire

Évaluer la portabilité effective des modèles et des outils, y compris MCP et l'inférence locale.

## Première synthèse

Une compatibilité d'API ne prouve pas l'équivalence du comportement : schémas d'outils, erreurs, streaming, limites et états de conversation doivent être testés. La couche d'adaptation doit isoler ces différences. MCP concerne l'exposition de capacités et de ressources ; il ne constitue ni un moteur d'inférence ni une garantie automatique de permission minimale.

Pour une exécution locale, archiver la révision des poids, le tokenizer, le runtime, la configuration et le matériel utilisé. La quantification se juge sur les tâches retenues ; aucune perte de qualité universellement inférieure à un pour cent n'est établie par le corpus. Le coût inclut mémoire, énergie, supervision et temps de maintenance.

Le panorama de la source daté de septembre 2026 doit être traité comme une liste de candidats historiques à revérifier. Par exemple, la fiche officielle de Codestral 24.05 indique MNPL, ce qui interdit de classer toute la famille Codestral sous Apache 2.0. Une décision d'adoption requiert l'identifiant exact, sa licence et une évaluation datée, non un jugement global sur une famille.

## Déroulé prévu

1. Protocoles de génération, appels d'outils, JSON-RPC et MCP.
2. Licence par artefact, modèle exact et provenance.
3. Runtime, quantification, mémoire, débit et qualité.
4. Autorisations des connecteurs, données sortantes et évaluation de migration.

## Mise en pratique

Définir un protocole comparatif et une matrice de permissions d'un connecteur Git en lecture seule.

## Critère de réussite

Version, licence, capacités testées, refus attendus, mesures et risques résiduels sont consignés.

## Sources et limites

[O-MD §2, §4](../../sources/originaux/manuel_orchestration_logicielle.md) ; [I-MD §12.1 à §12.6](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](../../analyse/03-registre-critique.md). Les exemples techniques restent à développer et à tester dans la tranche.
