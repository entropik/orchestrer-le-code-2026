# B12 - Choisir ses outils et préserver son indépendance

> Lecture ingénieure · Chapitre rédigé.

[Sommaire](../SOMMAIRE.md) · [Lire la version accessible](../01-lecture-accessible/12-ecosysteme-et-independance.md) · [Fiche de rédaction](../../tranches/B12-ecosysteme-et-independance.md)

## Ce que tu sauras faire

Évaluer la portabilité effective des modèles et des outils, y compris MCP et l'inférence locale.

---

## Première synthèse

### 1. La couche d'adaptation agnostique et l'interchangeabilité des modèles

La plus grande vulnérabilité stratégique d'une organisation exploitant des agents d'intelligence artificielle est l'enfermement technologique (*Vendor Lock-in*)[^1]. Coupler directement la logique de ses harnais ou de ses scripts d'automatisation aux spécificités d'un SDK propriétaire (formats de requêtes exclusifs, structures d'erreurs non standard, gestion opaque des conversations) rend l'infrastructure captive des fluctuations tarifaires et des dépréciations unilatérales de modèles.

L'ingénierie logicielle robuste impose d'interposer un **Port d'Inférence Agnostique** (Pattern Hexagonal / Ports & Adaptateurs) adossé aux standards industriels de communication :

```text
ARCHITECTURE DE ROUTAGE AGNOSTIQUE ET SOUVERAINE :

                        [ HARNAIS AGENTIQUE SOUVERAIN ]
                        (Aider / Claude Code / Roo Code / OpenHands)
                                       │
                                       ▼ (Contrat d'API Standard OpenAI / JSON-RPC)
                 ┌──────────────────────────────────────────────┐
                 │         COUCHE D'ADAPTATION LOCALE           │
                 │         (Masquage des PII & Routage)         │
                 └──────────────────────┬───────────────────────┘
                                        │
             ┌──────────────────────────┼──────────────────────────┐
             ▼                          ▼                          ▼
  [ MOTEURS CLOUD PROPRIÉTAIRES] [ INFÉRENCE LOCALE DURCIE ] [ GPU SERVEUR DÉDIÉ ]
  • Anthropic API (Claude 3.7)   • Ollama / llama.cpp        • vLLM / SGLang
  • OpenAI API (o-series, GPT-4o)• macOS Metal / Linux CPU   • Instances Nvidia H100/A100
  • Données anonymisées          • Données confidentielles   • Débit token massif
```

L'interchangeabilité ne se décrète pas sur une simple ressemblance de syntaxe :
1. **Les sorties structurées (*Structured Outputs*)** : Chaque fournisseur interprète différemment la conformité aux schémas JSON (`json_schema` strict vs prompts de guidage). Un adaptateur de modèle doit valider la réponse générée par un parseur strict avant de la propager au système hôte.
2. **Le formatage des outils (*Function Calling*)** : Les conventions de déclaration des schémas d'outils et de sérialisation des arguments varient d'un moteur à l'autre. Le harnais isole ces variations dans un traducteur de format unique.
3. **La gestion du streaming et des erreurs réseau** : Les coupures de flux SSE (*Server-Sent Events*) et les codes d'erreur de saturation de débit (*Rate Limits* HTTP 429) doivent être normalisés par l'adaptateur selon une hiérarchie d'exceptions interne.

[^1]: Gregor Hohpe, *The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise*, O'Reilly Media, 2020.

---

### 2. Audit rigoureux des licences d'artefacts d'IA : Réfutation des amalgames

Dans le domaine de l'intelligence artificielle, l'expression « open source » fait l'objet d'un abus de langage généralisé. Une distinction juridique et technique fondamentale doit être opérée entre :
- **Le code source d'un runtime** (ex. : vLLM sous licence Apache 2.0, llama.cpp sous licence MIT).
- **Les poids numériques du modèle (*Open Weights*)** : Des fichiers binaires de tenseurs (`.safetensors`, `.gguf`) dont l'accès ne confère pas automatiquement les droits d'un logiciel libre selon la définition de l'Open Source Initiative (OSI).

