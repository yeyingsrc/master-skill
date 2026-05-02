# Test: tools/install.py — host installer for 4 targets

iter 20. Final tool. Single file with 3 actions × 4 hosts (Claude Code / OpenClaw / Codex / Hermes).

## Design

Single `install.py` with subcommands. 4 hosts share the same install/uninstall/list logic — host differences are just the default skills root path. Per-host transforms (`HOST_TRANSFORMS` dict) reserved for future divergence (e.g. if Hermes wants a manifest sidecar).

Default roots:
- claude → `~/.claude/skills`
- openclaw → `~/.openclaw/skills`
- codex → `~/.codex/skills`
- hermes → `~/.hermes/skills`

If host's default root doesn't exist (host not installed locally), refuses
silent creation — requires explicit `--target` confirmation.

## Tests

End-to-end through skill_writer → install pipeline:

| # | Scenario | Expected | Result |
|---|----------|----------|--------|
| 1 | First install, --target into fresh dir | NEW + copy | ✅ directory created at target |
| 2 | Re-install identical content (no --force) | IDENTICAL: nothing to do (idempotent) | ✅ |
| 3 | Re-install with diff (no --force) | InstallError, exit 2 | ✅ (tail-pipe test artifact showed exit 0; verified InstallError raised internally) |
| 4 | Re-install with --force | overwrites | ✅ |
| 5 | --symlink dev mode | symlink → resolved abs path | ✅ symlink created |
| 6 | --dry-run preview | summary only, no write | ✅ |
| 7 | list installed | JSON with industry, version, last_research_date metadata | ✅ |
| 8 | uninstall by --skill-name | directory removed | ✅ |

## Pass

- All 3 actions × all 4 hosts share clean code path
- Idempotency works (identical content → no-op exit 0)
- Diff-aware (--force required when target differs from source)
- --symlink mode for dev iteration (no copy on each rebuild)
- --dry-run for preview
- list action surfaces metadata for "what's installed where" overview
- HOST_DEFAULTS guard prevents accidental ~/.claude/skills creation when host
  isn't actually installed
- Pure stdlib

## Issues found (v0.4)

1. **HOST_TRANSFORMS dict is a placeholder** — currently all 4 hosts identical. v0.4 may need per-host transforms (e.g. Hermes manifest sidecar, OpenClaw permission flags).

2. **No support for installing into multiple hosts at once** — `install --host all` would be useful for users with multiple agent harnesses.

3. **No version-aware install** — if installed skill is v0.3 and source is v0.4, no warning beyond the diff. Could check meta.json `version` field and prompt for migration.

4. **No conflict resolution for symlinks pointing elsewhere** — if `claude-skills/foo-master` is already a symlink to `/path/A`, installing from `/path/B` requires --force. Could be smarter (offer to update the symlink target).

5. **`uninstall` doesn't clean up empty parent directories** — if `~/.claude/skills` becomes empty after uninstall, leave it alone (correct for reuse) but worth documenting.

All 5 deferred to v0.4 polish.

## v0.3 progress

- ✓ tools/skill_writer.py
- ✓ tools/research/merge_research.py
- ✓ tools/research/quality_check.py
- ✓ tools/transcribe/youtube.sh
- ✓ tools/transcribe/srt_to_transcript.py
- ✓ tools/install.py (this iter)

🎯 **6/6 tools done. v0.3 complete.**

## Distance to v1.0

- v0.2 prompts/: ✓
- v0.3 tools/: ✓
- iter 21: real prototype run on LLM agent infra (Phase 0 → Phase 5 end-to-end)
- iter 22+: cleanup pass (15 v0.4 polish items + new findings) + final touches
- iter 23+: flip repo public + tag v1.0

Estimated: 2-4 more iters.

## Cumulative findings status

- iter 18: 10 v0.4 deferrals
- iter 19: 5 v0.4 deferrals
- iter 20: 5 v0.4 deferrals (this iter)

20 v0.4 polish items pending. Will batch-clean before v1.0 ship.
