# Cleanup pass — iter 18 (2026-05-02)

iter 14-17 accumulated 20 findings. This pass clears 10 highest-leverage; 10 deferred to v0.4 polish.

## Files touched (5)

### `prompts/synthesis.md` (3 fixes)

1. **Industry-type-aware candidate floor** (iter 14 #3)
   New table: technical ≥15 / academic ≥12 / vertical ≥8 / regulated specialized ≥5. Replaces the rigid "≥15" minimum that broke for cold/闭源 industries.

2. **Step 3-4 relabeled "integration" not "synthesis"** (iter 14 #1)
   Phase 2 Step 3 工具栈 + Step 4 工作流 are direct consumes from Track 02/03, not extraction work. Title now reflects this so Phase 3 doesn't expect heavy synthesis work in these steps.

3. **Phase 5 entry condition** (iter 14 #5)
   Added explicit gate: Phase 5 入口 requires Phase 4 verdict ≥ PARTIAL + user confirmation in Phase 4 report. Phase 5 is polish, not substantive fix. FAIL → back to Phase 2/3.

### `prompts/quality_check.md` (2 fixes)

4. **Ground truth source spans Tracks 1+3+4** (iter 14 #2)
   4.1 sanity check: questions can come from Track 01 figures' direct answers (highest weight) / Track 03 workflows' explicit-X-then-Y / Track 04 canon's clear judgments. Was canon-only.

5. **Voice-check sample selection rule** (iter 14 #4)
   3 reference samples for 4.3 must be: 1 from Track 01 long interview transcript / 1 from Track 05 top podcast or newsletter (last 3 months) / 1 from Track 04 modern textbook chapter opening. Avoid SEO blogs and marketing.

### `tools/skill_writer.py` (1 fix — real bug)

6. **Triggers YAML array now populated** (iter 15 #1)
   Pre-process step uses regex to substitute the multi-line YAML block before simple `{{x}}` replacement. Tested: synthetic intake's 5 triggers correctly land as YAML array list items in the output frontmatter.

### `tools/research/merge_research.py` (1 fix)

7. **Per-track primary-ratio warning** (iter 16 #3)
   Quality gate now flags individual tracks with primary ratio < 40%, not just overall. Tested: 17%-primary track correctly listed as weak.

### `tools/research/quality_check.py` (3 fixes)

8. **Meta-vs-body inconsistency → PARTIAL with both numbers** (iter 17 #1)
   Item 1 (mental models count) now compares meta.json vs body parse. If they disagree, returns PARTIAL with "meta.json says X, body has Y sections — meta out of sync, re-run skill_writer or update meta". Was: silent fallback to meta.

9. **Item 12 (multi-figure consensus) heuristic improved** (iter 17 #2)
   Now looks for explicit attribution patterns (`figures:`, `出现于:`, `(A / B / C)`) instead of guessing from any prose containing slashes. Falls back to FAIL only if 1/3+ of models lack ≥2 figure citations; else PARTIAL with hint to add explicit annotations.

10. **Item 11 (time-decay) threshold reflects spec** (iter 17 #3)
    SKILL.md spec is "工具 + 工作流 + 法规节都有 last_updated" — 3 sections × 1 marker. Now passes with 3+ markers across these 3 sections, not 2 each. PARTIAL message describes which key sections are uncovered.

## Deferred to v0.4 (10 findings)

- iter 15 #2-5: synthesis body inline injection / backup test / research-dir copy test / template parsing brittleness — all v0.4 polish on skill_writer, not blocking
- iter 16 #1, #2, #4, #5: icon regex, hardcoded floors → adaptive median, contradiction detection, JSON option flag — all merge_research polish
- iter 17 #4, #5: tool-tier 02-tools fallback parse, voice-check Tier-1 jargon surrogate — both quality_check enhancements

## Re-tests

| Fix | Test | Result |
|-----|------|--------|
| #6 triggers YAML | skill_writer create with 5 triggers | ✅ all 5 land in YAML array |
| #7 per-track ratio | 17%-primary track | ✅ flagged "01-figures (17%)" |
| #8 meta-vs-body | meta=5 / body=2 | ✅ PARTIAL "meta.json says 5, body has 2..." |

## 累计 findings status after iter 18

- iter 1-13: cleared in cleanup passes 1-3 (38 total cleared)
- iter 14: 5 → 5 cleared (3 prompt + 2 prompt) ✅
- iter 15: 5 → 1 cleared (triggers YAML), 4 deferred to v0.4
- iter 16: 5 → 1 cleared (per-track ratio), 4 deferred
- iter 17: 5 → 3 cleared (meta-vs-body / item 12 / item 11), 2 deferred

**Cleared this iter: 10. Deferred to v0.4: 10.** Cumulative pending = 10 (all v0.4 polish).

## Pattern observation update

- iter 5/6 cleanup: 13 findings → 4 files
- iter 10 cleanup: 15 findings → 4 files
- iter 13 cleanup: 10 findings → 2 files
- iter 18 cleanup: 10 cleared / 10 deferred → 5 files

The deferral pattern is new this iter — first time we've explicitly carried polish forward instead of clearing all. v0.4 cleanup will batch the deferred 10 + whatever new findings come from iter 19-21.

## Distance to v1.0

- v0.3 progress: 3/6 tools (skill_writer / merge_research / quality_check)
- iter 19+: tools/transcribe/youtube.sh + srt_to_transcript.py (1 iter)
- iter 20+: install_*.py for 4 hosts (1-2 iters)
- iter 21+: real prototype run on LLM agent infra → v1.0 ship

Estimated: 3-5 more iters.