> [!CAUTION]
> **Réfutation de la classification globale d'une famille de modèles** :  
> Il est juridiquement erroné d'affirmer qu'une famille de modèles relève globalement d'une licence libre sans examiner l'artefact précis.  
> Par exemple, alors que certains modèles de Mistral AI sont distribués sous licence permissive Apache 2.0, la version officielle **Codestral 24.05** est régie par la licence **MNPL** (*Mistral Non-Production License*)[^2]. Cette licence autorise l'évaluation et la recherche, mais **interdit formellement toute exploitation commerciale ou en production sans licence commerciale payante distincte**.  
> De même, les licences de type *Llama Community* ou *DeepSeek Open Model License* comportent des clauses d'attribution spécifiques, des plafonds d'utilisateurs actifs mensuels ou des restrictions sur l'entraînement de modèles concurrents.

L'architecte tient à jour un **SBOM Cognitif** (*Software Bill of Materials*) consignant pour chaque modèle utilisé : son identifiant SHA exact de révision, sa licence textuelle applicable, son auteur, et la date d'audit de conformité.

[^2]: Mistral AI, *Codestral 24.05 Model Card & License Notice*, 2024. Fiche officielle stipulant la licence MNPL.

---

### 3. Runtimes d'inférence, quantification et calcul du TCO réel

L'hébergement local ou sur serveur dédié de modèles à poids ouverts s'appuie sur des moteurs d'inférence spécialisés :

#### A. Les moteurs d'exécution
- **vLLM & SGLang (Serveurs de production et grappes GPU)** : Implémentent l'algorithme *PagedAttention* qui gère la mémoire tampon KV (*Key-Value Cache*) par pagination dynamique non contiguë, éliminant la fragmentation de la VRAM et autorisant le traitement par lots continus (*Continuous Batching*).
- **llama.cpp & Ollama (Stations de travail et environnements mixtes)** : Développés en C/C++ sans dépendance externe lourde. Permettent l'inférence optimisée sur processeurs Apple Silicon (via Metal) et architectures CPU via extensions vectorielles (AVX-512).

#### B. Quantification et évaluation de la fidélité
La quantification compresse les poids numériques du modèle en réduisant leur précision de 16 bits à virgule flottante (`FP16`) vers des entiers sur 8 ou 4 bits (`Q8_0`, `Q4_K_M` en format GGUF, AWQ ou EXL2)[^3].

