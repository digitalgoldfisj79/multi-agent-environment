"""Offline tests: no Azure or Claude calls. The model is replaced by scripted fakes."""

import json
import os
import shutil
import subprocess
from pathlib import Path
from types import SimpleNamespace

import pytest
from PIL import Image, ImageDraw

from video2cua.computer import Computer, ToolError, to_playwright_key
from video2cua.execute import render_runbook, run
from video2cua.extract import changed_blocks, extract, trim
from video2cua.runbook import RUNBOOK_SCHEMA, to_markdown, unresolved_params, validate
from video2cua.synthesize import build_content, narration_between, synthesize
from video2cua.transcribe import parse_vtt

CHROMIUM = os.environ.get("V2C_TEST_CHROMIUM", "/opt/pw-browsers/chromium")
needs_ffmpeg = pytest.mark.skipif(not shutil.which("ffmpeg"), reason="ffmpeg not installed")


# ---------- fixtures ----------

def _ui_state(draw_fn, size=(640, 400)):
    img = Image.new("RGB", size, "white")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, size[0], 40], fill=(30, 60, 120))  # title bar
    draw_fn(d)
    return img


@pytest.fixture
def screen_video(tmp_path) -> Path:
    """A 12 s fake screen recording: 4 UI states held 3 s each, with an audio track."""
    states = [
        lambda d: d.rectangle([50, 80, 400, 110], outline="black"),                       # empty form
        lambda d: (d.rectangle([50, 80, 400, 110], outline="black"),
                   d.text((55, 88), "ACME-0042", fill="black")),                           # typed value
        lambda d: (d.rectangle([50, 80, 400, 110], outline="black"),
                   d.text((55, 88), "ACME-0042", fill="black"),
                   d.rectangle([200, 150, 600, 350], fill=(220, 220, 220))),               # dialog open
        lambda d: d.rectangle([0, 60, 640, 400], fill=(200, 240, 200)),                   # success page
    ]
    src = tmp_path / "src"
    src.mkdir()
    for i, s in enumerate(states):
        _ui_state(s).save(src / f"s{i}.png")
    video = tmp_path / "demo.mp4"
    subprocess.run([
        "ffmpeg", "-v", "error", "-y",
        "-framerate", "1/3", "-i", str(src / "s%d.png"),
        "-f", "lavfi", "-i", "sine=frequency=440:duration=12",
        "-vf", "fps=10,format=yuv420p", "-t", "12", "-shortest", str(video),
    ], check=True)
    return video


def _sample_runbook(approved=True):
    return {
        "title": "Look up invoice",
        "goal": "Open an invoice by ID and submit it for approval",
        "applications": ["Browser"],
        "preconditions": ["Signed in"],
        "parameters": [
            {"name": "invoice_id", "description": "Invoice ID", "example_from_video": "ACME-0042", "sensitive": False},
            {"name": "pin", "description": "Approval PIN", "example_from_video": "", "sensitive": True},
        ],
        "steps": [
            {"id": 1, "intent": "Enter the invoice ID", "action_type": "type", "target": "Invoice ID box",
             "value": "{{invoice_id}}", "expected_result": "ID shown", "evidence_t": 3.0,
             "requires_confirmation": False, "uncertainty": ""},
            {"id": 2, "intent": "Submit", "action_type": "click", "target": "Submit button",
             "value": "", "expected_result": "Submitted banner", "evidence_t": 9.0,
             "requires_confirmation": True, "uncertainty": ""},
        ],
        "success_criteria": ["Banner reads Submitted"],
        "open_questions": [],
        "_meta": {"approved": approved},
    }


# ---------- extract ----------

@needs_ffmpeg
def test_extract_keeps_one_frame_per_ui_state(screen_video, tmp_path):
    work = tmp_path / "work"
    m = extract(screen_video, work, fps=2.0, max_gap_s=10.0)
    ts = [f["t"] for f in m["frames"]]
    assert m["meta"]["has_audio"] and (work / m["audio"]).exists()
    # 4 states change at t=0,3,6,9 (+ the forced last frame). Frame sampling at 2 fps
    # means each change is seen within 0.5 s of when it happens.
    assert len(ts) == 5, ts
    for want, got in zip([0, 3, 6, 9], ts):
        assert want <= got <= want + 0.5, ts
    assert all((work / f["path"]).exists() for f in m["frames"])
    # Resumable: a second call returns the checkpoint without re-running ffmpeg.
    assert extract(screen_video, work) == m


@needs_ffmpeg
def test_extract_respects_max_frames(screen_video, tmp_path):
    m = extract(screen_video, tmp_path / "w", fps=2.0, max_frames=3)
    ts = [f["t"] for f in m["frames"]]
    # Ends always kept; of the middle changes, the success page (whole screen) is
    # the largest, so it survives over the typed text and the dialog.
    assert len(ts) == 3 and ts[0] == 0.0 and ts[-1] == 11.5
    assert 9.0 <= ts[1] <= 9.5, ts


