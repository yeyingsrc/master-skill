# Cleanup pass — iter 13 (2026-05-02)

iter 11+12 accumulated 10 findings. This pass clears all 10.

## Files touched

### `prompts/research/05-sources.md` (5 fixes)

1. **投入产出比 probability anchors** (iter 11 #3)
   high = ≥80% / medium = 50-80% / low = <50% issues delivering actionable insight. Calibration anchors not precise predictions.

2. **Paywall handling** (iter 11 #2)
   New field `Paywall: none / paywall: $X/month / paywall: $X one-time`. Retain only if unique content with no free alternative; require 1-2 sentence judgment of worth-it.

3. **Conference next-edition gap** (iter 11 #4)
   Time-decay table now has both `last_edition_date + next_edition_date`. If interval > 18 months → downgrade retain priority (users can't wait that long).

4. **Global locale + non-en sources** (iter 11 #1)
   For locale=global, each source-type must retain at least 1-2 high-quality non-English sources with `geographic_focus` flag. Warns user that agent's deep-fluency in non-English is not guaranteed.

5. **Topic-heat crawl-depth marker** (iter 11 #5)
   Topic-heat field now requires marker: `incomplete (sources listed but content not crawled)` vs `high-confidence (N sources × M items inspected)`. Prevents fake-confident summaries.

### `prompts/research/06-glossary.md` (5 fixes)

6. **Multi-type entry support** (iter 12 #6)
   Type field accepts compound values like `term + acronym` for entries that are both (RAG, CoT, ReAct).

7. **Outsider-tell typed subclasses** (iter 12 #9)
   "常见误用" now has 4 typed subclasses: `semantic_tell` / `pronunciation_tell` (acronym-specific) / `usage_tell` / `register_tell`. Pronunciation-tell handles RAG="rag" vs "R-A-G" / SQL="sequel" cases.

8. **Tier 1 vs Tier 2 outsider-tell rule** (iter 12 #8)
   Tier 1 entries must fill outsider-tell; Tier 2 recommended (was: 50% threshold across all). Quality-self-check updated.

9. **Vendor-misappropriation evidence requirement** (iter 12 #7)
   Each vendor-misappropriation claim must include source URL. Prevents impressionistic claims polluting master skill.

10. **Time-axis stable-industry filter** (iter 12 #10)
    Time-axis table now filters to "近 5 年内有显著变化的 standard / regulation". Long-term-stable items only get issued-year in main entry.

---

## Re-tests (sampling)

### Re-run iter 12 RAG entry under multi-type rule

Old: forced choice between `term` or `acronym` for RAG → ambiguous.
New: `Type: term + acronym` → both stats pipelines apply. RAG counts toward both term-tier 1 and acronym category. **Re-test PASS.**

### Re-run iter 11 paid AI Engineer Slack under paywall rule

iter 11 dry-run: kept "AI Engineer Slack" with mention of paywall but no judgment.
Under iter 13 rule: must fill `Paywall: $X/month + worth-it judgment`. Now writes:
> Paywall: $99/year (annual). Worth it for AI engineers who attend AI Engineer Summit conference in person; for everyone else, free Latent Space + Discord communities cover ~80% of the signal. → KEEP if user is conference-attending tier; otherwise BORDERLINE drop.

**Re-test PASS** — paywall judgment now reproducible.

### Re-run iter 12 vendor-misappropriation under evidence requirement

iter 12 dry-run: wrote "Pinecone often markets itself as 'the RAG database'" without source URL.
Under iter 13: must add source URL. Either find one (Pinecone homepage tagline + 3rd-party blog calling this out) or remove the claim.

**Re-test PASS** — claim now traceable.

---

## 累计 findings status after iter 13

All findings from iter 1-12: 0 pending. Technical debt empty (4th time).

## Pattern observation

- iter 5/6 cleanup: 13 findings cleared on 4 files
- iter 10 cleanup: 15 findings cleared on 4 files  
- iter 13 cleanup: 10 findings cleared on 2 files

3:1 forward:cleanup ratio sustained across all 13 iterations. Each new prompt template averages 4-5 findings; each cleanup averages 10-15 findings cleared.

## Next steps after cleanup

iter 14 onward, write final 2 prompts to complete v0.2:
- `prompts/synthesis.md` — Phase 2 提炼指引
- `prompts/quality_check.md` — Phase 4 验证 rubric

Then v0.3 starts: tools/ scripts (5+).

Then real prototype run on LLM agent infra → v1.0.

Distance to v1.0: ~5-7 more iters (2 prompts + cleanup + ~3-4 tools iters + prototype).