L'affirmation prétendant qu'une quantification 4 bits induit « universellement moins de 1 % de dégradation » ne repose sur aucune garantie mathématique universelle :
- La dégradation dépend fortement de la taille initiale du modèle (un modèle de 7B paramètres souffre davantage de la quantification qu'un modèle de 70B).
- **Le protocole d'évaluation empirique** : La fidélité du modèle quantifié doit être mesurée sur un banc d'essai représentatif (*Evals*)[^4] portant sur la génération de syntaxe valide, le respect de contraintes de typage et la résolution de tests unitaires existants.

#### C. Calcul formel de l'empreinte mémoire VRAM
Pour dimensionner le matériel d'hébergement, la mémoire vidéo requise s'estime par la formule :

$$\text{VRAM}_{\text{requise}} \approx \left(\frac{\text{Paramètres (Milliards)} \times \text{Bits par paramètre}}{8} \times 1{,}20\right) + \text{VRAM}_{\text{KV Cache}}$$

*Exemple pour un modèle de 32 milliards de paramètres quantifié en 4 bits avec contexte de 32k tokens* :  
Poids du modèle $\approx (32 \times 4) / 8 \times 1{,}20 \approx 19{,}2\text{ Go}$.  
Avec le cache KV pour plusieurs requêtes concurrentes, un minimum de **24 à 32 Go de mémoire unifiée / VRAM** est requis pour une exécution stable sans pagination sur disque swap.

[^3]: Tim Dettmers et al., *LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale*, NeurIPS, 2022.
[^4]: OpenAI, *Building Evals: A Guide to Creating Evaluations*, Documentation technique développeur, 2024.

---

### 4. Le standard ouvert MCP et la sécurité des connecteurs

Le **Model Context Protocol (MCP)**, spécifié par Anthropic fin 2024 et formalisé fin 2025[^5], fournit un protocole de transport standardisé basé sur JSON-RPC pour connecter des agents d'IA à des contextes de données et des outils externes.

```text
FLUX DU PROTOCOLE MODEL CONTEXT PROTOCOL (MCP) :

  [ Agent / Client Hôte ]               [ Serveur MCP Git ]           [ Dépôt Git ]
            │                                   │                           │
            ├── 1. initialize ─────────────────►│                           │
            │◄── 2. capabilities (tools, etc.) ─┤                           │
            │                                   │                           │
            ├── 3. tools/list ─────────────────►│                           │
            │◄── 4. [git_diff, git_log, ...] ───┤                           │
            │                                   │                           │
            ├── 5. tools/call: git_diff ───────►│                           │
            │                                   ├── 6. git diff (audit) ───►│
            │                                   │◄── 7. stdout diff ────────┤
            │◄── 8. content: Unified Diff ──────┤                           │
            │                                   │                           │
            ├── 9. tools/call: git_push ───────►│                           │
            │                                   ├── ❌ REJET FORMEL (403)   │
            │◄── 10. Erreur: Permission Refusée─┤                           │
```

> [!WARNING]
> **Réfutation de la sécurité implicite de MCP** :  
> Le protocole MCP ne constitue **en aucun cas une garantie de sécurité ou de permission minimale par lui-même**.  
> Le protocole assure uniquement la sérialisation des échanges de messages entre l'hôte et un processus serveur. Si un serveur MCP tiers implémente une fonction `run_command` exécutant des commandes shell sans filtrage strict des arguments, l'agent dispose des pleins pouvoirs du compte utilisateur du système d'exploitation.  
> Un connecteur déclaré « en lecture seule » doit être **formellement audité et vérifié par des tests de refus négatifs** (`refusal tests`), s'exécuter dans un bac à sable POSIX restreint, et refuser impérativement toute commande mutative (`push`, `commit`, `reset`, `checkout`).

[^5]: Model Context Protocol, *MCP Specification 2025-11-25: Basic Architecture and Authorization*, Anthropic & Open Source Community, 2025.

---

## Mise en pratique

Nous implémentons ci-dessous un module complet de gouvernance et d'outillage en Python 3.11 pur, comprenant :
1. Un **Serveur MCP Git Sécurisé en Lecture Seule** : Implémente le protocole JSON-RPC, expose exclusivement les primitives d'inspection (`git_status`, `git_diff`, `git_log`) et intercepte avec rejet formel toute commande d'écriture ou de mutation.
2. Un **Adaptateur d'Inférence Agnostique** : Masque automatiquement les informations sensibles (clés d'API, PII) avant de router la requête vers un moteur d'inférence (local ou distant).
3. Une **Suite de tests unitaires `unittest`** prouvant les refus de sécurité et l'intégrité des flux.

