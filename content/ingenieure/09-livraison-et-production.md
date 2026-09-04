{
  "title": "Passer du poste local à un service réel",
  "description": "Définir une chaîne de livraison traçable avec compatibilité, santé et limites d'infrastructure.",
  "weight": 9,
  "chapter_id": "B09",
  "theme": "09",
  "status": "redaction",
  "source_path": "manuscrit/02-lecture-ingenieure/09-livraison-et-production.md",
  "mirror": "/accessible/09-livraison-et-production",
  "related": [
    "/ingenieure/05-git-et-collaboration",
    "/ingenieure/10-exploitation-et-evolution"
  ],
  "notions": [
    {
      "label": "Artefact",
      "anchor": "artefact"
    },
    {
      "label": "CI",
      "anchor": "ci"
    },
    {
      "label": "Migration",
      "anchor": "migration"
    }
  ],
  "previous": "/ingenieure/08-donnees-et-migrations",
  "next": "/ingenieure/10-exploitation-et-evolution"
}

## Ce que tu sauras faire

Définir une chaîne de livraison traçable avec compatibilité, santé et limites d'infrastructure.

---

## Première synthèse

### 1. La chaîne CI/CD déterministe et l'identité par digest d'image

Dans l'ingénierie de production moderne, le déploiement n'est plus une opération artisanale exécutée manuellement par un opérateur, mais une **chaîne d'assemblage entièrement déterministe** orchestrée par un pipeline d'Intégration et de Déploiement Continus (CI/CD)[^1].

Pour qu'un déploiement soit mathématiquement reproductible, deux conditions doivent être réunies :
1. **Le verrouillage strict des dépendances** : L'utilisation de fichiers de verrouillage intègres (`package-lock.json`, `pnpm-lock.yaml`, `poetry.lock`) garantit que chaque dépendance est installée à son empreinte SHA exacte, éliminant le syndrome des builds divergents.
2. **L'identification formelle par Digest cryptographique** : Se fier à un tag Docker textuel tel que `:latest` ou même `:v1.2.0` est une hérésie en production : un tag est une étiquette mobile qui peut être réécrite. L'artefact déployé doit être identifié par son **Digest immuable SHA-256** :

$$\text{Identité Artefact} = \text{registry.domaine.com/app@sha256:7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069}$$

```text
CONSTRUCTION CONTENEURISÉE MULTI-STAGE REPRODUCTIBLE :

  ÉTAPE 1 : BUILDER (Environnement de compilation lourd)
  • Image de base : python:3.11-slim
  • Compilateurs C, headers, dépendances de dev
  • Compilation des modules natifs et vérification des types
            │
            ▼ (Copie exclusive des binaires compilés)
  ÉTAPE 2 : RUNNER FINAL (Environnement d'exécution durci)
  • Image minimale sans compilateur ni outils de packaging
  • Création d'un utilisateur sans privilèges : USER appuser (UID 10001)
  • Système de fichiers racine monté en lecture seule (read-only rootfs)
  • Surface d'attaque divisée par dix.
```

[^1]: Jez Humble et David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*, Addison-Wesley, 2010.

---

### 2. Le principe de moindre privilège et la gestion des secrets

Selon les recommandations de la *Twelve-Factor App* (Facteur III : Configuration)[^2], le code source applicatif doit être strictement agnostique de son environnement d'exécution. 

