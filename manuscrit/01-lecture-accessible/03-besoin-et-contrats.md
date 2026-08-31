# A03 - Transformer le besoin en contrat vérifiable

> Lecture accessible · Amorce de synthèse, chapitre à développer et à relire.

[Sommaire](../SOMMAIRE.md) · [Approfondir le même chapitre](../02-lecture-ingenieure/03-besoin-et-contrats.md) · [Fiche de rédaction](../../tranches/A03-besoin-et-contrats.md)

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

[O-MD §3, §12](../../sources/originaux/manuel_orchestration_logicielle.md) ; [I-MD §3, §9.3, §10.2](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](../../analyse/03-registre-critique.md). Les exemples techniques restent à développer et à tester dans la tranche.
