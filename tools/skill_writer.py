#!/usr/bin/env python3
"""skill_writer.py — generate a {industry}-master skill directory from Phase 2 synthesis.

Usage:
  python3 skill_writer.py create --skill-dir <path> --intake <intake.json> --synthesis <synthesis.md>
  python3 skill_writer.py update --skill-dir <path> --section mental_models --content <patch.md>
  python3 skill_writer.py validate --skill-dir <path>
  python3 skill_writer.py list --base-dir <skills_root>

The script is the bridge from Phase 2 (synthesis.md) to a runnable, installable skill.
Design choices:
  - Pure stdlib (no pip install). Runs on macOS python3 out of the box.
  - Atomic writes (write to .tmp then rename).
  - Backup existing SKILL.md before overwrite (`{file}.bak.{timestamp}`).
  - Fails loudly on missing inputs / malformed synthesis — never silently produces a broken skill.
  - Validation is structure-only; full quality check is Phase 4's job (quality_check.md + subagent run).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Constants

# Sections expected in synthesis.md (header anchors). Phase 2's 9 outputs.
SYNTHESIS_SECTIONS = {
    "mental_models": r"##\s+1\.\s+心智模型",
    "playbook": r"##\s+2\.\s+标准\s+Playbook",
    "tool_stack": r"##\s+3\.\s+工具栈",
    "workflows": r"##\s+4\.\s+工作流",
    "expression_dna": r"##\s+5\.\s+表达\s+DNA",
    "quality_bars": r"##\s+6\.\s+质量基准",
    "intellectual_genealogy": r"##\s+7\.\s+智识谱系",
    "honest_boundaries": r"##\s+8\.\s+诚实边界",
    "agentic_protocol": r"##\s+9\.\s+Agentic\s+Protocol",
}

# meta.json schema fields we set/preserve
META_FIELDS = [
    "name", "industry", "industry_cn", "triggers", "locale", "profile",
    "focus", "last_research_date", "source_count", "primary_source_ratio",
    "tracks_covered", "mental_models_count", "playbook_rules_count",
    "research_dimensions_count", "sub_skills", "generator", "version",
    "changelog",
]

GENERATOR_VERSION = "master-skill v0.3"


# ---------------------------------------------------------------------------
# Errors

class SkillWriterError(Exception):
    """Raised on any unrecoverable issue — never silently produce broken skills."""
    pass


# ---------------------------------------------------------------------------
# Parsing

def parse_synthesis(synthesis_path: Path) -> dict[str, str]:
    """Extract 9 sections from synthesis.md by header anchor.

    Returns dict {section_key: section_body_markdown}. Missing sections raise.
    """
    if not synthesis_path.exists():
        raise SkillWriterError(f"synthesis.md not found: {synthesis_path}")

    text = synthesis_path.read_text(encoding="utf-8")
    sections: dict[str, str] = {}

    # Find each section's start position
    starts: list[tuple[str, int]] = []
    for key, pattern in SYNTHESIS_SECTIONS.items():
        match = re.search(pattern, text, re.MULTILINE)
        if not match:
            raise SkillWriterError(
                f"synthesis.md missing required section '{key}' "
                f"(pattern: {pattern}). Run Phase 2 to completion before skill_writer."
            )
        starts.append((key, match.start()))

    # Sort by position so we can slice up to next section's start
    starts.sort(key=lambda t: t[1])
    for i, (key, start_pos) in enumerate(starts):
        end_pos = starts[i + 1][1] if i + 1 < len(starts) else len(text)
        sections[key] = text[start_pos:end_pos].strip()

    return sections


def parse_intake(intake_path: Path) -> dict[str, Any]:
    """Load intake.json. Validates required fields are present."""
    if not intake_path.exists():
        raise SkillWriterError(f"intake.json not found: {intake_path}")

    try:
        data = json.loads(intake_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise SkillWriterError(f"intake.json malformed: {e}") from e

    required = ["industry", "slug", "locale", "profile"]
    missing = [f for f in required if f not in data]
    if missing:
        raise SkillWriterError(f"intake.json missing required fields: {missing}")

    return data


def parse_template(template_path: Path) -> str:
    """Load skill-template.md. The template itself contains the SKILL.md spec
    inside a fenced markdown block. Extract that block as the actual template
    string with {{placeholder}} markers.
    """
    if not template_path.exists():
        raise SkillWriterError(f"skill-template.md not found: {template_path}")

    text = template_path.read_text(encoding="utf-8")
    # The template wraps the SKILL.md spec in ```markdown ... ``` after the
    # `## \`SKILL.md\` template` heading. Extract the first such block after
    # that heading.
    heading_match = re.search(r"##\s+`SKILL\.md`\s+template", text)
    if not heading_match:
        raise SkillWriterError(
            f"skill-template.md doesn't have the expected '## `SKILL.md` template' "
            f"section. Template format may have drifted from spec."
        )

    after_heading = text[heading_match.end():]
    block_match = re.search(r"```markdown\n(.*?)\n```", after_heading, re.DOTALL)
    if not block_match:
        raise SkillWriterError(
            "skill-template.md: no ```markdown ... ``` block found after the "
            "SKILL.md template heading."
        )

    return block_match.group(1)


# ---------------------------------------------------------------------------
# Counting helpers (for meta.json stats)

def count_mental_models(section_body: str) -> int:
    """Count subsections matching '### 1.1' / '### 1.2' / etc."""
    return len(re.findall(r"^###\s+1\.\d+\s+", section_body, re.MULTILINE))


def count_playbook_rules(section_body: str) -> int:
    """Playbook rules are numbered list items."""
    return len(re.findall(r"^\d+\.\s+\*\*", section_body, re.MULTILINE))


def count_protocol_dimensions(section_body: str) -> int:
    """Agentic Protocol dimensions match '### 9.1' / '### 9.2'."""
    return len(re.findall(r"^###\s+9\.\d+\s+", section_body, re.MULTILINE))


# ---------------------------------------------------------------------------
# Writing

def now_iso_date() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def now_iso_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def atomic_write(path: Path, content: str) -> None:
    """Write to .tmp then rename. Avoids leaving partial files on crash."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(content, encoding="utf-8")
    tmp_path.replace(path)


