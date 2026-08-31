# Synthèse : une intention, deux profondeurs de lecture

## Décision éditoriale

Le nouveau manuel enseigne la même démarche deux fois, avec deux profondeurs. La lecture accessible donne au lecteur les moyens de comprendre, questionner et décider. La lecture ingénieure lui permet ensuite d'expliquer les mécanismes, de concevoir une solution et d'en examiner les garanties.

Nous conservons la progression orientée décision de O-MD et la matière technique de I-MD. Nous ne juxtaposons pas les ouvrages et nous ne plaçons pas tous les approfondissements dans des encadrés au milieu de la première lecture. Chaque partie constitue un parcours complet.

## Ce qui est commun aux deux approches

Les deux documents s'accordent sur l'essentiel : la vitesse de génération ne suffit pas ; l'architecture rend les responsabilités visibles ; une demande doit devenir vérifiable ; Git conserve les changements ; les tests et la revue apportent des éléments de confiance ; la production exige des moyens d'observation et de reprise.

Leur différence est surtout une différence de point de vue. Le guide demande « quelle décision prendre, quelle preuve réclamer ? ». Le traité demande « par quel mécanisme obtenir cette propriété ? ». Le nouveau manuel relie ces deux questions chapitre par chapitre.

## Arbitrages de synthèse

| Sujet | Apport accessible | Apport ingénieur | Arbitrage retenu |
|---|---|---|---|
| Architecture | Responsabilités et monolithe modulaire. | Modules profonds, DDD, ports et seams. | Le découpage suit les changements et invariants, pas une architecture obligatoire. |
| Besoin | Scénario, acceptation, exclusions, ADR. | Schémas, types et parsing. | Le contrat technique formalise le besoin sans le remplacer. |
| Harnais | Mission claire et niveaux d'autorisation. | Inspection structurée, sandbox et boucle de validation. | Politique compréhensible + contrôles effectifs. |
| Git | Histoire et revue lisibles. | Worktrees, PR dépendantes et bisect. | Une intention cohérente, pas un plafond arbitraire de fichiers. |
| Tests | Preuves proportionnées aux risques. | TDD, propriétés, mutations et tests concurrents. | Tests utiles et relus, sans promesse de preuve universelle. |
| Livraison | Préparer, vérifier et observer. | Artefacts, migrations, reverse proxy et drainage. | Continuité et retour démontrés dans leur périmètre. |
| Exploitation | Mesurer, stabiliser et restaurer. | Télémétrie, SQL, pools, WAL et reprise. | Objectifs et mesures plutôt que délais universels. |
| Écosystème | Choisir selon les besoins et les données. | Versions, licences, runtime, protocoles et évaluation. | Indépendance mesurée plutôt que interchangeabilité supposée. |

Sources : O-MD chapitres 1 à 14 ; I-MD chapitres 1 à 12, localisés dans l'[inventaire](01-corpus.md).

## Une méthode de pilotage et une séquence technique

ORCHESTRE reste la méthode nommée, car elle accompagne le décideur avant, pendant et après la réalisation. Les six phases KISS deviennent des étapes techniques à l'intérieur d'une tranche, pas une deuxième méthode concurrente à mémoriser.

| ORCHESTRE, issu de O-MD §11 | Travail technique relié à I-MD §9 |
|---|---|
| Observer ; Résultat | Inspection et spécification. |
| Cartographier ; Hypothèse | Frontières, contrats, décisions et risques. |
| Expérimenter | Tests initiaux et implémentation minimale. |
| Sécuriser | Intégration, droits, échecs et moyens de reprise. |
| Tracer | Commits, contrats, ADR et dossier de livraison. |
| Relire | Revue du changement et de ses preuves. |
| Exposer | Staging, publication autorisée et observation. |

Cette correspondance est une proposition éditoriale. Elle résout une tension du corpus : le guide recommande des tranches verticales, tandis que certains exemples du traité découpent le travail par couches. Une fonctionnalité reste une tranche démontrable ; elle peut contenir plusieurs sous-étapes techniques.

## Deux lectures sans contradiction

A07 peut expliquer qu'un réessai ne doit pas recréer une commande. B07 montre comment définir l'intention, placer une contrainte et traiter les échecs partiels. A07 ne dit jamais qu'un bouton désactivé suffit : il simplifie le vocabulaire, pas l'invariant.

A12 peut expliquer qu'un modèle local ne signifie pas une exploitation gratuite. B12 détaille le runtime, la mémoire, la licence et le protocole d'évaluation. Les deux parlent de la même décision ; seule la résolution de l'explication change.

Un lecteur peut parcourir A01 à A12 sans ouvrir B. Un autre peut lire B01 à B12 avec un rappel bref des problèmes métier. Un troisième peut lire A03 puis B03 directement. Les liens miroirs et un glossaire partagé soutiennent ces usages.

## Couverture du traité complet

| Source technique I-MD | Chapitres miroirs du nouveau manuel |
|---|---|
| §1 Harnais | 01 et 04 |
| §2 Abstractions et modularité | 02 ; seams réutilisés en 10 |
| §3 Contrats | 03 |
| §4 Git | 05 |
| §5 Vérification | 06 |
| §6 Asynchronisme | 07 |
| §7 Persistance | 08 et 10 |
| §8 Déploiement | 09 |
| §9 KISS | 01 et 11 |
| §10 Prompts | 03, 04, 09 et 11 ; fiches partagées |
| §11 Exploitation et mémoire | 04, 07 et 10 |
| §12 Écosystème | **12 dans les deux lectures** |

Les cas O-MD §12 et §13 alimentent tout le fil rouge et sont réunis au nouveau chapitre 11. Les fiches O-MD §14 deviennent des annexes communes. La matière du chapitre 12 ajouté par l'utilisateur n'est donc ni perdue ni limitée à une annexe.
