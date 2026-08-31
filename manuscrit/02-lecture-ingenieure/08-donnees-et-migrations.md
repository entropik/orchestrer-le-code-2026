# B08 - Protéger les données et faire évoluer leur structure

> Lecture ingénieure · Amorce de synthèse, chapitre à développer et à relire.

[Sommaire](../SOMMAIRE.md) · [Lire la version accessible](../01-lecture-accessible/08-donnees-et-migrations.md) · [Fiche de rédaction](../../tranches/B08-donnees-et-migrations.md)

## Ce que tu sauras faire

Choisir contraintes, transactions et migrations à partir des anomalies à empêcher.

## Première synthèse

La transaction délimite ce qui doit être atomique dans une base donnée. Elle ne rend pas automatiquement atomique un appel au stockage objet ou à un fournisseur de paiement. Le choix du niveau d'isolation doit partir des anomalies possibles et des politiques de retry, non d'une préférence abstraite pour le niveau le plus strict.

Une migration expand-contract décrit une période de compatibilité, pas seulement trois fichiers SQL. La double écriture, le backfill, les anciennes instances et la décision de supprimer une colonne doivent être coordonnés. Le dernier retrait peut rendre l'ancien binaire inutilisable ; ce point doit apparaître dans le plan de retour.

Pour l'atelier, l'unicité d'une réception se définit par organisation et intention. Avant de créer la contrainte, examiner les données existantes et les clients anciens. La stratégie de sauvegarde doit couvrir la base et les objets associés : restaurer des métadonnées qui pointent vers des fichiers absents ne restaure pas le service.

## Déroulé prévu

1. Unicité, transactions et niveaux d'isolation.
2. Concurrence optimiste et verrouillage pessimiste.
3. Expand-contract, backfill et compatibilité de versions.
4. Sauvegarde de base, archives WAL, PITR et exercice de restauration.

## Mise en pratique

Écrire un plan de migration avec état des anciennes données, coexistence, contrôles de fin et restauration.

## Critère de réussite

Le plan définit le point irréversible et vérifie la cohérence entre métadonnées et fichiers.

## Sources et limites

[O-MD §2, §3, §8, §10, §13](../../sources/originaux/manuel_orchestration_logicielle.md) ; [I-MD §7](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](../../analyse/03-registre-critique.md). Les exemples techniques restent à développer et à tester dans la tranche.