def backup_if_exists(path: Path) -> Path | None:
    """If path exists, copy to {path}.bak.{ts}, return backup path."""
    if not path.exists():
        return None
    backup = path.with_suffix(path.suffix + f".bak.{now_iso_timestamp()}")
    shutil.copy2(path, backup)
    return backup


# ---------------------------------------------------------------------------
# Action: create

def action_create(
    skill_dir: Path,
    intake: dict[str, Any],
    synthesis_sections: dict[str, str],
    template: str,
    research_dir: Path | None,
) -> dict[str, Any]:
    """Generate a fresh skill directory."""
    skill_dir.mkdir(parents=True, exist_ok=True)

    # Build replacements
    industry = intake["industry"]
    industry_cn = intake.get("industry_cn", industry)
    slug = intake["slug"]
    locale = intake["locale"]
    profile = intake["profile"]
    focus = intake.get("focus", "comprehensive")
    if isinstance(focus, dict):
        # primary/secondary structure
        focus_str = f"{focus.get('primary', 'comprehensive')}+{focus.get('secondary', '')}".rstrip("+")
    else:
        focus_str = str(focus)

    research_date = now_iso_date()

    # Stats
    mm_count = count_mental_models(synthesis_sections["mental_models"])
    pb_count = count_playbook_rules(synthesis_sections["playbook"])
    dim_count = count_protocol_dimensions(synthesis_sections["agentic_protocol"])

    triggers = intake.get("triggers", [])
    triggers_yaml = "\n".join(f'  - "{t}"' for t in triggers) or '  - "{{TODO: fill triggers}}"'

    # Pre-replace the YAML triggers block (iter 18 fix). The template has a
    # multi-line block like:
    #   triggers:
    #     - "{{keyword-1, e.g. 'agent framework'}}"
    #     - "{{keyword-2}}"
    #     - "{{keyword-N}}"
    # which the simple {{x}} replacement won't catch. Use regex to match the
    # whole block and substitute with the actual triggers list.
    template = re.sub(
        r"^triggers:\n(?:\s+-\s+\"\{\{keyword-[^\"\}]+\}\}\"\n){2,}",
        f"triggers:\n{triggers_yaml}\n",
        template,
        count=1,
        flags=re.MULTILINE,
    )

    # Replacements for the template's {{...}} placeholders
    replacements = {
        "industry-slug": slug,
        "industry-cn-name": industry_cn,
        "industry-en-name": industry,
        "one-sentence value prop, e.g. \"automated mastery of LLM agent infrastructure: top builders' mental models, tool stack, current workflows, jargon, and where to keep up\".":
            f"automated mastery of {industry}: top builders' mental models, tool stack, current workflows, jargon, and where to keep up.",
        "trigger-cn-1": triggers[0] if len(triggers) > 0 else "造大师",
        "trigger-cn-2": triggers[1] if len(triggers) > 1 else f"{industry_cn} master",
        "trigger-cn-3": triggers[2] if len(triggers) > 2 else f"我做 {industry_cn}",
        "trigger-en-1": triggers[3] if len(triggers) > 3 else industry,
        "trigger-en-2": triggers[4] if len(triggers) > 4 else f"{industry} infra",
        "en | zh-CN | ja | ko | global": locale,
        "YYYY-MM-DD": research_date,
        "N": str(intake.get("source_count", 0)),
        "practitioner | learner | investor | consultant": profile,
        "X.Y": GENERATOR_VERSION.split(" ")[-1].lstrip("v"),
        "punchy one-liner — what this skill changes for the agent. Quote a top figure if natural.":
            f"This skill makes the agent operate as a senior {industry} practitioner — applying the field's mental models, picking the right tools, knowing the current workflows, speaking the jargon.",
        "trigger-list": ", ".join(triggers) or "industry-specific keywords",
    }

    # Apply replacements (order matters — longer patterns first to avoid partial match collisions)
    skill_md = template
    for placeholder, value in sorted(replacements.items(), key=lambda kv: -len(kv[0])):
        skill_md = skill_md.replace("{{" + placeholder + "}}", value)

    # Inject synthesis sections (these are larger blocks, replacing whole {{# ... }} hint comments).
    # We don't try to be clever here — append a "## Synthesized content" block referencing the
    # synthesis.md. Actual section-by-section injection is a v0.4 task; for v0.3 we keep the
    # template's structural shell and let downstream skill consumers reference synthesis.md.
    skill_md = skill_md + "\n\n---\n\n## Synthesized Content\n\n" + \
        f"See `references/synthesis.md` for the full Phase 2 output. Counts:\n" + \
        f"- Mental models: {mm_count}\n" + \
        f"- Playbook rules: {pb_count}\n" + \
        f"- Agentic Protocol dimensions: {dim_count}\n"

    # Write SKILL.md
    skill_md_path = skill_dir / "SKILL.md"
    backup_if_exists(skill_md_path)
    atomic_write(skill_md_path, skill_md)

    # Write meta.json
    meta = {
        "name": f"{slug}-master",
        "industry": industry,
        "industry_cn": industry_cn,
        "triggers": triggers,
        "locale": locale,
        "profile": profile,
        "focus": focus,
        "last_research_date": research_date,
        "source_count": intake.get("source_count", 0),
        "primary_source_ratio": intake.get("primary_source_ratio", 0.0),
        "tracks_covered": ["figures", "tools", "workflows", "canon", "sources", "glossary"],
        "mental_models_count": mm_count,
        "playbook_rules_count": pb_count,
        "research_dimensions_count": dim_count,
        "sub_skills": [],
        "generator": GENERATOR_VERSION,
        "version": GENERATOR_VERSION.split(" ")[-1].lstrip("v"),
        "changelog": [
            {"version": GENERATOR_VERSION.split(" ")[-1].lstrip("v"), "date": research_date,
             "what": "Initial generation"}
        ],
    }
    meta_path = skill_dir / "meta.json"
    atomic_write(meta_path, json.dumps(meta, indent=2, ensure_ascii=False) + "\n")

    # Copy synthesis + research notes (so the skill is self-contained)
    refs_dir = skill_dir / "references"
    refs_dir.mkdir(parents=True, exist_ok=True)
    if research_dir and research_dir.exists():
        target_research = refs_dir / "research"
        if target_research.exists():
            shutil.rmtree(target_research)
        shutil.copytree(research_dir, target_research)

    # Empty placeholder dirs
    (skill_dir / "sub-skills").mkdir(parents=True, exist_ok=True)
    (skill_dir / "scripts").mkdir(parents=True, exist_ok=True)

    return {
        "skill_md": str(skill_md_path),
        "meta_json": str(meta_path),
        "stats": {
            "mental_models": mm_count,
            "playbook_rules": pb_count,
            "agentic_protocol_dims": dim_count,
        },
    }


