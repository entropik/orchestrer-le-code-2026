{
  "title": "Choisir ses outils et préserver son indépendance",
  "description": "Comparer cloud et local selon l'usage, les coûts et les données plutôt que selon une promesse.",
  "weight": 12,
  "chapter_id": "A12",
  "theme": "12",
  "status": "redaction",
  "source_path": "manuscrit/01-lecture-accessible/12-ecosysteme-et-independance.md",
  "mirror": "/ingenieure/12-ecosysteme-et-independance",
  "related": [
    "/accessible/04-harnais-et-contexte",
    "/accessible/06-tests-et-preuves"
  ],
  "notions": [
    {
      "label": "MCP",
      "anchor": "mcp"
    },
    {
      "label": "Modèle à poids ouverts",
      "anchor": "modele-a-poids-ouverts"
    },
    {
      "label": "Runtime d'inférence",
      "anchor": "runtime-d-inference"
    }
  ],
  "previous": "/accessible/11-methode-et-cas-pratiques"
}

## Ce que tu sauras faire

Comparer cloud et local selon l'usage, les coûts et les données plutôt que selon une promesse.

---

## Première synthèse

### 1. L'artisan et ses machines : pourquoi l'indépendance est la clé de la pérennité

Imagine un maître imprimeur ou un ébéniste d'art qui déciderait d'équiper son atelier avec une presse ultra-perfectionnée. Le constructeur de la machine lui annonce avec le sourire :
- La machine fonctionne uniquement si elle est connectée en permanence aux serveurs du constructeur à l'autre bout du monde.
- Le tarif d'utilisation à la page imprimée peut être multiplié par trois du jour au lendemain sans négociation.
- Chaque document imprimé dans l'atelier est scanné et transmis au constructeur pour « améliorer ses services ».
- Et si un jour le constructeur change de stratégie ou fait faillite, la presse cesse immédiatement de fonctionner, transformée en bloc d'acier inutile.

Quel artisan accepterait de confier l'avenir de son entreprise à de telles conditions ? Aucun.

Pourtant, dans le monde numérique d'aujourd'hui, des milliers d'entrepreneurs et de développeurs tombent exactement dans ce piège. Séduits par les démonstrations éblouissantes des derniers modèles d'intelligence artificielle, ils construisent toute leur activité autour d'une seule interface propriétaire fermée. Le jour où l'opérateur modifie ses tarifs, bloque leur compte pour une erreur de filtre ou ferme une version de modèle, leur système s'effondre.

Être un bon pilote en 2026, c'est savoir tirer parti de la puissance extraordinaire de l'IA **sans jamais lui vendre son indépendance**.

---

### 2. Modèle, moteur, agent et connecteur : clarifier les concepts

Dans les discussions sur l'intelligence artificielle, tout est souvent confondu sous l'étiquette vague d'« IA ». Pour décider avec clarté, distingue quatre rôles fondamentaux :

```text
LES QUATRE ÉTAGES D'UN ENVIRONNEMENT DE TRAVAIL AGENTIQUE :

  ┌─────────────────────────────────────────────────────────────┐
  │ 1. L'AGENT (Le copilote de développement)                   │
  │    • Exemples : Claude Code, Aider, Roo Code, Goose.         │
  │    • Son rôle : Lit tes instructions, planifie les étapes,   │
  │      navigue dans tes fichiers et prépare des modifications.│
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼ (Appels d'outils et requêtes)
  ┌─────────────────────────────────────────────────────────────┐
  │ 2. LE CONNECTEUR / PROTOCOLE (La prise standard)            │
  │    • Standard : Model Context Protocol (MCP), JSON-RPC.     │
  │    • Son rôle : Définit comment l'agent communique avec     │
  │      l'extérieur (base de données, dépôt Git, terminal).    │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼ (Envoi des textes à analyser)
  ┌─────────────────────────────────────────────────────────────┐
  │ 3. LE [RUNTIME D'INFÉRENCE](../03-annexes/05-glossaire.md) (Le moteur d'exécution) │
  │    • Exemples : Ollama, vLLM, API cloud distante.           │
  │    • Son rôle : Le logiciel qui charge le modèle et calcule │
  │      les probabilités des mots (en local sur GPU ou cloud). │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼ (Poids mathématiques)
  ┌─────────────────────────────────────────────────────────────┐
  │ 4. LE MODÈLE (Le cerveau linguistique)                      │
  │    • Exemples : Claude 3.7, GPT-4o, DeepSeek-R1, Qwen 2.5.  │
  │    • Son rôle : Le fichier de milliards de paramètres qui    │
  │      génère le raisonnement et le texte.                    │
  └─────────────────────────────────────────────────────────────┘
```

