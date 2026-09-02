# Recherche du manuel

## Origine et périmètre

Adaptation de la recherche maison du dépôt local `C:/Code/digest-web`, examiné à la révision `c5c6c95f289fd882e03be4a3ef8591082327a577`. Les points de départ sont `assets/js/digest.js` (normalisation, filtrage par tous les termes, cache et gestion des erreurs) et `layouts/index.html` (index JSON produit par Hugo, minifié et identifié par son empreinte).

La recherche active de Digest ne dépend pas de Fuse/PaperMod. Aucune bibliothèque du thème PaperMod, aucun favori, service d'administration, calendrier ou catalogue Digest n'est importé ici. Le dépôt Digest n'est pas modifié.

## Adaptations au livre

- Index des pages du manuel, plus le contenu de la page de références ; inclut les quatre Markdown intégraux et les quatre extractions PDF publiés en HTML. Les images des pages PDF ne sont pas indexées. Un résultat de source ouvre sa page de lecture complète.
- Prise en compte des titres, du texte, des descriptions, des identifiants de chapitre et des notions en marge.
- Les libellés des schémas graphiques sont indexés ; leur copie ASCII dépliable est exclue de l'index pour éviter de dupliquer les mêmes textes. Les autres blocs de code restent indexés.
- Filtres pour les deux lectures, les références et annexes, le projet et la rédaction.
- Priorité aux titres, puis aux chapitres ; extraits textuels et affichage par lots de vingt résultats.
- Index chargé à la première requête, partagé entre recherches et rechargeable après erreur.
- Numéro de révision de la recherche pour ignorer une réponse devenue obsolète.
- Résultats construits avec `textContent`, liens limités au site et au préfixe de publication.
- Recherche clavier avec `/`, sans détourner la saisie dans un champ ; champ et filtres natifs, nombre de résultats annoncé.
- Aucun appel à un service de recherche tiers. La requête figure dans l'URL pour permettre de revenir à la recherche ou de la partager.

## Vérification

Après `hugo --panicOnWarning`, exécuter `node --test tests/test_search.mjs`. Le test du rendu vérifie les 24 chapitres, les destinations, les notions et un budget maximal de 750 Ko pour l'index.

Pour vérifier un autre dossier de sortie, définir la variable d'environnement `MANUEL_SITE_DIR`. Les chemins et l'index doivent également fonctionner lorsque le site est servi sous un préfixe.
