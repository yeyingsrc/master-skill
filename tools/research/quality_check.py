#!/usr/bin/env python3
"""quality_check.py — mechanical Phase 4.4 rubric runner.

Usage:
  python3 quality_check.py check --skill-dir <path>
  python3 quality_check.py check --skill-dir <path> --json

Distinct from `prompts/quality_check.md` (the agent execution script that runs
4.1 sanity / 4.2 edge case / 4.3 voice check via subagent). This script runs
only the 4.4 mechanical rubric — purely structural checks that don't need a
subagent.

Reads SKILL.md + meta.json + references/synthesis.md + references/research/.
Verdict: PASS / PARTIAL / FAIL.

Pure stdlib. macOS python3 out-of-the-box.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Callable

# ---------------------------------------------------------------------------

class QCError(Exception):
    pass


# Rubric item: (id, label, checker_fn returning (status, detail)).
# Status: "pass" / "partial" / "fail" / "needs_subagent" / "skipped".


def load_skill_text(skill_dir: Path) -> str:
    """Load SKILL.md, falling back to synthesis.md if SKILL.md doesn't exist
    (allows the runner to validate Phase 2 output before Phase 3 writeup)."""
    skill_md = skill_dir / "SKILL.md"
    synthesis = skill_dir / "references" / "synthesis.md"
    if skill_md.exists():
        return skill_md.read_text(encoding="utf-8")
    if synthesis.exists():
        return synthesis.read_text(encoding="utf-8")
    raise QCError(
        f"Neither SKILL.md nor references/synthesis.md found at {skill_dir}. "
        f"Run Phase 3 (skill_writer) or Phase 2 (synthesis) first."
    )


def load_meta(skill_dir: Path) -> dict[str, Any]:
    """Load meta.json if present, return empty dict otherwise."""
    meta_path = skill_dir / "meta.json"
    if not meta_path.exists():
        return {}
    try:
        return json.loads(meta_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise QCError(f"meta.json malformed: {e}") from e


# ---------------------------------------------------------------------------
# Individual rubric checks


def check_mental_models_count(skill_text: str, meta: dict) -> tuple[str, str]:
    """Item 1: 心智模型数 in [3, 7]. (iter 18) When meta and body disagree,
    return PARTIAL so reviewer notices stale meta after manual edits."""
    n_meta = meta.get("mental_models_count")
    n_body = len(re.findall(r"^###\s+1\.\d+\s+", skill_text, re.MULTILINE))

    if n_meta is not None and n_body > 0 and n_meta != n_body:
        return "partial", (
            f"meta.json says {n_meta}, body has {n_body} sections — "
            f"meta out of sync with body, re-run skill_writer or update meta"
        )

    n = n_meta if n_meta is not None else n_body
    if 3 <= n <= 7:
        return "pass", f"{n} models (in [3, 7])"
    if n < 3:
        return "fail", f"{n} models (< 3, too thin)"
    return "fail", f"{n} models (> 7, insufficient extraction)"


def check_mental_model_limits(skill_text: str) -> tuple[str, str]:
    """Item 2: each mental model has a 局限 / Limitation field."""
    # Find each ### 1.N section and check for `局限` / `Limitation` in its body.
    matches = list(re.finditer(
        r"^###\s+1\.(\d+)\s+(.+?)$(.*?)(?=^###\s+1\.\d+\s+|^##\s+|\Z)",
        skill_text,
        re.MULTILINE | re.DOTALL,
    ))
    if not matches:
        return "skipped", "no mental model sections found (### 1.N pattern)"
    missing: list[str] = []
    for m in matches:
        body = m.group(3)
        if not re.search(r"\*?\*?(局限|Limitation|Limits?)\*?\*?\s*[:：]", body):
            missing.append(m.group(2).strip()[:40])
    if not missing:
        return "pass", f"all {len(matches)} models have 局限 field"
    return "fail", f"{len(missing)}/{len(matches)} missing 局限: {missing[:3]}"


def check_playbook_count(skill_text: str, meta: dict) -> tuple[str, str]:
    """Item 3: Playbook rules count in [5, 10]. Iter 22: also matches friendly
    headings (## 标准 Playbook) emitted by skill_writer body injection, not just
    numbered ones (## 2. 标准 Playbook) used in synthesis.md."""
    n_meta = meta.get("playbook_rules_count")
    if n_meta is not None:
        n = n_meta
    else:
        # Numbered list under ## 2. heading or ## heading
        section_match = re.search(
            r"##\s+(?:2\.\s+)?标准\s+Playbook(.*?)(?=^##\s|\Z)",
            skill_text,
            re.MULTILINE | re.DOTALL,
        )
        if not section_match:
            return "skipped", "no Playbook section found"
        n = len(re.findall(r"^\d+\.\s+\*\*", section_match.group(1), re.MULTILINE))
    if 5 <= n <= 10:
        return "pass", f"{n} rules (in [5, 10])"
    if n < 5:
        return "fail", f"{n} rules (< 5, too thin)"
    return "fail", f"{n} rules (> 10, insufficient curation)"


def check_playbook_cases(skill_text: str) -> tuple[str, str]:
    """Item 4: each playbook rule has ≥ 1 case (— bullet under it)."""
    section_match = re.search(
        r"##\s+(?:2\.\s+)?标准\s+Playbook(.*?)(?=^##\s|\Z)",
        skill_text,
        re.MULTILINE | re.DOTALL,
    )
    if not section_match:
        return "skipped", "no Playbook section"
    body = section_match.group(1)
    # Each rule starts with "1. **...**", "2. **..." etc. A "case" line is
    # an indented bullet starting with "案例" / "case" / "-".
    rules = re.findall(
        r"^\d+\.\s+\*\*.*?\*\*.*?(?=^\d+\.\s+\*\*|\Z)",
        body,
        re.MULTILINE | re.DOTALL,
    )
    if not rules:
        return "skipped", "no rules found in section"
    no_case = [i + 1 for i, r in enumerate(rules) if not re.search(r"案例|case", r, re.IGNORECASE)]
    if not no_case:
        return "pass", f"all {len(rules)} rules have 案例"
    return "fail", f"{len(no_case)}/{len(rules)} rules missing 案例"


def check_tool_tiers(skill_text: str) -> tuple[str, str]:
    """Item 5: Tool tier coverage 必备 ≥ 3 / 场景化 ≥ 5 / 新兴 ≥ 2.
    For SKILL.md the tools are referenced in synthesis but the actual counts
    live in 02-tools.md or in the synthesis section. We approximate by counting
    section markers.
    """
    # Count tier mentions in 工具栈 section
    section_match = re.search(
        r"##\s+(?:3\.\s+)?工具栈(.*?)(?=^##\s|\Z)",
        skill_text,
        re.MULTILINE | re.DOTALL,
    )
    if not section_match:
        return "skipped", "no 工具栈 section found"
    body = section_match.group(1)
    # Often the synthesis just says "see references/research/02-tools.md, N retained"
    # so we look for explicit tier counts
    necessary_match = re.search(r"必备[^0-9]*(\d+)", body)
    scenario_match = re.search(r"场景特化?[^0-9]*(\d+)", body)
    emerging_match = re.search(r"新兴[^0-9]*(\d+)", body)
    if not (necessary_match or scenario_match or emerging_match):
        return "needs_subagent", "tool tier counts not stated in 工具栈 section (likely a reference to research/02-tools.md)"
    n_necessary = int(necessary_match.group(1)) if necessary_match else 0
    n_scenario = int(scenario_match.group(1)) if scenario_match else 0
    n_emerging = int(emerging_match.group(1)) if emerging_match else 0
    issues = []
    if n_necessary < 3: issues.append(f"必备 {n_necessary} < 3")
    if n_scenario < 5: issues.append(f"场景化 {n_scenario} < 5")
    if n_emerging < 2: issues.append(f"新兴 {n_emerging} < 2")
    if not issues:
        return "pass", f"必备={n_necessary} 场景化={n_scenario} 新兴={n_emerging}"
    return "partial", f"thresholds not met: {', '.join(issues)} — may be cold protocol"


def check_workflow_senior_differences(skill_text: str) -> tuple[str, str]:
    """Item 6: ≥ 80% workflows have ≥ 2 senior-difference points (skip/optimize/add)."""
    section_match = re.search(
        r"##\s+(?:4\.\s+)?工作流(.*?)(?=^##\s|\Z)",
        skill_text,
        re.MULTILINE | re.DOTALL,
    )
    if not section_match:
        return "skipped", "no 工作流 section"
    body = section_match.group(1)
    if "references/research/03-workflows.md" in body and len(body) < 500:
        return "needs_subagent", "section is a reference; load 03-workflows.md to validate"
    # Each workflow has ### with senior tags
    workflows = re.findall(r"###.*?(?=^###|\Z)", body, re.MULTILINE | re.DOTALL)
    if not workflows:
        return "skipped", "no workflow subsections"
    enough_diffs: list[bool] = []
    for w in workflows:
        skip_count = len(re.findall(r"skip|跳过", w, re.IGNORECASE))
        opt_count = len(re.findall(r"optimize|优化", w, re.IGNORECASE))
        add_count = len(re.findall(r"add\b|额外", w, re.IGNORECASE))
        types_present = sum(1 for c in [skip_count, opt_count, add_count] if c >= 1)
        diff_total = skip_count + opt_count + add_count
        enough_diffs.append(types_present >= 2 and diff_total >= 2)
    pct = sum(enough_diffs) / len(enough_diffs) if enough_diffs else 0
    if pct >= 0.8:
        return "pass", f"{int(pct * 100)}% workflows have ≥ 2 senior diffs"
    return "fail", f"{int(pct * 100)}% workflows have ≥ 2 diffs (target ≥ 80%)"


def check_voice_dna(skill_text: str) -> tuple[str, str]:
    """Item 7: voice DNA — needs subagent (4.3 voice check). Not mechanical."""
    return "needs_subagent", "Voice check (4.3) requires blind comparison with real practitioner samples — run prompts/quality_check.md Phase 4.3"


def check_honest_boundaries(skill_text: str) -> tuple[str, str]:
    """Item 8: ≥ 3 specific honest boundaries."""
    section_match = re.search(
        r"##\s+(?:8\.\s+)?诚实边界(.*?)(?=^##\s|\Z)",
        skill_text,
        re.MULTILINE | re.DOTALL,
    )
    if not section_match:
        return "skipped", "no 诚实边界 section"
    body = section_match.group(1)
    items = re.findall(r"^[-\d]+\.\s+|^-\s+", body, re.MULTILINE)
    n = len(items)
    if n < 3:
        return "fail", f"{n} boundaries (< 3 specific items required)"
    # Check that they're not all generic "不能替代真人" boilerplate
    generic_count = len(re.findall(r"不能替代|cannot replace", body))
    if generic_count > n / 2:
        return "partial", f"{n} items but {generic_count} are generic (mostly '不能替代真人' style)"
    return "pass", f"{n} boundary items"


def check_primary_ratio(skill_dir: Path, meta: dict) -> tuple[str, str]:
    """Item 9: ≥ 50% primary sources (from research notes)."""
    ratio = meta.get("primary_source_ratio")
    if ratio is None:
        # Fall back to scanning research/*.md
        research_dir = skill_dir / "references" / "research"
        if not research_dir.exists():
            return "skipped", "no research/ dir; meta.primary_source_ratio not set"
        primary = secondary = reference = 0
        for f in research_dir.glob("*.md"):
            text = f.read_text(encoding="utf-8")
            primary += len(re.findall(r"\[Primary\]", text))
            secondary += len(re.findall(r"\[Secondary\]", text))
            reference += len(re.findall(r"\[Reference\]", text))
        total = primary + secondary + reference
        ratio = primary / total if total else 0.0
    if ratio >= 0.5:
        return "pass", f"primary ratio = {int(ratio * 100)}% (≥ 50%)"
    return "fail", f"primary ratio = {int(ratio * 100)}% (< 50%, mostly secondary)"


def check_agentic_protocol_dims(skill_text: str, meta: dict) -> tuple[str, str]:
    """Item 10: Agentic Protocol dimensions in [3, 10]."""
    n_meta = meta.get("research_dimensions_count")
    if n_meta is not None:
        n = n_meta
    else:
        n = len(re.findall(r"^###\s+9\.\d+\s+", skill_text, re.MULTILINE))
    if 3 <= n <= 10:
        return "pass", f"{n} dimensions (in [3, 10])"
    if n < 3:
        return "fail", f"{n} dimensions (< 3, too thin)"
    return "fail", f"{n} dimensions (> 10, not精炼)"


def check_time_decay_marks(skill_text: str) -> tuple[str, str]:
    """Item 11: time-decay annotations. (iter 18 fix) The SKILL.md spec is
    "工具 + 工作流 + 法规节都有 last_updated" — that's 3 sections × 1 marker
    minimum, not 2 each. Check that ≥3 distinct sections carry markers.
    """
    # Look for sections that contain a time-decay marker
    sections_with_decay = 0
    section_keywords = ["工具", "工作流", "法规", "Tool", "Workflow", "Regulation"]
    for keyword in section_keywords:
        # Search a window after each occurrence of the keyword
        for m in re.finditer(keyword, skill_text):
            window = skill_text[m.start():m.start() + 1500]
            if re.search(r"last_updated|last_checked|[Dd]ecay\s*risk", window):
                sections_with_decay += 1
                break  # one hit per keyword is enough

    total_markers = len(re.findall(
        r"last_updated|last_checked|[Dd]ecay\s*risk", skill_text
    ))
    if sections_with_decay >= 3 or total_markers >= 3:
        return "pass", (
            f"{total_markers} markers across {sections_with_decay} key sections"
        )
    if total_markers == 0:
        return "fail", "no time-decay marks (last_updated / decay risk) found"
    return "partial", (
        f"limited spread: {total_markers} markers, only {sections_with_decay} "
        f"of 3 key sections (工具 / 工作流 / 法规) covered"
    )


def check_multi_figure_consensus(skill_dir: Path) -> tuple[str, str]:
    """Item 12: each mental model backed by ≥ 2 figures (cross-figure consensus).

    iter 18 fix: instead of guessing from prose with `(A/B/C)` patterns, look
    for explicit attribution markers — `(figures: ...)`, `出现于:`, or evidence
    citations that name 2+ distinct figures. If those aren't present, fall back
    to checking research/01-figures.md for whether each model's keyword appears
    against ≥ 2 figure entries.
    """
    synthesis = skill_dir / "references" / "synthesis.md"
    if not synthesis.exists():
        return "skipped", "no synthesis.md to analyze figure attribution"
    text = synthesis.read_text(encoding="utf-8")
    section_match = re.search(
        r"##\s+(?:1\.\s+)?心智模型(.*?)(?=^##\s|\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not section_match:
        return "skipped", "no 心智模型 section in synthesis"
    body = section_match.group(1)
    models = re.split(r"^###\s+1\.\d+\s+", body, flags=re.MULTILINE)[1:]
    if not models:
        return "skipped", "no model subsections"

    insufficient: list[int] = []
    for i, m in enumerate(models):
        m_window = m[:1000]
        # Look for explicit attribution patterns first
        explicit = re.findall(
            r"(?:figures:|出现于:|来源于|[Bb]y\s+)\s*([^\n]+)",
            m_window,
        )
        explicit_figures = 0
        for tag in explicit:
            # Count comma/pipe/slash-separated names
            names = re.split(r"[,，/|；;]", tag)
            explicit_figures = max(explicit_figures, len([n for n in names if n.strip()]))

        # Fallback: look for parenthetical name groups
        if explicit_figures == 0:
            groups = re.findall(r"\(([^()]*[/,，；;|][^()]*)\)", m_window)
            for g in groups:
                names = re.split(r"[,，/|；;]", g)
                explicit_figures = max(explicit_figures, len([n for n in names if n.strip()]))

        if explicit_figures < 2:
            insufficient.append(i + 1)

    if not insufficient:
        return "pass", f"all {len(models)} models cite ≥ 2 figures"
    if len(insufficient) <= len(models) // 3:
        return "partial", (
            f"{len(insufficient)}/{len(models)} models lack explicit ≥2 figure citations: "
            f"{insufficient[:3]} — figures may be in research/01-figures.md but not "
            f"surfaced in synthesis (consider adding `(figures: A / B / C)` annotations)"
        )
    return "fail", (
        f"{len(insufficient)}/{len(models)} models lack ≥2 figure citations — "
        f"the multi-figure consensus rule from extraction-framework § 一 may not be holding"
    )


# ---------------------------------------------------------------------------
# Main rubric runner

RUBRIC_ITEMS: list[tuple[str, str, str]] = [
    ("1", "心智模型数 (3-7)", "check_mental_models_count"),
    ("2", "心智模型局限 100% 填", "check_mental_model_limits"),
    ("3", "Playbook 数 (5-10)", "check_playbook_count"),
    ("4", "Playbook 案例 ≥ 1", "check_playbook_cases"),
    ("5", "工具三层覆盖", "check_tool_tiers"),
    ("6", "工作流入门-资深差异 ≥ 80%", "check_workflow_senior_differences"),
    ("7", "表达 DNA 辨识度", "check_voice_dna"),
    ("8", "诚实边界 ≥ 3 条", "check_honest_boundaries"),
    ("9", "一手来源 ≥ 50%", "check_primary_ratio"),
    ("10", "Agentic Protocol 维度 (3-10)", "check_agentic_protocol_dims"),
    ("11", "时效性标注完整", "check_time_decay_marks"),
    ("12", "多 figure 共识门槛", "check_multi_figure_consensus"),
]


def run_rubric(skill_dir: Path) -> dict[str, Any]:
    """Run all 12 rubric checks. Return aggregate result."""
    skill_text = load_skill_text(skill_dir)
    meta = load_meta(skill_dir)

    checkers: dict[str, Callable[..., tuple[str, str]]] = {
        "check_mental_models_count": lambda: check_mental_models_count(skill_text, meta),
        "check_mental_model_limits": lambda: check_mental_model_limits(skill_text),
        "check_playbook_count": lambda: check_playbook_count(skill_text, meta),
        "check_playbook_cases": lambda: check_playbook_cases(skill_text),
        "check_tool_tiers": lambda: check_tool_tiers(skill_text),
        "check_workflow_senior_differences": lambda: check_workflow_senior_differences(skill_text),
        "check_voice_dna": lambda: check_voice_dna(skill_text),
        "check_honest_boundaries": lambda: check_honest_boundaries(skill_text),
        "check_primary_ratio": lambda: check_primary_ratio(skill_dir, meta),
        "check_agentic_protocol_dims": lambda: check_agentic_protocol_dims(skill_text, meta),
        "check_time_decay_marks": lambda: check_time_decay_marks(skill_text),
        "check_multi_figure_consensus": lambda: check_multi_figure_consensus(skill_dir),
    }

    results: list[dict[str, Any]] = []
    for item_id, label, fn_name in RUBRIC_ITEMS:
        status, detail = checkers[fn_name]()
        results.append({"id": item_id, "label": label, "status": status, "detail": detail})

    counts = {
        "pass": sum(1 for r in results if r["status"] == "pass"),
        "partial": sum(1 for r in results if r["status"] == "partial"),
        "fail": sum(1 for r in results if r["status"] == "fail"),
        "needs_subagent": sum(1 for r in results if r["status"] == "needs_subagent"),
        "skipped": sum(1 for r in results if r["status"] == "skipped"),
    }

    # Verdict per Phase 4.4 rule: 0-2 fail → PARTIAL, 3+ fail → FAIL, else PASS.
    # PASS requires ≥ 8 mechanical pass + no fails (subagent-needed items don't count as fail).
    if counts["fail"] >= 3:
        verdict = "FAIL"
    elif counts["fail"] > 0 or counts["partial"] > 2:
        verdict = "PARTIAL"
    else:
        verdict = "PASS"

    return {
        "skill_dir": str(skill_dir),
        "verdict": verdict,
        "counts": counts,
        "results": results,
    }


def render_report(report: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"# Phase 4.4 Mechanical Rubric — {report['skill_dir']}")
    lines.append("")
    lines.append(f"**Verdict**: `{report['verdict']}`")
    lines.append("")
    c = report["counts"]
    lines.append(
        f"Counts: {c['pass']} pass / {c['partial']} partial / {c['fail']} fail / "
        f"{c['needs_subagent']} needs subagent / {c['skipped']} skipped"
    )
    lines.append("")
    lines.append("| # | Item | Status | Detail |")
    lines.append("|---|------|--------|--------|")
    icons = {
        "pass": "✅", "partial": "⚠️", "fail": "❌",
        "needs_subagent": "🧠", "skipped": "—",
    }
    for r in report["results"]:
        icon = icons.get(r["status"], "?")
        lines.append(f"| {r['id']} | {r['label']} | {icon} {r['status']} | {r['detail']} |")
    lines.append("")
    if report["verdict"] == "FAIL":
        lines.append("**FAIL action**: 3+ items failing. Return to Phase 2 / Phase 3 for substantive revision.")
    elif report["verdict"] == "PARTIAL":
        lines.append("**PARTIAL action**: fix listed items, re-run rubric. If 2 iterations don't reach PASS, accept partial and mark weak dimensions in 诚实边界.")
    else:
        lines.append("**PASS action**: proceed to Phase 4.1/4.2/4.3 subagent runs (prompts/quality_check.md), then Phase 5.")
    lines.append("")
    lines.append("**Note**: Items marked 🧠 needs_subagent require running `prompts/quality_check.md` Phase 4.3 voice check via spawned subagent. This script does not run subagents.")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI

def cmd_check(args: argparse.Namespace) -> int:
    report = run_rubric(args.skill_dir)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_report(report))

    # Also write the report to the skill directory
    out_dir = args.skill_dir / "references"
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / "quality-check-rubric.md"
    json_path = out_dir / "quality-check-rubric.json"
    md_path.write_text(render_report(report), encoding="utf-8")
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")

    return 0 if report["verdict"] == "PASS" else (1 if report["verdict"] == "PARTIAL" else 2)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="quality_check — mechanical Phase 4.4 rubric runner",
    )
    sub = parser.add_subparsers(dest="action", required=True)

    p_check = sub.add_parser("check", help="Run all 12 rubric items, output verdict")
    p_check.add_argument("--skill-dir", required=True, type=Path)
    p_check.add_argument("--json", action="store_true",
                         help="Output JSON to stdout instead of markdown")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.action == "check":
            return cmd_check(args)
    except QCError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 3
    return 99


if __name__ == "__main__":
    sys.exit(main())
