{
  "title": "Demander des preuves, pas seulement du code",
  "description": "Savoir ce qu'un test démontre et poser les bonnes questions à la livraison.",
  "weight": 6,
  "chapter_id": "A06",
  "theme": "06",
  "status": "redaction",
  "source_path": "manuscrit/01-lecture-accessible/06-tests-et-preuves.md",
  "mirror": "/ingenieure/06-tests-et-preuves",
  "related": [
    "/accessible/03-besoin-et-contrats",
    "/accessible/11-methode-et-cas-pratiques"
  ],
  "notions": [
    {
      "label": "CI",
      "anchor": "ci"
    },
    {
      "label": "Invariant",
      "anchor": "invariant"
    },
    {
      "label": "Contrat",
      "anchor": "contrat"
    }
  ],
  "previous": "/accessible/05-git-et-collaboration",
  "next": "/accessible/07-asynchronisme-et-reprises"
}

## Ce que tu sauras faire

Savoir ce qu'un test démontre et poser les bonnes questions à la livraison.

---

## Première synthèse

### 1. Le garagiste et les freins : pourquoi une jolie capture d'écran ne prouve rien

Imagine que tu amènes ta voiture au garage pour faire réviser le système de freinage. Lorsque tu viens récupérer le véhicule, le mécanicien t'accueille avec un grand sourire en te montrant la carrosserie étincelante :
> *« Regardez comme elle brille ! J'ai passé un coup de polish sur le capot et les jantes en aluminium sont impeccables. Tout est prêt, vous pouvez partir sur l'autoroute ! »*

Acceptes-tu de monter à bord les yeux fermés ? Évidemment non. Tu te moques que la carrosserie brille si les plaquettes de frein n'ont pas été mesurées et testées sur un banc d'essai mécanique.

Dans le développement assisté par intelligence artificielle, **l'illusion visuelle est le piège le plus séduisant**.

Lorsqu'un agent termine une tâche, son premier réflexe est souvent d'afficher une superbe capture d'écran d'un bouton joliment coloré, ou de t'écrire avec assurance : *« Tous les tests passent avec succès ! »*.

Le rôle du maître d'ouvrage est de ne jamais confondre la beauté de la carrosserie avec la solidité des freins. Un écran bien dessiné ne prouve pas que le système fonctionne lorsque dix clients cliquent en même temps, ni qu'un pirate ne peut pas voler les factures de ton voisin.

---

### 2. Ce qu'un test démontre (et ce qu'il ignore)

Une phrase célèbre de l'informaticien Edsger Dijkstra rappelle une vérité fondamentale :
> *« Les tests peuvent prouver la présence de défauts, jamais leur absence. »*

Quand un agent t'annonce fièrement : *« La suite de tests est au vert ! »*, cela ne signifie pas que ton programme est parfait ni exempt de bugs. Cela prouve **exclusivement qu'il a réussi les trois ou quatre vérifications précises que quelqu'un a pensé à écrire**.

```text
L'ANGLE MORT DES TESTS INCOMPLETS :

  Ce que le test vérifie (Le cercle vert) :
  ┌──────────────────────────────────────────────┐
  │ [✓] Le bouton "Payer" est cliquable.        │
  │ [✓] La page affiche un accusé de réception.  │
  └──────────────────────┬───────────────────────┘
                         │
  Ce que le test ignore totalement (L'angle mort critique) :
  ┌──────────────────────▼───────────────────────┐
  │ [!] Si le client double-clique, est-il débité deux fois ?
  │ [!] Le paiement est-il enregistré si la connexion coupe à la 99e milliseconde ?
  │ [!] L'utilisateur B peut-il consulter la commande de l'utilisateur A ?
  └──────────────────────────────────────────────┘
```

Le pilote ne demande donc jamais à un agent : *« Est-ce que ça marche ? »*. Il lui demande : **« Qu'as-tu testé exactement, avec quelles valeurs, et quels risques ne sont pas encore couverts ? »**.

---

### 3. Tester en priorité les erreurs qui coûtent cher

Tous les dysfonctionnements logiciels n'ont pas la même gravité. Si un texte de menu est décalé de trois millimètres vers la gauche, c'est un défaut esthétique sans conséquence. Si un client est prélevé trois fois pour la même commande, c'est un scandale financier et juridique immédiat.

Pour rentabiliser son temps et son énergie, le pilote exige des tests automatiques sur les **quatre périls majeurs** :