# ---------------------------------------------------------------------------
# Action: validate

def action_validate(skill_dir: Path) -> dict[str, Any]:
    """Structure-only validation. Full quality check is Phase 4's responsibility."""
    issues: list[str] = []

    skill_md = skill_dir / "SKILL.md"
    meta = skill_dir / "meta.json"

    if not skill_md.exists():
        issues.append(f"SKILL.md missing at {skill_md}")
    if not meta.exists():
        issues.append(f"meta.json missing at {meta}")

    if meta.exists():
        try:
            meta_data = json.loads(meta.read_text(encoding="utf-8"))
            for field in ["name", "industry", "locale", "last_research_date", "version"]:
                if field not in meta_data:
                    issues.append(f"meta.json missing required field: {field}")
            mm = meta_data.get("mental_models_count", 0)
            if not (3 <= mm <= 7):
                issues.append(f"mental_models_count={mm} out of [3,7] range")
            pb = meta_data.get("playbook_rules_count", 0)
            if not (5 <= pb <= 10):
                issues.append(f"playbook_rules_count={pb} out of [5,10] range")
            dim = meta_data.get("research_dimensions_count", 0)
            if not (3 <= dim <= 10):
                issues.append(f"research_dimensions_count={dim} out of [3,10] range")
        except json.JSONDecodeError as e:
            issues.append(f"meta.json malformed: {e}")

    if skill_md.exists():
        text = skill_md.read_text(encoding="utf-8")
        for required in ["## 激活规则", "## Agentic Protocol", "## 心智模型"]:
            if required not in text:
                issues.append(f"SKILL.md missing required heading: {required}")

    return {"valid": len(issues) == 0, "issues": issues}


