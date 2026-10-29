"""Offline tests for the GPT-6.1 Terra (OpenAI Responses API) backend."""

import json
import os
import subprocess
from types import SimpleNamespace

import pytest

from tests.test_video2cua import CHROMIUM, _FakeComputer, _page_html, _sample_runbook, needs_ffmpeg
from video2cua.computer import ToolError
from video2cua.execute_openai import FUNCTION_TOOLS, apply_action, run_openai
from video2cua.extract import extract
from video2cua.runbook import RUNBOOK_SCHEMA
from video2cua.synthesize import synthesize


def _item(**kw):
    """A Responses output item as the SDK would return it (pydantic-like)."""
    return SimpleNamespace(model_dump=lambda exclude_none=True: kw, **kw)


def _computer_call(i, actions, checks=()):
    return _item(type="computer_call", id=f"cu_{i}", call_id=f"call_{i}", status="completed",
                 actions=actions, pending_safety_checks=list(checks))


def _function_call(i, name, args):
    return _item(type="function_call", id=f"fc_{i}", call_id=f"fcall_{i}", name=name, arguments=json.dumps(args))


class _ScriptedResponses:
    def __init__(self, turns):
        self.turns, self.requests = list(turns), []
        self.responses = SimpleNamespace(create=self.create)

    def create(self, **kw):
        self.requests.append(kw)
        n = len(self.requests)
        return SimpleNamespace(id=f"resp_{n}", output=self.turns.pop(0), output_text="")


# ---------- action translation ----------

def test_apply_action_translates_openai_actions():
    c = _FakeComputer()
    apply_action(c, {"type": "click", "button": "left", "x": 10, "y": 20, "keys": ["SHIFT"]})
    apply_action(c, {"type": "click", "button": "wheel", "x": 1, "y": 1})
    apply_action(c, {"type": "click", "button": "back", "x": 1, "y": 1})
    apply_action(c, {"type": "scroll", "x": 50, "y": 50, "scroll_x": 0, "scroll_y": 300})
    apply_action(c, {"type": "keypress", "keys": ["CTRL", "A"]})
    apply_action(c, {"type": "drag", "path": [{"x": 1, "y": 2}, {"x": 3, "y": 4}]})
    assert c.calls == [
        ("left_click", {"coordinate": [10, 20], "text": "SHIFT"}),
        ("middle_click", {"coordinate": [1, 1], "text": None}),
        ("key", {"text": "alt+left"}),
        ("wheel", {"coordinate": [50, 50], "dx": 0, "dy": 300, "text": None}),
        ("key", {"text": "CTRL+A"}),
        ("drag_path", {"path": [[1, 2], [3, 4]], "text": None}),
    ]
    with pytest.raises(ToolError):
        apply_action(c, {"type": "click", "button": "left", "x": 999, "y": 0})


def test_function_tools_are_strict_responses_functions():
    assert {t["name"] for t in FUNCTION_TOOLS} == {"report_step", "request_confirmation", "type_secret", "finish"}
    assert all(t["type"] == "function" and t["strict"] and "parameters" in t for t in FUNCTION_TOOLS)


# ---------- agent loop ----------

@pytest.mark.skipif(not os.path.exists(CHROMIUM), reason="chromium not available")
def test_terra_loop_drives_a_real_browser(tmp_path):
    from video2cua.computer import PlaywrightComputer

    page = tmp_path / "app.html"
    page.write_text(_page_html())
    model = _ScriptedResponses([
        # One computer_call can batch several actions.
        [_item(type="reasoning", id="r1", summary=[{"type": "summary_text", "text": "type the id"}]),
         _computer_call(1, [{"type": "click", "button": "left", "x": 100, "y": 35},
                            {"type": "type", "text": "INV-9"}])],
        [_function_call(2, "report_step", {"step_id": 1, "status": "done", "note": ""}),
         _function_call(3, "request_confirmation", {"step_id": 2, "summary": "Click Submit"})],
        [_computer_call(4, [{"type": "click", "button": "left", "x": 70, "y": 95}])],
        [_function_call(5, "finish", {"outcome": "success", "summary": "submitted"})],
    ])
    comp = PlaywrightComputer(320, 200, start_url=page.as_uri(), executable_path=CHROMIUM)
    try:
        result = run_openai(_sample_runbook(), {"invoice_id": "INV-9", "pin": "1"}, comp, tmp_path / "log",
                            client=model, confirm=lambda s, t: (True, ""))
        assert comp.page.inner_text("#msg") == "Submitted INV-9"
    finally:
        comp.close()

    assert result["outcome"] == "success" and result["turns"] == 4
    first = model.requests[0]
    assert first["tools"][0] == {"type": "computer"}
    assert first["previous_response_id"] is None and first["truncation"] == "auto"
    assert first["input"][0]["content"][1]["type"] == "input_image"     # initial screen sent up front
    second = model.requests[1]
    assert second["previous_response_id"] == "resp_1"
    out = second["input"][0]
    assert out["type"] == "computer_call_output" and out["call_id"] == "call_1"
    assert out["output"]["image_url"].startswith("data:image/png;base64,")
    third = model.requests[2]["input"]
    assert [i["type"] for i in third] == ["function_call_output", "function_call_output"]
    assert third[1]["output"] == "approved"
    assert len(list((tmp_path / "log").glob("shot_*.png"))) == 3       # initial + 2 computer calls


