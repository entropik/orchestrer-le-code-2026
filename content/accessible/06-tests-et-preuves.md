{
  "title": "Demander des preuves, pas seulement du code",
  "description": "Savoir ce qu'un test démontre et poser les bonnes questions à la livraison.",
  "weight": 6,
  "chapter_id": "A06",
  "theme": "06",
  "status": "amorce",
  "source_path": "manuscrit/01-lecture-accessible/06-tests-et-preuves.md",
  "mirror": "/ingenieure/06-tests-et-preuves",
  "related": [
    "/accessible/03-besoin-et-contrats",
    "/accessible/11-methode-et-cas-pratiques"
  ],
  "notions": [
    {
      "label": "CI",
      "anchor": "ci"
    },
    {
      "label": "Invariant",
      "anchor": "invariant"
    },
    {
      "label": "Contrat",
      "anchor": "contrat"
    }
  ],
  "previous": "/accessible/05-git-et-collaboration",
  "next": "/accessible/07-asynchronisme-et-reprises"
}

## Ce que tu sauras faire

Savoir ce qu'un test démontre et poser les bonnes questions à la livraison.

## Première synthèse

« Les tests passent » n'est utile que si l'on sait lesquels et ce qu'ils vérifient. Un test peut prouver que le bouton apparaît tout en ignorant que le fichier est accessible à un autre client. Commence par les erreurs qui coûteraient le plus cher : perte, duplication, divulgation ou blocage.

Demande une preuve du problème avant la correction, puis la même vérification après. Pour un doublon, il faut montrer que deux demandes représentant la même intention ne créent qu'une seule commande. Un résultat visuel agréable ne répond pas à cette question.

Les tests automatiques, l'essai du parcours réel et la lecture du changement se complètent. Aucun ne donne une certitude universelle. Une livraison fiable indique les vérifications exécutées et les risques qu'elles ne couvrent pas encore.

## Déroulé prévu

1. Exemple attendu, test automatique et essai réel.
2. Tester les erreurs coûteuses.
3. Lire un résultat de test sans surinterpréter le vert.
4. Demander une seconde lecture du changement.

## Mise en pratique

Associer une preuve au risque de doublon, au risque d'accès croisé et au risque de fichier incomplet.

## Critère de réussite

Les trois risques ont des critères distincts et aucun n'est déclaré couvert par une simple capture d'écran.

## Sources et limites

[O-MD §7](/references/sources/o-md#section-7) ; [I-MD §5](/references/sources/i-md#section-5).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A06](/redaction/a06-tests-et-preuves).
