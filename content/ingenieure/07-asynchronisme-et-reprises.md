{
  "title": "Faire travailler le système sans perdre les opérations",
  "description": "Analyser atomicité, livraison, déduplication et reprise des effets distribués.",
  "weight": 7,
  "chapter_id": "B07",
  "theme": "07",
  "status": "amorce",
  "source_path": "manuscrit/02-lecture-ingenieure/07-asynchronisme-et-reprises.md",
  "mirror": "/accessible/07-asynchronisme-et-reprises",
  "related": [
    "/ingenieure/08-donnees-et-migrations",
    "/ingenieure/10-exploitation-et-evolution"
  ],
  "notions": [
    {
      "label": "Idempotence",
      "anchor": "idempotence"
    },
    {
      "label": "Outbox",
      "anchor": "outbox"
    },
    {
      "label": "Invariant",
      "anchor": "invariant"
    }
  ],
  "previous": "/ingenieure/06-tests-et-preuves",
  "next": "/ingenieure/08-donnees-et-migrations"
}

## Ce que tu sauras faire

Analyser atomicité, livraison, déduplication et reprise des effets distribués.

## Première synthèse

Déplacer un traitement dans un worker change les modes de panne : la livraison peut être répétée, l'accusé de réception peut être perdu et un effet externe peut réussir juste avant un crash. L'idempotence doit porter sur l'effet métier, avec une clé dont la portée et le comportement en cas de contenu différent sont définis.

Une outbox enregistre l'intention d'émettre dans la même transaction que l'état métier. Le relais reste susceptible de publier deux fois s'il s'arrête entre publication et marquage. Les consommateurs doivent donc supporter les doublons ; l'outbox ne constitue pas une promesse générale d'exécution exactement une fois.

Les notifications PostgreSQL ne remplacent pas à elles seules une file durable de travaux. De même, un verrou temporaire dans un cache ne suffit pas à prouver l'unicité d'un effet externe. La décision de différer un traitement dépend de sa charge, de sa durée acceptable et de son besoin de reprise, pas d'un seuil universel de 50 millisecondes.

## Déroulé prévu

1. Blocage CPU, attente d'entrées-sorties et budgets de latence.
2. File durable, worker, accusé de réception et reprise.
3. Clé d'idempotence, portée, empreinte et durée de conservation.
4. Outbox, retry borné, jitter, disjoncteur et quarantaine.

## Mise en pratique

Énumérer les fenêtres de crash entre transaction, publication, effet et accusé de réception.

## Critère de réussite

Chaque fenêtre possède un état récupérable, un responsable de reprise et une protection documentée contre le doublon.

## Sources et limites

[O-MD §1, §2, §12, §13](/references/sources/o-md#section-1) ; [I-MD §6, §11.2, §11.3](/references/sources/i-md#section-6).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Références pour approfondir

- [PostgreSQL — NOTIFY](https://www.postgresql.org/docs/current/sql-notify.html) — Notifications de sessions ; à distinguer d'une file durable de travaux. [Notice et chapitres associés](/references#ref-notify).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche B07](/redaction/b07-asynchronisme-et-reprises).
