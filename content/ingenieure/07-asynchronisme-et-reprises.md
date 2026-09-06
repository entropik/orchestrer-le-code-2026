{
  "title": "Faire travailler le système sans perdre les opérations",
  "description": "Analyser atomicité, livraison, déduplication et reprise des effets distribués.",
  "weight": 7,
  "chapter_id": "B07",
  "theme": "07",
  "status": "redaction",
  "source_path": "manuscrit/02-lecture-ingenieure/07-asynchronisme-et-reprises.md",
  "mirror": "/accessible/07-asynchronisme-et-reprises",
  "related": [
    "/ingenieure/08-donnees-et-migrations",
    "/ingenieure/10-exploitation-et-evolution"
  ],
  "notions": [
    {
      "label": "Idempotence",
      "anchor": "idempotence"
    },
    {
      "label": "Outbox",
      "anchor": "outbox"
    },
    {
      "label": "Invariant",
      "anchor": "invariant"
    }
  ],
  "previous": "/ingenieure/06-tests-et-preuves",
  "next": "/ingenieure/08-donnees-et-migrations"
}

## Ce que tu sauras faire

Analyser atomicité, livraison, déduplication et reprise des effets distribués.

---

## Première synthèse

### 1. L'illusion du « Exactly-Once » et la réalité du réseau faillible

