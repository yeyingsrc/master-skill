#!/usr/bin/env python3
"""install.py — install a generated `{slug}-master` skill into a host.

Usage:
  python3 install.py --host claude --source /path/to/skill-dir
  python3 install.py --host openclaw --source /path/to/skill-dir
  python3 install.py --host codex --source /path/to/skill-dir
  python3 install.py --host hermes --source /path/to/skill-dir

Options:
  --target <dir>        override the host's default skills root
  --symlink             symlink instead of copy (dev mode)
  --force               overwrite existing skill at target
  --dry-run             preview what would happen, don't write
  --uninstall           remove the installed skill instead of installing

Each host has a default skills root:
  claude   → ~/.claude/skills
  openclaw → ~/.openclaw/skills
  codex    → ~/.codex/skills
  hermes   → ~/.hermes/skills

If the host's root doesn't exist (host not installed), the installer warns and
asks for explicit `--target` confirmation. We never `mkdir -p ~/.claude/skills`
without confirming the host is intentional — avoids creating empty config dirs
in `~/`.

Pure stdlib. macOS python3 out-of-the-box.
"""
from __future__ import annotations

import argparse
import filecmp
import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any

HOST_DEFAULTS: dict[str, Path] = {
    "claude": Path.home() / ".claude" / "skills",
    "openclaw": Path.home() / ".openclaw" / "skills",
    "codex": Path.home() / ".codex" / "skills",
    "hermes": Path.home() / ".hermes" / "skills",
}

# Per-host metadata adjustments. v1.0 keeps these identical (all hosts read
# SKILL.md), but the installer leaves room for future host-specific transforms
# (e.g., Hermes might want a different file extension or a manifest sidecar).
HOST_TRANSFORMS: dict[str, dict[str, Any]] = {
    "claude": {"manifest": None},
    "openclaw": {"manifest": None},
    "codex": {"manifest": None},
    "hermes": {"manifest": None},
}


class InstallError(Exception):
    pass


# ---------------------------------------------------------------------------
# Helpers

