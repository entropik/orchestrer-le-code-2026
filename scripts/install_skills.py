#!/usr/bin/env python3
"""
scripts/install_skills.py — Installation et synchronisation agnostique des 37 skills de Matt Pocock.
Installe à la fois :
1. Dans le projet local : .agents/skills/<name>/ (Repository-as-Code pour Git, étudiants, CI/CD)
2. Dans le hub global : ~/.agents/skills/<name>/
3. Dans les répertoires d'agents : ~/.claude/skills/, ~/.gemini/skills/, ~/.codex/skills/ (Codex, Claude, Gemini, Kimi)
"""

import os
import shutil
import pathlib
import sys

def safe_remove(path: pathlib.Path):
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)

def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    matt_source = pathlib.Path("/tmp/mattpocock-skills/skills")
    
    if not matt_source.exists():
        print(f"Erreur : source {matt_source} introuvable.")
        sys.exit(1)

    # 1. Collecter tous les skills de Matt
    skills = {}
    for skill_file in matt_source.rglob("SKILL.md"):
        skill_dir = skill_file.parent
        name = skill_dir.name
        skills[name] = skill_dir

    print(f"Total skills découverts dans la source : {len(skills)}")

    # Destinations locales et globales
    local_agents = root / ".agents" / "skills"
    home = pathlib.Path.home()
    global_agents = home / ".agents" / "skills"
    claude_skills = home / ".claude" / "skills"
    gemini_skills = home / ".gemini" / "skills"
    codex_skills = home / ".codex" / "skills"

    # Création des dossiers cibles
    for d in [local_agents, global_agents, claude_skills, gemini_skills, codex_skills]:
        d.mkdir(parents=True, exist_ok=True)

    installed_local = 0
    installed_global = 0

    for name, src_dir in sorted(skills.items()):
        # A. Installation dans le projet local (.agents/skills/<name>)
        dst_local = local_agents / name
        if name == "ask-matt" and dst_local.exists():
            # Conserver notre version enrichie pour le projet
            pass
        else:
            if dst_local.exists() or dst_local.is_symlink():
                safe_remove(dst_local)
            shutil.copytree(src_dir, dst_local)
            installed_local += 1

        # B. Installation dans ~/.agents/skills/<name>
        dst_global = global_agents / name
        if dst_global.exists() or dst_global.is_symlink():
            safe_remove(dst_global)
        shutil.copytree(src_dir, dst_global)
        installed_global += 1

        # C. Liens / Synchronisation pour Claude, Gemini et Codex
        # Pour Claude Code (~/.claude/skills)
        claude_target = claude_skills / name
        if not claude_target.exists() and not claude_target.is_symlink():
            try:
                claude_target.symlink_to(f"../../.agents/skills/{name}")
            except Exception:
                shutil.copytree(src_dir, claude_target)

        # Pour Gemini / Antigravity (~/.gemini/skills)
        gemini_target = gemini_skills / name
        if not gemini_target.exists() and not gemini_target.is_symlink():
            try:
                gemini_target.symlink_to(f"../../.agents/skills/{name}")
            except Exception:
                shutil.copytree(src_dir, gemini_target)

        # Pour Codex (~/.codex/skills)
        codex_target = codex_skills / name
        if not codex_target.exists() and not codex_target.is_symlink():
            try:
                codex_target.symlink_to(f"../../.agents/skills/{name}")
            except Exception:
                shutil.copytree(src_dir, codex_target)

    print("\n" + "=" * 65)
    print("INSTALLATION & SYNCHRONISATION AGNOSTIQUE DES SKILLS")
    print("=" * 65)
    print(f"✅ Local projet (.agents/skills/) : {len(list(local_agents.iterdir()))} skills installés")
    print(f"✅ Hub global   (~/.agents/skills/) : {len(list(global_agents.iterdir()))} skills installés/à jour")
    print(f"✅ Claude Code  (~/.claude/skills/) : synchronisé ({len(list(claude_skills.iterdir()))} skills)")
    print(f"✅ Gemini/AGY   (~/.gemini/skills/) : synchronisé ({len(list(gemini_skills.iterdir()))} skills)")
    print(f"✅ OpenAI Codex (~/.codex/skills/)  : synchronisé ({len(list(codex_skills.iterdir()))} skills)")
    print("=" * 65)

if __name__ == "__main__":
    main()
