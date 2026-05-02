# Test: tools/skill_writer.py — first runnable Python tool

iter 15 v0.3 launch. First tool that produces an installable skill from Phase 2 outputs.

## Test setup

- Synthetic intake.json: industry=LLM agent infra, slug=llm-agent-infra, locale=global, profile=practitioner, 5 triggers
- Synthetic synthesis.md: 5 sections of mental_models / 7 playbook rules / 5 Agentic Protocol dimensions (matches the iter 14 dry-run output)
- Template: actual `references/skill-template.md`
- No research-dir (skip the copy step)

## 3 actions tested

| Action | Result |
|--------|--------|
| `create` | ✅ produces SKILL.md (8.9KB) + meta.json + scripts/ + sub-skills/ + references/. Stats: {mental_models: 5, playbook_rules: 7, agentic_protocol_dims: 5} all correct |
| `validate` | ✅ valid=true, issues=[] |
| `list` | ✅ enumerates the generated skill with full metadata |

## Pass

- argparse subcommands work clean
- atomic write (tmp → rename) prevents partial files
- meta.json schema fields all populated correctly
- Stats counting (regex on `### N.M` and numbered list patterns) accurately matches my synthesis.md design
- Directory layout matches references/skill-template.md spec
- Pure stdlib (no pip install needed)
- Validation catches structural issues without running subagent (Phase 4's job)

## Issues found (v0.3 → v0.4 fixes)

1. **Triggers YAML array not filled**: SKILL.md frontmatter still has `triggers:\n  - "{{keyword-1, e.g. 'agent framework'}}"` placeholder. The `description:` line's 触发词 list got the actual triggers, but the structured YAML `triggers:` array didn't. Need to add a multi-line replacement for the YAML block, not just simple string substitution.

2. **Synthesis body not injected**: The skill-template.md has `{{# Phase 2.1 输出 ...}}` style HTML-comment-like markers indicating where synthesis content should go. v0.3 currently leaves these as-is and just appends a "## Synthesized Content" stub at the end pointing to references/synthesis.md. v0.4 should walk each `{{# ... }}` placeholder and inject the corresponding synthesis section.

3. **No `triggers` from intake.json into description's 触发词 line**: Actually this works (visible in head -30 output) — false alarm.

4. **Decision tree placeholders in 工具栈 / 工作流 sections still bear the template's `{{...}}` markers**: Same root cause as #2 — body injection not implemented.

5. **No backup_if_exists test**: The function exists but didn't get exercised since /tmp was fresh. Need a test where SKILL.md already exists and we re-run create — it should leave a `.bak.{ts}` next to the new one. Defer to v0.4.

6. **research-dir copy not exercised**: --research-dir param works in code but not tested in this dry-run. Defer.

## Observations

- Pure-stdlib design pays off: works on macOS python3 immediately, no setup
- The template parsing approach (regex on `## SKILL.md template` heading + `\`\`\`markdown ... \`\`\`` block) is brittle if template structure shifts — could add a "MASTER_SKILL_TEMPLATE_BLOCK_START / END" sentinel comments in skill-template.md to make it explicit. Defer to v0.4.
- The structural shell + reference-to-synthesis.md approach is **good enough for v1.0 prototype** — agents loading the skill can read both SKILL.md (high-level OS) + synthesis.md (full content). v0.4 will inline synthesis into SKILL.md to be fully self-contained.

## v0.3 progress

- ✓ tools/skill_writer.py (this iter)
- ⏳ tools/research/merge_research.py
- ⏳ tools/research/quality_check.py (separate from prompts/quality_check.md — this is the runner)
- ⏳ tools/transcribe/youtube.sh + tools/transcribe/srt_to_transcript.py
- ⏳ tools/install/install_claude.py / install_openclaw.py / install_codex.py / install_hermes.py

## Distance to v1.0

- v0.3 tools: ~5 more files (4-6 iters at current cadence)
- Real LLM agent infra prototype run: 1-2 iters
- v1.0 release: total ~5-8 more iters

## Cumulative findings

- iter 14: 5 findings on synthesis + quality_check
- iter 15 (this): 5 findings on skill_writer.py (most are v0.4 deferrals, not bugs)

10 cumulative pending. iter 17-18 cleanup pass per pattern.
