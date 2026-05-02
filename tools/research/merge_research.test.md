# Test: tools/research/merge_research.py — Phase 1.5 review aggregator

iter 16. Second tool. Aggregates 6 research files into a structured Phase 1.5 review summary.

## Test setup

Synthesized 6 representative research/*.md files for "LLM agent infra":
- 01-figures: 13 entries, 28 source markers (19P/6S/3R)
- 02-tools: 18 entries, 30 source markers (22P/5S/3R)
- 03-workflows: 7 entries, 14 sources (9P/4S/1R)
- 04-canon: 22 entries, 25 sources (15P/4S/6R)
- 05-sources: 23 entries, 29 sources (23P/1S/5R)
- 06-glossary: 26 entries, 29 sources (26P/0S/3R)

Each track ends with a `## Phase 2 提炼提示` block.

## Two actions tested

### `merge` (initial healthy run)

Output (json):
```json
{
  "verdict_pass": true,
  "cold_tracks": [],
  "totals": { "primary": 114, "secondary": 20, "reference": 21,
              "grand_total": 155, "overall_primary_ratio": 0.74 }
}
```

Generated `synthesis-summary.md`:
- 6-row track table with item count vs floor, source distribution, primary ratio, cold flag
- Quality gate verdict with explicit pass/fail criteria
- Per-track Phase 2 interface preserved verbatim (the strategic value — these are subagent-prepared candidate signals for Phase 2)

✅ verdict matches health: 6/6 above floor, 74% primary, no missing tracks → PASS

### Stress test (shrink figures to below floor)

Manually trimmed 01-figures.md to 3 entries + appended "本 track 信号薄弱". Re-ran merge:
- ✅ cold_tracks correctly = ["01-figures"]
- ✅ figures row marked 🔵, other 5 rows marked ✅
- ✅ verdict_pass still `true` (only 1 cold track, < 3 threshold for COLD INDUSTRY)
- ✅ `show` action prints same table to stdout

## Bug found and fixed during test

**Initial regex `冷僻|冷门|信号薄弱` had false positives.**

It matched the literal text "冷僻信号" appearing in every track's Phase 2 interface
boilerplate ("**冷僻信号**: 不冷僻"). Result: ALL 6 tracks marked cold even though item
counts were above floor and bodies said "不冷僻".

Fixed regex to match explicit positive declarations only:
```python
r"(?:本.{0,8}(?:track|维度|轨)?\s*(?:信号薄弱|不足))"
r"|(?:冷门领域协议生效)"
r"|(?:冷僻领域[，,]\s*仅找到)"
r"|(?:维度信号薄弱)"
```

This requires affirmative statements like "本 track 信号薄弱" / "冷门领域协议生效" /
"冷僻领域，仅找到 N 位", not generic "冷僻" mentions in section headers.

Re-ran healthy test → verdict_pass: true, cold_tracks: [] ✓
Re-ran cold-track test → cold_tracks: ["01-figures"] ✓
Both fire correctly.

## Pass

- 6-track aggregation works across heterogeneous track formats
- Per-track item counting with track-specific regex patterns (different headings: 📖📄🎓💡 in canon, 📰🎙️🎪 in sources, plain `### N.` in others)
- Source markers `[Primary]/[Secondary]/[Reference]` count correctly
- Endorsement-type counters (figure_long / figure_short / course_syllabus) capture the iter-13 cleanup additions
- Phase 2 interface blocks preserved verbatim (the strategic value preserved)
- Cold-signal detection now mechanical (item floor + only-real-cold-language regex)
- Verdict `is_cold_industry` requires ≥ 3 cold tracks (avoids spurious cold flags)
- JSON output strips inline phase2_interface (it's in the .md), keeping JSON queryable for programmatic use
- Pure stdlib

## Issues found (v0.4 deferral mostly)

1. **Track 05 sources item-counter regex is fragile**: I used `(?:📰|🎙️|🎪|👥|📊|.{1,3})` to match type icons but this is hacky. Should use the actual icon set explicitly.

2. **Per-track item floors are hardcoded**: Different industries should have different floors (cold industry threshold is industry-specific). Should adopt the adaptive median approach from iter-10's tool-stack fix.

3. **No per-track "primary ratio < 50%" warning**: Tools ratio = 73% is fine but if a track had 30% primary, the verdict only checks overall ratio not per-track. Should add per-track ratio warning at < 40%.

4. **No detection of cross-track contradictions**: SKILL.md says "矛盾点" should appear in the review. merge_research doesn't detect or report cross-track contradictions — that's currently still a manual review step. v0.4 could add: scan for terms appearing in one track but explicitly missing/contradicted in another.

5. **synthesis-summary.json strips Phase 2 interface but keeps the structure**: useful for programmatic, but the consumer (Phase 2 synthesis subagent) might want the JSON to also include the interface blocks. Consider making it optional via `--include-phase2-content` flag.

## v0.3 progress

- ✓ tools/skill_writer.py (iter 15)
- ✓ tools/research/merge_research.py (iter 16)
- ⏳ tools/research/quality_check.py runner (Phase 4 mechanical part)
- ⏳ tools/transcribe/youtube.sh + tools/transcribe/srt_to_transcript.py
- ⏳ tools/install/install_claude.py / install_openclaw.py / install_codex.py / install_hermes.py

2/6 tools done. Distance to v1.0: ~4-7 more iters (4 tool iters + 1 cleanup + 1 prototype run).

## Cumulative findings

- iter 14: 5
- iter 15: 5
- iter 16: 5 (this iter)

15 cumulative pending. iter 18 cleanup pass per pattern (or earlier if they accumulate quickly).
