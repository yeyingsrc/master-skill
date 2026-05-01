# Cleanup pass — iter 5 (2026-05-01)

iter 4 ended with 13 cumulative findings. This pass clears 5 of them across 2 files.

## Files touched

### `SKILL.md`

1. **Phase 1 changed from "纯并行" to "wave structure" (iter 4 #5, CRITICAL).**
   New wave breakdown:
   - Wave 1 (parallel): Track 04 canon / 05 sources / 06 glossary — independent search paths
   - Wave 2 (parallel, seeded by Wave 1): Track 01 figures / 02 tools — bootstrap from canon authors + sources guests
   - Wave 3 (seeded by both): Track 03 workflows — synthesizes how figures use which tools
   
   Each wave ≤ 3 min budget; total Phase 1 should land in 10-15 min. If a track fails within a wave, downstream wave fallbacks to web-search bootstrap.

2. **Agentic Protocol dim count "5-8" → "3-10 by complexity" (iter 1 finding).**
   Aligned with extraction-framework.md § 九 which already specified the variable range.

### `references/extraction-framework.md`

3. **Triple-gate § 一: added "Step 0 候选清单准备" (iter 2 finding).**
   Synthesis agent now must list 15-30 candidates first (output: `synthesis-candidates.md`) before running the gate. Avoids anchoring bias from sequential evaluation.

4. **Triple-gate evaluation states formalized to PASS / PARTIAL / FAIL (iter 2 + iter 4 borderline findings).**
   Each verification now produces 3 states. Explicit PARTIAL handling rules:
   - Verify 1 PARTIAL → treated as FAIL (cross-figure consensus is the floor)
   - Verify 2 PARTIAL = "generates but doesn't distinguish industry" → FAIL
   - Verify 3 PARTIAL = "industry-amplified version of generic" → enters mental-model section with mandatory amplification-degree capture

5. **Verdict matrix expanded (iter 2 finding).**
   Old: PASS-3 / PASS-1or2 / PASS-0 (3 buckets).
   New: PASS-3 (full) / PASS-2 with verify-3 PARTIAL (amplified) / 1+ FAIL with 2+ PASS (heuristic) / ≤1 PASS (industry boilerplate).

---

## Re-tests

### Re-run iter 2 candidate 3 ("Production reality vs demo glamour") under new rules

iter 2 had verdict "BORDERLINE PASS, mark as 行业放大版" — verbal patch on top of the 3-bucket system.

Under iter 5 rules:
- Verify 1 (跨场景复现): ✅ — figures × scenarios both ≥ 2
- Verify 2 (生成力): ✅ — generates "demo →追问 production case" reflex
- Verify 3 (排他性): ⚠️ PARTIAL — "demo vs prod gap" is generic but in LLM agent infra **特别尖锐** because model stochasticity amplifies it by an order of magnitude

**New verdict: ✅✅⚠️ = 行业放大版心智模型**, enters mental-model section with description requirement: "必须明确写出 'in LLM agent infra 比一般技术行业放大很多' + 量化（model stochasticity makes the gap 10x bigger）".

Outcome same as iter 2 but **rationale now explicit and reproducible** rather than ad-hoc-judged. **Re-test PASS.**

### Re-walk iter 4 Track 01 dry-run under wave structure

iter 4 was implicitly running Track 01 in pure-parallel mode and the wide-net step said "look at biggest companies' founders" with no source for "biggest". I had to use intuition.

Under iter 5 wave structure:
- Wave 1 finishes first → Track 04 canon now has core papers (ReAct paper, AutoGPT writeups, Anthropic agent docs etc.) and Track 05 sources has core podcasts (Latent Space, Practical AI etc.)
- Wave 2 Track 01 starts with seeded candidates: ReAct authors (Yao et al.) + Latent Space common guests (Karpathy, Husain, Willison, Knoop, Liu, Schluntz) + AutoGPT contributors + LangChain founder Chase
- That's ~15 seeded candidates **without** any guesswork
- Wide-net step then expands by 5-15 second-order recommendations from those primary seeds

**Re-test PASS** — wave structure produces a more grounded candidate set faster. The iter 4 finding about "20-30 candidate floor too high" is partially mitigated: with seed-based expansion, hitting 20 becomes mechanical rather than speculative.

---

## Findings status after iter 5

| iter | Finding | Status |
|------|---------|--------|
| 1 | triggers field in skill-template | ✅ done iter 3 |
| 1 | Agentic Protocol dim count "5-8" → "3-10" | ✅ done iter 5 |
| 2 | extraction borderline rule | ✅ done iter 5 |
| 2 | extraction candidate-list prep | ✅ done iter 5 |
| 2 | extraction partial generative power | ✅ done iter 5 |
| 3 | intake "max 2 rounds" rhythm starting point | 🔲 pending — iter 6 |
| 3 | intake focus single-value too narrow | 🔲 pending — iter 6 |
| 3 | intake completion-trigger token | 🔲 pending — iter 6 |
| 3 | intake slug generation rule | 🔲 pending — iter 6 |
| 3 | intake existing_skill check timing | 🔲 pending — iter 6 |
| 4 | 01-figures candidate floor 20-30 too high | ⚠️ partially mitigated by wave seeding (iter 5) |
| 4 | 01-figures borderline candidate handling | 🔲 pending — iter 6 |
| 4 | 01-figures sub-skill candidate flag | 🔲 pending — iter 6 |
| 4 | 01-figures academic figure exclusion too strict | 🔲 pending — iter 6 |
| 4 | Phase 1 wave structure | ✅ done iter 5 |

After iter 5: **5 cleared, 1 partially mitigated, 8 pending.**

Next iter (6) target: clear the remaining 8 in `intake.md` (5) and `01-figures.md` (4 minus the partially-mitigated one). That's also a cleanup pass.

After iter 6 cleanup → write `02-tools.md` (the next research subagent template).
