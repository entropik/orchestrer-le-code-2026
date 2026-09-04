# Fiches réflexes communes aux deux lectures

Ces listes de contrôle fournissent les garde-fous partagés par le pilotage accessible et l'ingénierie approfondie avant chaque engagement d'action.

## Lancer une tâche

- Quel résultat pour quel utilisateur ?
- Quelles données et quelles zones du projet sont concernées ?
- Qu'est-ce qui est autorisé : analyser, modifier, partager, publier ?
- Quels cas limites et quelles preuves observables sont exigés ?
- À quel moment précis arrêter le travail de l'agent pour solliciter un arbitrage humain ?

## Accepter une contribution

- L'intention est claire et la liste des fichiers modifiés est rigoureusement justifiée.
- Les tests indiquent les commandes de reproduction, les résultats attendus et les limites.
- Les droits d'accès, les flux de données et les effets de bord répétés sont examinés.
- Les décisions d'architecture et les changements de contrats sont tracés dans des ADRs.
- La stratégie de retour arrière prend en compte l'état des données persistantes, pas seulement le code source.

## Autoriser une livraison

- Version sémantique et artefact de déploiement formellement identifiés.
- Configuration d'environnement et secrets disponibles avec les permissions de moindre privilège.
- Procédure de migration répétée et validée dans un environnement miroir adapté.
- Parcours critique utilisateur vérifié et instrumenté après bascule.
- Rôle de l'observateur, seuils d'arrêt d'urgence et mécanismes de reprise après incident documentés.

## Comparer deux outils ou modèles

- Même tâche de référence, même jeu d'essai et mêmes critères d'acceptation stricts.
- Versions exactes, licences d'exploitation et conditions d'hébergement identifiées.
- Résultats bruts, taux de corrections humaines nécessaires et coût complet (tokens/temps) enregistrés.
- Flux sortants de données, télémétrie et autorisations des connecteurs tiers audités.
- Faisabilité et coût réel d'un remplacement ultérieur testés en pratique.

---

*Adaptation éditoriale de O-MD §14 et I-MD §10/§12. Pour l'enchaînement opérationnel pas à pas, consulter le [Guide des workflows](02-guide-des-workflows.md), l'[Architecture du harnais](03-architecture-du-harnais.md) et le [Catalogue des 37 skills](04-catalogue-des-skills.md).*
