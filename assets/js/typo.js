/**
 * Module de mise en forme typographique pour le français.
 * - Évite les signes de ponctuation orphelins / solitaires en début ou fin de ligne (. , ; ! ? : » « % € $ etc.)
 * - Évite les mots orphelins (solitaires / veuves) sur la dernière ligne d'un alinéa
 * - Lie les nombres et leurs unités usuelles (ex: 500 mégaoctets, 98 %, 15 minutes, 2 heures)
 * - Préserve strictement les blocs de code, balises interactives et formules mathématiques
 */

/**
 * Applique les règles de ponctuation insécable et d'unités sur une chaîne de texte.
 * @param {string} text
 * @returns {string}
 */
export function formatText(text) {
  if (!text) return text;

  // 1. Suppression de tout espace erroné avant ponctuation basse simple : . , …
  text = text.replace(/[ \t]+([.,…])/g, '$1');

  // 2. Espace insécable avant les signes de ponctuation haute / double et symboles : ? ! ; : » % € $ ‰
  text = text.replace(/[ \t]+([?!;:»%€$‰])/g, '\u00A0$1');

  // 3. Espace insécable après les guillemets ouvrants : « ‹
  text = text.replace(/([«‹])[ \t]+/g, '$1\u00A0');

  // 4. Espace insécable entre nombres et unités / symboles
  text = text.replace(/(\d)[ \t]+(%|€|\$|£|mégaoctets|gigaoctets|octets|Mo|Go|ko|To|minutes?|min|secondes?|sec|heures?|jours?|ans?)\b/gi, '$1\u00A0$2');

  // 5. Espace insécable après les abréviations et titres courants : p. 42, chap. 3, vol. 1, etc.
  text = text.replace(/\b(chapitre|chap\.|p\.|vol\.|art\.|n°)[ \t]+(\d+)/gi, '$1\u00A0$2');

  return text;
}

/**
 * Relie les deux derniers mots d'un texte par une espace insécable (anti-solitaire / anti-veuve).
 * @param {string} text
 * @returns {string}
 */
export function bindLastWord(text) {
  if (!text) return text;
  return text.replace(/ ([^ \u00A0\t\r\n]+[\u00A0]*[?!;:»%€$‰.…]*)$/, '\u00A0$1');
}

/**
 * Parcourt un conteneur DOM et applique les règles typographiques françaises.
 * @param {HTMLElement} [root=document.body]
 */
export function formatTypography(root = document.body) {
  if (!root || typeof document === 'undefined') return;

  const walker = document.createTreeWalker(
    root,
    NodeFilter.SHOW_TEXT,
    {
      acceptNode(node) {
        let parent = node.parentElement;
        while (parent && parent !== root) {
          const tag = parent.tagName.toLowerCase();
          if (
            ['pre', 'code', 'kbd', 'samp', 'script', 'style', 'textarea', 'input', 'select', 'svg'].includes(tag) ||
            parent.classList.contains('katex') ||
            parent.classList.contains('highlight') ||
            parent.classList.contains('chroma')
          ) {
            return NodeFilter.FILTER_REJECT;
          }
          parent = parent.parentElement;
        }
        return node.nodeValue && node.nodeValue.trim() ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP;
      }
    }
  );

  const textNodes = [];
  while (walker.nextNode()) {
    textNodes.push(walker.currentNode);
  }

  for (const node of textNodes) {
    const formatted = formatText(node.nodeValue);
    if (node.nodeValue !== formatted) {
      node.nodeValue = formatted;
    }
  }

  // Anti-solitaire : relier le dernier mot de chaque alinéa/titre pour qu'il ne soit jamais isolé
  const blocks = root.querySelectorAll('p, li, blockquote, dt, dd, h1, h2, h3, h4, h5, h6, .lead, .intro-note');
  for (const block of blocks) {
    const blockWalker = document.createTreeWalker(block, NodeFilter.SHOW_TEXT, {
      acceptNode(n) {
        let p = n.parentElement;
        while (p && p !== block) {
          const t = p.tagName.toLowerCase();
          if (['pre', 'code', 'kbd', 'samp', 'script', 'style'].includes(t)) return NodeFilter.FILTER_REJECT;
          p = p.parentElement;
        }
        return n.nodeValue && n.nodeValue.trim() ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP;
      }
    });

    let lastTextNode = null;
    while (blockWalker.nextNode()) {
      lastTextNode = blockWalker.currentNode;
    }

    if (lastTextNode && lastTextNode.nodeValue) {
      const bound = bindLastWord(lastTextNode.nodeValue);
      if (lastTextNode.nodeValue !== bound) {
        lastTextNode.nodeValue = bound;
      }
    }
  }
}

/**
 * Initialise le sélecteur de confort de lecture (taille de texte) et synchronise le localStorage.
 */
export function initTextScale() {
  if (typeof document === 'undefined') return;
  const buttons = document.querySelectorAll('.text-scale-btn');
  if (!buttons.length) return;

  function updateActive(scale) {
    buttons.forEach((btn) => {
      const active = btn.getAttribute('data-scale') === scale;
      btn.setAttribute('aria-pressed', active ? 'true' : 'false');
      btn.classList.toggle('active', active);
    });
  }

  const currentScale = document.documentElement.getAttribute('data-text-scale') || 'normal';
  updateActive(currentScale);

  buttons.forEach((btn) => {
    btn.addEventListener('click', () => {
      const scale = btn.getAttribute('data-scale') || 'normal';
      if (scale === 'normal') {
        document.documentElement.removeAttribute('data-text-scale');
        try { localStorage.removeItem('oc-text-scale'); } catch (e) {}
      } else {
        document.documentElement.setAttribute('data-text-scale', scale);
        try { localStorage.setItem('oc-text-scale', scale); } catch (e) {}
      }
      updateActive(scale);
    });
  });
}

/**
 * Initialise le formatage typographique et le contrôle de taille au chargement de la page.
 */
export function initTypography() {
  if (typeof document === 'undefined') return;
  initTextScale();
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => formatTypography());
  } else {
    formatTypography();
  }
}