def test_trim_prefers_large_changes():
    kept = [(0, 10**9), (5, 3), (9, 40), (14, 2), (20, 12), (30, 10**9)]
    assert trim(kept, 4) == [0, 9, 20, 30]
    assert trim(kept, 10) == [0, 5, 9, 14, 20, 30]


def test_small_typed_text_counts_as_a_change():
    blank = _ui_state(lambda d: d.rectangle([50, 80, 400, 110], outline="black"), size=(1920, 1080))
    typed = blank.copy()
    ImageDraw.Draw(typed).text((55, 88), "ACME-0042", fill="black")
    assert changed_blocks(blank.convert("L"), typed.convert("L")) >= 2
    assert changed_blocks(blank.convert("L"), blank.convert("L")) == 0


# ---------- transcript ----------

def test_parse_vtt_handles_teams_voice_tags():
    vtt = """WEBVTT

1
00:00:01.000 --> 00:00:03.500
<v Jane Doe>Open the invoices page.</v>

2
00:00:04.000 --> 00:00:06.000
<v Jane Doe>Type the invoice number.</v>
"""
    segs = parse_vtt(vtt)
    assert segs == [
        {"start": 1.0, "end": 3.5, "text": "Open the invoices page."},
        {"start": 4.0, "end": 6.0, "text": "Type the invoice number."},
    ]
    assert narration_between(segs, 3.0, 5.0) == "Open the invoices page. Type the invoice number."
    assert narration_between(segs, 6.0, 9.0) == ""


# ---------- runbook ----------

def test_schema_is_strict_everywhere():
    def walk(node):
        if node.get("type") == "object":
            assert node["additionalProperties"] is False
            assert set(node["required"]) == set(node["properties"])
            for v in node["properties"].values():
                walk(v)
        if node.get("type") == "array":
            walk(node["items"])
    walk(RUNBOOK_SCHEMA)


def test_validate_flags_bad_runbooks():
    rb = _sample_runbook()
    assert validate(rb) == []
    rb["steps"][0]["value"] = "{{order_no}}"
    rb["parameters"][1]["example_from_video"] = "1234"
    rb["steps"][1]["id"] = 5
    problems = validate(rb)
    assert len(problems) == 3, problems


def test_markdown_and_render_withhold_secrets():
    rb = _sample_runbook()
    md = to_markdown(rb)
    assert "| `invoice_id` |" in md and "**yes**" in md
    text = render_runbook(rb, {"invoice_id": "INV-9", "pin": "424242"})
    assert "INV-9" in text and "{{invoice_id}}" not in text
    assert "424242" not in text
    assert unresolved_params(rb, {"invoice_id": "x"}) == ["pin"]


# ---------- synthesize (fake model) ----------

class _FakeStream:
    def __init__(self, msg, sink, kwargs):
        self.msg, sink["kwargs"] = msg, kwargs

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def get_final_message(self):
        return self.msg


@needs_ffmpeg
def test_synthesize_sends_interleaved_frames_and_writes_runbook(screen_video, tmp_path):
    work = tmp_path / "w"
    manifest = extract(screen_video, work)
    transcript = {"source": "test", "segments": [{"start": 2.5, "end": 3.2, "text": "type the ID"}]}
    rb = {k: v for k, v in _sample_runbook().items() if k != "_meta"}
    msg = SimpleNamespace(
        content=[SimpleNamespace(type="text", text=json.dumps(rb))], stop_reason="end_turn",
        stop_details=None, model="claude-opus-5-5", usage=SimpleNamespace(input_tokens=1, output_tokens=1),
    )
    sink = {}
    client = SimpleNamespace(beta=SimpleNamespace(messages=SimpleNamespace(
        stream=lambda **kw: _FakeStream(msg, sink, kw))))
    out = synthesize(work, manifest, transcript, client=client)

    content = sink["kwargs"]["messages"][0]["content"]
    images = [c for c in content if c["type"] == "image"]
    assert len(images) == len(manifest["frames"])
    assert any("type the ID" in c.get("text", "") for c in content)
    assert sink["kwargs"]["output_config"]["format"]["schema"] is RUNBOOK_SCHEMA
    assert out["_meta"]["approved"] is False and out["_meta"]["problems"] == []
    assert (work / "runbook.md").exists()


# ---------- computer + execute ----------

def test_key_mapping():
    assert to_playwright_key("ctrl+shift+t") == "Control+Shift+t"
    assert to_playwright_key("Return") == "Enter"
    assert to_playwright_key("f5") == "F5"
    assert to_playwright_key("super+l") == "Meta+l"


class _FakeComputer(Computer):
    width, height = 100, 100

    def __init__(self):
        self.calls = []

    def screenshot_png(self):
        return b"\x89PNG"

    def perform(self, action, params):
        self.calls.append((action, params))


