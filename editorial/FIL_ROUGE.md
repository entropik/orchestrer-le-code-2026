# Fil rouge : l'atelier d'impression

## Même produit dans les deux lectures

Un client d'un atelier transmet un PDF associé à une commande. L'atelier peut le consulter et le fabriquer uniquement après réception complète et validation. Plusieurs organisations utilisent le même service ; leurs documents restent séparés.

Les cas viennent du guide d'orchestration, chapitres 12 et 13. Les choix ci-dessous constituent le contrat pédagogique du nouveau manuel, pas la description d'une application existante.

## Vocabulaire et décisions éditoriales

- Acteurs : client, opérateur de l'atelier, agent de code, responsable de publication.
- Données : organisation, commande, document, session d'envoi, tentative de traitement.
- Limite de l'exemple : 500 Mo décimaux, soit 500 000 000 octets. Cette précision tranche une ambiguïté du corpus ; ce n'est pas une recommandation universelle.
- États pédagogiques : préparé, en cours, reçu, validé, rejeté, expiré.
- « Reçu » signifie transfert complet ; « validé » signifie contrôles requis réussis.
- Un document rejeté n'est pas fabriqué. Un client ne consulte pas les documents d'une autre organisation.
- Deux requêtes pour une même intention ne doivent pas créer deux commandes.
- La procédure de nouvelle soumission après rejet sera détaillée au chapitre 11 ; elle doit conserver une trace de la tentative précédente.

## Progression

La partie zéro construit une version miniature et locale : lire une commande fictive, inspecter le début d'un fichier, appliquer des règles et produire un rapport. Elle ne traite ni upload, compte utilisateur, base de données ni production.

Les chapitres 01 à 06 cadrent le service et ses preuves. Les chapitres 07 à 10 examinent les reprises, les données, la livraison et l'exploitation. Le chapitre 11 rejoue un ajout de fonctionnalité et une enquête sur un doublon. Le chapitre 12 applique les mêmes missions au choix des outils et des modèles.

## Ce qui reste à concevoir

Le fournisseur de stockage, le framework, le moteur de file et le runtime ne sont pas imposés. Les variantes techniques doivent défendre les mêmes invariants. Les extraits exécutables, fixtures et corrigés détaillés seront produits pendant la rédaction des tranches B.

Aucun fichier client, identifiant réel, accès de production ou service payant n'est nécessaire pour rédiger ces exemples.
