#!/usr/bin/env python3
"""Generate an ORIGINAL, copyright-free ambient bed and mux it onto a silent clip.

Why: Instagram's API cannot attach licensed library music, and silent Reels
underperform. A code-synthesised pad (no samples, no third-party audio) has
no copyright exposure. On TikTok you can still swap in a trending track from
TikTok's Commercial Music Library in the publish form.

Usage:
  python ambient_audio.py <in.mp4> <out.mp4> [--seed N] [--mood warm|cool]
"""
import argparse
import json
import subprocess
import wave
from pathlib import Path

import numpy as np

SR = 44100
MOODS = {
    # root-position chords as frequency lists (Hz); slow, consonant voicings
    "warm": [[130.81, 196.00, 261.63, 329.63],   # Cmaj
             [110.00, 164.81, 220.00, 261.63],   # Am
             [87.31, 130.81, 174.61, 220.00],    # Fmaj
             [98.00, 146.83, 196.00, 246.94]],   # Gmaj
    "cool": [[146.83, 220.00, 293.66, 349.23],   # Dm
             [116.54, 174.61, 233.08, 293.66],   # Bb
             [130.81, 196.00, 261.63, 329.63],   # C
             [110.00, 164.81, 220.00, 261.63]],  # Am
}


def probe(path: str) -> dict:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format",
                          "-of", "json", path], capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def synth(duration: float, mood: str, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = int(duration * SR)
    t = np.arange(n) / SR
    chords = MOODS[mood]
    seg = duration / len(chords)
    pad = np.zeros(n)
    for i, chord in enumerate(chords):
        env = np.clip(1 - np.abs((t - (i + 0.5) * seg) / (seg * 0.75)), 0, 1) ** 1.5
        for f in chord:
            detune = 1 + rng.uniform(-0.002, 0.002)
            pad += env * (np.sin(2 * np.pi * f * detune * t)
                          + 0.3 * np.sin(2 * np.pi * 2 * f * detune * t)) / len(chord)
    pad *= 0.85 + 0.15 * np.sin(2 * np.pi * 0.2 * t)          # slow breathing LFO
    brown = np.cumsum(rng.normal(0, 1, n)); brown -= np.convolve(brown, np.ones(4410) / 4410, "same")
    brown /= np.max(np.abs(brown)) + 1e-9                      # soft room tone
    crackle = (rng.random(n) < 0.0004) * rng.normal(0, 1, n)   # sparse vinyl-like ticks
    mix = 0.55 * pad + 0.06 * brown + 0.05 * crackle
    fade = int(0.8 * SR)
    mix[:fade] *= np.linspace(0, 1, fade); mix[-fade:] *= np.linspace(1, 0, fade)
    mix /= np.max(np.abs(mix)) + 1e-9
    return (mix * 0.5 * 32767).astype(np.int16)                # ~-6 dBFS peak


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("inp"); ap.add_argument("out")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--mood", choices=list(MOODS), default="warm")
    ap.add_argument("--force", action="store_true", help="replace existing audio")
    a = ap.parse_args()

    info = probe(a.inp)
    has_audio = any(s["codec_type"] == "audio" for s in info["streams"])
    duration = float(info["format"]["duration"])
    if has_audio and not a.force:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", a.inp, "-c", "copy",
                        "-movflags", "+faststart", a.out], check=True)
        print(json.dumps({"audio": "kept_original", "duration": duration}))
        return
    wav = Path(a.out).with_suffix(".wav")
    with wave.open(str(wav), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(synth(duration, a.mood, a.seed).tobytes())
    # H.264 + AAC, yuv420p, faststart: satisfies both Instagram Reels and TikTok specs
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", a.inp, "-i", str(wav),
                    "-map", "0:v:0", "-map", "1:a:0", "-c:v", "libx264", "-preset", "slow",
                    "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
                    "-ar", "44100", "-shortest", "-movflags", "+faststart", a.out], check=True)
    wav.unlink()
    print(json.dumps({"audio": "synthesised", "mood": a.mood, "seed": a.seed, "duration": duration}))


if __name__ == "__main__":
    main()