#### La doctrine d'isolation des secrets
- **Zéro secret dans le code ou l'image** : Aucun mot de passe, jeton API ou certificat TLS ne doit être injecté lors du `docker build`.
- **Injection au runtime via variables d'environnement chiffrées** : Les secrets sont fournis au démarrage du conteneur par le gestionnaire d'infrastructure hôte (fichiers d'environnement restreints POSIX `chmod 600` ou gestionnaire de secrets type HashiCorp Vault / Doppler).
- **Principe de moindre privilège (*Least Privilege*)** : Le conteneur s'exécute sous une identité non-root dédiée (`appuser`). Il lui est formellement interdit d'écrire hors de son répertoire temporaire éphémère (`/tmp`).

[^2]: Adam Wiggins, *The Twelve-Factor App*, 2011, standard de conception pour applications modernes déployables dans le cloud.

---

### 3. Reverse Proxy, terminaison TLS et sondes de santé discriminantes

En production, un serveur applicatif (Uvicorn, Gunicorn, Node.js) ne doit jamais être exposé directement sur le port public 80 ou 443. Il est systématiquement abrité derrière un **Reverse Proxy haute performance** (Caddy, Nginx ou Traefik) qui prend en charge :
- La négociation et le renouvellement automatique des certificats TLS (via le protocole ACME / Let's Encrypt).
- La terminaison SSL et la compression HTTP/2 et HTTP/3.
- La protection contre les dénis de service et le lissage du débit (*Rate Limiting*).

```text
TOPOLOGIE RÉSEAU AVEC REVERSE PROXY ET SONDES DE SANTÉ :

   [ Trafic Public HTTPS (Port 443) ]
                   │
                   ▼
     ┌───────────────────────────┐
     │ REVERSE PROXY (Caddy)     │ ◄── Terminaison TLS, Let's Encrypt, Rate Limiting
     └─────────────┬─────────────┘
                   │
      ┌────────────┴────────────┐
      ▼                         ▼
┌──────────────┐          ┌──────────────┐
│ INSTANCE A   │          │ INSTANCE B   │
│ (Active)     │          │ (En staging) │
└──────┬───────┘          └──────┬───────┘
       │                         │
       ▼                         ▼
Sonde LIVENESS :            Sonde READINESS :
« Le processus répond-il    « La base est-elle migrée et prête
  sans deadlock ? »           à recevoir des requêtes clients ? »
```

#### Distinction vitale entre Liveness et Readiness Probes
Une erreur d'infrastructure fréquente consiste à utiliser une sonde unique pour évaluer l'état d'un conteneur. Le système doit impérativement distinguer deux questions orthogonales :

| Type de Sonde | Question posée au Conteneur | Action de l'Orchestrateur si Échec |
|---|---|---|
| **Liveness Probe (Sonde de vie)** | Le processus Python tourne-t-il encore ou est-il figé dans une boucle infinie ou un deadlock ? | **Redémarrage immédiat** du conteneur (`docker restart`). |
| **Readiness Probe (Sonde d'aptitude)** | L'instance a-t-elle terminé son pré-chauffage, chargé ses caches et vérifié la compatibilité de sa connexion à la base de données ? | **Retrait immédiat du routage** du reverse proxy : le conteneur n'est PAS tué, mais aucune requête client ne lui est envoyée tant qu'il n'est pas prêt. |

---

### 4. Déploiement Blue-Green et drainage des connexions sans coupure

Pour garantir un déploiement continu sans interruption de service (*Zero-Downtime Deployment*), l'ingénierie privilégie la topologie **Blue-Green**[^3] :

```text
CYCLE DE BASCULE SANS COUPURE BLUE-GREEN :

  ÉTAPE 1 : PRÉ-CHAUFFAGE DE LA NOUVELLE VERSION (GREEN)
  • L'instance existante BLUE sert 100 % du trafic de production.
  • L'orchestrateur déploie la nouvelle instance GREEN sur un port interne isolé.
  • GREEN exécute ses vérifications internes. Le reverse proxy interroge sa Readiness Probe.

  ÉTAPE 2 : BASCULE ATOMIQUE DU TRAFIC
  • Dès que GREEN est déclarée READY, le reverse proxy réoriente instantanément
    les nouvelles requêtes vers GREEN (rechargement atomique de la configuration).

  ÉTAPE 3 : DRAINAGE DES CONNEXIONS (CONNECTION DRAINING)
  • L'instance BLUE ne reçoit plus aucune nouvelle requête.
  • Elle dispose d'une fenêtre de grâce (ex: 30 secondes) pour terminer les requêtes
    en cours de traitement avant son arrêt ordonné.
  • Si un problème survient dans les premières minutes, la bascule inverse vers BLUE
    s'opère en moins d'une seconde (*Instant Rollback*).
```

[^3]: Martin Fowler, *BlueGreenDeployment*, 2010.

---

## Mise en pratique

### Orchestrateur de Déploiement Blue-Green avec Sondes et Rollback en Python 3.11

Le programme suivant implémente un simulateur complet d'orchestration Blue-Green gérant les sondes de santé discriminantes, la bascule atomique et le retour arrière immédiat en cas de défaillance :

```python
"""Module d'ingénierie de déploiement : Orchestrateur Blue-Green et Sondes.

Démontre la gestion de la bascule sans coupure, le drainage des requêtes
et le rollback automatique sous Python 3.11.
"""
from dataclasses import dataclass
from typing import Optional
import unittest


# ============================================================================
# 1. MODÈLE DU CONTENEUR APPLICATIF ET DES SONDES DE SANTÉ
# ============================================================================

@dataclass
class EtatConteneur:
    nom_slot: str  # "BLUE" ou "GREEN"
    digest_sha256: str
    est_en_vie: bool  # Liveness
    est_pret: bool    # Readiness
    connexions_actives: int = 0


class ApplicationInstance:
    """Instance logicielle s'exécutant dans un conteneur isolé."""

    def __init__(self, nom_slot: str, digest_sha256: str) -> None:
        self.etat = EtatConteneur(
            nom_slot=nom_slot,
            digest_sha256=digest_sha256,
            est_en_vie=True,
            est_pret=False,
        )

    def sonder_liveness(self) -> bool:
        """Vérifie que le runtime n'est pas figé."""
        return self.etat.est_en_vie

    def sonder_readiness(self) -> bool:
        """Vérifie que les connexions externes sont établies."""
        return self.etat.est_en_vie and self.etat.est_pret

    def marquer_prete(self) -> None:
        self.etat.est_pret = True

    def simuler_crash(self) -> None:
        self.etat.est_en_vie = False


# ============================================================================
# 2. L'ORCHESTRATEUR DE ROUTAGE BLUE-GREEN
# ============================================================================

class DeploiementEchecErreur(Exception):
    """Émise lorsqu'une nouvelle instance échoue à satisfaire sa Readiness Probe."""
    pass


class OrchestrateurBlueGreen:
    """Contrôleur gérant la bascule de trafic et le drainage de connexions."""

    def __init__(self, instance_initiale: ApplicationInstance) -> None:
        if not instance_initiale.sonder_readiness():
            raise ValueError("L'instance initiale doit être immédiatement prête.")
        self.instance_active = instance_initiale
        self.instance_en_attente: Optional[ApplicationInstance] = None
        self.journal_bascules: list[str] = [f"Initialisation sur {instance_initiale.etat.nom_slot}"]

    def deployer_nouvelle_version(self, nouvelle_instance: ApplicationInstance) -> bool:
        """Tente de promouvoir une nouvelle version sans coupure de trafic."""
        self.instance_en_attente = nouvelle_instance

        # 1. Vérification de la Sonde de Vie (Liveness)
        if not nouvelle_instance.sonder_liveness():
            self.instance_en_attente = None
            raise DeploiementEchecErreur("Échec Liveness : L'instance ne démarre pas.")

        # 2. Vérification de la Sonde d'Aptitude (Readiness)
        if not nouvelle_instance.sonder_readiness():
            # Rollback automatique : la nouvelle instance est rejetée
            self.instance_en_attente = None
            raise DeploiementEchecErreur(
                f"Échec Readiness sur {nouvelle_instance.etat.nom_slot} : "
                "Bascule annulée, trafic maintenu sur l'ancienne version."
            )

        # 3. Bascule atomique du routeur
        ancienne = self.instance_active
        self.instance_active = nouvelle_instance
        self.journal_bascules.append(
            f"Bascule de {ancienne.etat.nom_slot} vers {nouvelle_instance.etat.nom_slot}"
        )

        # 4. Drainage des connexions de l'ancienne version
        self._drainer_connexions(ancienne)
        return True

    def _drainer_connexions(self, ancienne_instance: ApplicationInstance) -> None:
        """Simule le drainage propre des requêtes en cours avant extinction."""
        ancienne_instance.etat.connexions_actives = 0
```

---

### La suite de tests prouvant la bascule Zero-Downtime et le Rollback automatique

```python
class TestDeploiementBlueGreen(unittest.TestCase):
    """Suite vérifiant la sécurité de bascule et l'annulation sur panne."""

    def test_deploiement_nominal_reussi(self) -> None:
        # 1. Démarrage initial avec slot Blue actif
        app_blue = ApplicationInstance("BLUE", "sha256:aaaa")
        app_blue.marquer_prete()
        orchestrateur = OrchestrateurBlueGreen(app_blue)
        self.assertEqual(orchestrateur.instance_active.etat.nom_slot, "BLUE")

        # 2. Préparation du slot Green
        app_green = ApplicationInstance("GREEN", "sha256:bbbb")
        app_green.marquer_prete()  # Passage de la sonde de readiness

        # 3. Déploiement et bascule
        succes = orchestrateur.deployer_nouvelle_version(app_green)
        self.assertTrue(succes)
        self.assertEqual(orchestrateur.instance_active.etat.nom_slot, "GREEN")
        self.assertEqual(orchestrateur.instance_active.etat.digest_sha256, "sha256:bbbb")
        self.assertEqual(app_blue.etat.connexions_actives, 0)

    def test_rollback_automatique_si_readiness_echoue(self) -> None:
        # 1. Slot Blue actif et sain
        app_blue = ApplicationInstance("BLUE", "sha256:aaaa")
        app_blue.marquer_prete()
        orchestrateur = OrchestrateurBlueGreen(app_blue)

        # 2. Slot Green défaillant : le processus tourne, mais la base n'est pas prête
        app_green_en_panne = ApplicationInstance("GREEN", "sha256:cccc")
        # On n'appelle PAS marquer_prete() pour simuler une panne de readiness

        # 3. Tentative de déploiement -> doit lever une exception et conserver Blue
        with self.assertRaises(DeploiementEchecErreur) as ctx:
            orchestrateur.deployer_nouvelle_version(app_green_en_panne)

        self.assertIn("Échec Readiness", str(ctx.exception))
        # Invariant absolu : L'instance active reste strictement BLUE
        self.assertEqual(orchestrateur.instance_active.etat.nom_slot, "BLUE")
        self.assertEqual(orchestrateur.instance_active.etat.digest_sha256, "sha256:aaaa")


if __name__ == "__main__":
    unittest.main()
```

---

## Exercice d'arbitrage & Corrigé commenté

### Le cas d'ingénierie : L'image Docker non durcie tournant sous root

Un agent autonome soumet le `Dockerfile` suivant pour déployer l'API de commande en production :

```dockerfile
# Dockerfile soumis par l'agent (Faute de sécurité majeure) :
FROM python:latest
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "main.py"]
```

### La grille d'audit de l'architecte

1. **Tag flottant non reproductible (`python:latest`)** : Reconstruire cette image dans trois mois installera une version majeure différente de Python et d'autres bibliothèques système, brisant le déterminisme du build.
2. **Absence de multi-stage build** : L'image finale embarque le compilateur GCC, les outils de packaging et l'historique complet du cache pip, alourdissant le conteneur de 900 Mo inutiles.
3. **Exécution sous privilèges `root`** : Le conteneur s'exécute sous le compte super-utilisateur. Si une faille d'injection de commande est exploitée dans l'API, l'attaquant obtient les droits root à l'intérieur du conteneur avec un risque d'évasion (*Container Escape*).

### Le corrigé commenté

**Décision de l'architecte** : Rejet immédiat de la PR avec exigence d'un `Dockerfile` durci multi-stage :

```dockerfile
# Dockerfile industriel de référence :
FROM python:3.11-slim AS builder
WORKDIR /build
COPY requirements.lock ./
RUN pip install --no-cache-dir --prefix=/install -r requirements.lock

FROM python:3.11-slim AS runner
WORKDIR /app
# 1. Utilisateur sans privilèges
RUN useradd -u 10001 -r -s /usr/sbin/nologin appuser
# 2. Copie exclusive des dépendances nécessaires
COPY --from=builder /install /usr/local
COPY --chown=appuser:appuser src/ ./src/
# 3. Exécution non-root
USER 10001
EXPOSE 8080
CMD ["python", "src/main.py"]
```

---

## Checklist réflexe du pilote

Avant de signer l'autorisation de mise en production d'une version logicielle, vérifie ces six invariants d'infrastructure :

- [ ] **L'image est identifiée par son Digest** : Le déploiement référence l'empreinte immuable `sha256:...` et non une étiquette textuelle mouvante.
- [ ] **Le conteneur est non-root** : L'application s'exécute sous une identité système restreinte (`USER 10001`) sans droits d'administration.
- [ ] **Les sondes sont discriminantes** : Le système distingue la sonde de vie (*Liveness*) de la sonde d'aptitude (*Readiness*).
- [ ] **Le reverse proxy gère le TLS** : Les certificats HTTPS sont automatisés et isolent le serveur d'application de l'exposition directe.
- [ ] **Le drainage des requêtes est assuré** : Les anciennes instances disposent d'un délai suffisant pour terminer leurs requêtes avant coupure.
- [ ] **Le Rollback est testé** : La procédure de retour arrière vers la version précédente s'exécute de manière automatisée en moins de deux minutes.

---

## Sources et limites

Ce chapitre approfondit les pratiques de livraison continue et de résilience d'infrastructure :
- **O-MD §8** ([Manuel d'Orchestration Logicielle](/references/sources/o-md)) : La transition du poste local au service réel, les configurations hors code, les artefacts immuables et le protocole Go/No-Go.
- **I-MD §8 et §10.2** ([Manuel d'Ingénierie Logicielle](/references/sources/i-md)) : L'ingénierie CI/CD, les conteneurs multi-stage durcis, la terminaison TLS par reverse proxy et les déploiements Blue-Green avec sondes de santé.

Pour maîtriser l'observabilité en production, les métriques Prometheus, la centralisation des logs et la gestion des incidents, poursuis vers le chapitre suivant : **[B10 — Exploiter, observer et faire évoluer](/ingenieure/10-exploitation-et-evolution)**. Pour réviser les concepts sans outillage de programmation, consulte le miroir accessible : **[A09 — Passer du poste local à un service réel](/accessible/09-livraison-et-production)**.

## Références pour approfondir

- [Caddy — module de limitation de débit](https://caddyserver.com/docs/modules/http.handlers.rate_limit) — Module non standard : sa présence doit être vérifiée. [Notice et chapitres associés](/references#ref-caddy).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche B09](/redaction/b09-livraison-et-production).
