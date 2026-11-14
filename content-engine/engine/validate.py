#!/usr/bin/env python3
"""Check a day's media against Instagram + TikTok specs before anything is queued.

Specs encoded here (sources):
  Instagram content publishing docs: images JPEG only; carousel <= 20 items.
  TikTok (Higgsfield tiktok_prepare_publish tool spec): video MP4/WebM/MOV,
    3-600 s, >= 360 px both sides, 23-60 fps; photos JPEG/WebP, <= 1080x1920.
  Instagram Reels practical limits (3-90 s for Reels publishing) -- UNVERIFIED
    exact upper bound; we only ever produce ~10 s clips so the margin is large.

Usage: python validate.py <day_dir>   -> prints JSON report, exit 1 on any failure
"""
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image


def video_report(p: Path) -> dict:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json",
                          str(p)], capture_output=True, text=True, check=True)
    info = json.loads(out.stdout)
    v = next(s for s in info["streams"] if s["codec_type"] == "video")
    num, den = map(int, v["avg_frame_rate"].split("/"))
    fps = num / den if den else 0
    dur = float(info["format"]["duration"])
    w, h = int(v["width"]), int(v["height"])
    has_audio = any(s["codec_type"] == "audio" for s in info["streams"])
    checks = {
        "duration_3_90s": 3 <= dur <= 90,
        "fps_23_60": 23 <= fps <= 60,
        "min_side_360": min(w, h) >= 360,
        "vertical_9_16": abs(w / h - 9 / 16) < 0.02,
        "h264": v["codec_name"] == "h264",
        "yuv420p": v.get("pix_fmt") == "yuv420p",
        "size_under_300MB": p.stat().st_size < 300 * 1024 * 1024,
    }
    return {"file": p.name, "w": w, "h": h, "fps": round(fps, 2), "duration": round(dur, 2),
            "codec": v["codec_name"], "audio": has_audio, "checks": checks}


def image_report(p: Path) -> dict:
    im = Image.open(p)
    w, h = im.size
    checks = {
        "jpeg": im.format == "JPEG",
        "fits_1080x1920": (w <= 1080 and h <= 1920) or (w <= 1920 and h <= 1080),
        "aspect_4_5": abs(w / h - 4 / 5) < 0.02,
        "under_8MB": p.stat().st_size < 8 * 1024 * 1024,
    }
    return {"file": p.name, "w": w, "h": h, "format": im.format, "checks": checks}


def main(day_dir: str) -> int:
    d = Path(day_dir)
    rep = {"video": None, "images": []}
    reel = d / "reel.mp4"
    if reel.exists():
        rep["video"] = video_report(reel)
    for p in sorted(d.glob("slide_*.jpg")):
        rep["images"].append(image_report(p))
    allc = ([rep["video"]] if rep["video"] else []) + rep["images"]
    rep["all_pass"] = bool(allc) and all(all(r["checks"].values()) for r in allc)
    rep["carousel_count_ok"] = 2 <= len(rep["images"]) <= 20
    print(json.dumps(rep, indent=2))
    return 0 if rep["all_pass"] and rep["carousel_count_ok"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
