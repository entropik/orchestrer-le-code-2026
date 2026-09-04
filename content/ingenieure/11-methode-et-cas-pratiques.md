{
  "title": "Appliquer ORCHESTRE du besoin à la résolution",
  "description": "Raccorder la méthode de pilotage aux étapes techniques sans construire un cycle en cascade.",
  "weight": 11,
  "chapter_id": "B11",
  "theme": "11",
  "status": "amorce",
  "source_path": "manuscrit/02-lecture-ingenieure/11-methode-et-cas-pratiques.md",
  "mirror": "/accessible/11-methode-et-cas-pratiques",
  "related": [
    "/ingenieure/01-piloter-un-systeme",
    "/ingenieure/06-tests-et-preuves"
  ],
  "notions": [
    {
      "label": "ADR",
      "anchor": "adr"
    },
    {
      "label": "Tranche verticale",
      "anchor": "tranche-verticale"
    },
    {
      "label": "Idempotence",
      "anchor": "idempotence"
    }
  ],
  "previous": "/ingenieure/10-exploitation-et-evolution",
  "next": "/ingenieure/12-ecosysteme-et-independance"
}

## Ce que tu sauras faire

Raccorder la méthode de pilotage aux étapes techniques sans construire un cycle en cascade.

## Première synthèse

Les six phases KISS du traité organisent la fabrication : spécification, contrats, tests, implémentation, intégration et livraison. ORCHESTRE organise la décision et la preuve. Les deux grilles se combinent à l'intérieur d'une tranche verticale ; elles ne justifient pas de construire toutes les tables avant tout parcours utilisateur.

Le cas de réception de fichier doit conserver les mêmes acteurs, états et contraintes que la lecture accessible. La version ingénieure ajoute les contrats, fenêtres de crash, jeux d'essai et procédures de livraison. Elle ne doit pas changer de produit pour exhiber une architecture plus sophistiquée.

Le cas de doublon exige un test d'intégration concurrent, une définition de l'intention et une migration compatible avec les clients existants. Le compte rendu final sépare démonstration sur fixture, test sur infrastructure réelle et observation de production. Une illustration dans un livre ne doit jamais être présentée comme une exécution effectivement menée.

## Déroulé prévu

1. Correspondance ORCHESTRE et six phases KISS.
2. Tranches verticales et sous-étapes de réalisation (formalisation complète dans le [Guide des workflows agentiques](/annexes/workflows-agentiques)).
3. Upload : session, droits, finalisation et reprise.
4. Doublon : reproduction causale, contrainte, migration et observation.

## Mise en pratique

Produire deux dossiers de réalisation avec SPEC, ADR, matrice de tests et plan de livraison.

## Critère de réussite

Chaque décision de la partie accessible trouve sa justification technique, sans garantie ajoutée après coup.

## Sources et limites

[O-MD §5, §11, §12, §13, §14](/references/sources/o-md#section-5) ; [I-MD §9, §10](/references/sources/i-md#section-9).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Rédaction de ce chapitre

[Objectifs et critères de la tranche B11](/redaction/b11-methode-et-cas-pratiques).
