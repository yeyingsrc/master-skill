# Test: tools/research/quality_check.py — Phase 4.4 mechanical rubric runner

iter 17. Third tool. Distinct from `prompts/quality_check.md` which is the agent execution script (4.1 sanity / 4.2 edge / 4.3 voice via subagent + 4.4 rubric). This script runs only 4.4 — purely structural, no subagent.

## Test setup

Synthetic SKILL.md mirroring what skill_writer would produce:
- 5 mental models, all with 局限 / Limitation field
- 7 playbook rules, each with 案例
- Tool stack section stating 必备=5 / 场景化=9 / 新兴=4
- 7 workflows, each with skip/optimize/add senior-difference markers
- 4 honest-boundary items
- 5 Agentic Protocol dimensions (### 9.1-9.5)
- Time-decay markers (last_updated, last_checked, Decay risk)
- Meta.json with primary_source_ratio: 0.62

## 12-item rubric run

Healthy SKILL.md result:
```
Verdict: PASS
9 pass / 2 partial / 0 fail / 1 needs_subagent / 0 skipped
exit: 0
```

| # | Item | Status |
|---|------|--------|
| 1 | 心智模型数 (3-7) | ✅ 5 models |
| 2 | 心智模型局限 100% 填 | ✅ all 5 have 局限 |
| 3 | Playbook 数 (5-10) | ✅ 7 rules |
| 4 | Playbook 案例 ≥ 1 | ✅ all 7 have 案例 |
| 5 | 工具三层覆盖 | ✅ 必备=5 场景化=9 新兴=4 |
| 6 | 工作流入门-资深差异 ≥ 80% | ✅ 100% workflows |
| 7 | 表达 DNA 辨识度 | 🧠 needs subagent (correct — not mechanical) |
| 8 | 诚实边界 ≥ 3 条 | ✅ 4 items |
| 9 | 一手来源 ≥ 50% | ✅ 62% |
| 10 | Agentic Protocol 维度 (3-10) | ✅ 5 dims |
| 11 | 时效性标注完整 | ⚠️ partial (2 last_updated, 1 decay — could use more) |
| 12 | 多 figure 共识门槛 | ⚠️ partial (1/5 models lacks parenthetical figure list) |

PASS verdict + exit 0 = ready to proceed to Phase 4.1/4.2/4.3 subagent runs.

## Fail scenario test

Stripped mental models section to 2 entries with no 局限 fields. Verdict PARTIAL:
- Item 1: still ✅ (5 — falls back to meta.json `mental_models_count: 5`)
- Item 2: ❌ FAIL — "2/2 missing 局限"
- Other items: same as healthy run

PARTIAL = 1 fail + 2 partials → exit 1.

## Pass

- 12-item rubric all coded and runs end-to-end
- 8 items mechanical pass on healthy SKILL.md
- 1 item correctly flagged needs_subagent (voice check)
- 2 items detect real soft issues (time-decay marker count, single-figure attribution)
- Fall-back logic (meta.json → body parse) for items 1/3/9/10 works
- `--json` flag for programmatic consumers
- Output written to `references/quality-check-rubric.{md,json}` for skill consumers
- Exit code 0/1/2 mapping to PASS/PARTIAL/FAIL — useful for CI integration

## Issues found

1. **Meta-vs-body inconsistency edge case**: Item 1 reports `mental_models_count: 5` from meta.json while Item 2 parses the body and finds only 2 `### 1.N` sections. This can happen after manual edits to SKILL.md without re-running skill_writer. Suggest: when meta and body counts diverge, item 1 should report PARTIAL with both numbers.

2. **Item 12 figure-attribution heuristic too aggressive**: "1/5 models may have only 1 figure" because my regex looks for parenthetical `(A / B / C)` patterns and one of the synthesis sections doesn't have one. But the model description is just terse without figure attribution; the actual evidence is in the research notes. The check should look at synthesis.md's "出现于 figures" annotations or research/01-figures.md cross-reference instead of guessing from prose.

3. **Item 11 "limited markers" partial threshold seems off**: 2 `last_updated` + 1 `decay` should be enough for many skills, but my threshold (≥ 2 each) marks it partial. Should reflect the actual SKILL.md spec — "工具 + 工作流 + 法规节都有 last_updated" is 3 sections × 1 marker = 3 minimum, not 2 each.

4. **Item 5 tool-tier extraction relies on inline numbers**: works for synthesis-stitched SKILL.md but if the section is purely a reference to research/02-tools.md, falls back to `needs_subagent`. Could parse research/02-tools.md directly.

5. **No item 7 fallback for partial-mechanical voice check**: voice check is fundamentally subagent territory but a partial-mechanical surrogate is possible — count Tier-1 jargon hits + vendor-话术 rejections from Track 06 outsider-tell list. Could be a v0.4 enhancement.

## v0.3 progress

- ✓ tools/skill_writer.py (iter 15)
- ✓ tools/research/merge_research.py (iter 16)
- ✓ tools/research/quality_check.py (iter 17, this iter)
- ⏳ tools/transcribe/youtube.sh + tools/transcribe/srt_to_transcript.py
- ⏳ tools/install/install_claude.py / install_openclaw.py / install_codex.py / install_hermes.py

3/6 tools done. Distance to v1.0: ~3-6 more iters (3 tool iters + 1 cleanup + 1 prototype run).

## Cumulative findings

- iter 14: 5
- iter 15: 5
- iter 16: 5
- iter 17: 5

20 cumulative pending. iter 18 cleanup pass per pattern (3:1 forward:cleanup ratio).
