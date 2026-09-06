import { initTypography } from './typo.js';

initTypography();

// Colophon d'atelier & Easter Egg console (F12)
console.log(
  `%c┌────────────────────────────────────────────────────────────────────────┐\n` +
  `│  ORCHESTRER LE CODE EN 2026 · DANS L'ATELIER DE L'AUTEUR               │\n` +
  `├────────────────────────────────────────────────────────────────────────┤\n` +
  `│  Ce manuel n'est pas le fruit d'un chatbot solitaire dans un onglet.   │\n` +
  `│                                                                        │\n` +
  `│  Setup de fabrication :                                                │\n` +
  `│  • ADE : Orca (flotte multi-worktrees Git isolés, 0 collision)         │\n` +
  `│  • Gouvernance : Skills de Matt Pocock (doctrine du harnais 3 couches) │\n` +
  `│  • Modèles : Gemini (maïeutique, vision) + Codex (rigueur de code)     │\n` +
  `│                                                                        │\n` +
  `│  100 % statique · 0 traceur · 61 planches vectorielles · Tests au vert │\n` +
  `│  Marc Tallec © 2026 · Licence CC BY-NC-ND 4.0 / MIT                    │\n` +
  `└────────────────────────────────────────────────────────────────────────┘`,
  "font-family: monospace; font-size: 11px; line-height: 1.3; color: #ff5c35; font-weight: bold;"
);

(function () {
  const toggle = document.getElementById('nav-toggle');
  const header = document.getElementById('site-header');
  const nav = document.getElementById('site-nav');
  if (!toggle || !header || !nav) return;

  function setOpen(open) {
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    toggle.setAttribute('aria-label', open ? 'Fermer le menu de navigation' : 'Ouvrir le menu de navigation');
    header.classList.toggle('nav-open', open);
  }

  toggle.addEventListener('click', function (e) {
    e.stopPropagation();
    const isOpen = toggle.getAttribute('aria-expanded') === 'true';
    setOpen(!isOpen);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      toggle.focus();
    }
  });

  document.addEventListener('click', function (e) {
    if (toggle.getAttribute('aria-expanded') === 'true' && !header.contains(e.target)) {
      setOpen(false);
    }
  });

  nav.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      if (window.innerWidth <= 960) {
        setOpen(false);
      }
    });
  });
})();
