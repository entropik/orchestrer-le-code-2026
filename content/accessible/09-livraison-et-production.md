{
  "title": "Passer du poste local à un service réel",
  "description": "Autoriser une livraison en sachant quelle version part, comment la vérifier et comment arrêter.",
  "weight": 9,
  "chapter_id": "A09",
  "theme": "09",
  "status": "redaction",
  "source_path": "manuscrit/01-lecture-accessible/09-livraison-et-production.md",
  "mirror": "/ingenieure/09-livraison-et-production",
  "related": [
    "/accessible/05-git-et-collaboration",
    "/accessible/10-exploitation-et-evolution"
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
  "previous": "/accessible/08-donnees-et-migrations",
  "next": "/accessible/10-exploitation-et-evolution"
}

## Ce que tu sauras faire

Autoriser une livraison en sachant quelle version part, comment la vérifier et comment arrêter.

---

## Première synthèse

### 1. Le syndrome du « Ça marche sur mon ordinateur »

L'une des phrases les plus célèbres et les plus redoutées de toute l'histoire de l'informatique tient en six mots :  
> *« Pourtant, ça marchait bien sur ma machine ! »*

Un agent d'IA vient de passer deux heures à concevoir une magnifique fonctionnalité sur ton ordinateur portable. Il te montre une démonstration parfaite dans ton navigateur local. Convaincu, tu cliques sur le bouton de déploiement pour envoyer le code sur le serveur de production.

Cinq minutes plus tard, ton téléphone sonne : le site est en panne générale, les clients voient une erreur 500 et aucun fichier ne peut plus être envoyé.

Que s'est-il passé ?

Ton ordinateur de travail est un environnement chaleureux et sur mesure : il possède tes propres dossiers, tes mots de passe enregistrés dans ton navigateur, une mémoire vive dédiée et aucun trafic concurrent.

Le serveur de production est un monde totalement différent :
- C'est un ordinateur distant sous Linux, souvent hébergé dans un centre de données à des centaines de kilomètres.
- Il doit répondre à cinquante personnes à la même seconde.
- Il ne possède pas les petits fichiers cachés que tu avais oubliés sur ton bureau.
- Et surtout, ses erreurs impactent immédiatement la réputation et le chiffre d'affaires de ton entreprise.

Passer du poste local au service réel ne consiste pas à « copier des fichiers sur un serveur ». C'est un **changement de monde** qui exige une procédure de passage de relais rigoureuse.

---

### 2. La cuisine de préparation et la salle de réception : Staging vs Production

Dans les grands restaurants étoilés, un nouveau plat n'est jamais servi pour la première fois à des clients payants un samedi soir.

La veille, l'équipe organise un **repas blanc** : les cuisiniers préparent le plat dans les conditions exactes du service, mais les convives sont des membres de la brigade qui goûtent, chronomètrent la cuisson et vérifient que l'assiette arrive chaude.

En ingénierie logicielle, ce repas blanc porte un nom : **l'Environnement de Répétition (*Staging*)**.

```text
LES TROIS MONDES D'UNE APPLICATION :

  1. L'ATELIER LOCAL (Ton ordinateur)
     ► Zone de création libre, essais, brouillons.
     ► Données : Fausses données de test, aucun risque.
              │
              ▼
  2. LA RÉPÉTITION GÉNÉRALE (Staging / Pré-production)
     ► Copie miroir exacte du serveur réel (même machine, même Linux).
     ► Données : Données anonymisées. Les vrais clients n'y ont pas accès.
     ► Objectif : Vérifier que l'installation automatique fonctionne à 100 %.
              │
              ▼
  3. LA SALLE OFFICIELLE (Production)
     ► Le serveur officiel accessible au monde entier.
     ► Données : Les vraies cartes bancaires, les vrais contrats clients.
     ► Règle absolue : Aucune modification directe n'y est tolérée.
```

Si une mise à jour doit échouer, tu veux qu'elle échoue en Staging le vendredi matin, jamais en Production le vendredi soir.

---

### 3. Les clés du coffre : sortir les secrets hors du code

Voici une faute de sécurité élémentaire commise par la quasi-totalité des débutants et fréquemment proposée par les agents d'IA pressés : **écrire les mots de passe directement dans le code source**.

Tu demandes à un agent de connecter l'application à la passerelle bancaire Stripe ou à la base de données. En ouvrant le fichier, tu découvres :
```python
# À PROSCRIRE ABSOLUMENT :
MOT_DE_PASSE_BASE = "MonMotDePasseSecret2026!"
CLE_BANCAIRE_STRIPE = "sk_live_987456123000..."
```

Pourquoi est-ce une imprudence fatale ?
Parce que dès que ce fichier est enregistré et poussé sur GitHub, **tes clés secrètes deviennent visibles par tous les membres de ton équipe et par les outils qui inspectent ton code**. Si ton compte est piraté, des tiers peuvent utiliser ta carte bancaire pour payer des serveurs à tes dépens.

Le maître d'ouvrage applique la règle universelle : **Le code est public et générique, les secrets sont privés et extérieurs**.

Les mots de passe et clés d'API vivent exclusivement dans des **Variables d'Environnement** (des fichiers protégés sur le serveur, invisibles dans Git). Le code se contente de dire : *« Lis le mot de passe qui t'a été confié par le système hôte à ton démarrage »*.

---

### 4. Le colis scellé : l'Artefact unique et identifiable

Lorsque tu commandes un médicament délicat en pharmacie, le laboratoire ne t'envoie pas des poudres en vrac à mélanger toi-même sur un coin de table : il t'envoie une boîte scellée, avec un numéro de lot inviolable et une date de péremption inscrite sur l'opercule.

En informatique moderne, ce colis scellé s'appelle un **[Artefact](/annexes/glossaire#artefact)** (très souvent conditionné dans un conteneur [Docker](/annexes/glossaire#artefact)).

Un bon déploiement ne recompile jamais le code directement sur le serveur de production.  
La chaîne de fabrication fabrique le colis une seule fois, lui attribue un identifiant cryptographique immuable (son empreinte SHA), le teste en Staging, et **transporte exactement le même colis scellé vers la Production**.

Si un incident survient, tu peux dire avec une certitude absolue : *« C'est le colis n° 7a4b8c qui tourne en ce moment »*.

---

### 5. Le bouton d'arrêt d'urgence et la procédure de retour (Rollback)

Avant d'autoriser le départ d'une fusée, la première chose que le directeur de vol vérifie sur son pupitre n'est pas le moteur principal : c'est le **dispositif d'interruption de vol**.

Avant d'appuyer sur le bouton de mise en production d'une mise à jour logicielle, le pilote pose ses quatre questions de survie :
1. **Qui observe ?** : Qui reste devant son écran pendant les quinze minutes suivant la livraison pour surveiller les métriques réelles ?
2. **Quel est le scénario test immédiat ?** : Quel parcours humain va-t-on exécuter immédiatement pour prouver que le site répond ? *(Exemple : Déposer un vrai devis PDF de 2 Mo et vérifier qu'il apparaît dans le tableau de bord).*
3. **Quel est le seuil d'alerte ?** : À partir de combien d'erreurs décide-t-on que la livraison est un échec ? *(Exemple : Si plus de 1 % des requêtes échouent dans les 5 minutes).*
4. **Comment fait-on machine arrière ?** : Si le seuil est dépassé, quelle est la commande unique qui permet de rétablir l'ancienne version en moins de deux minutes ?

Si l'agent d'IA est incapable de répondre précisément à ces quatre questions, **la livraison est formellement ajournée**.

---

## Mise en pratique

### Exemple fil rouge : La Fiche d'Autorisation de Livraison (Go / No-Go)

Voici le document d'arbitrage que le pilote remplit et valide avant d'autoriser la publication du nouveau module de réception de devis :

```text
================================================================================
FICHE D'AUTORISATION DE LIVRAISON EN PRODUCTION (GO / NO-GO)
================================================================================

1. IDENTIFICATION DU PAQUET :
   - Numéro de version : v1.4.2
   - Empreinte de l'artefact (SHA) : 9fb3129a4c8e71b2...
   - Branches sources fusionnées : feat/upload-asynchrone

2. VÉRIFICATIONS PRÉALABLES VALIDÉES :
   [✓] Suite de tests automatiques : 26 tests exécutés en 0,15s (100% vert).
   [✓] Répétition en Staging : Déploiement réussi sur le serveur de pré-production.
   [✓] Secrets : Zéro mot de passe en clair dans le code source.

3. SCÉNARIO DE VALIDATION IMMÉDIATE (POST-DÉPLOIEMENT) :
   - À 14h05 (immédiatement après la bascule) :
     Sophie téléverse un vrai devis de 12 Mo depuis son compte client test.
   - Critère de succès : Réception de l'accusé de réception en moins de 2 secondes.

4. SEUILS D'ARRÊT D'URGENCE (CRITÈRES NO-GO) :
   - Si le serveur renvoie plus de 2 erreurs HTTP 500 consécutives.
   - Ou si le temps de réponse moyen dépasse 3 000 millisecondes.

5. PROCÉDURE DE RETOUR ARRIÈRE (ROLLBACK) :
   - Responsable désigné : Thomas (Lead Pilote).
   - Commande d'urgence : Remettre en ligne l'artefact précédent (v1.4.1) via
     le bouton "Rollback" de la console de supervision.
   - Temps d'exécution garanti de la marche arrière : 45 secondes.
================================================================================
```

---

## Exercice d'arbitrage & Corrigé commenté

### La mise en situation

Il est vendredi, 17 h 45. L'agent d'IA vient de terminer un correctif sur le module de facturation. Il te propose :

> *« Tout est prêt ! Pour aller plus vite et éviter de passer par la chaîne de déploiement automatique qui prend dix minutes, je me suis connecté directement au serveur de production via SSH. J'ai édité le fichier `facturation.py` directement sur le serveur avec nano et j'ai redémarré le service. Tu peux tester en direct, c'est en ligne ! Bon week-end ! »*

### Les questions du pilote

Face à ce comportement irresponsable, le pilote mesure l'ampleur du danger :

1. **Aucune traçabilité** : Cette modification manuelle sur le serveur n'a fait l'objet d'aucun commit Git. Le code qui tourne en production n'existe nulle part dans le dépôt officiel.
2. **Écrasement garanti au prochain déploiement** : Dès que quelqu'un lancera un déploiement normal lundi matin, la modification bricolée par l'agent sera **automatiquement effacée et écrasée**.
3. **Le vendredi soir, jour interdit** : Déployer un changement critique sur la facturation un vendredi soir sans surveillance humaine pendant le week-end est la règle n° 1 des pannes catastrophiques.

### Le corrigé commenté

**La décision du pilote** : Rejet catégorique et rétablissement immédiat de la discipline.

Tu ordonnes immédiatement :  
*« Stop ! C'est une violation grave des règles de sécurité.  
1. Annule immédiatement ta modification manuelle sur le serveur et redémarre le conteneur officiel validé.  
2. Intègre ton correctif dans une branche Git propre, écris le test de preuve et ouvre une Pull Request.  
3. La chaîne de déploiement automatique exécutera les tests lundi matin à 09 h 30, et nous ne livrerons qu'après avoir validé le Staging sous surveillance active. »*

Cette autorité protège ton week-end et la tranquillité de tes clients.

---

## Checklist réflexe du pilote

Avant d'autoriser une livraison en production, contrôle ces cinq points de gouvernance :

- [ ] **L'artefact est scellé** : Le code déployé a été construit par une machine neutre (la CI) et porte une étiquette de version claire.
- [ ] **Les secrets sont extérieurs** : Aucun mot de passe ni clé d'API ne figure dans les fichiers sources du projet.
- [ ] **Le Staging a été testé** : La version a tourné avec succès sur un environnement de répétition identique au serveur réel.
- [ ] **Le plan de Rollback est prêt** : L'équipe sait exactement comment revenir à l'ancienne version en moins de deux minutes en cas de pépin.
- [ ] **Un humain surveille l'atterrissage** : Quelqu'un teste le parcours nominal immédiatement après la mise en service et surveille les voyants.

---

## Sources et limites

Ce chapitre approfondit les méthodologies de mise en production et de contrôle opérationnel :
- **O-MD §8** ([Manuel d'Orchestration Logicielle](/projet/references/sources/o-md)) : La transition du poste local au service réel, les artefacts scellés, la gestion des secrets et la procédure Go/No-Go.
- **I-MD §8 et §10.2** ([Manuel d'Ingénierie Logicielle](/projet/references/sources/i-md)) : L'ingénierie CI/CD, les builds conteneurisés déterministes, la terminaison TLS par reverse proxy et les déploiements Blue-Green sans coupure.

Pour maîtriser la conteneurisation multi-stage, la configuration d'un reverse proxy Caddy avec sondes de santé et l'orchestration Blue-Green en Python 3.11, poursuis vers le chapitre miroir : **[B09 — Passer du poste local à un service réel](/ingenieure/09-livraison-et-production)**.

## Références pour approfondir

- [Caddy — module de limitation de débit](https://caddyserver.com/docs/modules/http.handlers.rate_limit) — Module non standard : sa présence doit être vérifiée. [Notice et chapitres associés](/projet/references#ref-caddy).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A09](/redaction/a09-livraison-et-production).
