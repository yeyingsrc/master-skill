#!/usr/bin/env python3
"""srt_to_transcript.py — strip timestamps, line numbers, HTML tags from .srt/.vtt files.

Usage:
  python3 srt_to_transcript.py <input.srt|input.vtt> [output.txt]

If output not specified, writes alongside input as `{stem}_transcript.txt`.

Features:
  - Skip cue numbers (pure-digit lines)
  - Skip timecode lines (HH:MM:SS pattern)
  - Strip HTML/VTT tags (`<i>`, `<c>`, `align:left`, etc.)
  - Dedupe consecutive duplicate lines (auto-subs frequently emit dupes)
  - Group short consecutive sentences into 200-char paragraphs
  - Print stats (words, paragraphs, dupe-strip ratio) to stderr

Pure stdlib. macOS python3 out-of-the-box.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

CUE_NUMBER = re.compile(r"^\d+$")
TIMECODE = re.compile(r"^\d{2}:\d{2}:\d{2}")
HTML_TAG = re.compile(r"<[^>]+>")
VTT_DIRECTIVE = re.compile(r"\b(?:align|position|line|size|vertical):[^\s]+", re.IGNORECASE)
WEBVTT_HEADER = re.compile(r"^WEBVTT\b", re.IGNORECASE)
NOTE_LINE = re.compile(r"^NOTE\b", re.IGNORECASE)
SENTENCE_END = re.compile(r"[。！？.!?]$")


def clean_lines(content: str) -> list[str]:
    raw = []
    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue
        if CUE_NUMBER.match(line):
            continue
        if TIMECODE.match(line):
            continue
        if WEBVTT_HEADER.match(line) or NOTE_LINE.match(line):
            continue
        line = HTML_TAG.sub("", line)
        line = VTT_DIRECTIVE.sub("", line).strip()
        if line:
            raw.append(line)
    return raw


def dedupe_consecutive(lines: list[str]) -> tuple[list[str], int]:
    out: list[str] = []
    dupes = 0
    for line in lines:
        if out and line == out[-1]:
            dupes += 1
            continue
        out.append(line)
    return out, dupes


def group_paragraphs(lines: list[str], max_len: int = 200) -> list[str]:
    paragraphs: list[str] = []
    current: list[str] = []

    for line in lines:
        current.append(line)
        joined = " ".join(current)
        if len(joined) >= max_len or SENTENCE_END.search(line):
            paragraphs.append(joined)
            current = []
    if current:
        paragraphs.append(" ".join(current))
    return paragraphs


def transcribe(input_path: Path, output_path: Path | None = None) -> Path:
    if not input_path.exists():
        print(f"ERROR: input not found: {input_path}", file=sys.stderr)
        sys.exit(2)

    if output_path is None:
        output_path = input_path.with_name(f"{input_path.stem}_transcript.txt")

    content = input_path.read_text(encoding="utf-8", errors="replace")
    raw = clean_lines(content)
    deduped, dupe_count = dedupe_consecutive(raw)
    paragraphs = group_paragraphs(deduped)

    output_path.write_text("\n\n".join(paragraphs) + "\n", encoding="utf-8")

    stats = {
        "input": str(input_path),
        "output": str(output_path),
        "raw_lines": len(raw),
        "after_dedupe": len(deduped),
        "dupes_stripped": dupe_count,
        "paragraphs": len(paragraphs),
        "words_approx": sum(len(p.split()) for p in paragraphs),
    }
    for k, v in stats.items():
        print(f"{k}: {v}", file=sys.stderr)
    return output_path


def main(argv: list[str]) -> int:
    if not (2 <= len(argv) <= 3):
        print("Usage: srt_to_transcript.py <input.srt|input.vtt> [output.txt]",
              file=sys.stderr)
        return 1
    input_path = Path(argv[1])
    output_path = Path(argv[2]) if len(argv) == 3 else None
    transcribe(input_path, output_path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
