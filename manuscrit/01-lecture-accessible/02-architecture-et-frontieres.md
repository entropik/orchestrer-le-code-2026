# A02 - Organiser l'architecture et les responsabilités

> Lecture accessible · Amorce de synthèse, chapitre à développer et à relire.

[Sommaire](../SOMMAIRE.md) · [Approfondir le même chapitre](../02-lecture-ingenieure/02-architecture-et-frontieres.md) · [Fiche de rédaction](../../tranches/A02-architecture-et-frontieres.md)

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

[O-MD §1, §2](../../sources/originaux/manuel_orchestration_logicielle.md) ; [I-MD §2](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](../../analyse/03-registre-critique.md). Les exemples techniques restent à développer et à tester dans la tranche.