Changer de modèle ne t'oblige pas à changer d'agent. Changer d'agent ne modifie pas le code de ton application. Cette séparation en couches étanches est ta première protection contre l'enfermement.

---

### 3. Poids accessibles ne veut pas dire « libre de tout usage »

On entend souvent parler de « modèles open source ». Dans le monde de l'IA, cette expression est souvent trompeuse.

Il faut distinguer deux réalités très différentes :
1. **Les modèles à [poids ouverts](/annexes/glossaire) (*Open Weights*)** : Les créateurs publient le fichier contenant les milliards de paramètres du modèle. Tu peux le télécharger sur ta machine et l'exécuter hors ligne sans payer au mot prononcé.
2. **La licence d'utilisation réelle** : Avoir accès aux poids ne signifie pas que tu as le droit de tout faire !

> [!WARNING]
> **Le cas d'école des licences spécifiques** :  
> Un modèle peut être téléchargeable gratuitement tout en imposant des restrictions commerciales sévères. Par exemple, la version **Codestral 24.05** de Mistral a été publiée sous licence **MNPL** (*Mistral Non-Production License*), qui autorise la recherche et les tests personnels mais **interdit formellement l'utilisation en production commerciale sans accord payant**.  
> À l'inverse, des modèles publiés sous licence **Apache 2.0** ou **MIT** accordent une liberté totale d'exploitation commerciale.

Avant d'intégrer un modèle dans les fondations de ton entreprise, ne te contente pas du nom de la marque : vérifie la licence juridique exacte de la version que tu déploies.

---

### 4. Cloud ou Local : le vrai calcul du coût complet (TCO)

Le débat entre modèles hébergés dans le cloud et modèles exécutés en local sur sa propre machine est souvent faussé par des caricatures :
- *« Le cloud est une hérésie pour la confidentialité ! »*
- *« Le local est 100 % gratuit et sans contrainte ! »*

La réalité est beaucoup plus pragmatique et s'évalue sur le **coût complet de possession** (*Total Cost of Ownership*)[^1] :

| Critère d'arbitrage | Modèle Cloud Propriétaire (API distante) | Modèle à Poids Ouverts Local (Sur ton matériel) |
| :--- | :--- | :--- |
| **Confidentialité des données** | Les données transitent par un tiers. Exige un accord strict de non-réentraînement et le masquage des secrets. | **Étanchéité physique** : Aucun octet ne quitte ton réseau local si les flux sortants sont coupés. |
| **Investissement matériel** | Zéro achat de matériel. Fonctionne sur un simple ordinateur portable de bureautique. | Nécessite un investissement lourd : station de travail avec carte graphique dédiée (GPU) et mémoire vidéo abondante (VRAM). |
| **Coût à l'usage** | Facturé au token consommé (quelques centimes à quelques euros par million de mots). Très économique pour un usage modéré. | Coût matériel fixe + électricité + temps humain passé à configurer, maintenir et mettre à jour les runtimes. |
| **Pérennité du comportement** | Le fournisseur peut modifier, brider ou déprécier une version de modèle sans préavis. | **Reproductibilité totale** : Les fichiers de poids téléchargés restent identiques pour toujours sur tes disques. |

#### La stratégie hybride gagnante
Pour la majorité des entreprises et ateliers numériques en 2026, la meilleure stratégie n'est pas le tout-cloud ou le tout-local, mais **l'hybridation intelligente** :
- Utiliser les grands modèles cloud pour la réflexion stratégique, la conception de l'architecture et les arbitrages complexes (en prenant soin de ne jamais leur transmettre de secrets ni de données personnelles de clients).
- Utiliser des modèles locaux légers et spécialisés pour le traitement des données sensibles internes, les tests de non-régression massifs et le travail hors-ligne.