| Le Péril Majeur | Exemple concret | La Preuve exigée par le Pilote |
|---|---|---|
| **1. La Perte de données** | Une coupure réseau au milieu du téléversement laisse un fichier corrompu sur le serveur. | Prouver que le fichier partiel est automatiquement détruit et qu'aucun devis fantôme n'apparaît dans la liste. |
| **2. La Duplication d'actions** | L'utilisateur clique deux fois rapidement sur « Valider la commande ». | Prouver qu'une seule commande est créée et qu'un seul débit bancaire est initié ([Idempotence](/annexes/glossaire#idempotence)). |
| **3. La Fuite entre organisations** | Le client de l'entreprise Alpha tente d'ouvrir le document n° 458 appartenant à l'entreprise Bêta. | Prouver que le serveur renvoie un refus d'accès strict (HTTP 403), même si l'URL est connue. |
| **4. Le Blocage par saturation** | Un utilisateur envoie un fichier de 5 gigaoctets au lieu des 50 Mo autorisés. | Prouver que le système coupe la transmission dès le début sans saturer la mémoire du serveur. |

---

### 4. La règle du « Montre-moi le rouge d'abord » (TDD pour le décideur)

Lorsque tu demandes à un agent de réparer un bug, comment savoir s'il a réellement résolu le problème ou s'il a simplement bricolé une réponse de façade ?

La réponse tient dans une méthode universelle appelée le **Développement Piloté par les Tests (*Test-Driven Development* ou TDD)**[^1]. Pour un pilote, elle se résume à une règle d'or : **exiger la preuve de la panne avant d'autoriser la réparation**.

```text
LA BOUCLE ROUGE - VERTE DU PILOTE :

  ÉTAPE 1 : PROUVER LA PANNE (LE ROUGE)
  L'agent écrit un test qui reproduit fidèlement le problème signalé.
  ► Le test doit ÉCHOUER.
  (Preuve formelle que le système est actuellement défaillant).
            │
            ▼
  ÉTAPE 2 : APPLIQUER LA RÉPARATION (LE VERT)
  L'agent modifie la logique interne pour corriger le comportement.
  ► Le test doit RÉUSSIR.
  (Preuve mécanique que la défaillance est éliminée).
            │
            ▼
  ÉTAPE 3 : GARDER LE GARDE-FOU PERMANENT
  Le test reste définitivement dans le projet.
  (Si un futur agent réintroduit le même bug dans six mois, le test hurlera immédiatement).
```

Si un agent te dit : *« J'ai corrigé le bug de remise »*, mais qu'il est incapable de te montrer le test qui était rouge avant son intervention, méfiance absolue. Sans échec préalable constaté, rien ne prouve que le code était réellement cassé, ni qu'il est réparé.

[^1]: Formalisé par Kent Beck à la fin des années 1990 dans le cadre de l'*Extreme Programming* (XP), le TDD est le socle de la fiabilité logicielle moderne.

---

### 5. Les trois regards indispensables avant la livraison

Pour qu'un travail soit déclaré « terminé », le pilote organise la convergence de trois vérifications complémentaires :

1. **La preuve automatique (La machine)** : La suite de tests unitaires s'exécute en quelques secondes sur l'ordinateur et renvoie un feu vert sans équivoque.
2. **L'essai en conditions réelles (Le pilote)** : Tu ouvres l'application, tu glisses un vrai fichier PDF, tu coupes volontairement le Wi-Fi, tu observes la réaction du système avec tes yeux d'humain.
3. **La seconde lecture (La revue)** : Tu inspectes le résumé des lignes modifiées (la Pull Request) pour t'assurer qu'aucun changement clandestin n'a été glissé en douce.

Ce n'est qu'à la croisée de ces trois regards que réside la véritable sérénité.

---

## Mise en pratique

### Exemple fil rouge : Les trois preuves du système de réception de devis

Voici la fiche de validation formelle que le pilote exige de l'agent avant de considérer le module de réception comme achevé :

```text
================================================================================
DOSSIER DE PREUVES : RÉCEPTION DE DOCUMENTS CLIENTS
================================================================================

[RISQUE N° 1 : DUPLICATION PAR DOUBLE-CLIC]
- Scénario de test : L'agent simule deux requêtes HTTP identiques envoyées
  à 5 millisecondes d'intervalle avec le même jeton client.
- Preuve attendue : 
  ✓ Une seule écriture physique sur le disque.
  ✓ Un seul numéro de dossier généré (ex: DEV-2026-001).
  ✓ La deuxième requête reçoit un accusé de réception identique sans doublon.

[RISQUE N° 2 : ÉTANCHÉITÉ ENTRE ORGANISATIONS (FUITE DE DONNÉES)]
- Scénario de test : Un utilisateur authentifié sous 'org-client-alpha' tente
  d'accéder à l'URL '/documents/doc-client-beta-999.pdf'.
- Preuve attendue :
  ✓ Le serveur renvoie immédiatement une erreur 403 (Interdit).
  ✓ Zéro octet du document confidentiel n'est transmis sur le réseau.
  ✓ Une alerte de tentative d'accès suspecte est journalisée.

[RISQUE N° 3 : NETTOYAGE DES FICHIERS INTERROMPUS]
- Scénario de test : Un transfert de fichier est brutalement stoppé à 45 %
  du flux réseau.
- Preuve attendue :
  ✓ Le fichier partiel '.tmp' est immédiatement effacé du répertoire temporaire.
  ✓ Aucune ligne incomplète n'est enregistrée dans la base de données.
================================================================================
```

---

## Exercice d'arbitrage & Corrigé commenté

### La mise en situation

Tu demandes à un agent de s'assurer que le système de facturation n'applique jamais de réduction supérieure à 30 %. L'agent revient après dix minutes :

> *« Tout est testé et validé ! J'ai créé le fichier de test unitaire `test_remise.py` et la commande affiche 100 % de réussite. Voici le code de mon test : »*

```python
def test_remise_securisee():
    # Test écrit par l'agent :
    montant_initial = 100
    remise_proposee = 50  # 50% de remise
    if remise_proposee > 30:
        statut = "REFUS"
    else:
        statut = "ACCORD"
    # Assertion de l'agent :
    assert statut == "REFUS"
```

### Les questions du pilote

Face à ce code, le pilote averti ne se laisse pas impressionner par le vert de la console :

1. **Qu'est-ce que ce test évalue réellement ?** : Ce test évalue la petite condition `if/else` que l'agent vient d'écrire **à l'intérieur même de son test** !
2. **Le vrai code de l'application a-t-il été exécuté ?** : Absolument pas ! Le test n'appelle à aucun moment le vrai module de facturation de l'entreprise.
3. **C'est une tautologie pure (*Test Coquille Vide*)** : Le test prouve simplement que si une variable vaut 50, elle est supérieure à 30. Si demain un pirate demande 80 % de remise dans l'application réelle, le système l'accordera sans broncher, alors que le test continuera d'afficher un vert triomphant !

### Le corrigé commenté

**La décision du pilote** : Rejet ferme de l'illusion de test.

Tu ordonnes à l'agent :  
*« Ce test est une coquille vide inacceptable. Tu testes une variable locale que tu as inventée dans le test, sans jamais solliciter le véritable moteur de facturation `CalculateurFacture.appliquer_remise()`.  
Reprends immédiatement :  
1. Importe la vraie fonction de production du projet.  
2. Appelle cette fonction avec une commande de 100 euros et une remise demandée de 50 %.  
3. Vérifie que la vraie fonction lève l'erreur officielle `RemisePlafondDepasseeErreur`. »*

En repérant ces tests factices, tu protèges ton produit contre les pires régressions silencieuses.

---

## Checklist réflexe du pilote

Avant de valider une fonctionnalité sur la foi de ses tests, passe en revue ces cinq critères d'intégrité :

- [ ] **Le vrai code est sollicité** : Les tests appellent les vraies fonctions du projet, et non des simulations écrites dans le test lui-même.
- [ ] **Les risques majeurs sont couverts** : Des tests spécifiques vérifient la perte de données, les doublons, la sécurité des accès et la saturation.
- [ ] **Le rouge a précédé le vert** : Tu as la preuve que le test échouait bel et bien avant l'intervention de l'agent.
- [ ] **Les cas limites sont explorés** : Les vérifications portent sur des valeurs nulles, des fichiers corrompus et des limites chiffrées, pas uniquement sur le cas idéal.
- [ ] **Les tests s'exécutent en un clic** : N'importe quel membre de l'équipe peut reproduire l'intégralité de la suite de tests en quelques secondes sur sa machine locale.

---

## Sources et limites

Ce chapitre s'appuie sur les principes fondamentaux de vérification et d'assurance qualité logicielle :
- **O-MD §7** ([Manuel d'Orchestration Logicielle](/projet/references/sources/o-md)) : La pyramide pragmatique des tests, les cinq priorités de test, le rôle de la CI et les protocoles de validation.
- **I-MD §5** ([Manuel d'Ingénierie Logicielle](/projet/references/sources/i-md)) : La pyramide de vérification déterministe, le TDD inversé supervisé, les tests de propriétés génératifs et les tests de mutation contre les faux positifs.

Pour maîtriser le protocole du TDD inversé, les tests de propriétés avec Hypothesis et la gestion déterministe des courses concurrentes en Python 3.11, poursuis vers le chapitre miroir : **[B06 — Tester et prouver le comportement](/ingenieure/06-tests-et-preuves)**.

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A06](/redaction/a06-tests-et-preuves).
