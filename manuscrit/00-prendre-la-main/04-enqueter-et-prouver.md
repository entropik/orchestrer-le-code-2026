# P04 — Enquêter et demander des preuves

## Situation et résultat observable

Le programme affiche un rapport cohérent pour `affiche.pdf`. Cette observation ne démontre pas qu'il traite correctement un fichier vide, une mauvaise extension ou la taille limite. « Ça marche » doit devenir une liste de comportements couverts et de risques encore ouverts.

## Ta prédiction

Prépare une table avec cinq cas : PDF valide, extension `.txt`, taille nulle, taille exacte de 500 000 000 et signature absente. Pour chaque ligne, écris l'état et les raisons attendues avant de lire les tests.

## Un test compare

```js
import test from "node:test";
import assert from "node:assert/strict";
import { evaluerDocument } from "../src/validation.js";

test("distingue un document vide", () => {
  const rapport = evaluerDocument({
    chemin: "vide.pdf",
    tailleOctets: 0,
    signature: "%PDF-"
  });
  assert.equal(rapport.etat, "rejete");
  assert.deepEqual(rapport.raisons, ["Le document est vide."]);
});
```

Le test prépare une entrée, appelle le comportement et compare le résultat à une attente. On nomme parfois ces temps Arrange, Act, Assert ; retiens d'abord le raisonnement. L'assertion est l'oracle : elle décide si l'observation correspond au contrat.

## Ce qu'un test ne prouve pas

Ce test démontre un comportement pour l'entrée construite et l'implémentation exécutée. Il ne démontre pas que tous les PDF sont sûrs, que le fichier peut être imprimé, ni que les droits d'une organisation sont respectés. Une assertion erronée peut rendre vert un comportement erroné.

Une capture d'écran ne remplace pas le test d'une règle interne. Inversement, un test unitaire ne remplace pas l'essai de la commande réelle. Les preuves se complètent.

## Les cinq cas

- Le cas nominal montre le chemin attendu.
- La mauvaise extension exerce une règle de format.
- La taille nulle protège une frontière basse.
- La taille exacte protège l'interprétation de la limite.
- La signature absente distingue le nom du début réel du contenu.

La taille maximale est fournie directement à la fonction pure : aucun fichier de 500 Mo n'est créé. Un bon test contrôle la règle avec le dispositif le plus petit pertinent.

## Une méthode d'enquête

1. **Reproduire** : obtenir le même écart avec une commande précise.
2. **Réduire** : retirer ce qui n'est pas nécessaire au défaut.
3. **Formuler** : écrire plusieurs causes possibles.
4. **Observer** : choisir une expérience qui sépare les hypothèses.
5. **Corriger** : modifier le mécanisme identifié, pas seulement le message.
6. **Empêcher le retour** : conserver un test qui échouait avant la correction.

Une hypothèse n'est pas un fait. « La condition exclut peut-être zéro » devient testable en appelant la fonction avec zéro et en inspectant la condition correspondante.

## Incident guidé

Remplace volontairement `tailleOctets <= 0` par `tailleOctets < 0`. Le fichier vide devient valide. Avant de demander une correction, adresse à l'agent :

> Le test du fichier vide échoue. Ne modifie rien. Donne trois hypothèses, puis pour chacune l'observation minimale qui permet de l'écarter. Commence par les entrées et les attentes du test.

Une bonne aide ralentit la conclusion. Si l'agent propose immédiatement un patch, rappelle la règle de l'exercice. Quand l'hypothèse sur la frontière est étayée, demande le changement minimal et le test de non-régression.

## Erreur de préparation ou défaut du produit

Un test peut échouer parce qu'un import est faux, qu'une fixture manque ou que le programme n'a pas été construit. Dans ce cas, la règle métier n'a peut-être jamais été exécutée. Distingue :

- erreur de préparation : le test ne rejoint pas le comportement ;
- défaut de logique : le comportement observé contredit le contrat ;
- attente incorrecte : l'oracle contredit la règle décidée.