```python
"""Module d'ingénierie d'indépendance technologique et d'outillage MCP sécurisé.

Implémente un connecteur MCP Git strictement confiné en lecture seule avec
tests de refus et un routeur d'inférence agnostique avec masquage de secrets.
"""

from dataclasses import dataclass
from enum import Enum
import json
import re
from typing import Any, Callable, Dict, List, Optional
import unittest


# ===========================================================================
# 1. SERVEUR MCP GIT SÉCURISÉ EN LECTURE SEULE (CONFINEMENT FORMEL)
# ===========================================================================

class CodeErreurMCP(int, Enum):
    METHODE_NON_TROUVEE = -32601
    PARAMETRES_INVALIDES = -32602
    COMMANDE_INTERDITE = -32001
    VIOLATION_SECURITE = -32003


class CommandeNonAutoriseeErreur(Exception):
    """Levée lorsqu'une commande tente de modifier l'état du dépôt."""


class ServeurMCPGitLectureSeule:
    """Implémente un sous-ensemble hermétique et auditable d'outils Git."""

    # Liste blanche stricte des outils d'inspection autorisés
    OUTILS_AUTORISES = {
        "git_status": "Affiche l'état des fichiers modifiés sans modifier le dépôt.",
        "git_diff": "Affiche le diff unifié des modifications en cours.",
        "git_log": "Affiche l'historique des commits récents.",
    }

    # Liste noire des commandes proscrites passibles de rejet immédiat
    COMMANDES_PROSCRITES = {"push", "commit", "reset", "clean", "checkout", "merge", "rebase"}

    def __init__(self, backend_execution: Callable[[str, List[str]], str]) -> None:
        self._execution_commande = backend_execution

    def traiter_requete_jsonrpc(self, requete_json: str) -> str:
        """Traite une requête entrante conforme à la spécification JSON-RPC 2.0."""
        try:
            message = json.loads(requete_json)
        except json.JSONDecodeError:
            return json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": "Parse error"}, "id": None})

        req_id = message.get("id")
        method = message.get("method")
        params = message.get("params", {})

        if method == "tools/list":
            outils = [
                {"name": nom, "description": desc}
                for nom, desc in self.OUTILS_AUTORISES.items()
            ]
            return json.dumps({"jsonrpc": "2.0", "result": {"tools": outils}, "id": req_id})

        if method == "tools/call":
            nom_outil = params.get("name")
            arguments = params.get("arguments", {})

            # Vérification de liste blanche
            if nom_outil not in self.OUTILS_AUTORISES:
                return json.dumps({
                    "jsonrpc": "2.0",
                    "error": {
                        "code": CodeErreurMCP.COMMANDE_INTERDITE.value,
                        "message": f"Accès refusé : L'outil '{nom_outil}' est formellement interdit en mode lecture seule."
                    },
                    "id": req_id
                })

            # Audit de sécurité des arguments pour prévenir les injections de commandes
            for arg in arguments.values():
                if any(proscrit in str(arg).split() for proscrit in self.COMMANDES_PROSCRITES):
                    return json.dumps({
                        "jsonrpc": "2.0",
                        "error": {
                            "code": CodeErreurMCP.VIOLATION_SECURITE.value,
                            "message": "Violation de sécurité : Argument de mutation intercepté dans l'outil d'inspection."
                        },
                        "id": req_id
                    })

            # Exécution isolée de l'outil d'inspection
            try:
                sortie = self._executer_outil(nom_outil, arguments)
                return json.dumps({
                    "jsonrpc": "2.0",
                    "result": {"content": [{"type": "text", "text": sortie}]},
                    "id": req_id
                })
            except Exception as e:
                return json.dumps({
                    "jsonrpc": "2.0",
                    "error": {"code": -32603, "message": f"Erreur interne : {str(e)}"},
                    "id": req_id
                })

        return json.dumps({
            "jsonrpc": "2.0",
            "error": {"code": CodeErreurMCP.METHODE_NON_TROUVEE.value, "message": "Méthode non implémentée."},
            "id": req_id
        })

    def _executer_outil(self, nom_outil: str, arguments: Dict[str, Any]) -> str:
        if nom_outil == "git_status":
            return self._execution_commande("git", ["status", "--porcelain"])
        if nom_outil == "git_diff":
            chemin = arguments.get("file_path", ".")
            return self._execution_commande("git", ["diff", "--", str(chemin)])
        if nom_outil == "git_log":
            limite = str(arguments.get("limit", 5))
            return self._execution_commande("git", ["log", "-n", limite, "--oneline"])
        raise NotImplementedError(nom_outil)


# ===========================================================================
# 2. ADAPTATEUR D'INFÉRENCE AGNOSTIQUE AVEC MASQUAGE DE SECRETS
# ===========================================================================

@dataclass(frozen=True)
class ReponseInference:
    modele_utilise: str
    texte_genere: str
    tokens_entree: int
    tokens_sortie: int


class AdaptateurInferenceAgnostique:
    """Normalise les appels d'inférence et masque les données sensibles."""

    REGEX_SECRETS = [
        re.compile(r"(?i)(api[_-]?key|token|password|bearer|secret)\s*[:=]\s*['\"]?([a-zA-Z0-9_\-\.]{8,})['\"]?"),
        re.compile(r"sk-[a-zA-Z0-9]{20,}"),
    ]

    def __init__(self, nom_modele: str, endpoint_url: str) -> None:
        self.nom_modele = nom_modele
        self.endpoint_url = endpoint_url

    def assainir_prompt(self, prompt: str) -> str:
        """Remplace les secrets découverts par une étiquette anonymisée."""
        texte_propre = prompt
        for regex in self.REGEX_SECRETS:
            texte_propre = regex.sub(r"[SECRET_MASQUE_PAR_LE_HARNAIS]", texte_propre)
        return texte_propre

    def executer_generation(
        self,
        prompt: str,
        backend_mock: Optional[Callable[[str, str], str]] = None,
    ) -> ReponseInference:
        """Exécute l'inférence après nettoyage du contexte."""
        prompt_securise = self.assainir_prompt(prompt)

        # Simulation de l'appel HTTP vers le runtime d'inférence (OpenAI-compatible)
        if backend_mock:
            texte_brut = backend_mock(self.nom_modele, prompt_securise)
        else:
            texte_brut = f"Réponse générée par {self.nom_modele} sur prompt sécurisé."

        return ReponseInference(
            modele_utilise=self.nom_modele,
            texte_genere=texte_brut,
            tokens_entree=len(prompt_securise.split()),
            tokens_sortie=len(texte_brut.split()),
        )
```

