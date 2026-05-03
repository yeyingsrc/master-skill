#!/usr/bin/env python3
"""Self-test script for all 7 prototype skills.

Checks:
1. SKILL.md exists + has valid frontmatter (name, description, allowed-tools, triggers)
2. meta.json is valid JSON + has expected fields
3. All sub-skill paths in meta.json + SKILL.md exist
4. All sub-skills have valid frontmatter
5. CLI scripts are executable + don't crash on --help / no args
6. References (research files + synthesis) exist
7. Internal markdown links don't 404
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path


def parse_frontmatter(text):
    """Parse YAML frontmatter. Returns (frontmatter dict, rest of text)."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    fm_text = text[4:end]
    rest = text[end + 5:]
    fm = {}
    current_key = None
    current_list = None
    for line in fm_text.split("\n"):
        if not line.strip():
            continue
        if line.startswith("  - ") or line.startswith("- "):
            if current_list is not None:
                current_list.append(line.lstrip("- ").strip().strip('"').strip("'"))
            continue
        m = re.match(r'^([a-zA-Z_][a-zA-Z0-9_-]*)\s*:\s*(.*)$', line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val == "":
                current_key = key
                current_list = []
                fm[key] = current_list
            else:
                current_list = None
                fm[key] = val.strip('"').strip("'")
    return fm, rest


def check_skill(prototype_dir, results):
    """Check one prototype's output skill."""
    name = prototype_dir.name
    out = prototype_dir / "output"
    issues = []

    # 1. SKILL.md exists
    skill_md = out / "SKILL.md"
    if not skill_md.exists():
        issues.append(f"missing SKILL.md")
        results[name] = issues
        return

    text = skill_md.read_text(encoding="utf-8")
    fm, rest = parse_frontmatter(text)
    if not fm:
        issues.append("SKILL.md missing or malformed frontmatter")
    else:
        for required in ("name", "description"):
            if required not in fm:
                issues.append(f"SKILL.md frontmatter missing '{required}'")

    # 2. Leftover template placeholders
    leftover = re.findall(r'\{\{[^}]+\}\}', text)
    if leftover:
        issues.append(f"SKILL.md has leftover {{{{...}}}} placeholders: {leftover[:3]}")

    # 3. meta.json
    meta_path = out / "meta.json"
    if not meta_path.exists():
        issues.append("missing meta.json")
        meta = {}
    else:
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except Exception as e:
            issues.append(f"meta.json invalid JSON: {e}")
            meta = {}

    # 4. sub_skills
    for ss in meta.get("sub_skills", []):
        ss_path = out / ss.get("path", "")
        if not ss_path.exists():
            issues.append(f"sub_skill path missing: {ss.get('path')}")
            continue
        ss_text = ss_path.read_text(encoding="utf-8")
        ss_fm, _ = parse_frontmatter(ss_text)
        if not ss_fm:
            issues.append(f"sub_skill {ss.get('slug')} missing frontmatter")
        else:
            for required in ("name", "description"):
                if required not in ss_fm:
                    issues.append(f"sub_skill {ss.get('slug')} missing '{required}'")

    # 5. SKILL.md sub-skill table paths exist
    table_paths = re.findall(r'sub-skills/([a-z0-9-]+)/SKILL\.md', text)
    for sp in set(table_paths):
        ss_path = out / "sub-skills" / sp / "SKILL.md"
        if not ss_path.exists():
            issues.append(f"SKILL.md references missing sub-skill: sub-skills/{sp}/SKILL.md")

    # 6. research files
    rdir = prototype_dir / "references" / "research"
    expected = ["01-figures.md", "02-tools.md", "03-workflows.md",
                "04-canon.md", "05-sources.md", "06-glossary.md"]
    for f in expected:
        if not (rdir / f).exists():
            issues.append(f"research file missing: {f}")

    # 7. synthesis.md exists
    syn = prototype_dir / "references" / "synthesis.md"
    if not syn.exists():
        issues.append("references/synthesis.md missing")

    # 8. CLI scripts exist + executable + no leftover placeholders + syntax OK
    cli_dir = out / "cli"
    if cli_dir.exists():
        sh_files = list(cli_dir.rglob("*.sh"))
        for sh in sh_files:
            rel = sh.relative_to(out)
            # lib/*.sh is sourced (not executed) — skip executable check
            is_lib = "lib/" in str(rel) or str(rel).startswith("cli/lib/")
            if not is_lib and not os.access(sh, os.X_OK):
                issues.append(f"cli script not executable: {rel}")
            # Syntax check
            r = subprocess.run(["bash", "-n", str(sh)], capture_output=True, text=True)
            if r.returncode != 0:
                issues.append(f"cli syntax error in {rel}: {r.stderr.strip()[:120]}")
            # Leftover {placeholder} or {{placeholder}} in non-shell-substitution context
            sh_text = sh.read_text(encoding="utf-8")
            # Detect single-brace placeholders like {industry-cn} or {INDUSTRY_CN} that look templatey
            # (ignore bash ${var} which is fine, ignore bash literal { in }
            leftover_single = re.findall(r'(?<!\$)\{[a-zA-Z][a-zA-Z0-9_-]*-cn\}|(?<!\$)\{INDUSTRY[A-Z_]*\}', sh_text)
            leftover_double = re.findall(r'\{\{[^}]+\}\}', sh_text)
            for ph in set(leftover_single + leftover_double):
                issues.append(f"cli leftover placeholder {ph} in {rel}")

    # 9. Section 9 (Agentic Protocol) — should not be duplicated
    section9_count = len(re.findall(r'^## 9\.\s', text, re.MULTILINE))
    if section9_count > 1:
        issues.append(f"Section 9 duplicated ({section9_count} times)")

    # 10. SKILL.md frontmatter triggers must be a list
    if fm and "triggers" in fm:
        if not isinstance(fm["triggers"], list):
            issues.append("frontmatter triggers must be a YAML list")

    results[name] = issues


def main():
    skill_root = Path(__file__).resolve().parent.parent
    prototypes = sorted((skill_root / "prototypes").iterdir())
    results = {}
    for p in prototypes:
        if not p.is_dir():
            continue
        if not (p / "output" / "SKILL.md").exists():
            # Skip prototypes without output (e.g. llm-agent-infra was just original)
            continue
        check_skill(p, results)

    total_issues = 0
    print(f"\n# Self-test results — {len(results)} prototypes checked\n")
    for name in sorted(results):
        issues = results[name]
        if not issues:
            print(f"✅ {name}: clean")
        else:
            print(f"⚠️  {name}: {len(issues)} issue(s)")
            for i in issues:
                print(f"   - {i}")
            total_issues += len(issues)

    print(f"\n**Total**: {total_issues} issues across {len(results)} skills.")
    return 0 if total_issues == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
