# ADR 0001 : Architecture de harnais agnostique en trois couches

- **Statut** : Accepté
- **Date** : 2026-09-04
- **Contexte** : Comment outiller les agents d'intelligence artificielle (Claude Code, OpenAI Codex, Google Gemini, Kimi, Cursor) sans lier le projet à un écosystème propriétaire, tout en garantissant une reproductibilité absolue lors des clonages du dépôt par des étudiants ou des contributeurs.

## Décision

Nous adoptons une **architecture de harnais en trois couches** (*Layered Architecture*) adossée au standard ouvert `.agents/` :

1. **Couche Globale (Poste de travail : `~/.`)** : Héberge les réflexes personnels et méthodologiques transverses (`ask-matt`, `grill-me`, `wait-what`, `teach`).
2. **Couche Projet (Dépôt Git : `.agents/skills/` à la racine)** : Héberge l'ensemble des 37 compétences d'ingénierie et de fabrication de code, versionnées dans l'historique Git et adaptées aux commandes réelles du dépôt (`python3.11 -m unittest`, Hugo).
3. **Couche Runtime / Mémoire Vive (`CONTEXT.md` et `docs/adr/`)** : Héberge le glossaire vivant du domaine et le registre des décisions structurantes.

Nous appliquons la règle de **précédence stricte (*shadowing*)** : le local à la racine surcharge systématiquement le global.

## Options Considérées

- **Installation purement globale (`~/.claude/` ou `~/.gemini/`)** : Rejetée car elle génère le syndrome « *Ça marche sur ma machine* » ; les étudiants clonant le dépôt ne disposent d'aucun guidage sans installation manuelle fastidieuse.
- **Formats propriétaires multiples (`.claude/` d'un côté, `.cursor/` de l'autre, `prompts/`)** : Rejetée pour éviter la dispersion, les incohérences de maintenance et l'enfermement technologique (*vendor lock-in*).

## Conséquences

- **Autonomie immédiate** : Un simple `git clone` fournit à tout développeur, étudiant ou agent autonome le harnais complet et les 37 compétences prêtes à l'emploi.
- **Portabilité totale** : Les mêmes compétences sous `.agents/skills/<name>/SKILL.md` sont exécutables indifféremment par Claude, Codex, Gemini/Antigravity, Cursor et Kimi.
- **Traçabilité** : Toute évolution des règles d'ingénierie est auditée et versionnée au même titre que le code du manuel.