---

### La suite de tests prouvant les refus de sécurité et le masquage

```python
class TestEcosystemeEtIndependance(unittest.TestCase):
    """Vérifie le respect des listes blanches MCP et le masquage des secrets."""

    def test_serveur_mcp_lecture_seule_refuse_les_mutations(self) -> None:
        """Prouve que toute tentative de mutation Git est rejetée formellement."""
        commandes_executees: List[tuple[str, List[str]]] = []

        def faux_exec(prog: str, args: List[str]) -> str:
            commandes_executees.append((prog, args))
            return "ok"

        serveur = ServeurMCPGitLectureSeule(faux_exec)

        # 1. Appel nominal autorisé : git_status
        req_status = json.dumps({
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {"name": "git_status"},
            "id": 1
        })
        rep_status = json.loads(serveur.traiter_requete_jsonrpc(req_status))
        self.assertIn("result", rep_status)
        self.assertEqual(commandes_executees[-1], ("git", ["status", "--porcelain"]))

        # 2. Tentative d'appel d'un outil de mutation inexistant : git_push
        req_push = json.dumps({
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {"name": "git_push"},
            "id": 2
        })
        rep_push = json.loads(serveur.traiter_requete_jsonrpc(req_push))
        self.assertIn("error", rep_push)
        self.assertEqual(rep_push["error"]["code"], CodeErreurMCP.COMMANDE_INTERDITE.value)
        self.assertIn("formellement interdit", rep_push["error"]["message"])

        # 3. Tentative d'injection d'une sous-commande mutative via les arguments de git_diff
        req_injection = json.dumps({
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {
                "name": "git_diff",
                "arguments": {"file_path": "main.py; git push origin main"}
            },
            "id": 3
        })
        rep_injection = json.loads(serveur.traiter_requete_jsonrpc(req_injection))
        self.assertIn("error", rep_injection)
        self.assertEqual(rep_injection["error"]["code"], CodeErreurMCP.VIOLATION_SECURITE.value)

    def test_adaptateur_inference_masque_les_secrets_avant_envoi(self) -> None:
        """Vérifie que les clés d'API ne transitent jamais vers le runtime distant."""
        adaptateur = AdaptateurInferenceAgnostique(
            nom_modele="qwen-2.5-coder-32b",
            endpoint_url="http://localhost:11434/v1",
        )
        prompt_vulnérable = "Voici ma clé secrète api_key: sk-abcdef123456789012345678 pour tester l'upload."
        prompt_nettoye = adaptateur.assainir_prompt(prompt_vulnérable)

        # La clé originale doit avoir totalement disparu
        self.assertNotIn("sk-abcdef123456789012345678", prompt_nettoye)
        self.assertIn("[SECRET_MASQUE_PAR_LE_HARNAIS]", prompt_nettoye)


if __name__ == "__main__":
    unittest.main()
```

---

## Exercice d'arbitrage & Corrigé commenté

### Le cas d'ingénierie : L'intégration d'un serveur MCP Git communautaire non audité

Pour faciliter l'interaction de l'agent avec le dépôt, un développeur propose d'ajouter au fichier de configuration de l'éditeur le connecteur MCP suivant trouvé sur un forum communautaire :