[^1]: David A. Wheeler, *Why Open Source Software / Free Software (OSS/FS)? Look at the Numbers!*, 2015. Analyse des coûts réels de possession logicielle.

---

### 5. Préparer sa sortie : la règle de réversibilité

Pour rester libre, le pilote applique une discipline de fer : **tout ce qui a de la valeur dans ton projet doit être portable**.

Si ton fournisseur d'IA fermait ses portes ce soir :
- Tes besoins métier sont-ils écrits dans des fichiers Markdown lisibles par n'importe qui, ou enfermés dans une boîte de discussion propriétaire ?
- Tes règles de validation et d'architecture sont-elles consignées dans des [ADR](/annexes/glossaire) clairs dans ton dépôt Git ?
- Tes tests automatisés peuvent-ils tourner sur n'importe quel ordinateur sans connexion Internet ?

Si la réponse est oui, tu es un dirigeant libre. Tu peux changer d'outil, de modèle ou de fournisseur en une matinée, sans drame et sans perdre un seul jour de travail.

---

## Mise en pratique

### Le banc d'essai comparatif de l'atelier d'impression

Pour choisir l'outillage de l'atelier sans se fier aux discours marketing, le pilote organise une évaluation rigoureuse sur **trois tâches réelles** représentatives de notre quotidien, exécutées avec des données factices :

```text
LES TROIS TÂCHES TESTS DU BANC D'ESSAI :

  Tâche 1 (Spécification) :
  Rédiger les critères d'acceptation stricts pour le contrôle prepresse
  du fond perdu d'un fichier PDF (3 mm sur chaque bord).

  Tâche 2 (Code & Base) :
  Écrire la migration SQL non bloquante et la contrainte d'unicité
  pour empêcher les doublons de commande.

  Tâche 3 (Audit & Sécurité) :
  Relire un diff de 40 lignes et repérer une fuite potentielle de secret
  dans un journal de log.
```

Voici la grille d'arbitrage comparant deux solutions candidates pour équiper notre atelier :