## Test vert trompeur

Imagine une assertion qui attend `valide` pour zéro. Elle passe avec le défaut. Le vert ne vaut que par la qualité de la question posée. Relis séparément les modifications de tests : changer simultanément le produit et l'oracle peut faire disparaître silencieusement une exigence.

## Approfondir la qualité d'une preuve

### Plusieurs distances de vérification

Le test de `evaluerDocument` isole une fonction : rapide et précis, mais éloigné du disque. Un test de `inspecterDocument` emploie une fixture : il couvre la lecture réelle et peut échouer pour des raisons d'environnement. Lancer la commande couvre le trajet local complet. Choisis la preuve selon la question au lieu d'empiler des tests identiques à différentes distances.

Pour une règle de taille, la fonction pure est le niveau direct. Pour un chemin absent, il faut exercer la frontière de fichier. Pour le code de sortie, il faut observer le processus ou isoler son orchestration.

### Concevoir l'oracle avant l'implémentation

Écris : « exactement 500 000 000 octets est autorisé », puis traduis cette phrase en assertion. Si tu lis d'abord le code, tu risques de recopier son opérateur et de confirmer le défaut. Les exemples attendus proviennent du contrat, pas du résultat actuel.

Une assertion trop vague comme « une raison existe » ne protège pas le motif présenté. Une assertion trop liée à l'ordre casse lors d'un changement sans importance. Choisis la propriété qui porte réellement la décision.

### Journal d'enquête

Consigne brièvement commande, résultat et conclusion. Ne transforme pas dix suppositions en dix découvertes. Une expérience peut soutenir une hypothèse sans exclure toutes les autres.

Évite les stratégies suivantes : modifier plusieurs conditions à la fois, répéter sans varier l'entrée, ajouter un délai arbitraire, réécrire entièrement le composant ou affaiblir l'assertion. Elles peuvent déplacer le symptôme sans établir la cause.

### Retirer temporairement la correction

Réintroduire volontairement le défaut ciblé permet de vérifier la force du test. S'il reste vert, il ne détecte pas le mécanisme annoncé. Restaure immédiatement la correction après l'expérience.

Cette petite mutation ne prouve pas toute la suite. Elle répond à une question : ce test attrape-t-il cet opérateur fautif ? Les campagnes systématiques et leurs limites apparaîtront en B06.

### Lire un rapport de test

Repère nombre de tests, premier scénario fautif et différence entre attendu et observé. Un arrêt avant l'annonce des tests indique souvent une erreur de construction. Conserve une sortie assez complète pour reproduire, sans noyer le compte rendu sous des lignes étrangères au défaut.

Demande à l'agent la commande exacte et son code de sortie. « Tout est bon » n'est pas un rapport de vérification.

## Exercice autonome sans agent

À partir de la condition fautive, reproduis le défaut, vérifie que le test échoue pour la bonne raison, localise la condition, corrige un seul opérateur et relance toute la suite. Rédige ensuite quatre phrases : symptôme, cause, correction et preuve.

{{< correction >}}
Le symptôme est l'acceptation d'une taille nulle. La cause est l'opérateur `<`, qui ne contient pas zéro. La correction minimale est `<=`. La preuve comprend le test qui échoue avant, passe après, puis l'ensemble des tests qui confirme l'absence de régression détectée dans leur périmètre.
{{< /correction >}}

## Porte de sortie

- [ ] Je peux dire ce que chaque cas de test couvre.
- [ ] Je ne confonds pas test vert et certitude générale.
- [ ] Je formule une hypothèse avant de modifier.
- [ ] Je distingue préparation, logique et oracle.
- [ ] Je peux présenter une preuve avant/après et ses limites.

Formule finale : « Cette vérification démontre … pour … ; elle ne démontre pas encore … »

## Références de l'étape

[Module de test de Node.js](https://nodejs.org/api/test.html) · [Assertions strictes de Node.js](https://nodejs.org/api/assert.html#strict-assertion-mode). Documentation vérifiée le 1er septembre 2026.
