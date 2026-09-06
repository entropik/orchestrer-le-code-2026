{
  "title": "Analyse du corpus",
  "source_path": "analyse/01-corpus.md"
}

Analyse du 31 août 2026. Huit fichiers fournis, organisés en deux familles éditoriales. Les identifiants ci-dessous sont ceux utilisés dans toutes les fiches. Les empreintes et comptages reproductibles sont dans [inventaire.json](/projet/corpus).

## Inventaire commenté

| ID | Document | Étendue observée | Rôle |
|---|---|---|---|
| O-MD | [manuel_orchestration_logicielle.md](/projet/references/sources/o-md) | 14 chapitres, avant-propos et conclusion ; 8 226 mots par découpage sur les espaces | Référence pédagogique principale. |
| O-PDF | [manuel_orchestration_logicielle.pdf](/projet/references/sources/o-pdf) | 31 pages ; environ 3 996 mots extraits | Version plus courte, pas un équivalent exhaustif du Markdown. |
| O1-PDF | [manuel_orchestration_logicielle (1).pdf](/projet/references/sources/o1-pdf) | 55 pages ; 8 285 mots extraits, en-têtes compris | Export développé, même progression générale que O-MD. |
| O2-PDF | [manuel_orchestration_logicielle (2).pdf](/projet/references/sources/o2-pdf) | 55 pages | Doublon binaire exact de O1-PDF. |
| S-PDF | [manuel_architecture_systemique_complet.pdf](/projet/references/sources/s-pdf) | 25 pages ; sommaire et fin couvrant les chapitres 1 à 9 | État antérieur du traité ; ne contient pas les chapitres 10 à 12. |
| S-MD | [MANUEL_ARCHITECTURE_SYSTEMIQUE_COMPLET.md](/projet/references/sources/s-md) | 10 chapitres ; 10 300 mots | Traité avec bibliothèque de prompts. |
| SF-MD | [MANUEL_ARCHITECTURE_SYSTEMIQUE_COMPLET_EDITION_FINALE.md](/projet/references/sources/sf-md) | 11 chapitres ; 11 993 mots | Ajout exploitation, résilience, mémoire et reprise. |
| I-MD | [MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md](/projet/references/sources/i-md) | 12 chapitres ; 13 214 mots | **Référence technique principale demandée par l'utilisateur.** |

Les mots ne sont pas une mesure de qualité ni un indicateur d'équivalence exacte. L'extraction PDF ajoute en-têtes et pieds de page, peut déformer les tableaux et ne remplace pas une comparaison éditoriale.

## Ce que les comparaisons établissent

O1-PDF et O2-PDF ont la même taille et le même SHA-256 : ils sont strictement identiques. Ils restent conservés sous leurs noms d'origine pour tracer les huit pièces, mais ne comptent pas comme deux sources indépendantes.

Le diff S-MD → SF-MD ajoute le chapitre 11 et son entrée au sommaire. Il ne constitue pas une révision critique du corps précédent.

Le diff SF-MD → I-MD ajoute le chapitre 12 et met à jour la présentation. Il corrige aussi des échappements de formules et ajoute un titre de commandes worktree. Les prescriptions anciennes restent largement inchangées : « complet » ne signifie donc pas « techniquement validé ».

Le sommaire de S-PDF (page 2) et ses dernières pages (23 à 25) s'arrêtent à la méthode KISS, chapitre 9. Le PDF court O-PDF conserve la progression générale mais n'offre pas le développement de O-MD ; les volumes et sections développées diffèrent. Les deux familles ne doivent pas être fusionnées par simple concaténation.

## Approche O : apprendre à décider

Le guide part de métaphores compréhensibles puis relie architecture, cadrage, harnais, Git, tests et production. ORCHESTRE donne une mémoire courte de la démarche. Les deux cas longs, réception d'un PDF et doublon de commande, montrent comment passer d'un symptôme à des critères puis à des preuves.

Sa force est la progression et l'explicitation des autorisations. Sa limite est la densité parfois élevée de notions techniques pour un lecteur débutant ; plusieurs approfondissements devront passer dans la lecture B. Les exemples sont pédagogiques, pas des résultats d'essais exécutés.

## Approche I : expliquer les garanties et mécanismes

Le traité apporte modules profonds, seams, DDD, ports/adaptateurs, schema-first, worktrees, tests de propriétés et de mutation, concurrence, outbox, migrations et exploitation. Le chapitre 12 élargit la question au choix des modèles, à l'inférence locale et aux connecteurs.

Sa force est de rendre visibles les mécanismes cachés derrière les décisions. Sa limite est de présenter plusieurs choix situés comme des lois universelles : tailles de PR, seuils de latence, architecture obligatoire, tests assimilés à des preuves formelles et garanties absolues d'hébergement. Le registre critique évite leur reprise sans nuance.

## Chapitre 12 : ce qui doit être conservé et revérifié

Conserver les six questions : portabilité, modèles et licences, moteurs d'inférence, agents, MCP et arbitrage cloud/local. Ne pas recopier son palmarès comme une photographie validée de 2026.

Le titre « Septembre 2026 » est postérieur à la date d'analyse du 31 août. Ce repère est une mention du document, pas une période déjà vérifiée. Les licences sont à vérifier par version ; les promesses de quantification, confidentialité et disponibilité sont à remplacer par des hypothèses testables.

## Méthode et limites de cette analyse

Copies exactes des originaux ; empreintes SHA-256 ; extraction des quatre PDF ; comparaison des versions Markdown ; examen des sommaires, sections et ajouts ; contrôle visuel d'une page représentative de chacune des deux familles PDF. Il ne s'agit pas d'un audit typographique exhaustif des 166 pages fournies, ni d'une exécution des exemples.

Une vérification externe ciblée a porté sur quelques affirmations à risque ; elle est documentée dans le [registre critique](/projet/references/registre-critique). Le panorama complet des outils et modèles demeure un travail de rédaction pour A12/B12. Aucun ordre figurant dans les sources n'a été exécuté en tant qu'instruction.