```json
{
  "mcpServers": {
    "super-git": {
      "command": "npx",
      "args": ["-y", "super-git-mcp-server@latest"],
      "env": {
        "GIT_ALLOW_ANY_COMMAND": "true"
      }
    }
  }
}
```

### La grille d'audit de l'architecte

1. **Exécution dynamique non versionnée (`npx -y ...@latest`)** : Cette configuration télécharge et exécute à la volée la dernière version du paquet npm sans vérification de hachage SHA ni de fichier de verrouillage (`lockfile`). Une attaque par empoisonnement de la chaîne logistique (*Supply Chain Attack*) sur ce paquet confère immédiatement l'exécution de code arbitraire sur le poste du développeur.
2. **Flag permissif destructeur (`GIT_ALLOW_ANY_COMMAND: true`)** : Ce commutateur désactive tout filtrage de sécurité et autorise l'agent à exécuter des commandes destructrices (`git reset --hard`, `git push --force`, `git clean -fdx`).
3. **Absence d'isolation de processus** : Le processus serveur s'exécute avec les droits complets de l'utilisateur hôte, ayant accès aux clés SSH de la machine (`~/.ssh/id_ed25519`) et à toutes les variables d'environnement locales.

### Le corrigé commenté

**Décision de l'architecte** : Rejet immédiat de la configuration.

L'architecte impose les trois contre-mesures formelles suivantes :
1. **Épinglage de version et audit de code source** : Utiliser exclusivement un binaire inspecté, vérifié par son empreinte cryptographique SHA-256.
2. **Confinement en lecture seule par conception** : Utiliser un adaptateur conforme au serveur `ServeurMCPGitLectureSeule` développé plus haut, n'exposant strictement que `status`, `diff` et `log`.
3. **Isolation de bac à sable (Sandboxing)** : Exécuter le connecteur MCP dans un conteneur éphémère ou sous un utilisateur système dédié (`git-inspector`) sans accès en écriture sur le système de fichiers hôte ni sur le trousseau de clés d'administration.

---

## Checklist réflexe du pilote

Avant de signer l'adoption d'un composant de l'écosystème d'IA ou d'un serveur d'outillage, valide ces six exigences d'ingénierie :

- [ ] **L'API est standardisée** : Le code applicatif communique exclusivement via le contrat OpenAI-compatible ou JSON-RPC normalisé.
- [ ] **Les licences d'artefacts sont auditées** : Chaque modèle dispose d'une fiche consignant sa licence juridique exacte (MNPL, Apache 2.0, MIT, etc.).
- [ ] **Les serveurs MCP sont en lecture seule auditée** : Les capacités mutatives sont neutralisées à la source et vérifiées par des tests de refus formels.
- [ ] **La VRAM est dimensionnée avec marge** : Le calcul de mémoire vidéo intègre la quantification des poids et le volume dynamique du cache KV.
- [ ] **Les flux de données sont étanches** : Aucun secret ni donnée PII ne traverse la frontière réseau sans masquage cryptographique préalable.
- [ ] **La réversibilité est éprouvée** : Le remplacement d'un modèle par un modèle concurrent s'exécute par simple modification d'une variable de routage.

---

## Sources et limites

Ce chapitre approfondit les architectures agnostiques et la gouvernance des modèles et protocoles :
- **O-MD §2 et §4** ([Manuel d'Orchestration Logicielle](../../sources/originaux/manuel_orchestration_logicielle.md)) : L'indépendance de l'orchestrateur, la maîtrise des coûts et les arbitrages technologiques.
- **[I-MD §12.1 à §12.6](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md)** ([Manuel d'Ingénierie Logicielle](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md)) : L'architecture de routage agnostique, le panorama des modèles à poids ouverts, la quantification VRAM, les moteurs d'inférence vLLM/Ollama, et le standard Model Context Protocol (MCP).
- [Architecture du harnais & Smart Zone](../03-annexes/03-architecture-du-harnais.md) : Doctrine racine vs global, gestion des fenêtres de tokens et sandboxing.

Pour réviser les principes stratégiques de souveraineté sans outillage de programmation, consulte le miroir accessible : **[A12 — Choisir ses outils et préserver son indépendance](../01-lecture-accessible/12-ecosysteme-et-independance.md)**.
