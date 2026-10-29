"""Stage 1: pull key frames and the audio track out of an MP4.

Frames are sampled at a fixed rate, then reduced to the ones where the screen
visibly changed. Screen recordings are mostly static, so this keeps the frames
that show each UI state (a menu opening, a dialog, typed text) and drops the
rest. Requires ffmpeg and ffprobe on PATH.
"""

import json
import subprocess
from pathlib import Path

from PIL import Image, ImageChops

from .checkpoint import read_json, write_json

MANIFEST = "frames.json"


def probe(video: Path) -> dict:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", str(video)],
        check=True, capture_output=True, text=True,
    ).stdout
    info = json.loads(out)
    vstream = next(s for s in info["streams"] if s["codec_type"] == "video")
    return {
        "duration_s": float(info["format"]["duration"]),
        "width": int(vstream["width"]),
        "height": int(vstream["height"]),
        "has_audio": any(s["codec_type"] == "audio" for s in info["streams"]),
    }


def _work_image(path: Path, max_width: int = 1280) -> Image.Image:
    # Near-native resolution: typed text is often only a few dozen pixels tall at
    # 1080p, and a small thumbnail would average it away.
    img = Image.open(path).convert("L")
    if img.width > max_width:
        img = img.resize((max_width, max(1, round(max_width * img.height / img.width))))
    return img


def changed_blocks(a: Image.Image, b: Image.Image, block: int = 32, min_pixels: int = 20) -> int:
    """Number of block x block tiles in which at least min_pixels pixels changed visibly.

    Counting tiles rather than pixels keeps a short typed word (a few tiles) above
    the bar while compression noise (scattered, faint) stays below it.
    """
    mask = ImageChops.difference(a, b).point(lambda v: 255 if v > 24 else 0)
    n = 0
    for y in range(0, mask.height, block):
        for x in range(0, mask.width, block):
            if mask.crop((x, y, x + block, y + block)).histogram()[255] >= min_pixels:
                n += 1
    return n


def select_changed_frames(paths: list[Path], min_blocks: int, max_gap: int) -> list[tuple[int, int]]:
    """(index, score) of frames that differ from the last kept frame in >= min_blocks tiles.

    The first and last frames are always kept, and a frame is force-kept after
    max_gap samples without one, so slow changes (a progress bar, text typed one
    character at a time) still get sampled.
    """
    if not paths:
        return []
    kept = [(0, 10**9)]
    last = _work_image(paths[0])
    for i in range(1, len(paths)):
        cur = _work_image(paths[i])
        score = changed_blocks(last, cur)
        if score >= min_blocks or i - kept[-1][0] >= max_gap:
            kept.append((i, score))
            last = cur
    if kept[-1][0] != len(paths) - 1:
        kept.append((len(paths) - 1, 10**9))
    return kept


def trim(kept: list[tuple[int, int]], max_frames: int) -> list[int]:
    """Keep the max_frames largest changes (first and last always), in time order.

    Large changes (a new page, a dialog) matter more than small ones (a pointer
    moving), so when there are too many frames the small ones go first.
    """
    if len(kept) <= max_frames:
        return [i for i, _ in kept]
    ends = {kept[0][0], kept[-1][0]}
    middle = sorted(kept[1:-1], key=lambda k: -k[1])[: max_frames - len(ends)]
    return sorted(ends | {i for i, _ in middle})


def extract(video: Path, work: Path, fps: float = 2.0, min_blocks: int = 2,
            max_gap_s: float = 10.0, max_frames: int = 60) -> dict:
    manifest_path = work / MANIFEST
    if manifest_path.exists():
        return read_json(manifest_path)

    meta = probe(video)
    raw = work / "raw_frames"
    raw.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-i", str(video), "-vf", f"fps={fps}", str(raw / "f_%06d.png")],
        check=True,
    )
    paths = sorted(raw.glob("f_*.png"))
    candidates = select_changed_frames(paths, min_blocks, max_gap=max(1, round(max_gap_s * fps)))
    kept = trim(candidates, max_frames)

    frames_dir = work / "frames"
    frames_dir.mkdir(exist_ok=True)
    frames = []
    for i in kept:
        # ffmpeg's fps filter emits frame n at t = n / fps (n starting at 0).
        t = round(i / fps, 2)
        dest = frames_dir / f"t{t:08.2f}.png"
        paths[i].replace(dest)
        frames.append({"t": t, "path": str(dest.relative_to(work))})
    for p in raw.glob("f_*.png"):
        p.unlink()
    raw.rmdir()

    audio = None
    if meta["has_audio"]:
        audio_path = work / "audio.wav"
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-i", str(video), "-vn", "-ac", "1", "-ar", "16000", str(audio_path)],
            check=True,
        )
        audio = str(audio_path.relative_to(work))

    manifest = {
        "video": str(video),
        "meta": meta,
        "params": {"fps": fps, "min_blocks": min_blocks, "max_gap_s": max_gap_s, "max_frames": max_frames},
        "sampled_frames": len(paths),
        "changed_frames": len(candidates),
        "frames": frames,
        "audio": audio,
    }
    write_json(manifest_path, manifest)
    return manifest