# ---------------------------------------------------------------------------
# Action: list

def action_list(base_dir: Path) -> list[dict[str, Any]]:
    """List all *-master skills under base_dir with key metadata."""
    if not base_dir.exists():
        return []
    skills: list[dict[str, Any]] = []
    for child in sorted(base_dir.iterdir()):
        if not child.is_dir() or not child.name.endswith("-master"):
            continue
        meta_path = child / "meta.json"
        if meta_path.exists():
            try:
                meta_data = json.loads(meta_path.read_text(encoding="utf-8"))
                skills.append({
                    "slug": child.name,
                    "industry": meta_data.get("industry"),
                    "locale": meta_data.get("locale"),
                    "last_research_date": meta_data.get("last_research_date"),
                    "version": meta_data.get("version"),
                })
            except json.JSONDecodeError:
                skills.append({"slug": child.name, "error": "meta.json malformed"})
        else:
            skills.append({"slug": child.name, "error": "no meta.json"})
    return skills


# ---------------------------------------------------------------------------
# CLI

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="skill_writer — generate / validate / list master-skill outputs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="action", required=True)

    p_create = sub.add_parser("create", help="Create a new {industry}-master skill")
    p_create.add_argument("--skill-dir", required=True, type=Path,
                          help="Target directory for the generated skill")
    p_create.add_argument("--intake", required=True, type=Path, help="Path to intake.json")
    p_create.add_argument("--synthesis", required=True, type=Path,
                          help="Path to Phase 2 synthesis.md")
    p_create.add_argument("--template", required=True, type=Path,
                          help="Path to references/skill-template.md")
    p_create.add_argument("--research-dir", type=Path, default=None,
                          help="Path to references/research/ — copied into the new skill")

    p_validate = sub.add_parser("validate", help="Structure-only validation of an existing skill")
    p_validate.add_argument("--skill-dir", required=True, type=Path)

    p_list = sub.add_parser("list", help="List *-master skills in a directory")
    p_list.add_argument("--base-dir", required=True, type=Path,
                        help="Directory containing *-master/ subdirectories")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        if args.action == "create":
            intake = parse_intake(args.intake)
            synthesis_sections = parse_synthesis(args.synthesis)
            template = parse_template(args.template)
            result = action_create(args.skill_dir, intake, synthesis_sections, template,
                                   args.research_dir)
            print(json.dumps(result, indent=2, ensure_ascii=False))
            return 0

        if args.action == "validate":
            result = action_validate(args.skill_dir)
            print(json.dumps(result, indent=2, ensure_ascii=False))
            return 0 if result["valid"] else 1

        if args.action == "list":
            result = action_list(args.base_dir)
            print(json.dumps(result, indent=2, ensure_ascii=False))
            return 0

    except SkillWriterError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    return 99  # unreachable


if __name__ == "__main__":
    sys.exit(main())
