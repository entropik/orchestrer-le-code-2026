{
  "title": "Passer du poste local à un service réel",
  "description": "Définir une chaîne de livraison traçable avec compatibilité, santé et limites d'infrastructure.",
  "weight": 9,
  "chapter_id": "B09",
  "theme": "09",
  "status": "amorce",
  "source_path": "manuscrit/02-lecture-ingenieure/09-livraison-et-production.md",
  "mirror": "/accessible/09-livraison-et-production",
  "related": [
    "/ingenieure/05-git-et-collaboration",
    "/ingenieure/10-exploitation-et-evolution"
  ],
  "notions": [
    {
      "label": "Artefact",
      "anchor": "artefact"
    },
    {
      "label": "CI",
      "anchor": "ci"
    },
    {
      "label": "Migration",
      "anchor": "migration"
    }
  ],
  "previous": "/ingenieure/08-donnees-et-migrations",
  "next": "/ingenieure/10-exploitation-et-evolution"
}

## Ce que tu sauras faire

Définir une chaîne de livraison traçable avec compatibilité, santé et limites d'infrastructure.

## Première synthèse

Le pipeline construit et vérifie un artefact, puis le promeut avec une configuration maîtrisée. Un tag contenant un SHA reste une convention de nommage : l'identité de l'image se contrôle par son digest. Les migrations et les paramètres nécessaires font partie de la traçabilité de la livraison.

Une bascule sans coupure dépend de la capacité disponible, de la compatibilité du schéma, de la disponibilité réelle de la nouvelle instance et du drainage de l'ancienne. Un rechargement du reverse proxy ne prouve pas à lui seul la continuité du service. Les sondes doivent distinguer processus vivant et aptitude à servir le trafic.

Les exemples de configuration doivent annoncer leurs prérequis. Le module de limitation de débit Caddy cité dans les sources n'est pas livré avec la distribution standard. Les permissions des secrets doivent être testées avec l'identité effective du processus qui les lit, et non déduites de la seule présence d'un fichier d'environnement.

## Déroulé prévu

1. CI, dépendances verrouillées et artefact identifié par digest.
2. VPS, reverse proxy, réseau et persistance.
3. Configuration, secrets et privilèges minimaux.
4. Staging, bascule, drainage et rollback compatible.

## Mise en pratique

Spécifier les étapes de livraison et un scénario d'échec au moment de la bascule.

## Critère de réussite

La version, la migration et l'image réellement servies sont retrouvables ; les prérequis de configuration sont explicites.

## Sources et limites

[O-MD §8](/references/sources/o-md#section-8) ; [I-MD §8, §10.2](/references/sources/i-md#section-8).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Références pour approfondir

- [Caddy — module de limitation de débit](https://caddyserver.com/docs/modules/http.handlers.rate_limit) — Module non standard : sa présence doit être vérifiée. [Notice et chapitres associés](/references#ref-caddy).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche B09](/redaction/b09-livraison-et-production).