Dans l'ingénierie des systèmes distribués, prétendre garantir une livraison « exactement une fois » (*Exactly-Once Delivery*) à travers un réseau physique non fiable relève de l'illusion théorique. En vertu du **problème des deux généraux** (*Two Generals' Problem*)[^1], il est formellement démontré qu'aucun protocole synchrone ne peut garantir un consensus absolu sur un canal sujet aux pertes de paquets.

Tout système d'échange distribué (RabbitMQ, Apache Kafka, Redis Streams, Amazon SQS) fonctionne sous la contrainte de la **livraison au moins une fois (*At-Least-Once Delivery*)** :
- Le producteur publie un message sur le bus.
- Le travailleur (*worker*) consomme le message et exécute le traitement métier.
- Le travailleur renvoie un accusé de réception (*Acknowledgement* ou ACK).
- Si le réseau coupe avant que l'ACK n'atteigne le broker, ce dernier considère légitimement que le travailleur est mort et **réexpédie le même message à un autre travailleur**.

```text
LE CYCLE DE RÉPÉTITION INÉVITABLE EN RÉSEAU FAILLIBLE :

  [ Broker de Messages ] ──── 1. Envoi Tâche #42 ────► [ Worker A ]
           ▲                                                │
           │                                          (Calcul réussi)
           │                                                │
           x ── 2. ACK perdu sous coupure réseau ◄──────────┘
           │
   (Timeout Broker)
           │
           ▼
  [ Broker de Messages ] ──── 3. Rejeu Tâche #42 ─────► [ Worker B ]
                                                      💥 RISQUE DE DOUBLE EXÉCUTION
```

L'ingénierie résiliente pose donc un postulat immuable : **la responsabilité de la non-duplication repose intégralement sur le consommateur**. Le domaine doit être mathématiquement [Idempotent](/annexes/glossaire#idempotence).

[^1]: Jim Gray, *Notes on Data Base Operating Systems*, Operating Systems: An Advanced Course, Springer-Verlag, 1978.

---

### 2. Le Transactional Outbox Pattern : éradiquer le problème du double-write

L'anti-pattern le plus destructeur produit par les agents de code consiste à vouloir écrire dans la base de données relationnelle locale et publier sur le broker de messages dans la même fonction applicative :

```python
# Anti-pattern critique : Le piège du Double-Write
def valider_commande(commande):
    db.session.add(commande)
    db.session.commit()          # Point de rupture 1 : La DB peut échouer
    bus_messages.publier(commande) # Point de rupture 2 : Le bus peut crasher ici !
```

Si le processus est tué ou si le réseau s'effondre entre la ligne `commit()` et la ligne `publier()`, la base de données enregistre la commande, mais l'événement n'est jamais publié sur le bus : le client a payé, mais l'atelier de fabrication n'est jamais prévenu.

La solution architecturale standard est le **Transactional Outbox Pattern**[^2] :

```text
FONCTIONNEMENT DU TRANSACTIONAL OUTBOX PATTERN :

  ┌────────────────────────────────────────────────────────────────────────┐
  │ TRANSACTION ACID LOCALE UNIQUE                                         │
  │ 1. INSERT INTO commandes (id, montant, statut) VALUES ('cmd-1', ...); │
  │ 2. INSERT INTO outbox (id, canal, payload) VALUES ('evt-1', ...);     │
  │ COMMIT TRANSACTION; ◄── Atomicité parfaite : Tout réussit ou tout échoue│
  └───────────────────────────────────┬────────────────────────────────────┘
                                      │
                                      ▼
             ┌──────────────────────────────────────────────────┐
             │ RELAIS ASYNCHRONE (Poller ou CDC / Debezium)     │
             │ Lit la table outbox et publie sur le broker      │
             └────────────────────────┬─────────────────────────┘
                                      │
                                      ▼
                      [ Broker Kafka / RabbitMQ / SQS ]
```

L'événement d'émission fait partie intégrante de la transaction de données locale. Si la machine hôte subit une coupure de courant, l'événement est garanti d'être persisté sur disque et sera relayé dès le redémarrage.

[^2]: Chris Richardson, *Microservices Patterns: With examples in Java*, Manning Publications, 2018.

---

### 3. Anatomie formelle d'une clé d'idempotence

Une clé d'idempotence ne peut pas se réduire à un simple entier incrémental. Pour garantir l'isolation multi-locataires (*multi-tenancy*) et prévenir les attaques par collision, sa structure doit être composite :

$$\text{CléIdempotence} = \text{SHA256}(\text{TenantId} \mathbin{\Vert} \text{NomOperation} \mathbin{\Vert} \text{NonceClient})$$

```text
MACHINE À ÉTATS D'UN VERROU D'IDEMPOTENCE :

                      [ Requête entrante ]
                               │
                               ▼
                    ┌─────────────────────┐
                    │ La clé existe-t-elle│
                    │  dans le registre ? │
                    └──────────┬──────────┘
                               │
            ┌──────────────────┴──────────────────┐
        (NON : Nouvelle)                      (OUI : Connue)
            ▼                                     ▼
   ┌──────────────────┐               ┌────────────────────────┐
   │ État: PROCESSING │               │ Vérifier Empreinte du  │
   │ Verrou posé (TTL)│               │ Payload de la requête  │
   └────────┬─────────┘               └───────────┬────────────┘
            │                                     │
     (Calcul Métier)                   ┌──────────┴──────────┐
            │                     (Identique)            (Divergent)
            ▼                          ▼                      ▼
   ┌──────────────────┐       ┌──────────────────┐  ┌──────────────────┐
   │ État: COMPLETED  │       │ Renvoyer réponse │  │ Rejet HTTP 409   │
   │ Résultat gelé    │       │ archivée (Cache) │  │ Conflit d'intégrité
   └──────────────────┘       └──────────────────┘  └──────────────────┘
```

Si un client soumet une seconde requête avec la **même clé d'idempotence mais un montant ou un document différent**, le système doit refuser le traitement avec une erreur HTTP 409 (Conflit) : la clé a été réutilisée pour maquiller une seconde intention distincte.

---

### 4. Backoff exponentiel et Full Jitter : désamorcer le troupeau tonitruant

Lorsqu'un service tiers (par exemple le serveur d'API d'authentification) tombe en panne pendant trois minutes puis redémarre, des milliers de clients dont les requêtes ont échoué tentent de se reconnecter simultanément.

Si les réessais utilisent un délai déterministe (ex: toutes les 5 secondes), tous les clients frappent le serveur à la même seconde en pulsations synchronisées. Cette vague submerge immédiatement le service qui s'effondre à nouveau : c'est l'effet dévastateur du **troupeau tonitruant (*Thundering Herd*)**.

La parade algorithmique fondamentale (formalisée par Marc Brooker chez AWS Architecture)[^3] est le **Full Jitter** :

$$t_{\text{attente}} = \text{Uniforme}\left(0, \min(t_{\max}, t_{\text{base}} \times 2^{\text{tentative}})\right)$$

```text
COMPARAISON DES CHARGES DE RÉESSAIS SUR UN SERVICE EN REPRISE :

  Sans Jitter (Pulsations synchrones destructrices) :
  Requêtes/s
  1000 ┌      ▲            ▲            ▲
       │      │            │            │
       │      │            │            │
     0 └──────┴────────────┴────────────┴──────────► Temps
              t=5s         t=10s        t=15s

  Avec Full Jitter (Dispersion uniforme de Poisson) :
  Requêtes/s
   200 ┌   ▄█▅▃▆▂▄▅▃▄▆▂▄▅▃▄▆▂▄▅▃▄▆▂▄▅▃▄▆▂▄▅▃▄
       │   █████████████████████████████████
     0 └───────────────────────────────────────────► Temps
           (Le service absorbe la charge sans saturer)
```

En tirant aléatoirement le délai d'attente sur l'ensemble de la fenêtre exponentielle, les réessais sont uniformément distribués dans le temps, offrant au serveur la capacité de dépiler la file de reprise sans surtension.

[^3]: Marc Brooker, *Exponential Backoff And Jitter*, AWS Architecture Blog, 2015.

---

## Mise en pratique

### Registre d'idempotence, Outbox transactionnelle et Full Jitter en Python 3.11

Le programme suivant implémente l'architecture complète d'un worker asynchrone résilient :
- Registre d'idempotence avec détection de mutations de payload.
- File de messages avec réessais bornés et routage en Dead Letter Queue (DLQ).
- Calculateur de délai à backoff exponentiel et Full Jitter.
- Suite de tests unitaires exécutable et rigoureuse.

```python
"""Module d'ingénierie distribuée : Idempotence, Outbox et Reprises.

Démontre la résilience aux pannes réseau, l'éradication des doublons
et la gestion des files de rebut sous Python 3.11.
"""
from dataclasses import dataclass
from typing import Any, Optional
import hashlib
import random
import unittest


# ============================================================================
# 1. LE REGISTRE D'IDEMPOTENCE
# ============================================================================

class IdempotenceConflitPayloadErreur(Exception):
    """Émise si la même clé est soumise avec des données différentes."""
    pass


@dataclass
class EnregistrementIdempotence:
    statut: str  # "PROCESSING", "COMPLETED", "FAILED"
    sha256_payload: str
    reponse_stockee: Optional[dict[str, Any]] = None


class RegistreIdempotenceMemoire:
    """Registre garantissant qu'un effet métier n'est exécuté qu'une fois."""

    def __init__(self) -> None:
        self._registre: dict[str, EnregistrementIdempotence] = {}

    def reserver_ou_recuperer(
        self, cle: str, payload_brut: bytes
    ) -> tuple[bool, Optional[dict[str, Any]]]:
        """Renvoie (doit_executer: bool, reponse_existante: Optional[dict])."""
        sha = hashlib.sha256(payload_brut).hexdigest()

        if cle in self._registre:
            existant = self._registre[cle]
            if existant.sha256_payload != sha:
                raise IdempotenceConflitPayloadErreur(
                    f"Conflit d'intégrité : Clé {cle} réutilisée avec un payload différent."
                )
            if existant.statut == "COMPLETED":
                return False, existant.reponse_stockee
            # Si PROCESSING, une tentative est déjà en cours
            return False, {"statut": "EN_COURS"}

        # Nouvelle clé : réservation
        self._registre[cle] = EnregistrementIdempotence(
            statut="PROCESSING",
            sha256_payload=sha
        )
        return True, None

    def completer(self, cle: str, reponse: dict[str, Any]) -> None:
        if cle in self._registre:
            self._registre[cle].statut = "COMPLETED"
            self._registre[cle].reponse_stockee = reponse


# ============================================================================
# 2. ALGORITHME DE BACKOFF EXPONENTIEL AVEC FULL JITTER
# ============================================================================

class CalculateurBackoff:
    """Implémente la distribution uniforme de Marc Brooker (AWS Architecture)."""

    @classmethod
    def calculer_delai_secondes(
        cls,
        tentative: int,
        base_secondes: float = 1.0,
        plafond_secondes: float = 30.0
    ) -> float:
        delai_exponentiel = min(plafond_secondes, base_secondes * (2 ** tentative))
        # Full Jitter : tirage uniforme entre 0 et le délai exponentiel calculé
        return random.uniform(0.0, delai_exponentiel)


# ============================================================================
# 3. LE WORKER ASYNCHRONE ET LA FILE DE REBUT (DEAD LETTER QUEUE)
# ============================================================================

@dataclass(frozen=True)
class MessageTache:
    id_message: str
    cle_idempotence: str
    payload_octets: bytes
    tentatives_effectuees: int = 0


class WorkerTraitementAsynchrone:
    """Consommateur robuste avec déduplication et routage DLQ."""

    MAX_RETRIES = 3

    def __init__(self, registre: RegistreIdempotenceMemoire) -> None:
        self.registre = registre
        self.compteur_effets_metier_reels = 0
        self.file_morte_dlq: list[MessageTache] = []

    def executer_effet_metier_externe(self, payload: bytes) -> dict[str, Any]:
        """Action non réversible (ex: appel bancaire, écriture disque certifiée)."""
        self.compteur_effets_metier_reels += 1
        return {"statut": "SUCCES", "taille_traitee": len(payload)}

    def traiter_message(self, message: MessageTache, simuler_echec_metier: bool = False) -> dict[str, Any]:
        doit_executer, reponse_existante = self.registre.reserver_ou_recuperer(
            message.cle_idempotence,
            message.payload_octets
        )

        if not doit_executer:
            # Idempotence : court-circuit immédiat sans reproduire l'effet métier
            return reponse_existante or {"statut": "IGNORE_DOUBLON"}

        if simuler_echec_metier:
            # Échec de la tâche
            nouvelles_tentatives = message.tentatives_effectuees + 1
            if nouvelles_tentatives >= self.MAX_RETRIES:
                # Épuisement des réessais : transfert en Dead Letter Queue
                self.file_morte_dlq.append(message)
                return {"statut": "ABANDON_DLQ", "tentatives": nouvelles_tentatives}
            return {"statut": "RETRY_PROGRAMME", "tentatives": nouvelles_tentatives}

        # Traitement nominal
        reponse = self.executer_effet_metier_externe(message.payload_octets)
        self.registre.completer(message.cle_idempotence, reponse)
        return reponse
```

---

### La suite de tests prouvant l'idempotence et la gestion des échecs

```python
class TestAsynchronismeEtIdempotence(unittest.TestCase):
    """Vérifie l'unicité de l'effet sous rejeu et le transfert en DLQ."""

    def test_rejeu_cinq_fois_produit_un_seul_effet(self) -> None:
        registre = RegistreIdempotenceMemoire()
        worker = WorkerTraitementAsynchrone(registre)

        message = MessageTache(
            id_message="msg-001",
            cle_idempotence="IDEM-CLE-UNIQUE-999",
            payload_octets=b"Donnees importantes du devis 458"
        )

        # 1. Premier passage : exécution réelle de l'effet
        rep1 = worker.traiter_message(message)
        self.assertEqual(rep1["statut"], "SUCCES")
        self.assertEqual(worker.compteur_effets_metier_reels, 1)

        # 2. Rejeu 4 fois consécutives (simulation de rediffusion At-Least-Once)
        for _ in range(4):
            rep_doublon = worker.traiter_message(message)
            self.assertEqual(rep_doublon["statut"], "SUCCES")

        # Invariant absolu : Malgré 5 appels, l'effet métier n'a eu lieu qu'UNE seule fois
        self.assertEqual(worker.compteur_effets_metier_reels, 1)

    def test_rejet_mutation_de_payload_sur_meme_cle(self) -> None:
        registre = RegistreIdempotenceMemoire()
        worker = WorkerTraitementAsynchrone(registre)

        message_original = MessageTache("msg-1", "CLE-A", b"Payload initial")
        worker.traiter_message(message_original)

        # Tentative frauduleuse ou bug : même clé, mais payload altéré
        message_mutant = MessageTache("msg-2", "CLE-A", b"Payload DIFFERENT !")
        with self.assertRaises(IdempotenceConflitPayloadErreur):
            worker.traiter_message(message_mutant)

    def test_routage_en_dead_letter_queue_apres_3_echecs(self) -> None:
        registre = RegistreIdempotenceMemoire()
        worker = WorkerTraitementAsynchrone(registre)

        message_corrompu = MessageTache("msg-err", "CLE-ERR", b"Octets corrompus", tentatives_effectuees=2)
        
        # 3e tentative en échec -> doit partir en DLQ
        rep = worker.traiter_message(message_corrompu, simuler_echec_metier=True)
        self.assertEqual(rep["statut"], "ABANDON_DLQ")
        self.assertEqual(len(worker.file_morte_dlq), 1)
        self.assertEqual(worker.file_morte_dlq[0].id_message, "msg-err")

    def test_calcul_full_jitter_dans_les_bornes(self) -> None:
        for tentative in range(5):
            delai = CalculateurBackoff.calculer_delai_secondes(tentative, base_secondes=1.0, plafond_secondes=16.0)
            borne_max = min(16.0, 1.0 * (2 ** tentative))
            self.assertGreaterEqual(delai, 0.0)
            self.assertLessEqual(delai, borne_max)


if __name__ == "__main__":
    unittest.main()
```

---

## Exercice d'arbitrage & Corrigé commenté

### Le cas d'ingénierie : L'appel HTTP externe dans une transaction SQL verrouillante

Un agent de code propose la Pull Request suivante pour traiter l'encaissement d'un abonnement récurrent :

```python
# Code soumis par l'agent dans app/services/abonnement.py (Faute d'architecture critique) :
def renouveler_abonnement(compte_id: str):
    with db.transaction():
        # Verrouillage pessimiste de la ligne du compte client en base
        compte = db.query(Compte).filter_by(id=compte_id).with_for_update().one()
        
        # APPEL RÉSEAU SYNCHRONE VERS LA PASSERELLE BANCAIRE DANS LA TRANSACTION SQL :
        reponse_banque = requests.post(
            "https://api.prestataire-bancaire.com/v1/charges",
            json={"montant": compte.forfait_mensuel, "client": compte.stripe_id},
            timeout=30  # Timeout de 30 secondes !
        )
        
        if reponse_banque.status_code == 200:
            compte.date_fin_validite += datetime.timedelta(days=30)
            db.session.commit()
```

### La grille d'audit de l'architecte

1. **Prise d'otage des connexions de base de données (*Connection Pool Exhaustion*)** : Effectuer un appel HTTP tiers (pouvant durer jusqu'à 30 secondes) à l'intérieur d'une transaction SQL avec `with_for_update()` sature le pool de connexions PostgreSQL. Si 50 renouvellements tournent en parallèle, la base de données entière cesse de répondre à tous les autres utilisateurs.
2. **Vulnérabilité aux timeouts fantômes** : Si la passerelle bancaire débite le client au bout de 29 secondes mais que la requête coupe à la 30e seconde, la transaction SQL effectue un `ROLLBACK`. Le client est débité sur son compte bancaire, mais son abonnement n'est pas renouvelé dans la base locale.