def validate_source(source: Path) -> dict[str, Any]:
    """Confirm source looks like a master-skill directory."""
    if not source.exists():
        raise InstallError(f"source not found: {source}")
    if not source.is_dir():
        raise InstallError(f"source is not a directory: {source}")
    skill_md = source / "SKILL.md"
    meta_json = source / "meta.json"
    if not skill_md.exists():
        raise InstallError(f"SKILL.md not found in {source} — is this a master-skill output?")
    if not meta_json.exists():
        raise InstallError(f"meta.json not found in {source}")

    try:
        meta = json.loads(meta_json.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise InstallError(f"meta.json malformed: {e}") from e

    if "name" not in meta:
        raise InstallError("meta.json missing 'name' field")
    if not meta["name"].endswith("-master"):
        # Soft warn rather than fail — user might have non-standard naming
        print(f"WARN: skill name '{meta['name']}' doesn't end with -master "
              f"(non-standard but allowed)", file=sys.stderr)
    return meta


def resolve_target_root(host: str, target_override: Path | None) -> Path:
    """Resolve where the skill goes. If host root doesn't exist, prompt
    confirmation via explicit --target."""
    if target_override:
        return target_override
    default = HOST_DEFAULTS.get(host)
    if default is None:
        raise InstallError(f"unknown host: {host}; use --target to specify a path")
    if not default.exists():
        raise InstallError(
            f"host '{host}' default root {default} doesn't exist — host may not be "
            f"installed. Pass --target {default} to confirm and create it, or use a "
            f"different path."
        )
    return default


def diff_summary(src: Path, dst: Path) -> list[str]:
    """Compare directories shallowly. Return list of changes."""
    if not dst.exists():
        return [f"NEW: {dst} doesn't exist"]
    cmp = filecmp.dircmp(src, dst)
    changes: list[str] = []
    if cmp.left_only:
        changes.extend(f"ADD: {f}" for f in cmp.left_only)
    if cmp.right_only:
        changes.extend(f"REMOVE-on-target-only: {f}" for f in cmp.right_only)
    if cmp.diff_files:
        changes.extend(f"MODIFY: {f}" for f in cmp.diff_files)
    if not changes:
        changes.append("IDENTICAL: nothing to do")
    return changes


# ---------------------------------------------------------------------------
# Actions

def action_install(args: argparse.Namespace) -> int:
    source: Path = args.source
    meta = validate_source(source)
    skill_name = meta["name"]

    target_root = resolve_target_root(args.host, args.target)
    target_dir = target_root / skill_name

    summary = {
        "host": args.host,
        "source": str(source),
        "target": str(target_dir),
        "mode": ("symlink" if args.symlink else "copy") + (" (force)" if args.force else ""),
        "dry_run": bool(args.dry_run),
    }

    # Show preview
    print(json.dumps({**summary, "changes": diff_summary(source, target_dir)},
                     indent=2, ensure_ascii=False))

    if args.dry_run:
        print("[dry-run, no changes]")
        return 0

    # Refuse silent overwrite without --force
    if target_dir.exists() and not args.force:
        # Only refuse if it's a different skill or has uncommitted changes;
        # if identical, treat as idempotent success.
        diffs = diff_summary(source, target_dir)
        if diffs == ["IDENTICAL: nothing to do"]:
            print("OK: target identical to source, nothing to do (idempotent)")
            return 0
        raise InstallError(
            f"target {target_dir} exists and differs from source. "
            f"Pass --force to overwrite, --dry-run to preview, or --uninstall first."
        )

    # Ensure target root exists
    target_root.mkdir(parents=True, exist_ok=True)

    # Wipe existing target if force
    if target_dir.exists() and args.force:
        if target_dir.is_symlink():
            target_dir.unlink()
        else:
            shutil.rmtree(target_dir)

    # Install
    if args.symlink:
        target_dir.symlink_to(source.resolve(), target_is_directory=True)
        print(f"OK: symlink {target_dir} → {source.resolve()}")
    else:
        shutil.copytree(source, target_dir)
        print(f"OK: copied {source} → {target_dir}")

    return 0


def action_uninstall(args: argparse.Namespace) -> int:
    if not args.source and not args.skill_name:
        raise InstallError(
            "uninstall requires --skill-name (e.g. llm-agent-infra-master) or "
            "--source pointing at the original skill dir to derive the name from"
        )
    if args.source:
        meta = validate_source(args.source)
        skill_name = meta["name"]
    else:
        skill_name = args.skill_name

    target_root = resolve_target_root(args.host, args.target)
    target_dir = target_root / skill_name

    if not target_dir.exists():
        print(f"OK: nothing to uninstall, {target_dir} doesn't exist")
        return 0

    if args.dry_run:
        print(f"[dry-run] would remove {target_dir}")
        return 0

    if target_dir.is_symlink():
        target_dir.unlink()
        print(f"OK: removed symlink {target_dir}")
    else:
        shutil.rmtree(target_dir)
        print(f"OK: removed directory {target_dir}")
    return 0


def action_list(args: argparse.Namespace) -> int:
    """List installed master-skills under host's skills root."""
    target_root = resolve_target_root(args.host, args.target)
    if not target_root.exists():
        print(json.dumps({"host": args.host, "root": str(target_root), "installed": []},
                         indent=2, ensure_ascii=False))
        return 0
    installed: list[dict[str, Any]] = []
    for entry in sorted(target_root.iterdir()):
        if not entry.is_dir() and not entry.is_symlink():
            continue
        if not entry.name.endswith("-master"):
            continue
        meta_path = entry / "meta.json"
        info: dict[str, Any] = {"name": entry.name, "path": str(entry),
                                 "is_symlink": entry.is_symlink()}
        if meta_path.exists():
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
                info["industry"] = meta.get("industry")
                info["version"] = meta.get("version")
                info["last_research_date"] = meta.get("last_research_date")
            except json.JSONDecodeError:
                info["error"] = "meta.json malformed"
        installed.append(info)
    print(json.dumps({"host": args.host, "root": str(target_root), "installed": installed},
                     indent=2, ensure_ascii=False))
    return 0


# ---------------------------------------------------------------------------
# CLI

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="install master-skill outputs into Claude Code / OpenClaw / Codex / Hermes",
    )
    sub = parser.add_subparsers(dest="action", required=True)

    p_install = sub.add_parser("install", help="install a skill into a host")
    p_install.add_argument("--host", required=True, choices=list(HOST_DEFAULTS.keys()))
    p_install.add_argument("--source", required=True, type=Path,
                           help="path to the generated skill directory")
    p_install.add_argument("--target", type=Path, default=None,
                           help="override host's default skills root")
    p_install.add_argument("--symlink", action="store_true",
                           help="symlink instead of copying (dev mode)")
    p_install.add_argument("--force", action="store_true",
                           help="overwrite existing skill at target")
    p_install.add_argument("--dry-run", action="store_true")

    p_uninstall = sub.add_parser("uninstall", help="remove an installed skill")
    p_uninstall.add_argument("--host", required=True, choices=list(HOST_DEFAULTS.keys()))
    p_uninstall.add_argument("--source", type=Path, default=None,
                              help="original skill dir (used to derive skill name)")
    p_uninstall.add_argument("--skill-name", default=None,
                              help="explicit skill name (e.g. llm-agent-infra-master)")
    p_uninstall.add_argument("--target", type=Path, default=None)
    p_uninstall.add_argument("--dry-run", action="store_true")

    p_list = sub.add_parser("list", help="list installed master-skills under host")
    p_list.add_argument("--host", required=True, choices=list(HOST_DEFAULTS.keys()))
    p_list.add_argument("--target", type=Path, default=None)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.action == "install":
            return action_install(args)
        if args.action == "uninstall":
            return action_uninstall(args)
        if args.action == "list":
            return action_list(args)
    except InstallError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    return 99


if __name__ == "__main__":
    sys.exit(main())
