{
  "title": "Transformer le besoin en contrat vérifiable",
  "description": "Relier invariants, schémas, validation à l'exécution et compatibilité des contrats.",
  "weight": 3,
  "chapter_id": "B03",
  "theme": "03",
  "status": "amorce",
  "source_path": "manuscrit/02-lecture-ingenieure/03-besoin-et-contrats.md",
  "mirror": "/accessible/03-besoin-et-contrats",
  "related": [
    "/ingenieure/02-architecture-et-frontieres",
    "/ingenieure/06-tests-et-preuves"
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
  "previous": "/ingenieure/02-architecture-et-frontieres",
  "next": "/ingenieure/04-harnais-et-contexte"
}

## Ce que tu sauras faire

Relier invariants, schémas, validation à l'exécution et compatibilité des contrats.

## Première synthèse

Le schéma d'une requête ne remplace pas la règle métier. Une taille entière positive peut être syntaxiquement valide tout en dépassant le quota de l'organisation. Le contrat doit donc distinguer validation de structure, autorisation et invariants dépendant de l'état courant.

Définir les schémas avant l'implémentation rend les hypothèses inspectables. Cela n'impose pas de figer définitivement le contrat : une évolution justifiée passe par une décision explicite et des tests de compatibilité. Le compilateur vérifie une partie des usages internes ; les données externes doivent toujours être contrôlées à l'exécution.

Pour l'upload, documenter les unités, les identifiants, les erreurs, l'expiration et la finalisation. La limite pédagogique de 500 Mo doit devenir une quantité précise d'octets avant tout test. Un test qui vérifie seulement la forme du JSON ne prouve ni l'appartenance du fichier ni son intégrité.

## Déroulé prévu

1. SPEC, invariants et ADR (voir l'outillage dans le [Guide des workflows](/annexes/workflows)).
2. Schémas d'entrée, sortie et erreurs.
3. Typage statique versus parsing à l'exécution.
4. Évolution additive et compatibilité des consommateurs.

## Mise en pratique

Produire les contrats de création et de finalisation de session, avec erreurs et règles d'évolution.

## Critère de réussite

Structure, droits et invariants sont testables séparément ; aucune assertion de type ne sert de validation réseau.

## Sources et limites

[O-MD §3, §12](/references/sources/o-md#section-3) ; [I-MD §3, §9.3, §10.2](/references/sources/i-md#section-3).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Références pour approfondir

- [TypeScript — assertions de type](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions) — Les assertions de type ne vérifient pas les données à l'exécution. [Notice et chapitres associés](/references#ref-typescript).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche B03](/redaction/b03-besoin-et-contrats).