### Le corrigé commenté

**Décision de l'architecte** : Rejet immédiat de la PR (*Changes Requested*) avec obligation d'appliquer le Transactional Outbox Pattern :

```text
CONSIGNE DE REFACTORING DISTRIBUÉ :
1. Interdiction absolue d'exécuter des appels HTTP à l'intérieur d'une transaction SQL.
2. La transaction locale doit être ultra-rapide (5 millisecondes) :
   - Enregistrer l'intention dans la table 'outbox_paiements' avec clé d'idempotence unique.
   - Libérer immédiatement la connexion et le verrou de base.
3. Un worker d'arrière-plan dépile la table 'outbox_paiements' :
   - Exécute l'appel HTTP externe avec réessais en Full Jitter.
   - Enregistre le résultat final dans une nouvelle transaction courte dédiée.
```

---

## Checklist réflexe du pilote

Avant de déployer un traitement distribué ou une file d'arrière-plan, contrôle ces six critères d'ingénierie :

- [ ] **Les appels externes sont hors des transactions SQL** : Aucun appel HTTP, SMTP ou AWS ne s'exécute à l'intérieur d'une transaction de base de données ouverte.
- [ ] **Le pattern Outbox sécurise la persistance** : Tout événement critique est persisté dans la même transaction ACID que la donnée métier avant diffusion.
- [ ] **L'idempotence protège le consommateur** : Le worker tolère les livraisons dupliquées (*At-Least-Once*) sans reproduire d'effets secondaires.
- [ ] **La mutation de payload est détectée** : Une même clé soumise avec des données divergentes est immédiatement refoulée (HTTP 409).
- [ ] **Le Full Jitter est configuré** : Les réessais intègrent un tirage aléatoire uniforme pour désamorcer les tempêtes de reconnexion.
- [ ] **La Dead Letter Queue est surveillée** : Les messages en échec terminal sont acheminés vers une file de rebut avec alerte opérationnelle.

