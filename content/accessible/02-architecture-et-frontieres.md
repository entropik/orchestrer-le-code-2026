{
  "title": "Organiser l'architecture et les responsabilités",
  "description": "Reconnaître un découpage compréhensible et éviter la complexité prématurée.",
  "weight": 2,
  "chapter_id": "A02",
  "theme": "02",
  "status": "amorce",
  "source_path": "manuscrit/01-lecture-accessible/02-architecture-et-frontieres.md",
  "mirror": "/ingenieure/02-architecture-et-frontieres",
  "related": [
    "/accessible/03-besoin-et-contrats",
    "/accessible/08-donnees-et-migrations"
  ],
  "notions": [
    {
      "label": "Port",
      "anchor": "port"
    },
    {
      "label": "Contrat",
      "anchor": "contrat"
    },
    {
      "label": "ADR",
      "anchor": "adr"
    }
  ],
  "previous": "/accessible/01-piloter-un-systeme",
  "next": "/accessible/03-besoin-et-contrats"
}

## Ce que tu sauras faire

Reconnaître un découpage compréhensible et éviter la complexité prématurée.

## Première synthèse

Dans l'atelier, le comptoir reçoit une demande, la fabrication applique les règles et l'archive conserve les documents. Une application gagne à rendre ces responsabilités aussi lisibles. Si l'écran décide seul qu'un fichier appartient à une commande, un autre chemin d'accès peut contourner cette décision.

Séparer les responsabilités ne signifie pas multiplier les serveurs. Une application unique peut contenir un module Commandes, un module Documents et une interface de stockage bien définie. Le bon découpage se reconnaît à une question simple : peut-on changer la façon de stocker un fichier sans réécrire les règles de commande ?

Commence par le système le plus petit qui rend le service et permet de vérifier ses règles. Ajoute une séparation technique lorsqu'un besoin concret la justifie, pas parce que son nom semble plus professionnel.

## Déroulé prévu

1. Interface, règles et stockage : qui fait quoi ?.
2. Des modules cohérents dans une seule application.
3. Une frontière utile est une promesse claire.
4. Quand ajouter un service séparé.

## Mise en pratique

Dessiner le parcours du fichier et attribuer chaque décision à un composant.

## Critère de réussite

Le dessin distingue interface, règle d'accès et stockage, sans imposer plusieurs serveurs.

## Sources et limites

[O-MD §1, §2](/references/sources/o-md#section-1) ; [I-MD §2](/references/sources/i-md#section-2).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A02](/redaction/a02-architecture-et-frontieres).
