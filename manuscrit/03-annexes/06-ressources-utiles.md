# Ressources utiles & Observatoire des modèles

> Repères communs · Comparateurs, bancs d'essai, postes de pilotage et observatoires indépendants.

[Sommaire](../SOMMAIRE.md) · [Guide des workflows](02-guide-des-workflows.md) · [Glossaire partagé](05-glossaire.md) · [Chapitre 12 : Écosystème & Indépendance](../01-lecture-accessible/12-ecosysteme-et-independance.md)

Face à la prolifération des modèles d'intelligence artificielle et au battage publicitaire (*hype*) des laboratoires, le maître d'ouvrage et l'ingénieur doivent s'appuyer sur des **mesures empiriques, indépendantes et reproductibles**.

Cette annexe recense les outils de référence pour évaluer la qualité de raisonnement, choisir son environnement de développement agentique, isoler l'exécution dans des bacs à sable étanches, éprouver le code par des oracles déterministes et préserver sa souveraineté numérique.

> 💡 **Le carnet de veille continue de l'auteur**  
> Pour suivre au fil de l'eau les nouveaux modèles, les bancs d'essai de terrain et les expérimentations sans complaisance, l'auteur Marc Tallec tient à jour [Digest by Ooblik](https://digest.ooblik.com/), un observatoire resserré réunissant plus de 2 000 ressources sélectionnées sur l'IA, le code, l'architecture logicielle et l'artisanat numérique.

---

## 1. Les quatre grands comparateurs mondiaux de référence

Ces quatre plateformes constituent les piliers de l'évaluation contemporaine des grands modèles de langage (LLM) :