---

## Sources et limites

Ce chapitre approfondit les standards de résilience et d'architecture événementielle :
- **O-MD §1, §2, §12 et §13** ([Manuel d'Orchestration Logicielle](/projet/references/sources/o-md)) : L'idempotence, les transactions distribuées, les files de messages et la continuité de service.
- **I-MD §6, §11.2 et §11.3** ([Manuel d'Ingénierie Logicielle](/projet/references/sources/i-md)) : L'analyse des modes de panne, le Transactional Outbox Pattern, l'algorithme de Full Jitter et l'exploitation des Dead Letter Queues.

Pour concevoir la modélisation des bases relationnelles, les migrations de schéma sans coupure et l'intégrité transactionnelle, poursuis vers le chapitre suivant : **[B08 — Structurer les données et réussir les migrations](/ingenieure/08-donnees-et-migrations)**. Pour réviser les concepts sans outillage de programmation, consulte le miroir accessible : **[A07 — Faire travailler le système sans perdre les opérations](/accessible/07-asynchronisme-et-reprises)**.

## Références pour approfondir

- [PostgreSQL — NOTIFY](https://www.postgresql.org/docs/current/sql-notify.html) — Notifications de sessions ; à distinguer d'une file durable de travaux. [Notice et chapitres associés](/projet/references#ref-notify).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche B07](/redaction/b07-asynchronisme-et-reprises).
