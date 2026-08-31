{
  "title": "Appliquer ORCHESTRE du besoin à la résolution",
  "description": "Piloter une fonctionnalité puis une correction avec la même méthode de décision.",
  "weight": 11,
  "chapter_id": "A11",
  "theme": "11",
  "status": "amorce",
  "source_path": "manuscrit/01-lecture-accessible/11-methode-et-cas-pratiques.md",
  "mirror": "/ingenieure/11-methode-et-cas-pratiques",
  "related": [
    "/accessible/01-piloter-un-systeme",
    "/accessible/06-tests-et-preuves"
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
  "previous": "/accessible/10-exploitation-et-evolution",
  "next": "/accessible/12-ecosysteme-et-independance"
}

## Ce que tu sauras faire

Piloter une fonctionnalité puis une correction avec la même méthode de décision.

## Première synthèse

ORCHESTRE donne un fil conducteur : observer, définir le résultat, cartographier, choisir une hypothèse, expérimenter, sécuriser, tracer, relire et exposer. Tu n'as pas besoin de transformer chaque lettre en réunion. Il faut surtout pouvoir retrouver les décisions et les preuves importantes.

Pour le dépôt de PDF, commence par une petite réception complète, avec droits et état visibles. Ajoute ensuite la reprise après coupure et les contrôles nécessaires. Une tranche doit produire un comportement démontrable, pas seulement une nouvelle couche technique.

Pour un doublon de commande, ne confonds pas le déclencheur et le défaut. Un double clic peut déclencher deux requêtes ; la fragilité est que le serveur accepte deux fois la même intention. La méthode garde l'enquête ouverte jusqu'à une preuve du mécanisme, puis exige un test qui empêche son retour.

## Déroulé prévu

1. Les neuf étapes ORCHESTRE.
2. Cas fil rouge : recevoir un PDF avec reprise.
3. Cas incident : deux commandes pour une intention.
4. Décider, accepter et transmettre le travail.

## Mise en pratique

Écrire le dialogue de pilotage de ces deux cas, avec les décisions d'acceptation.

## Critère de réussite

Les neuf étapes sont retrouvables ; aucune publication n'est implicite.

## Sources et limites

[O-MD §5, §11, §12, §13, §14](/references/sources/o-md#section-5) ; [I-MD §9, §10](/references/sources/i-md#section-9).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A11](/redaction/a11-methode-et-cas-pratiques).
