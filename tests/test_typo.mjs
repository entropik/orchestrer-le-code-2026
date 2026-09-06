import test from "node:test";
import assert from "node:assert/strict";
import { formatText, bindLastWord } from "../assets/js/typo.js";

test("ponctuation haute précédée d'espace insécable", () => {
  assert.equal(formatText("serveur distant ?"), "serveur distant\u00A0?");
  assert.equal(formatText("Attention !"), "Attention\u00A0!");
  assert.equal(formatText("Oui ; en effet"), "Oui\u00A0; en effet");
  assert.equal(formatText("La liste :"), "La liste\u00A0:");
  assert.equal(formatText("98 %"), "98\u00A0%");
  assert.equal(formatText("100 €"), "100\u00A0€");
});

test("ponctuation basse simple sans espace", () => {
  assert.equal(formatText("fin de phrase ."), "fin de phrase.");
  assert.equal(formatText("premier mot , deuxième"), "premier mot, deuxième");
  assert.equal(formatText("en attendant …"), "en attendant…");
});

test("guillemets français ouvrants et fermants", () => {
  assert.equal(formatText("« mot remarquable »"), "«\u00A0mot remarquable\u00A0»");
  assert.equal(formatText("« citation » !"), "«\u00A0citation\u00A0»\u00A0!");
});

test("nombres et unités usuelles reliés", () => {
  assert.equal(formatText("fichier de 500 mégaoctets"), "fichier de 500\u00A0mégaoctets");
  assert.equal(formatText("connexion à 98 %"), "connexion à 98\u00A0%");
  assert.equal(formatText("délai de 15 minutes"), "délai de 15\u00A0minutes");
  assert.equal(formatText("pendant 2 heures"), "pendant 2\u00A0heures");
  assert.equal(formatText("chapitre 1"), "chapitre\u00A01");
  assert.equal(formatText("p. 42"), "p.\u00A042");
});

test("anti-solitaire : relie les deux derniers mots d'un paragraphe", () => {
  assert.equal(bindLastWord("serveur distant\u00A0?"), "serveur\u00A0distant\u00A0?");
  assert.equal(bindLastWord("bouton ne pose pas\u00A0:"), "bouton ne pose\u00A0pas\u00A0:");
  assert.equal(bindLastWord("Une phrase avec point final."), "Une phrase avec point\u00A0final.");
  assert.equal(bindLastWord("Un seul mot"), "Un seul\u00A0mot");
  assert.equal(bindLastWord("MotUnique"), "MotUnique");
});

test("cas réel du problème utilisateur : aucun signe solitaire", () => {
  let phrase = "Quand un client dépose un fichier de 500 mégaoctets, où va-t-il physiquement ? Reste-t-il sur ton ordinateur ou part-il sur un serveur distant ?";
  let formatee = formatText(phrase);
  let finale = bindLastWord(formatee);

  assert.equal(finale, "Quand un client dépose un fichier de 500\u00A0mégaoctets, où va-t-il physiquement\u00A0? Reste-t-il sur ton ordinateur ou part-il sur un serveur\u00A0distant\u00A0?");
  // Vérification : distant et ? sont liés par NBSP, serveur et distant sont liés par NBSP
  assert.ok(finale.includes("serveur\u00A0distant\u00A0?"));
  assert.ok(!finale.includes("distant ?"));
});

test("initTextScale : bascule les crans et synchronise l'attribut data-text-scale", async () => {
  let docScale = null;
  let stored = null;
  const callbacks = {};

  class MockElement {
    constructor(scale) {
      this.scale = scale;
      this.attrs = { "data-scale": scale, "aria-pressed": scale === "normal" ? "true" : "false" };
      this.classList = {
        classes: new Set(),
        toggle(cls, state) {
          if (state) this.classes.add(cls);
          else this.classes.delete(cls);
        }
      };
    }
    getAttribute(k) { return this.attrs[k]; }
    setAttribute(k, v) { this.attrs[k] = v; }
    addEventListener(event, fn) { callbacks[this.scale] = fn; }
  }

  const btnNormal = new MockElement("normal");
  const btnComfort = new MockElement("comfort");
  const btnLarge = new MockElement("large");

  global.document = {
    documentElement: {
      getAttribute(k) { return docScale; },
      setAttribute(k, v) { docScale = v; },
      removeAttribute(k) { docScale = null; }
    },
    querySelectorAll(sel) {
      return sel === ".text-scale-btn" ? [btnNormal, btnComfort, btnLarge] : [];
    }
  };
  global.localStorage = {
    getItem(k) { return stored; },
    setItem(k, v) { stored = v; },
    removeItem(k) { stored = null; }
  };

  const { initTextScale } = await import("../assets/js/typo.js");
  initTextScale();

  // Test 1: clic sur confort
  callbacks["comfort"]();
  assert.equal(docScale, "comfort");
  assert.equal(stored, "comfort");
  assert.equal(btnComfort.getAttribute("aria-pressed"), "true");
  assert.equal(btnNormal.getAttribute("aria-pressed"), "false");

  // Test 2: clic sur large
  callbacks["large"]();
  assert.equal(docScale, "large");
  assert.equal(stored, "large");
  assert.equal(btnLarge.getAttribute("aria-pressed"), "true");

  // Test 3: retour sur normal
  callbacks["normal"]();
  assert.equal(docScale, null);
  assert.equal(stored, null);
  assert.equal(btnNormal.getAttribute("aria-pressed"), "true");

  delete global.document;
  delete global.localStorage;
});