### 1. LMSYS Chatbot Arena : le vote humain à l'aveugle (*Blind Test*)
- **Accès direct** : [lmarena.ai](https://lmarena.ai/) (ou [chat.lmsys.org](https://chat.lmsys.org/))
- **Méthode** : Deux modèles anonymes reçoivent le même prompt soumis par un utilisateur réel. L'humain vote pour la meilleure réponse sans savoir quel laboratoire a produit le texte. Les classements sont calculés selon le système de points **Elo** (issu du monde des échecs).
- **Intérêt pour le pilote** : C'est le juge de paix de l'intelligence perçue et de l'alignement avec le besoin humain. Il est quasiment impossible à « tricher » par surapprentissage car les prompts du public sont imprévisibles.
- **Filtres recommandés** :
  - *Coding Leaderboard* : isole les performances sur les requêtes de programmation, de débogage et de script.
  - *Hard Prompts* : classe les modèles sur les requêtes complexes nécessitant un raisonnement logique rigoureux.
  - *Style Control* : élimine le biais de verbosité (évite qu'un modèle l'emporte simplement parce qu'il produit des réponses inutilement longues).

---

### 2. Artificial Analysis : la référence indépendante Vitesse, Prix & Latence
- **Accès direct** : [artificialanalysis.ai](https://artificialanalysis.ai/)
- **Méthode** : Mesures automatisées et rigoureusement standardisées réalisées sur les infrastructures d'inférence (fournisseurs d'API comme Anthropic, OpenAI, Google, Groq, Fireworks, Together, Mistral, AWS Bedrock).
- **Intérêt pour le pilote** : Déterminer la viabilité économique et opérationnelle d'un modèle pour un système réel. Un modèle légèrement plus intelligent mais dix fois plus cher ou trois fois plus lent peut être disqualifié pour un usage quotidien.
- **Métriques clés à surveiller** :
  - *Quality Index* : note synthétique de raisonnement et de justesse.
  - *Price per 1M Tokens* : coût d'entrée (prompt) et de sortie (génération).
  - *Tokens per Second* : vitesse brute de frappe de l'agent.
  - *Time to First Token (TTFT)* : latence initiale avant que l'agent ne commence à agir.

---

### 3. SWE-bench : le banc d'essai de l'ingénierie logicielle réelle
- **Accès direct** : [swebench.com](https://swebench.com/)
- **Méthode** : Conçu par des chercheurs de Princeton, SWE-bench (*Software Engineering Benchmark*) confronte les agents à de **vraies issues GitHub résolues** dans des dépôts open-source majeurs (Django, SymPy, Flask, pytest, etc.).
- **Intérêt pour le pilote** : Contrairement aux tests académiques qui demandent de coder une petite fonction isolée dans un bac à sable, SWE-bench exige de l'agent qu'il explore un dépôt entier, identifie les fichiers pertinents, applique un correctif et fasse passer la suite complète de tests sans rien casser.
- **Variantes de référence** :
  - *SWE-bench Verified* : sous-ensemble de 500 problèmes rigoureusement inspectés par des humains pour éliminer les énoncés ambigus ou les tests invalides.
  - *SWE-bench Lite* : 300 tâches représentatives pour mesurer la progression rapide des architectures d'agents.

---

### 4. Hugging Face Open LLM Leaderboard : l'observatoire des modèles ouverts
- **Accès direct** : [huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
- **Méthode** : Évaluation totalement ouverte, reproductible et automatisée de milliers de modèles à poids ouverts (*open weights*) soumis par la communauté et les laboratoires de recherche (Meta Llama, Mistral AI, Qwen, DeepSeek, Google Gemma).
- **Intérêt pour le pilote** : Identifier les modèles souverains ou auto-hébergeables capables de tourner sur une machine locale (via Ollama, vLLM ou LM Studio) ou sur un serveur privé, garantissant qu'aucune donnée métier ou confidentielle ne transite vers un tiers.
- **Batterie d'évaluation standardisée (v2)** : MMLU-Pro (connaissances étendues), IFEval (respect strict des consignes de format), GSM8k / MATH (calculs et algèbre), MuSR (raisonnement multi-étapes), GPQA (questions de niveau doctorat).

---

## 2. Bancs d'essai spécialisés pour l'édition de code et les agents

Au-delà des classements généralistes, plusieurs initiatives indépendantes mesurent l'efficacité des modèles dans le geste artisanal du développement :

### Aider LLM Leaderboards
- **Accès direct** : [aider.chat/docs/leaderboards/](https://aider.chat/docs/leaderboards/)
- **Rôle** : Conçu par Paul Gauthier (créateur d'Aider), ce banc d'essai évalue la capacité des modèles à éditer des fichiers réels sous forme de **diffs Git propres**, sans halluciner sur les lignes non modifiées et en respectant la syntaxe imposée.
- **Pourquoi c'est précieux** : Un modèle brillant en théorie qui ne sait pas produire un patch unifié ou qui tronque le reste du fichier est inutilisable dans un harnais de développement réel.

### LiveBench
- **Accès direct** : [livebench.ai](https://livebench.ai/)
- **Rôle** : Benchmark sans contamination dont les questions sont mensuellement renouvelées à partir de problèmes de concours récents, de publications scientifiques et d'actualités logicielles.
- **Pourquoi c'est précieux** : Élimine le phénomène de « bachotage » où les laboratoires entraînent leurs modèles sur les questions des anciens benchmarks pour gonfler artificiellement leurs scores.

### BigCodeBench
- **Accès direct** : [bigcode-bench.github.io/](https://bigcode-bench.github.io/)
- **Rôle** : Évalue les modèles sur l'utilisation rigoureuse de bibliothèques tierces réelles, la manipulation de structures de données complexes et les instructions de code avec dépendances multiples.

---

## 3. Les postes de pilotage agentique (IDE, ADE & Outils CLI)

L'environnement de travail ne se limite plus à un simple traitement de texte coloré. En 2026, l'ingénieur opère depuis des postes de commande conçus pour l'orchestration sous mandat :

### 1. Orca : l'ADE (*Agentic Development Environment*) multi-agents
- **Accès direct** : [stablyai/orca](https://github.com/stablyai/orca) (ou [onorca.dev](https://onorca.dev/))
- **Le concept d'ADE** : Contrairement à l'IDE classique centré sur la saisie manuelle de code par l'humain, l'ADE (*Agentic Development Environment*) est conçu pour piloter une **flotte d'agents autonomes en parallèle**.
- **Forces opérationnelles** :
  - **Isolation par Git Worktree** : chaque agent tourne dans son propre répertoire de travail isolé (*worktree*), avec son propre terminal et son onglet de navigation dédié. Aucun risque de collision de fichiers ou de conflit de branche intempestif.
  - **Exécution concurrente et arbitrage** : tu peux soumettre la même tâche à deux modèles ou prompts distincts (par exemple Claude Code d'un côté et Aider de l'autre), observer leurs démarches respectives en temps réel et fusionner la meilleure solution.
  - **Visualisation des parcours** : inspection visuelle de l'état du navigateur et des artefacts produits par chaque agent.

### 2. Claude Code : le terminal-first rigoureux
- **Éditeur** : Anthropic
- **Rôle** : Outil en ligne de commande fonctionnant directement dans le terminal hôte. Conçu pour explorer les dépôts profonds, lancer des sous-agents spécialisés et appliquer des garde-fous programmatiques via des hooks d'interception matérielle (`PreToolUse`).

### 3. Cursor : l'IDE natif agent le plus fluide
- **Éditeur** : Anysphere
- **Rôle** : Fork de VS Code profondément remanié. Excelle dans l'indexation vectorielle locale du code (`codebase indexing`), permettant à l'agent de comprendre les dépendances lointaines à travers des centaines de fichiers sans saturer son contexte.

### 4. Roo Code & Cline : les extensions libres et transparentes
- **Accès direct** : Extensions open-source pour VS Code / VSCodium
- **Rôle** : Permettent de basculer entre des modes étanches (*Architect*, *Coder*, *Ask*), d'imposer une validation humaine bouton par bouton avant chaque écriture sur le disque et de brancher n'importe quel fournisseur d'inférence (API propriétaire ou modèle local).

### 5. Aider : l'artisan du pair-programming en console
- **Accès direct** : [aider.chat](https://aider.chat/)
- **Rôle** : Outil CLI d'une sobriété exemplaire. Force l'agent à valider son travail par des commits Git atomiques et des messages de commit descriptifs.

---

## 4. Le protocole MCP (Model Context Protocol) & Catalogues de serveurs

Considéré comme le « standard USB-C » de l'intelligence artificielle, le **Model Context Protocol (MCP)** standardise la façon dont un agent lit des données et déclenche des actions dans le monde réel, en séparant strictement l'intelligence du modèle de l'infrastructure hôte.

En 2026, la spécification stateless permet d'exécuter des serveurs MCP sur des conteneurs légers ou des fonctions HTTP serverless sans maintenir de connexions persistantes complexes.

### Annuaires et registres de serveurs MCP
- **MCP Registry officiel** : [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) (serveurs de référence maintenus : Git, SQLite, PostgreSQL, Filesystem, GitHub, Brave Search).
- **Smithery.ai** : [smithery.ai](https://smithery.ai/) (catalogue communautaire avec installation en une ligne de commande et statistiques d'utilisation).
- **MCP Finder** : Moteur de recherche fédéré agrégeant le registre officiel, npm et Smithery pour identifier des capacités précises (ex. connecteur Stripe, Slack, Notion ou Docker).
- **PulseMCP** : [pulsemcp.com](https://www.pulsemcp.com/) (veille continue sur les nouveaux serveurs et les bibliothèques d'outils émergentes).

> [!CAUTION]
> **Règle de sécurité du pilote : l'empoisonnement d'outil (*Tool Poisoning*)**  
> Ne branche jamais un serveur MCP inconnu avec des droits d'écriture sans avoir audité son code source. Un serveur malveillant ou mal conçu peut exposer tes variables d'environnement ou exécuter des requêtes destructrices à l'insu de l'agent. Applique toujours le principe de moindre privilège (accès en lecture seule par défaut).

---

## 5. Bacs à sable, conteneurisation & Docker Desktop

Donner à un agent le droit d'exécuter du code et de lancer des commandes shell sur ton ordinateur personnel présente un risque industriel majeur. En 2026, l'isolation ne relève plus du confort : c'est une condition de survie.

### 1. Docker Desktop : le standard du poste de travail
- **Accès direct** : [docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
- **Rôle pour le pilote** : Docker Desktop reste la solution la plus répandue sur macOS, Windows et Linux pour orchestrer des conteneurs locaux, faire tourner des bases de données de test (PostgreSQL, Redis) et isoler des environnements d'exécution.
- **Les Devcontainers (`.devcontainer.json`)** :
  - Norme ouverte ([containers.dev](https://containers.dev/)) permettant de décrire l'intégralité de l'atelier logiciel (versions de Python, bibliothèques C, outils de build, extensions) dans un fichier texte versionné dans Git.
  - L'agent et le développeur travaillent à l'intérieur du conteneur sans jamais modifier ni polluer le système d'exploitation de la machine hôte.
- **Consommation & Alternatives légères** :
  - Sur macOS, Docker Desktop virtualise un noyau Linux qui peut mobiliser beaucoup de mémoire vive.
  - Pour les machines plus modestes ou les licences strictes en entreprise, des alternatives légères existent : **OrbStack** (ultra-rapide et économe en batterie sur macOS), **Podman Desktop** (open-source sans daemon root) ou **Colima**.

### 2. Bacs à sable matériels (MicroVMs) : l'étanchéité absolue
Lorsqu'un agent exécute du code complexe ou manipule des paquets non fiables, le conteneur partagé présente des risques d'évasion de noyau (*sandbox escape*). Les solutions modernes reposent sur des micro-machines virtuelles matérielles :
- **E2B (`e2b.dev`)** : la référence pour l'exécution agentique. Fournit des microVMs Firecracker isolées au niveau du noyau, capables de démarrer en quelques centaines de millisecondes, avec système de fichiers éphémère et filtrage strict des flux réseau sortants.
- **Daytona (`daytona.io`)** : plateforme open-source d'environnements de développement standardisés, permettant de créer et détruire des postes de travail virtuels en une commande CLI.

---

## 6. Les oracles déterministes : tester le code produit par l'IA

L'agent génère du code de manière probabiliste. Pour valider son travail, l'humain ne doit jamais se fier à ses promesses textuelles : il doit lui opposer des **oracles mathématiquement déterministes**.

### 1. Les tests de mutation (Mutation Testing)
*Le problème* : un agent peut très bien écrire 20 tests unitaires qui passent tous au vert... simplement parce que ses assertions sont triviales (`assert result is not None`).
*La solution* : l'outil de mutation injecte automatiquement des fautes dans le code (inversion de condition, modification de constante arithmétique). Si les tests de l'agent restent verts malgré ces fautes, les tests sont déclarés invalides (*mutants survivants*).
- **Mutmut** (Python) : [mutmut.readthedocs.io](https://mutmut.readthedocs.io/)
- **Stryker Mutator** (TypeScript, JavaScript, C#) : [stryker-mutator.io](https://stryker-mutator.io/)

### 2. Les tests basés sur les propriétés (Property-Based Testing)
Plutôt que de tester un seul exemple prévisible, ces outils génèrent des centaines de cas d'essai extrêmes (chaînes vides, entiers négatifs géants, caractères Unicode rares, fuseaux horaires invalides) pour débusquer les angles morts :
- **Hypothesis** (Python) : [hypothesis.readthedocs.io](https://hypothesis.readthedocs.io/)
- **fast-check** (TypeScript/JavaScript) : [fast-check.dev](https://fast-check.dev/)

### 3. La validation stricte aux frontières du système
Pour s'assurer qu'aucune donnée mal formée ne traverse les interfaces :
- **Pydantic** (Python) : validation runtime par schémas et typage statique.
- **Zod** ou **TypeBox** (TypeScript) : dérivation automatique des types statiques à partir de contrats runtime infranchissables.

---

## 7. Runtimes d'inférence locale : souveraineté et secret d'atelier

Pour traiter des données confidentielles, des secrets médicaux ou des brevets sans émettre le moindre paquet sur Internet :

| Outil | Cible principale | Point fort |
|---|---|---|
| **[Ollama](https://ollama.com/)** | Poste de travail local (Mac, Linux, Windows) | Téléchargement et exécution en une commande (`ollama run qwen2.5-coder`). API compatible OpenAI. |
| **[vLLM](https://vllm.ai/)** | Serveurs de production & GPU dédiés | Débit d'inférence record grâce à l'algorithme *PagedAttention*. Idéal pour héberger son propre modèle d'équipe. |
| **[llama.cpp](https://github.com/ggerganov/llama.cpp)** | Tout processeur CPU / GPU / Apple Silicon | Moteur universel ultra-optimisé en C++, sans dépendance Python, base de presque tout l'écosystème local. |
| **[LM Studio](https://lmstudio.ai/)** | Expérimentation visuelle sur poste local | Interface graphique soignée pour tester les invites, ajuster la quantification (GGUF) et exposer un serveur local. |

---

## 8. Observabilité, traçabilité et contrôle des coûts

Piloter un système agentique exige de pouvoir auditer chaque décision de l'agent : quel prompt a été envoyé ? Combien de tokens ont été consommés ? Quel outil a échoué ?

- **Langfuse** ([langfuse.com](https://langfuse.com/)) : plateforme d'observabilité open-source dédiée aux applications LLM et agents. Permet d'inspecter visuellement l'arbre d'exécution complet des agents, de tracer la consommation de tokens et de mesurer la latence.
- **OpenTelemetry GenAI Semantic Conventions** : la norme industrielle ouverte pour standardiser les métriques et les traces d'appels d'IA sans s'enfermer chez un éditeur de monitoring propriétaire.
- **Helicone** ([helicone.ai](https://www.helicone.ai/)) : proxy d'inférence léger permettant de mettre en cache les requêtes répétitives, d'alerter sur les dépassements de budget et d'analyser les coûts par utilisateur ou par tâche.

---

## 9. La grille d'arbitrage du pilote : comment lire un benchmark

Un classement n'est jamais une vérité absolue ; c'est une photographie artificielle à un instant donné. Applique systématiquement ces quatre principes d'hygiène mentale :

1. **Le risque de contamination des données** : si un exercice de test est public depuis plus de six mois, le modèle l'a très probablement ingéré lors de son entraînement. Privilégie toujours les benchmarks dynamiques ou à l'aveugle (*LMSYS*, *LiveBench*).
2. **Le compromis Raisonnement / Vitesse / Coût** : un modèle champion à SWE-bench mais facturant 30 $ le million de tokens et mettant une minute par réponse est parfait pour un audit d'architecture ou une revue critique, mais totalement inadapté à l'assistance de frappe au fil de l'eau.
3. **L'effet multiplicateur du cache de contexte (*Prompt Caching*)** : les fournisseurs d'API accordent des remises allant jusqu'à 80 % ou 90 % lorsque le contexte initial (`AGENTS.md`, règles, documentation) est conservé en mémoire vive chez l'hébergeur. Mesure toujours le coût réel avec cache activé.
4. **La primauté du harnais sur la puissance brute** : un modèle compact à 14 milliards de paramètres guidé par un `AGENTS.md` rigoureux et des tests automatisés produira toujours un logiciel plus pérenne qu'un modèle géant lâché en roue libre sans garde-fous.

---

## 10. Matrice de synthèse : deux trousses types selon ton profil

| Composant | Profil 1 : Créateur solo / Solopreneur / Béotien | Profil 2 : Ingénieur / Lead Tech / Équipe |
|---|---|---|
| **Poste de pilotage** | Claude Code (CLI) ou Cursor | Orca (ADE multi-agents) + Claude Code + Roo Code |
| **Garde-fous** | `AGENTS.md` + Tests pytest basiques | PreToolUse Hooks + Git Guardrails + Bacs MicroVMs |
| **Isolation locale** | Docker Desktop (Devcontainers) | Docker Desktop / OrbStack + MicroVMs E2B |
| **Modèle distant** | Claude Sonnet / OpenAI o-series via API | Routage multi-fournisseurs (OpenRouter / AWS Bedrock) |
| **Modèle souverain local** | Ollama (Qwen 2.5 Coder 7B / Mistral 7B) | vLLM sur cluster GPU interne (Llama 70B / Mistral Large) |
| **Vérification du code** | Linters + Suite de tests fonctionnels | Tests de mutation (Mutmut/Stryker) + Hypothesis |
| **Capacités & Outils** | Serveurs MCP standards (Filesystem, SQLite) | Serveurs MCP audités avec OAuth et portée restreinte |
| **Observabilité** | Tableau de bord fournisseur (facturation) | Langfuse auto-hébergé + OpenTelemetry |

---

*Pour approfondir la sélection des briques logicielles et l'indépendance vis-à-vis des fournisseurs, consulte le [Chapitre 12 : Choisir ses outils et préserver son indépendance](../01-lecture-accessible/12-ecosysteme-et-independance.md). Pour la mise en place concrète des garde-fous, consulte l'[Architecture du harnais](03-architecture-du-harnais.md). Pour continuer la veille au jour le jour, explore [Digest by Ooblik](https://digest.ooblik.com/).*