def test_out_of_bounds_click_is_rejected():
    with pytest.raises(ToolError):
        _FakeComputer().run({"action": "left_click", "coordinate": [500, 5]})


def _tool_use(i, name, inp):
    return SimpleNamespace(type="tool_use", id=f"tu_{i}", name=name, input=inp)


class _ScriptedModel:
    """Plays back one assistant turn per call and records each request."""

    def __init__(self, turns):
        self.turns, self.requests = list(turns), []
        self.beta = SimpleNamespace(messages=SimpleNamespace(create=self.create))

    def create(self, **kw):
        self.requests.append({**kw, "messages": list(kw["messages"])})  # loop mutates the list
        content = self.turns.pop(0)
        stop = "tool_use" if any(b.type == "tool_use" for b in content) else "end_turn"
        return SimpleNamespace(content=content, stop_reason=stop, stop_details=None)


def _page_html():
    return """<html><body style="margin:0">
<input id="inv" style="position:absolute;left:20px;top:20px;width:200px;height:30px">
<button id="go" style="position:absolute;left:20px;top:80px;width:100px;height:30px"
  onclick="document.getElementById('msg').innerText='Submitted '+document.getElementById('inv').value">Submit</button>
<div id="msg" style="position:absolute;left:20px;top:140px"></div></body></html>"""


@pytest.mark.skipif(not os.path.exists(CHROMIUM), reason="chromium not available")
def test_agent_loop_drives_a_real_browser(tmp_path):
    from video2cua.computer import PlaywrightComputer

    page = tmp_path / "app.html"
    page.write_text(_page_html())
    model = _ScriptedModel([
        [_tool_use(1, "computer", {"action": "screenshot"})],
        [_tool_use(2, "computer", {"action": "left_click", "coordinate": [100, 35]}),
         _tool_use(3, "computer", {"action": "type", "text": "INV-9"})],
        [_tool_use(4, "report_step", {"step_id": 1, "status": "done", "note": ""}),
         _tool_use(5, "request_confirmation", {"step_id": 2, "summary": "Click Submit for INV-9"})],
        [_tool_use(6, "computer", {"action": "left_click", "coordinate": [70, 95]})],
        [_tool_use(7, "report_step", {"step_id": 2, "status": "done", "note": ""}),
         _tool_use(8, "finish", {"outcome": "success", "summary": "submitted"})],
    ])
    asked = []
    comp = PlaywrightComputer(320, 200, start_url=page.as_uri(), executable_path=CHROMIUM)
    try:
        result = run(_sample_runbook(), {"invoice_id": "INV-9", "pin": "1"}, comp, tmp_path / "log",
                     client=model, confirm=lambda s, t: (asked.append(s) or (True, "")))
        assert comp.page.inner_text("#msg") == "Submitted INV-9"
    finally:
        comp.close()

    assert result["outcome"] == "success" and result["turns"] == 5
    assert result["steps"] == {1: {"status": "done", "note": ""}, 2: {"status": "done", "note": ""}}
    assert asked == [2]
    req = model.requests[0]
    assert req["betas"][0] == "computer-use-2025-11-24"
    assert req["tools"][0]["type"] == "computer_20251124"
    assert req["tools"][0]["display_width_px"] == 320
    # Every tool_use in a turn is answered in one user message, screenshots included.
    second_reply = model.requests[2]["messages"][-1]["content"]
    assert [r["tool_use_id"] for r in second_reply] == ["tu_2", "tu_3"]
    assert second_reply[0]["content"][-1]["type"] == "image"
    assert len(list((tmp_path / "log").glob("shot_*.png"))) == 4


def test_denied_confirmation_and_secret_typing(tmp_path):
    comp = _FakeComputer()
    model = _ScriptedModel([
        [_tool_use(1, "type_secret", {"param": "pin"}),
         _tool_use(2, "type_secret", {"param": "invoice_id"}),
         _tool_use(3, "request_confirmation", {"step_id": 2, "summary": "Submit"})],
        [_tool_use(4, "finish", {"outcome": "blocked", "summary": "operator declined"})],
    ])
    result = run(_sample_runbook(), {"invoice_id": "A", "pin": "9999"}, comp, tmp_path,
                 client=model, confirm=lambda s, t: (False, "not today"))
    assert comp.calls == [("type", {"text": "9999"})]
    replies = model.requests[1]["messages"][-1]["content"]
    assert replies[1]["is_error"] is True                     # non-secret param refused
    assert replies[2]["content"].startswith("denied: not today")
    assert result["outcome"] == "blocked"
    assert "9999" not in (tmp_path / "log.jsonl").read_text()  # secret never logged


def test_unapproved_runbook_is_refused(tmp_path):
    with pytest.raises(RuntimeError, match="not approved"):
        run(_sample_runbook(approved=False), {"invoice_id": "A", "pin": "1"}, _FakeComputer(), tmp_path,
            client=_ScriptedModel([]))
