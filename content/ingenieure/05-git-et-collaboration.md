{
  "title": "Garder une histoire fiable avec Git",
  "description": "Organiser branches, worktrees et revue sans confondre séparation de travail et sécurité.",
  "weight": 5,
  "chapter_id": "B05",
  "theme": "05",
  "status": "amorce",
  "source_path": "manuscrit/02-lecture-ingenieure/05-git-et-collaboration.md",
  "mirror": "/accessible/05-git-et-collaboration",
  "related": [
    "/ingenieure/06-tests-et-preuves",
    "/ingenieure/09-livraison-et-production"
  ],
  "notions": [
    {
      "label": "Worktree",
      "anchor": "worktree"
    },
    {
      "label": "PR",
      "anchor": "pr"
    },
    {
      "label": "Tranche verticale",
      "anchor": "tranche-verticale"
    }
  ],
  "previous": "/ingenieure/04-harnais-et-contexte",
  "next": "/ingenieure/06-tests-et-preuves"
}

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

[O-MD §6](/references/sources/o-md#section-6) ; [I-MD §4](/references/sources/i-md#section-4).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Références pour approfondir

- [Git — arbres de travail](https://git-scm.com/docs/git-worktree) — Fonctionnement et partage des ressources entre worktrees. [Notice et chapitres associés](/references#ref-git).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche B05](/redaction/b05-git-et-collaboration).
