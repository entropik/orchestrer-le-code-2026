# A05 - Garder une histoire fiable avec Git

> Lecture accessible · Amorce de synthèse, chapitre à développer et à relire.

[Sommaire](../SOMMAIRE.md) · [Approfondir le même chapitre](../02-lecture-ingenieure/05-git-et-collaboration.md) · [Fiche de rédaction](../../tranches/A05-git-et-collaboration.md)

## Ce que tu sauras faire

Distinguer enregistrer, partager, proposer et publier.

## Première synthèse

Un commit enregistre un état du code. Un push le partage. Une proposition de fusion permet de discuter d'un changement avant de l'intégrer. Aucune de ces actions ne signifie à elle seule que le service en production a changé.

Avant d'accepter une contribution, regarde son intention et son périmètre. Pourquoi un travail sur les fichiers modifie-t-il aussi la facturation ? Cela peut être justifié, mais il faut une explication. Un changement petit et cohérent est plus facile à examiner qu'un mélange de plusieurs objectifs.

Git conserve l'histoire du code, pas toutes les données du service. Revenir à une ancienne version du programme ne fait pas disparaître les fichiers reçus ni les modifications de base déjà effectuées. Le retour arrière doit donc être pensé comme une opération sur le système.

## Déroulé prévu

1. Dossier, sélection, commit et branche.
2. Push, PR et merge : des actes différents.
3. Relire un changement et résoudre un conflit de sens.
4. Revenir sur du code sans croire restaurer les données.

## Mise en pratique

Raconter le chemin d'une modification du poste local à une version publiée.

## Critère de réussite

Le récit ne confond ni commit et push, ni fusion et déploiement, ni revert et restauration.

## Sources et limites

[O-MD §6](../../sources/originaux/manuel_orchestration_logicielle.md) ; [I-MD §4](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](../../analyse/03-registre-critique.md). Les exemples techniques restent à développer et à tester dans la tranche.