| Solution comparée | Tâche 1 : Spécification | Tâche 2 : SQL non bloquant | Tâche 3 : Audit sécurité | Bilan d'indépendance & Décision |
| :--- | :--- | :--- | :--- | :--- |
| **Option A : Modèle Cloud Propriétaire de pointe**<br>*(API distante sécurisée avec accord de non-conservation)* | **Excellente** : Rédige des critères complets, identifie les cas limites (PDF sans repères de coupe). | **Excellente** : Propose directement le pattern `CREATE INDEX CONCURRENTLY`. | **Impeccable** : Détecte immédiatement la clé d'API loggée en clair à la ligne 12. | **Verdict** : Idéal pour le rôle d'architecte et de réviseur critique lors des phases de conception. Coût minime à la requête. |
| **Option B : Modèle Open Weights Local (32B)**<br>*(Exécuté via Ollama sur station Mac Studio de l'atelier)* | **Très bonne** : Résultat clair, conforme aux règles métier du fichier `CONTEXT.md`. | **Bonne après relance** : Avait initialement oublié le mot-clé `CONCURRENTLY`, corrigé à la 2e passe. | **Bonne** : Repère le secret, mais produit une explication plus verbeuse. | **Verdict** : Parfait pour le développement quotidien à l'atelier. Données des commandes 100 % isolées sur place. |

**La décision du pilote** : Nous adoptons l'Option B sur la machine de l'atelier pour toutes les opérations courantes de code, et nous réservons l'Option A via un routeur agnostique pour les révisions de sécurité majeures et les arbitrages d'architecture structurants.

---

## Exercice d'arbitrage & Corrigé commenté

### La mise en situation

Un membre de l'équipe propose d'accélérer le développement en souscrivant à une nouvelle plateforme tout-en-un très populaire :

> *« J'ai trouvé un outil génial ! C'est un environnement de développement en ligne fermé qui intègre son propre modèle d'IA magique. Il suffit de taper ce qu'on veut, il génère tout, héberge l'application sur ses propres serveurs et gère lui-même la base de données. Plus besoin de Git, plus besoin de Docker, plus besoin de comprendre le code ! Par contre, on ne peut pas exporter le code source facilement et le tarif passe à 200 € par mois et par utilisateur après le premier mois gratuit. On signe ? »*

### Les questions du pilote

Face à ce miroir aux alouettes, le pilote analyse les risques stratégiques :
1. **Perte totale de souveraineté** : L'entreprise ne possède plus son code, ne contrôle plus ses sauvegardes et ne peut plus faire tourner son application si l'abonnement s'arrête.
2. **Enfermement absolu (*Lock-in*)** : Sans Git et sans conteneurs Docker standards, il est impossible de migrer vers un autre hébergeur sans tout réécrire de zéro.
3. **Vulnérabilité financière** : L'atelier est à la merci des hausses de prix arbitraires du fournisseur.

### Le corrigé commenté

**La décision du pilote** : Rejet catégorique.

Tu réponds :  
*« Proposition refusée.  
1. Notre code source, nos spécifications et notre historique Git sont le patrimoine intellectuel de notre entreprise : ils doivent rester hébergés sur nos propres dépôts sous notre contrôle direct.  
2. Nous utilisons des standards universels (Markdown, Git, Docker, Python, PostgreSQL) que n'importe quel développeur ou n'importe quelle IA peut reprendre instantanément.  
3. Aucun outil qui confisque la portabilité du code et des données ne franchira la porte de notre atelier. »*

Cette clarté protège l'entreprise contre la disparition pure et simple de son outil de travail.

---

## Checklist réflexe du pilote

Pour garantir la pérennité et la liberté de ton projet technologique, vérifie ces cinq piliers d'indépendance :

- [ ] **Les actifs sont dans des formats ouverts** : Les règles métier, spécifications, tests et architectures sont écrits en Markdown et versionnés dans Git.
- [ ] **Les licences des modèles sont vérifiées** : Tu as lu la licence spécifique de chaque modèle utilisé (attention aux clauses interdisant l'usage commercial comme la MNPL).
- [ ] **L'architecture est agnostique** : Ton code communique via des protocoles standardisés (norme d'API ouverte, MCP) sans dépendre d'une bibliothèque fermée propre à un fournisseur.
- [ ] **Les secrets ne fuient jamais dans le cloud** : Aucune clé de chiffrement, mot de passe ni donnée personnelle client n'est transmise aux modèles externes lors des prompts.
- [ ] **Le plan de sortie est prêt** : Si ton outil d'IA principal disparaît demain matin, ton équipe sait quel modèle de substitution activer en moins de trente minutes.

---

## Sources et limites

Ce chapitre s'appuie sur les principes de souveraineté technologique et de gouvernance des systèmes :
- **O-MD §2 et §4** ([Manuel d'Orchestration Logicielle](/references/sources/o-md)) : La posture du pilote face aux outils, l'indépendance technologique, l'évaluation des coûts et la prévention de l'enfermement propriétaire.
- **[I-MD §12.1 à §12.6](/references/sources/i-md#section-12-1)** ([Manuel d'Ingénierie Logicielle](/references/sources/i-md)) : L'écosystème agnostique, le panorama des modèles à poids ouverts, les runtimes d'inférence, le standard MCP et la matrice d'arbitrage éthique et technique.

Pour maîtriser l'architecture technique des serveurs MCP sécurisés en lecture seule, le calcul rigoureux de la mémoire VRAM pour l'inférence locale et la mise en œuvre d'un adaptateur de modèle agnostique en Python 3.11, poursuis vers le chapitre miroir : **[B12 — Choisir ses outils et préserver son indépendance](/ingenieure/12-ecosysteme-et-independance)**.

## Références pour approfondir

- [Mistral — fiche Codestral 24.05](https://docs.mistral.ai/models/codestral-24-05) — Exemple historique de licence MNPL, pas une recommandation de modèle actuel. [Notice et chapitres associés](/references#ref-codestral).
- [MCP — autorisation, spécification 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) — Distinguer transport, autorisation et permissions effectives. [Notice et chapitres associés](/references#ref-mcp).
- [OpenAI — construire une évaluation](https://developers.openai.com/api/docs/guides/evals) — Définir tâches, données et critères ; cette référence n'établit aucun classement. [Notice et chapitres associés](/references#ref-evals).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A12](/redaction/a12-ecosysteme-et-independance).
