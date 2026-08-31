{
  "title": "Protéger les données et faire évoluer leur structure",
  "description": "Comprendre pourquoi les données demandent une prudence différente de celle du code.",
  "weight": 8,
  "chapter_id": "A08",
  "theme": "08",
  "status": "amorce",
  "source_path": "manuscrit/01-lecture-accessible/08-donnees-et-migrations.md",
  "mirror": "/ingenieure/08-donnees-et-migrations",
  "related": [
    "/accessible/07-asynchronisme-et-reprises",
    "/accessible/09-livraison-et-production"
  ],
  "notions": [
    {
      "label": "Migration",
      "anchor": "migration"
    },
    {
      "label": "RPO",
      "anchor": "rpo"
    },
    {
      "label": "RTO",
      "anchor": "rto"
    }
  ],
  "previous": "/accessible/07-asynchronisme-et-reprises",
  "next": "/accessible/09-livraison-et-production"
}

## Ce que tu sauras faire

Comprendre pourquoi les données demandent une prudence différente de celle du code.

## Première synthèse

Si deux personnes réservent le dernier exemplaire au même moment, vérifier le stock puis enregistrer la vente peut ne pas suffire. La règle doit être défendue à un endroit capable de coordonner les deux opérations, pas seulement dans l'écran de chacun.

Une migration change le rangement ou la forme des données. Pendant une mise à jour, l'ancien et le nouveau programme peuvent cohabiter. Ajouter une nouvelle information, remplir progressivement puis retirer l'ancienne est souvent plus sûr que tout renommer en une seule fois.

Avant de modifier des données importantes, demande quelle perte est acceptable et comment le service sera restauré. Une sauvegarde n'est une preuve de récupération qu'après un essai de restauration. Le fichier de sauvegarde et le résultat de cet essai sont deux choses différentes.

## Déroulé prévu

1. La base garde l'état durable.
2. Deux demandes simultanées et règle d'unicité.
3. Changer progressivement le rangement.
4. Sauvegarde, restauration et perte acceptable.

## Mise en pratique

Décrire une migration du statut du document sans empêcher l'ancienne version de fonctionner.

## Critère de réussite

La proposition distingue ajout, transition et retrait, et précise la limite du retour arrière.

## Sources et limites

[O-MD §2, §3, §8, §10, §13](/references/sources/o-md#section-2) ; [I-MD §7](/references/sources/i-md#section-7).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Références pour approfondir

- [PostgreSQL — NOTIFY](https://www.postgresql.org/docs/current/sql-notify.html) — Notifications de sessions ; à distinguer d'une file durable de travaux. [Notice et chapitres associés](/references#ref-notify).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A08](/redaction/a08-donnees-et-migrations).
