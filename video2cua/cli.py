"""Command line entry point.

  python -m video2cua.cli analyze demo.mp4 --work work/demo [--vtt demo.vtt] [--notes "..."]
      -> work/demo/{frames.json, frames/, transcript.json, runbook.json, runbook.md}
  (review runbook.md, edit runbook.json if needed, set "_meta": {"approved": true})
  python -m video2cua.cli run work/demo/runbook.json --param invoice_id=123 --start-url https://app.example
"""

import argparse
import json
import time
from pathlib import Path

from .checkpoint import read_json


def cmd_analyze(a) -> None:
    from .extract import extract
    from .synthesize import synthesize
    from .transcribe import transcribe

    work = Path(a.work)
    manifest = extract(Path(a.video), work, fps=a.fps, min_blocks=a.min_blocks, max_frames=a.max_frames)
    print(f"frames: {manifest['sampled_frames']} sampled, {manifest['changed_frames']} changed, "
          f"{len(manifest['frames'])} kept")
    transcript = transcribe(work, manifest, vtt=Path(a.vtt) if a.vtt else None, use_whisper=not a.no_whisper)
    print(f"transcript: {len(transcript['segments'])} segments ({transcript['source']})")
    if a.extract_only:
        return
    rb = synthesize(work, manifest, transcript, notes=a.notes or "", backend=a.backend)
    print(f"runbook: {len(rb['steps'])} steps, {len(rb['parameters'])} parameters -> {work / 'runbook.md'}")
    for p in rb["_meta"]["problems"]:
        print(f"  problem: {p}")
    if rb["open_questions"]:
        print(f"  {len(rb['open_questions'])} open questions for the reviewer")


def cmd_run(a) -> None:
    from .computer import PlaywrightComputer
    from .execute import run
    from .execute_openai import run_openai

    rb = read_json(Path(a.runbook))
    values = dict(kv.split("=", 1) for kv in a.param)
    computer = PlaywrightComputer(a.width, a.height, start_url=a.start_url, headless=not a.headed,
                                  executable_path=a.chromium)
    try:
        log_dir = Path(a.runbook).parent / f"run_{time.strftime('%Y%m%d_%H%M%S')}"
        loop = run_openai if a.backend == "openai" else run
        result = loop(rb, values, computer, log_dir, max_turns=a.max_turns)
    finally:
        computer.close()
    print(json.dumps(result, indent=2))
    print(f"log: {log_dir}")


def main() -> None:
    ap = argparse.ArgumentParser(prog="video2cua")
    sub = ap.add_subparsers(required=True)

    an = sub.add_parser("analyze", help="MP4 -> runbook")
    an.add_argument("video")
    an.add_argument("--work", required=True)
    an.add_argument("--vtt", help="existing WebVTT transcript (e.g. from Teams)")
    an.add_argument("--no-whisper", action="store_true")
    an.add_argument("--notes", help="context from the submitter, e.g. which system this is")
    an.add_argument("--fps", type=float, default=2.0)
    an.add_argument("--min-blocks", type=int, default=2, help="changed 32px tiles needed to keep a frame")
    an.add_argument("--max-frames", type=int, default=60)
    an.add_argument("--extract-only", action="store_true")
    an.add_argument("--backend", choices=["openai", "claude"], default="openai",
                    help="openai = GPT-6.1 Terra (default); claude = Claude on Foundry")
    an.set_defaults(fn=cmd_analyze)

    rn = sub.add_parser("run", help="approved runbook -> computer-use agent")
    rn.add_argument("runbook")
    rn.add_argument("--param", action="append", default=[], help="name=value; repeat")
    rn.add_argument("--start-url")
    rn.add_argument("--width", type=int, default=1280)
    rn.add_argument("--height", type=int, default=800)
    rn.add_argument("--headed", action="store_true")
    rn.add_argument("--chromium", help="Chromium executable path")
    rn.add_argument("--max-turns", type=int, default=80)
    rn.add_argument("--backend", choices=["openai", "claude"], default="openai")
    rn.set_defaults(fn=cmd_run)

    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