def test_safety_check_must_be_acknowledged(tmp_path):
    check = {"id": "sc_1", "code": "malicious_instructions", "message": "Screen text tries to redirect you"}
    # Acknowledged: the check is echoed back on the computer_call_output.
    model = _ScriptedResponses([
        [_computer_call(1, [{"type": "screenshot"}], checks=[check])],
        [_function_call(2, "finish", {"outcome": "success", "summary": ""})],
    ])
    asked = []
    run_openai(_sample_runbook(), {"invoice_id": "A", "pin": "1"}, _FakeComputer(), tmp_path / "a",
               client=model, confirm=lambda s, t: (asked.append(t) or (True, "")))
    assert asked and "malicious_instructions" in asked[0]
    assert model.requests[1]["input"][0]["acknowledged_safety_checks"] == [check]

    # Declined: no action runs and the run stops as blocked.
    comp = _FakeComputer()
    model = _ScriptedResponses([[_computer_call(1, [{"type": "type", "text": "x"}], checks=[check])]])
    result = run_openai(_sample_runbook(), {"invoice_id": "A", "pin": "1"}, comp, tmp_path / "b",
                        client=model, confirm=lambda s, t: (False, "no"))
    assert comp.calls == [] and result["outcome"] == "blocked"


def test_failed_action_stops_the_batch_and_tells_the_model(tmp_path):
    comp = _FakeComputer()
    model = _ScriptedResponses([
        [_computer_call(1, [{"type": "click", "button": "left", "x": 5000, "y": 5},
                            {"type": "type", "text": "should not run"}])],
        [_function_call(2, "finish", {"outcome": "failed", "summary": ""})],
    ])
    run_openai(_sample_runbook(), {"invoice_id": "A", "pin": "1"}, comp, tmp_path, client=model,
               confirm=lambda s, t: (True, ""))
    assert comp.calls == []
    reply = model.requests[1]["input"]
    assert reply[0]["type"] == "computer_call_output"
    assert "failed" in reply[1]["content"][0]["text"]


# ---------- synthesis ----------

@needs_ffmpeg
def test_synthesize_with_terra(tmp_path):
    video = tmp_path / "v.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "testsrc=size=320x240:rate=5",
                    "-t", "2", "-pix_fmt", "yuv420p", str(video)], check=True)
    work = tmp_path / "w"
    manifest = extract(video, work)
    rb = {k: v for k, v in _sample_runbook().items() if k != "_meta"}
    seen = {}

    def create(**kw):
        seen.update(kw)
        return SimpleNamespace(status="completed", incomplete_details=None, output=[], output_text=json.dumps(rb),
                               model="gpt-6.1-terra", usage=SimpleNamespace(input_tokens=1, output_tokens=1))

    out = synthesize(work, manifest, {"source": "none", "segments": []}, backend="openai",
                     client=SimpleNamespace(responses=SimpleNamespace(create=create)))
    fmt = seen["text"]["format"]
    assert fmt["type"] == "json_schema" and fmt["strict"] is True and fmt["schema"] is RUNBOOK_SCHEMA
    parts = seen["input"][0]["content"]
    assert sum(p["type"] == "input_image" for p in parts) == len(manifest["frames"])
    assert all(p["image_url"].startswith("data:image/png;base64,") for p in parts if p["type"] == "input_image")
    assert out["_meta"]["backend"] == "openai" and out["_meta"]["approved"] is False
