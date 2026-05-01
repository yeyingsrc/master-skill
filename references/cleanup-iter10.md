# Cleanup pass — iter 10 (2026-05-01)

iter 7-9 accumulated 15 findings. This pass clears all 15 across 4 files.

## Files touched

### `SKILL.md` (1 fix consolidated from 2 findings)

1. **Wave seed fallback unified rule** (iter 7 #1 + iter 8 #8)
   New table in Phase 1: 8+ seeds → normal; 5-7 → warn but go; 1-4 → degrade to half-seeded; 0 → STOP and ask user (3 options). Single rule replaces per-track duplicates.

### `prompts/research/02-tools.md` (4 fixes)

2. **GitHub stars baseline → adaptive median × 2** (iter 7 #2 + #3 — these were the same issue)
   No more hardcoded "LLM = 5k / 跨境电商 = 1k" tables. Take candidate-pool stars median, doubled = "必备 tier" threshold. Self-calibrating per-industry.

3. **Decision-tree case fallback** (iter 7 #4)
   "Real case" placeholder when no public case found: `[no public case found, based on stack-pattern analysis from N similar adoption signals]` + branch credibility downgrade.

4. **Decay-risk probability anchors** (iter 7 #5)
   high = >40% chance of significant change in 12mo; medium = 20-40% in 12-24mo; low = <20% in 24+mo. Probabilities are calibration anchors, not precise predictions.

### `prompts/research/03-workflows.md` (3 fixes; #8 covered by SKILL.md unified rule)

5. **Workflow boundary rules** (iter 8 #6 + #7 unified)
   Explicit table distinguishing workflow / decision-tree / micro-improvement. Decision-tree → reroute to Track 02; micro-improvement → drop or hint in Phase 2.6 反模式.

6. **Senior-difference type taxonomy** (iter 8 #9)
   Per-workflow card now requires `skip` / `optimize` / `add` typed differences. At least 2 types + ≥2 differences total to retain.

7. **Stable workflow handling** (iter 8 #10)
   Legacy industries with workflows unchanged 5-10y: legitimate to fill `近 12 个月: 无重大变化（行业稳态，最近一次显著变化是 YYYY 的 X 事件）` + decay risk: low. Not a missing-data signal.

### `prompts/research/04-canon.md` (5 fixes)

8. **Book superseded-by-newer-edition rule** (iter 9 #11)
   Same author + ≤4 years + new edition → mark `superseded_by` + DROP unless old version has independent teaching value (must articulate why in 1 sentence).

9. **Concept tier-1 vs tier-2 stratification** (iter 9 #12)
   Per-concept card now has `Tier` field. Tier 1: 10-15 core concepts every practitioner must know. Tier 2: 5-15 peripheral concepts senior people know.

10. **Rolling-format course handling** (iter 9 #13)
    `Format` accepts "rolling". Duration field: "rolling, ~N hours/month new content". Year+update field: "rolling, last 3 months key content: {{summary}}".

11. **Endorsement evidence type weighting** (iter 9 #14)
    Each endorsement now typed: `figure_long` (highest weight) / `figure_short` / `course_syllabus` / `conf_citation` / `blog_secondary`. Total ≥3 + at least 1 figure_long or course_syllabus required.

12. **Multi-origin concept source field** (iter 9 #15)
    Per-concept `来源` field supports both single-origin (paper + year) and multi-origin (`[primary]` + 1-3 `[significant follow-up]`). For concepts like RAG that have a foundational paper + meaningful follow-ups.

---

## Re-tests

### Re-run iter 7 GitHub stars判定 under adaptive median rule

iter 7 dry-run had 18 retained tools. Their stars distribution (eyeballed):
- Anthropic SDK: ~10k
- LangChain: 90k
- LlamaIndex: 35k
- LangSmith: ~5k
- Vespa: 6k
- Pinecone: hosted (no star)
- Pydantic-AI: 7k
- DSPy: 19k
- ...

Median ≈ 6-8k, so 必备 tier threshold = 12-16k.

Under new rule:
- LangChain (90k) ✅ 必备
- LlamaIndex (35k) ✅ 必备
- DSPy (19k) ✅ 必备 (this changes from场景特化 to 必备 — adoption signal stronger than expected)
- LangSmith (5k) → 场景特化 (was 必备 by old hardcoded rule, now correctly 场景特化 per actual adoption distribution)

**Re-test PASS** — adaptive rule produces tier assignments that better reflect actual adoption distribution.

### Re-run iter 8 vector DB choice / sync→streaming under boundary rules

iter 8 had me drop these candidates ad-hoc.

Under new explicit boundary rules:
- "Choose between hosted vs self-hosted vector DB" — ask "is this a continuous action chain or a one-time choice?" → one-time choice → **DROP to Track 02 decision tree**, mechanical decision now matches my ad-hoc drop ✓
- "Sync → streaming" — single-step optimization → **micro-improvement, not in any track**, mechanical ✓

**Re-test PASS** — boundary rules produce same outcome as iter 8 ad-hoc judgment but reproducibly.

### Re-run iter 9 DMLS 2022 vs AI Engineering 2024 supersedure

Under new rule: same author (Chip Huyen) + new edition within ≤4 years → mark `superseded_by`. DMLS independent value? "DMLS 2022 covers pre-LLM ML pipeline architecture deeply, while AI Engineering 2024 focuses on LLM era — for a learner who needs both eras, DMLS still has standalone value." So either retain with note `superseded_by` flag OR DROP.

For an `LLM agent infra` master skill, the LLM-era is enough → DROP DMLS 2022.
For an `ML engineering` master skill, both have independent value → KEEP both.

**Re-test PASS** — the rule produces context-appropriate decisions instead of one-size-fits-all.

---

## 累计 findings status after iter 10

| iter | Finding | Status |
|------|---------|--------|
| 1-6 | (15 findings) | ✅ all cleared (cumulative through iter 6) |
| 7 | 02-tools wave-1 seed quality fallback | ✅ done iter 10 (SKILL.md unified) |
| 7 | 02-tools stars baseline cross-industry | ✅ done iter 10 |
| 7 | 02-tools industry-baseline placeholder | ✅ done iter 10 (same fix) |
| 7 | 02-tools decision-tree no-public-case fallback | ✅ done iter 10 |
| 7 | 02-tools decay-risk probability anchors | ✅ done iter 10 |
| 8 | 03-workflows vs decision-tree boundary | ✅ done iter 10 |
| 8 | 03-workflows vs micro-improvement boundary | ✅ done iter 10 |
| 8 | 03-workflows wave 1+2 seed fallback | ✅ done iter 10 (SKILL.md unified) |
| 8 | 03-workflows senior-difference taxonomy | ✅ done iter 10 |
| 8 | 03-workflows stable workflow handling | ✅ done iter 10 |
| 9 | 04-canon book-superseded rule | ✅ done iter 10 |
| 9 | 04-canon concept tier stratification | ✅ done iter 10 |
| 9 | 04-canon rolling-format course | ✅ done iter 10 |
| 9 | 04-canon endorsement type weighting | ✅ done iter 10 |
| 9 | 04-canon multi-origin concept source | ✅ done iter 10 |

**15/15 cleared. Cumulative findings empty after iter 10.**

---

## Pattern observation across cleanup passes

iter 5/6 cleanup cleared 13 findings on 4 files. iter 10 cleared 15 findings on 4 files. Ratio: ~4 findings/iter dry-run on a fresh prompt template seems stable.

This suggests:
- For each new prompt template, expect ~5 findings from dry-run
- After 2-3 fresh templates, do a cleanup pass
- Pattern: alternate forward + cleanup at 3:1 ratio

If sustained: master-skill v0.2 (8 prompts total) needs roughly 8 forward iters + 3 cleanup iters = 11 iters total. Currently completed 10 iters with 7 prompt templates done. Estimated 1-2 more prompt iters + 1 cleanup → v0.2 done.

Then v0.3 (tools) ~5-7 iters. Then real prototype run → v1.0.

Total: ~5-9 more iters to v1.0.
