"""Stage 2: get the narration as timestamped segments.

Two sources, in order of preference:
  1. An existing WebVTT file (Teams and Stream recordings ship one), passed with --vtt.
  2. A Whisper deployment in your Foundry resource, called through the Azure OpenAI API.

Narration is optional: silent recordings still produce a runbook, with less
context about *why* each step happens.
"""

import os
import re
from pathlib import Path

from .checkpoint import read_json, write_json

TRANSCRIPT = "transcript.json"

_TS = r"(?:(\d+):)?(\d{1,2}):(\d{2})[.,](\d{3})"


def _secs(h, m, s, ms) -> float:
    return int(h or 0) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def parse_vtt(text: str) -> list[dict]:
    segments = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = re.match(rf"\s*{_TS}\s*-->\s*{_TS}", lines[i])
        if not m:
            i += 1
            continue
        start, end = _secs(*m.groups()[:4]), _secs(*m.groups()[4:])
        i += 1
        body = []
        while i < len(lines) and lines[i].strip():
            body.append(lines[i].strip())
            i += 1
        # Strip voice/style tags such as <v Jane Doe>...</v>.
        cue = re.sub(r"<[^>]+>", "", " ".join(body)).strip()
        if cue:
            segments.append({"start": round(start, 2), "end": round(end, 2), "text": cue})
    return segments


def transcribe_azure_whisper(audio: Path) -> list[dict]:
    from openai import AzureOpenAI

    client = AzureOpenAI(
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-06-01"),
    )
    with open(audio, "rb") as f:
        result = client.audio.transcriptions.create(
            model=os.environ.get("AZURE_WHISPER_DEPLOYMENT", "whisper"),
            file=f,
            response_format="verbose_json",
            timestamp_granularities=["segment"],
        )
    return [
        {"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()}
        for s in (result.segments or [])
    ]


def transcribe(work: Path, manifest: dict, vtt: Path | None = None, use_whisper: bool = True) -> dict:
    out = work / TRANSCRIPT
    if out.exists():
        return read_json(out)

    if vtt is not None:
        data = {"source": f"vtt:{vtt}", "segments": parse_vtt(vtt.read_text(encoding="utf-8"))}
    elif manifest.get("audio") and use_whisper and os.environ.get("AZURE_OPENAI_ENDPOINT"):
        data = {"source": "azure-whisper", "segments": transcribe_azure_whisper(work / manifest["audio"])}
    else:
        data = {"source": "none", "segments": []}
    write_json(out, data)
    return data
