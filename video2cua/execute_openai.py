"""Stage 4, OpenAI backend: follow an approved runbook with GPT-6.1 Terra.

Uses the Responses API's GA `computer` tool. Each computer_call can carry a
batch of actions; we perform them in order, then answer with one screenshot.
The custom tools (report_step, request_confirmation, type_secret, finish) are
the same as the Claude backend's, declared as function tools.
"""

import base64
import json
from pathlib import Path
from typing import Callable

from . import azure_openai
from .computer import Computer, ToolError
from .execute import CUSTOM_TOOLS, SYSTEM, TOOL_ERRORS, Session, render_runbook, terminal_confirm

FUNCTION_TOOLS = [
    {"type": "function", "name": t["name"], "description": t["description"],
     "parameters": t["input_schema"], "strict": True}
    for t in CUSTOM_TOOLS
]

# OpenAI's `wait` action has no duration.
WAIT_S = 2


def _xy(computer: Computer, a: dict) -> list[int]:
    xy = [a["x"], a["y"]]
    computer.check_xy(xy)
    return xy


def apply_action(computer: Computer, a: dict) -> None:
    """Translate one OpenAI computer action into Computer.perform calls."""
    kind = a["type"]
    mods = "+".join(a.get("keys") or [])
    if kind == "click":
        button = a.get("button", "left")
        if button in ("back", "forward"):
            computer.perform("key", {"text": "alt+left" if button == "back" else "alt+right"})
            return
        action = {"left": "left_click", "right": "right_click", "wheel": "middle_click"}[button]
        computer.perform(action, {"coordinate": _xy(computer, a), "text": mods or None})
    elif kind == "double_click":
        computer.perform("double_click", {"coordinate": _xy(computer, a), "text": mods or None})
    elif kind == "move":
        computer.perform("mouse_move", {"coordinate": _xy(computer, a)})
    elif kind == "drag":
        computer.perform("drag_path", {"path": [[p["x"], p["y"]] for p in a["path"]], "text": mods or None})
    elif kind == "scroll":
        computer.perform("wheel", {"coordinate": _xy(computer, a), "dx": a.get("scroll_x", 0),
                                   "dy": a.get("scroll_y", 0), "text": mods or None})
    elif kind == "keypress":
        computer.perform("key", {"text": "+".join(a["keys"])})
    elif kind == "type":
        computer.perform("type", {"text": a["text"]})
    elif kind == "wait":
        computer.perform("wait", {"duration": WAIT_S})
    elif kind == "screenshot":
        pass
    else:
        raise ToolError(f"unsupported action {kind!r}")


def _data_url(png: bytes) -> str:
    return "data:image/png;base64," + base64.standard_b64encode(png).decode()


def _dump(obj) -> dict:
    return obj.model_dump(exclude_none=True) if hasattr(obj, "model_dump") else dict(obj)


def run_openai(rb: dict, values: dict, computer: Computer, log_dir: Path, client=None,
               confirm: Callable[[int, str], tuple[bool, str]] = terminal_confirm,
               max_turns: int = 80, require_approved: bool = True) -> dict:
    session = Session(rb, values, computer, log_dir, confirm, require_approved)
    client = client or azure_openai.make_client()
    first = computer.screenshot_png()
    session.save_shot(first)
    next_input = [{"role": "user", "content": [
        {"type": "input_text", "text": render_runbook(rb, values).replace(
            "Start by taking a screenshot.", "The current screen is attached.")},
        {"type": "input_image", "image_url": _data_url(first), "detail": "original"},
    ]}]
    prev_id = None

    try:
        for turn in range(max_turns):
            session.result["turns"] = turn + 1
            resp = client.responses.create(
                model=azure_openai.AGENT_DEPLOYMENT,
                instructions=SYSTEM,
                input=next_input,
                previous_response_id=prev_id,
                tools=[{"type": "computer"}, *FUNCTION_TOOLS],
                reasoning={"effort": "high", "summary": "auto"},
                truncation="auto",
            )
            prev_id = resp.id
            next_input, acted = [], False

            for item in resp.output:
                item = _dump(item)
                kind = item["type"]
                if kind == "reasoning":
                    for s in item.get("summary", []):
                        session.record(kind="reasoning", text=s.get("text", ""))
                elif kind == "message":
                    for part in item.get("content", []):
                        if part["type"] == "refusal":
                            session.result.update(outcome="failed", summary=f"model declined: {part.get('refusal')}")
                            session.done = True
                        elif part["type"] == "output_text":
                            session.record(kind="text", text=part["text"])
                elif kind == "computer_call":
                    acted = True
                    next_input.extend(_computer_call(session, item))
                elif kind == "function_call":
                    acted = True
                    try:
                        out = session.handle(item["name"], json.loads(item["arguments"]))
                    except (*TOOL_ERRORS, json.JSONDecodeError) as e:
                        session.record(kind="tool_error", name=item["name"], error=str(e))
                        out = f"error: {e}"
                    next_input.append({"type": "function_call_output", "call_id": item["call_id"], "output": out})

            if session.done:
                break
            if not acted:
                session.result["summary"] = getattr(resp, "output_text", "") or session.result["summary"]
                break
    finally:
        result = session.close()
    return result


def _computer_call(session: Session, item: dict) -> list[dict]:
    """Perform a computer_call's actions; return the items that answer it."""
    checks = item.get("pending_safety_checks") or []
    if checks:
        # The API flagged something (e.g. a possible prompt injection on screen).
        # Nothing runs until a person acknowledges every check.
        text = "; ".join(f"{c.get('code')}: {c.get('message')}" for c in checks)
        ok, why = session.confirm(0, f"[safety check] {text}")
        session.record(kind="safety_check", checks=checks, approved=ok, reason=why)
        if not ok:
            session.result.update(outcome="blocked", summary=f"safety check not acknowledged: {text}")
            session.done = True
            return []

    actions = item.get("actions") or ([item["action"]] if item.get("action") else [])
    error = None
    for a in actions:
        session.record(kind="computer_action", input=a)
        try:
            apply_action(session.computer, a)
        except TOOL_ERRORS as e:
            # Stop the batch at the first failure: later actions assumed it worked.
            error = f"action {a.get('type')} failed: {e}. Later actions in that batch were not run."
            session.record(kind="tool_error", name="computer", error=error)
            break

    png = session.computer.screenshot_png()
    session.save_shot(png)
    out = [{
        "type": "computer_call_output",
        "call_id": item["call_id"],
        "output": {"type": "computer_screenshot", "image_url": _data_url(png)},
    }]
    if checks:
        out[0]["acknowledged_safety_checks"] = [{"id": c["id"], "code": c.get("code"), "message": c.get("message")}
                                               for c in checks]
    if error:
        out.append({"role": "user", "content": [{"type": "input_text", "text": error}]})
    return out
