# A09 - Passer du poste local à un service réel

> Lecture accessible · Amorce de synthèse, chapitre à développer et à relire.

[Sommaire](../SOMMAIRE.md) · [Approfondir le même chapitre](../02-lecture-ingenieure/09-livraison-et-production.md) · [Fiche de rédaction](../../tranches/A09-livraison-et-production.md)

## Ce que tu sauras faire

Autoriser une livraison en sachant quelle version part, comment la vérifier et comment arrêter.

## Première synthèse

Une application qui fonctionne sur le poste de travail n'est pas encore un service disponible pour ses utilisateurs. La production possède ses propres données, ses accès et ses risques. On prépare la livraison comme un passage de relais : version, configuration, vérification et responsable.

Le programme livré doit être identifiable. Si l'on découvre un problème, il faut retrouver le code et les changements de données réellement exécutés. Tester une version puis en reconstruire une autre sans contrôle affaiblit cette trace.

Avant d'autoriser la publication, demande un essai du parcours essentiel et un signal d'arrêt. Une page de santé verte ne dit pas forcément qu'un client peut envoyer son fichier. Une personne doit observer cette capacité après la mise en service.

## Déroulé prévu

1. Local, vérification automatique, répétition et production.
2. Construire une version identifiable.
3. Secrets et configuration hors du code.
4. Vérifier le parcours et préparer le retour.

## Mise en pratique

Remplir une fiche d'autorisation de livraison pour le dépôt de PDF.

## Critère de réussite

Version, scénario critique, observateur, seuil d'arrêt et retour sont tous renseignés.

## Sources et limites

[O-MD §8](../../sources/originaux/manuel_orchestration_logicielle.md) ; [I-MD §8, §10.2](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](../../analyse/03-registre-critique.md). Les exemples techniques restent à développer et à tester dans la tranche.
