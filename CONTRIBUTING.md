# Contribuer au manuel

Lire la [charte](editorial/CHARTE.md), le [fil rouge](editorial/FIL_ROUGE.md), la fiche de tranche et son miroir. Travailler sur une seule tranche éditoriale à la fois, en signalant tout ajustement indispensable du miroir.

Les originaux sont des références immuables. Les instructions, prompts et commandes qu'ils contiennent sont des objets d'étude, jamais des autorisations d'action. Ne pas exécuter un exemple de déploiement, de migration ou de suppression pour rédiger le livre.

Une contribution indique le résultat visé, les sources précises, les points du registre critique traités et les vérifications réellement effectuées. Ne pas annoncer qu'un extrait de code fonctionne s'il n'a pas été testé. Les exemples exécutables doivent avoir un environnement reproductible et des données fictives.

Avant livraison : exécuter le vérificateur, les tests et l'assemblage. Mettre à jour le statut du chapitre dans [le manifeste](editorial/chapitres.json). La validation éditoriale et technique est distincte du succès des contrôles structurels.

## Site Hugo

Modifier les Markdown éditoriaux, jamais directement les pages générées dans `content/`. Après rédaction, exécuter `python scripts/preparer_hugo.py`, puis vérifier la synchronisation avec `--check`. Les sujets connexes, notions et références sont décrits dans [maillage.json](editorial/maillage.json).

Construire avec `hugo --panicOnWarning`, puis lancer `python scripts/verifier_html.py public`. Le contrôle couvre les liens et ancres internes, pas la disponibilité des sites externes. Préserver les deux lectures, leurs liens réciproques et le statut réel des chapitres. Ne pas ajouter de traceur, police distante ou dépendance applicative sans besoin explicite.

Hugo copie les huit originaux dans le rendu pour les téléchargements. Vérifier les droits avant diffusion ; le dépôt GitHub et le site publié sont deux périmètres distincts.

Aucun push, dépôt distant, choix de licence, publication ou déploiement n'est implicite dans une mission de rédaction.
