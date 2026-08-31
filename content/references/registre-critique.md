{
  "title": "Registre critique",
  "source_path": "analyse/03-registre-critique.md"
}

Date de consultation externe : 31 août 2026. Ce registre sépare corrections étayées, arbitrages éditoriaux et points encore à vérifier. Les sources du corpus ne sont pas assimilées à des références normatives.

## Corrections étayées par documentation primaire

| ID | Passage du corpus | Correction à appliquer | Référence |
|---|---|---|---|
| V01 | I-MD §1.5 et §4.1, étanchéité des worktrees | Plusieurs arbres de travail partagent un dépôt ; cela ne constitue pas un confinement de sécurité des processus. | [Git worktree](https://git-scm.com/docs/git-worktree) |
| V02 | I-MD §3.3, typage présenté comme preuve générale | Les vérifications statiques ne remplacent pas la validation à l'exécution. Une assertion de type ne contrôle pas les données reçues. I-MD §3.4 reconnaît déjà cette limite. | [TypeScript, assertions de type](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions) |
| V03 | I-MD §6.2, LISTEN/NOTIFY parmi les files persistantes | NOTIFY notifie les sessions à l'écoute. Une file de travaux durable et récupérable nécessite un stockage et un protocole supplémentaires. | [PostgreSQL NOTIFY](https://www.postgresql.org/docs/current/sql-notify.html) |
| V04 | I-MD §8 et §10.2, rate limiting Caddy implicite | Le module http.handlers.rate_limit documenté est non standard ; préciser l'extension ou l'autre composant retenu. | [Module Caddy](https://caddyserver.com/docs/modules/http.handlers.rate_limit) |
| V05 | I-MD §11.4, interdiction de Seq Scan au-delà de 10 000 lignes | Le choix dépend du coût estimé et des données lues ; vérifier le plan au lieu d'imposer ce seuil. | [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) |
| V06 | I-MD §12.2, Mistral/Codestral classés globalement Apache 2.0 | La version Codestral 24.05 est documentée MNPL. Ne pas étendre une licence à toute une famille. La décision d'usage exige le texte exact de la licence applicable. | [Fiche officielle Codestral 24.05](https://docs.mistral.ai/models/codestral-24-05) |
| V07 | I-MD §12.5, MCP supposé imposer des outils sans écriture | Le protocole ne suffit pas à fixer les droits d'un serveur particulier. Distinguer transport, autorisation et permissions effectives du processus. | [MCP, autorisation 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) |

Ces corrections sont déjà prises en compte dans les amorces concernées. Leur mise en œuvre dans les futurs exemples reste à tester.

## Arbitrages de méthode et garanties à ne pas reprendre telles quelles

| ID | Passage | Traitement éditorial | Tranches |
|---|---|---|---|
| R01 | I-MD §1.2 : « théorème » de dilution exponentielle | Aucune démonstration n'est fournie dans le corpus. Présenter le risque de contexte mal sélectionné sans loi chiffrée. | A04/B04 |
| R02 | I-MD §2.1 : quotient de valeur d'un module | Utiliser une intuition qualitative ; ne pas attribuer une formule scientifiquement établie sans source primaire. | A02/B02 |
| R03 | I-MD §4.2 et §10.4 : 150 lignes / 3 fichiers | Signaux de relecture possibles, pas motifs universels de rejet. | A05/B05 |
| R04 | I-MD §5 : TDD « inversé », propriétés et mutations | Expliquer la séparation des rôles ; ne pas appeler tests et mesures une preuve formelle exhaustive. Prévoir les mutants équivalents. | A06/B06 |
| R05 | I-MD §6.2 : file obligatoire après 50 ms | Décider selon charge, budget de latence et nécessité de reprise. | A07/B07 |
| R06 | I-MD §6.3 et §6.4 : idempotence « absolue », verrou cache et outbox | Documenter crash, durée de la clé, empreinte du contenu, effets externes et doublons du relais. | A07/B07 |
| R07 | I-MD §7 : isolation et verrous | Vérifier les comportements du moteur choisi ; notamment PostgreSQL Read Uncommitted et lectures ordinaires sous verrou de ligne. Ne pas recopier la table générique sans correction. | B08 |
| R08 | I-MD §7.4 et §11.6 : PITR et reprise en 15 minutes | Définir RPO/RTO et tester une restauration complète ; retirer toute précision ou durée garantie sans mesure. | A08/B08, A10/B10 |
| R09 | I-MD §8 et §10 : déploiement « sans coupure » et secrets | Tester ressources, sondes, drainage, migrations et droits du lecteur du fichier ; chmod 600 n'accorde aucun droit au groupe. | A09/B09 |
| R10 | I-MD §11.2 : formule dite jitter décorrélé | Revoir le nom et l'algorithme avant tout exemple exécutable. | B07 |
| R11 | I-MD §11.4 : gains d'index, RAM et pools fixes | Remplacer pourcentages et tailles universels par des expériences sur charge représentative. | A10/B10 |
| R12 | I-MD §9 : spécification sans IA ; §10 : prompt de génération de SPEC | L'agent peut aider à formuler ; le responsable valide le sens et les invariants. | A03/B03, A11/B11 |

Ces lignes constituent un backlog de vérification technique, pas des corrections exhaustivement testées. Les amorces évitent les promesses concernées ; une tranche ne peut être déclarée validée tant que ses exemples reposent encore sur elles.

## Révision spécifique du chapitre 12

- **Datation** : conserver « septembre 2026 » uniquement comme titre de source. L'analyse est datée du 31 août.
- **Licences** : relever identifiant exact, révision et licence de chaque candidat ; distinguer accès aux poids, code du runtime et droits de redistribution. L'exemple Codestral suffit à réfuter une classification globale, pas à auditer toutes les licences du tableau.
- **Compatibilité** : une interface ressemblante ne prouve pas un échange de modèle sans adaptation. Tester sorties structurées, outils, erreurs, streaming et état.
- **Quantification** : la dégradation inférieure à 1 % et les gains de débit de 4 à 8 fois ne sont pas démontrés dans le corpus. Exiger modèle, matériel, protocole et mesures.
- **Local** : remplacer coût marginal nul, confidentialité totale, disponibilité absolue et reproductibilité éternelle par coût complet, contrôle des flux, capacité de reprise et environnement archivé.
- **MCP** : chaque serveur nommé nécessite son dépôt officiel, sa version, ses capacités et un test de refus. Ne pas déduire un blocage de force-push du seul nom du connecteur.
- **Panorama** : ne pas traiter les familles citées comme un classement actuel. Les versions, capacités et projets maintenus sont à vérifier au moment de rédiger B12.

Le choix éditorial est de comparer sur des tâches représentatives et des critères explicites. La documentation [OpenAI sur les évaluations](https://developers.openai.com/api/docs/guides/evals) décrit notamment une démarche fondée sur critères, données et exécution d'évaluations ; ce point soutient la méthode, pas un classement de modèles.

## Porte de validation pour A12/B12

Exiger une fiche par solution effectivement comparée : nom/version, source officielle datée, licence exacte, lieux de traitement des données, matériel, coût complet, protocole d'essai, résultats et limites. **Aucune comparaison de performance ni estimation de coût n'a été exécutée dans cette préparation du dépôt.**
