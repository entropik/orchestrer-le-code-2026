{
  "title": "Passer du poste local à un service réel",
  "description": "Autoriser une livraison en sachant quelle version part, comment la vérifier et comment arrêter.",
  "weight": 9,
  "chapter_id": "A09",
  "theme": "09",
  "status": "amorce",
  "source_path": "manuscrit/01-lecture-accessible/09-livraison-et-production.md",
  "mirror": "/ingenieure/09-livraison-et-production",
  "related": [
    "/accessible/05-git-et-collaboration",
    "/accessible/10-exploitation-et-evolution"
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
  "previous": "/accessible/08-donnees-et-migrations",
  "next": "/accessible/10-exploitation-et-evolution"
}

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

[O-MD §8](/references/sources/o-md#section-8) ; [I-MD §8, §10.2](/references/sources/i-md#section-8).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Références pour approfondir

- [Caddy — module de limitation de débit](https://caddyserver.com/docs/modules/http.handlers.rate_limit) — Module non standard : sa présence doit être vérifiée. [Notice et chapitres associés](/references#ref-caddy).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A09](/redaction/a09-livraison-et-production).
