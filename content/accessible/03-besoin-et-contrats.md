{
  "title": "Transformer le besoin en contrat vérifiable",
  "description": "Écrire une demande que deux personnes peuvent comprendre et vérifier de la même manière.",
  "weight": 3,
  "chapter_id": "A03",
  "theme": "03",
  "status": "amorce",
  "source_path": "manuscrit/01-lecture-accessible/03-besoin-et-contrats.md",
  "mirror": "/ingenieure/03-besoin-et-contrats",
  "related": [
    "/accessible/02-architecture-et-frontieres",
    "/accessible/06-tests-et-preuves"
  ],
  "notions": [
    {
      "label": "Contrat",
      "anchor": "contrat"
    },
    {
      "label": "Invariant",
      "anchor": "invariant"
    },
    {
      "label": "API",
      "anchor": "api"
    }
  ],
  "previous": "/accessible/02-architecture-et-frontieres",
  "next": "/accessible/04-harnais-et-contexte"
}

## Ce que tu sauras faire

Écrire une demande que deux personnes peuvent comprendre et vérifier de la même manière.

## Première synthèse

« Le client doit pouvoir envoyer son PDF » laisse trop de choix invisibles. La demande devient exploitable lorsqu'elle précise le client concerné, la commande, la limite de taille, la reprise après coupure et le moment où l'atelier peut utiliser le document.

Un critère d'acceptation raconte une vérification : lorsqu'un client tente d'ouvrir le fichier d'une autre organisation, l'accès est refusé. Un autre protège la réception : après une coupure, le fichier ne doit pas apparaître comme prêt à fabriquer. Ces phrases permettent de discuter du sens avant les détails techniques.

Écris aussi ce qui n'est pas prévu dans la tranche. Un petit résultat complet est plus facile à accepter qu'une longue liste d'écrans partiellement reliés. Les décisions difficiles à changer méritent une courte note avec leurs alternatives et leurs conséquences.

## Déroulé prévu

1. Partir du résultat utilisateur.
2. Décrire scénario, cas limites et exclusions.
3. Nommer les règles qui restent toujours vraies.
4. Garder la trace des décisions importantes.

## Mise en pratique

Écrire une fiche de réception de fichier avec cinq critères et trois exclusions.

## Critère de réussite

Chaque critère correspond à une observation possible ; les unités et acteurs sont explicites.

## Sources et limites

[O-MD §3, §12](/references/sources/o-md#section-3) ; [I-MD §3, §9.3, §10.2](/references/sources/i-md#section-3).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Références pour approfondir

- [TypeScript — assertions de type](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions) — Les assertions de type ne vérifient pas les données à l'exécution. [Notice et chapitres associés](/references#ref-typescript).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A03](/redaction/a03-besoin-et-contrats).
