# B05 - Garder une histoire fiable avec Git

> Lecture ingénieure · Amorce de synthèse, chapitre à développer et à relire.

[Sommaire](../SOMMAIRE.md) · [Lire la version accessible](../01-lecture-accessible/05-git-et-collaboration.md) · [Fiche de rédaction](../../tranches/B05-git-et-collaboration.md)

## Ce que tu sauras faire

Organiser branches, worktrees et revue sans confondre séparation de travail et sécurité.

## Première synthèse

Des worktrees fournissent plusieurs répertoires de travail rattachés au même dépôt. Ils facilitent des travaux simultanés sur des branches distinctes, mais ne constituent pas une barrière de sécurité contre un processus capable d'accéder au disque. Ils partagent également des éléments Git et peuvent encore entrer en conflit sur les ports ou les bases de test.

La taille d'une PR est un signal de coût de revue, pas une garantie de qualité. Une tranche traversant contrat, domaine, adaptateur et tests peut légitimement toucher plus de trois fichiers. Sa cohérence se juge par l'intention, les dépendances et la capacité de vérification.

La recherche de régression par bisect exige un oracle fiable et utilisable sur les versions historiques. Le script de reproduction, ses dépendances et les cas non testables doivent être traités explicitement. Identifier un commit corrélé au défaut ne dispense pas d'expliquer le mécanisme causal.

## Déroulé prévu

1. Objets, références, index et arbres de travail.
2. Worktrees et ressources d'exécution partagées.
3. PR dépendantes, stratégie de fusion et conflits.
4. Bisect reproductible et réversibilité réelle.

## Mise en pratique

Préparer un protocole de travail isolant branches, ports et données de test, puis une stratégie de bisect.

## Critère de réussite

Les ressources partagées et les conditions de reproduction sur anciens commits sont identifiées.

## Sources et limites

[O-MD §6](../../sources/originaux/manuel_orchestration_logicielle.md) ; [I-MD §4](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](../../analyse/03-registre-critique.md). Les exemples techniques restent à développer et à tester dans la tranche.
