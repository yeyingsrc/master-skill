#!/usr/bin/env python3
"""whisper_transcribe.py — transcribe audio to SRT using faster-whisper.

Called by local_video.sh after ffmpeg has produced a 16 kHz mono WAV.
Imports faster_whisper lazily inside transcribe() so the module loads cheap
when the user is just running --help or hitting an arg-parse error.

Usage:
  python3 whisper_transcribe.py --input audio.wav --output out.srt [--model medium] [--language zh]

Models (auto-downloaded by faster-whisper on first use, cached in ~/.cache):
  tiny       ~75 MB   fastest, lowest quality
  base       ~150 MB
  small      ~500 MB
  medium     ~1.5 GB  recommended default
  large-v3   ~3 GB    best quality, slower

Language: pass `zh` / `en` / `ja` / etc. to skip auto-detect (faster + more
accurate when you know the language already). Default = auto-detect.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def format_ts(seconds: float) -> str:
    """SRT timestamp: HH:MM:SS,mmm"""
    if seconds < 0:
        seconds = 0.0
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def transcribe(audio: Path, output: Path, model_name: str, language: str | None) -> dict:
    # Lazy import — keeps `--help` cheap and isolates the heavy dep.
    from faster_whisper import WhisperModel

    print(f"[whisper] loading model: {model_name}", file=sys.stderr)
    # int8 is the fastest reasonable compute_type on Apple Silicon CPU; users
    # with a CUDA GPU can override via env (FASTER_WHISPER_DEVICE=cuda).
    import os
    device = os.environ.get("FASTER_WHISPER_DEVICE", "auto")
    compute_type = os.environ.get("FASTER_WHISPER_COMPUTE", "int8")
    model = WhisperModel(model_name, device=device, compute_type=compute_type)

    print(f"[whisper] transcribing {audio.name} ...", file=sys.stderr)
    segments, info = model.transcribe(
        str(audio),
        language=language,
        beam_size=5,
        vad_filter=True,
        vad_parameters={"min_silence_duration_ms": 500},
    )
    print(
        f"[whisper] detected language: {info.language} "
        f"(prob: {info.language_probability:.2f}, duration: {info.duration:.1f}s)",
        file=sys.stderr,
    )

    seg_count = 0
    with output.open("w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, 1):
            f.write(f"{i}\n")
            f.write(f"{format_ts(seg.start)} --> {format_ts(seg.end)}\n")
            f.write(f"{seg.text.strip()}\n\n")
            seg_count = i

    print(f"[whisper] wrote {seg_count} segments → {output}", file=sys.stderr)
    return {
        "segments": seg_count,
        "language": info.language,
        "duration": info.duration,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Transcribe audio to SRT using faster-whisper.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--input", required=True, type=Path,
                        help="Input audio (WAV recommended, 16 kHz mono).")
    parser.add_argument("--output", required=True, type=Path,
                        help="Output SRT path.")
    parser.add_argument("--model", default="medium",
                        help="Whisper model: tiny / base / small / medium / large-v3 (default: medium).")
    parser.add_argument("--language", default=None,
                        help="Force language (zh / en / ja / ...). Default: auto-detect.")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"ERROR: input not found: {args.input}", file=sys.stderr)
        return 2

    args.output.parent.mkdir(parents=True, exist_ok=True)

    try:
        transcribe(args.input, args.output, args.model, args.language)
    except ImportError as e:
        print(f"ERROR: faster-whisper not importable: {e}", file=sys.stderr)
        print("       Install with: pip3 install faster-whisper", file=sys.stderr)
        return 3
    except Exception as e:
        print(f"ERROR: transcription failed: {e}", file=sys.stderr)
        return 4
    return 0


if __name__ == "__main__":
    sys.exit(main())
