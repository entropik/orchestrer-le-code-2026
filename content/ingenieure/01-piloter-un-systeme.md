{
  "title": "Piloter un système, pas une génération de code",
  "description": "Formaliser le système de contrôle entourant un agent et ses limites de garantie.",
  "weight": 1,
  "chapter_id": "B01",
  "theme": "01",
  "status": "amorce",
  "source_path": "manuscrit/02-lecture-ingenieure/01-piloter-un-systeme.md",
  "mirror": "/accessible/01-piloter-un-systeme",
  "related": [
    "/ingenieure/04-harnais-et-contexte",
    "/ingenieure/11-methode-et-cas-pratiques"
  ],
  "notions": [
    {
      "label": "Agent",
      "anchor": "agent"
    },
    {
      "label": "Harnais",
      "anchor": "harnais"
    },
    {
      "label": "Invariant",
      "anchor": "invariant"
    }
  ],
  "next": "/ingenieure/02-architecture-et-frontieres"
}

## Ce que tu sauras faire

Formaliser le système de contrôle entourant un agent et ses limites de garantie.

## Première synthèse

Le harnais est un système de contrôle : il sélectionne le contexte, autorise certaines actions, observe leurs effets et décide du passage à l'étape suivante. La génération peut varier ; les critères d'acceptation doivent rester identifiables. Dire que le harnais est déterministe ne suffit pas à établir la correction du programme qu'il accepte.

Pour la réception d'un fichier, le modèle d'état sépare au minimum la session créée, le transfert en cours, la réception complète et la validation métier. Chaque transition possède un acteur autorisé, une précondition et une trace observable. Le passage de reçu à utilisable exige une preuve distincte de la seule réussite de la requête HTTP.

Les contrôles portent aussi sur l'agent : droits du processus, ressources accessibles, budget et opérations externes. Une consigne textuelle exprime la politique ; elle ne remplace pas son application dans les outils et l'environnement. La revue doit donc examiner à la fois le changement produit et le dispositif qui a permis de le produire.

## Déroulé prévu

1. État, transitions, entrées-sorties et effets de bord.
2. Boucles de rétroaction : observation, action et validation.
3. Politiques d'autorisation et barrières effectivement appliquées.
4. Budget d'itération, conditions d'arrêt et preuve de livraison.

## Mise en pratique

Décrire la machine à états d'une mission et les contrôles empêchant une publication hors périmètre.

## Critère de réussite

Chaque transition indique son autorité, son observation et sa condition d'arrêt.

## Sources et limites

[O-MD §1, §4, §5](/references/sources/o-md#section-1) ; [I-MD §1, §9.5](/references/sources/i-md#section-1).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Rédaction de ce chapitre

[Objectifs et critères de la tranche B01](/redaction/b01-piloter-un-systeme).
