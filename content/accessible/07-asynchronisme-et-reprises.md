{
  "title": "Faire travailler le système sans perdre les opérations",
  "description": "Comprendre les traitements différés, les réessais et la protection contre les doublons.",
  "weight": 7,
  "chapter_id": "A07",
  "theme": "07",
  "status": "amorce",
  "source_path": "manuscrit/01-lecture-accessible/07-asynchronisme-et-reprises.md",
  "mirror": "/ingenieure/07-asynchronisme-et-reprises",
  "related": [
    "/accessible/08-donnees-et-migrations",
    "/accessible/10-exploitation-et-evolution"
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
  "previous": "/accessible/06-tests-et-preuves",
  "next": "/accessible/08-donnees-et-migrations"
}

## Ce que tu sauras faire

Comprendre les traitements différés, les réessais et la protection contre les doublons.

## Première synthèse

Un fichier peut être reçu sans être encore prêt à fabriquer. L'application doit pouvoir le dire : reçu, en cours de contrôle, validé ou rejeté. Cette distinction permet de continuer à utiliser le service pendant qu'un traitement long se déroule.

Un réseau peut couper après que le serveur a accepté une demande, mais avant que le client reçoive la réponse. Réessayer est alors raisonnable. Le système doit reconnaître la même intention pour éviter de créer deux commandes ou deux traitements facturés.

Une file d'attente ne résout pas tout. Il faut savoir ce qui attend, ce qui a échoué et qui peut relancer. Une tâche incompréhensible ne doit pas tourner indéfiniment : elle doit être mise de côté, signalée et examinée.

## Déroulé prévu

1. Recevoir une demande n'est pas finir le travail.
2. File d'attente, traitement et état visible.
3. Réessayer sans refaire l'effet métier.
4. Que faire d'une tâche qui échoue toujours ?.

## Mise en pratique

Décrire ce que voit le client lorsque le contrôle PDF échoue puis reprend.

## Critère de réussite

Le scénario sépare réception, validation, réessai et intervention humaine.

## Sources et limites

[O-MD §1, §2, §12, §13](/references/sources/o-md#section-1) ; [I-MD §6, §11.2, §11.3](/references/sources/i-md#section-6).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Références pour approfondir

- [PostgreSQL — NOTIFY](https://www.postgresql.org/docs/current/sql-notify.html) — Notifications de sessions ; à distinguer d'une file durable de travaux. [Notice et chapitres associés](/references#ref-notify).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A07](/redaction/a07-asynchronisme-et-reprises).
