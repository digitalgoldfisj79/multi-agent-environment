"""Executors for the computer_20251124 tool's actions.

The model only proposes actions; something has to perform them. Computer is the
interface the agent loops call. Its action vocabulary is the Claude
computer_20251124 one plus two extras (wheel, drag_path) that the OpenAI
computer tool's pixel scrolls and multi-point drags need. PlaywrightComputer drives a Chromium page whose
viewport is the "screen", which covers browser-based line-of-business apps. For
desktop apps, implement Computer over xdotool in a Linux VM (Anthropic's
reference computer-use-demo does this) or over a Windows VM's input API.

Run any implementation inside a disposable, isolated VM or container, never on
a colleague's own machine.
"""

import base64
import time
from abc import ABC, abstractmethod

# computer_20251124 actions, per Anthropic's reference implementation.
ACTIONS = {
    "screenshot", "cursor_position", "mouse_move", "left_click", "right_click", "middle_click",
    "double_click", "triple_click", "left_click_drag", "left_mouse_down", "left_mouse_up",
    "scroll", "type", "key", "hold_key", "wait", "zoom",
}


class ToolError(Exception):
    pass


class Computer(ABC):
    width: int
    height: int

    @abstractmethod
    def screenshot_png(self) -> bytes: ...

    @abstractmethod
    def perform(self, action: str, params: dict) -> str | None:
        """Perform a non-screenshot action. Returns optional text for the model."""

    def zoom_png(self, region) -> bytes:
        raise ToolError("zoom is not supported by this computer")

    def run(self, params: dict) -> list[dict]:
        """Execute one tool_use input and return tool_result content blocks."""
        action = params.get("action")
        if action not in ACTIONS:
            raise ToolError(f"unsupported action {action!r}")
        for key in ("coordinate", "start_coordinate"):
            if key in params:
                self.check_xy(params[key])
        if action == "zoom":
            region = params.get("region")
            if not (isinstance(region, (list, tuple)) and len(region) == 4
                    and region[0] < region[2] and region[1] < region[3]):
                raise ToolError(f"region must be [x0, y0, x1, y1] with x0 < x1 and y0 < y1, got {region!r}")
            return [self.image_block(self.zoom_png(region))]
        text = None if action == "screenshot" else self.perform(action, params)
        blocks = [{"type": "text", "text": text}] if text else []
        # Return a fresh screenshot after every action so the model sees its effect.
        blocks.append(self.image_block(self.screenshot_png()))
        return blocks

    def check_xy(self, xy) -> None:
        if not (isinstance(xy, (list, tuple)) and len(xy) == 2):
            raise ToolError(f"coordinate must be [x, y], got {xy!r}")
        x, y = xy
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise ToolError(f"coordinate {xy} outside the {self.width}x{self.height} screen")

    @staticmethod
    def image_block(png: bytes) -> dict:
        return {"type": "image", "source": {"type": "base64", "media_type": "image/png",
                                            "data": base64.standard_b64encode(png).decode()}}


# xdotool-style key names (what the model emits) -> Playwright key names.
_KEYMAP = {
    "ctrl": "Control", "control": "Control", "alt": "Alt", "shift": "Shift",
    "super": "Meta", "cmd": "Meta", "meta": "Meta", "win": "Meta",
    "return": "Enter", "enter": "Enter", "kp_enter": "Enter", "esc": "Escape", "escape": "Escape",
    "tab": "Tab", "backspace": "Backspace", "delete": "Delete", "space": " ",
    "up": "ArrowUp", "down": "ArrowDown", "left": "ArrowLeft", "right": "ArrowRight",
    "page_up": "PageUp", "prior": "PageUp", "page_down": "PageDown", "next": "PageDown",
    "home": "Home", "end": "End", "insert": "Insert",
    "arrowup": "ArrowUp", "arrowdown": "ArrowDown", "arrowleft": "ArrowLeft", "arrowright": "ArrowRight",
    "pageup": "PageUp", "pagedown": "PageDown", "option": "Alt", "del": "Delete",
}


def to_playwright_key(combo: str) -> str:
    """'ctrl+shift+t' -> 'Control+Shift+t', 'Return' -> 'Enter', 'F5' -> 'F5'."""
    parts = []
    for p in combo.split("+"):
        low = p.strip().lower()
        if low in _KEYMAP:
            parts.append(_KEYMAP[low])
        elif len(low) > 1 and low[0] == "f" and low[1:].isdigit():
            parts.append(low.upper())
        else:
            parts.append(p.strip())
    return "+".join(parts)


class PlaywrightComputer(Computer):
    def __init__(self, width: int = 1280, height: int = 800, start_url: str | None = None,
                 headless: bool = True, executable_path: str | None = None):
        from playwright.sync_api import sync_playwright

        self.width, self.height = width, height
        self._pw = sync_playwright().start()
        launch = {"headless": headless}
        if executable_path:
            launch["executable_path"] = executable_path
        self._browser = self._pw.chromium.launch(**launch)
        self.page = self._browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
        self._cursor = (0, 0)
        if start_url:
            self.page.goto(start_url)

    def close(self) -> None:
        self._browser.close()
        self._pw.stop()

    def screenshot_png(self) -> bytes:
        return self.page.screenshot(type="png")

    def _move(self, xy) -> None:
        self.page.mouse.move(*xy)
        self._cursor = tuple(xy)

    def _with_modifier(self, params, fn) -> None:
        # Modifier keys held during a click arrive in `text` (e.g. "shift").
        mod = params.get("text") or params.get("key")
        keys = to_playwright_key(mod).split("+") if mod else []
        for k in keys:
            self.page.keyboard.down(k)
        try:
            fn()
        finally:
            for k in reversed(keys):
                self.page.keyboard.up(k)

    def perform(self, action: str, p: dict) -> str | None:
        m, kb = self.page.mouse, self.page.keyboard
        if "coordinate" in p and action not in ("left_click_drag", "scroll", "wheel"):
            self._move(p["coordinate"])

        if action == "cursor_position":
            return f"X={self._cursor[0]},Y={self._cursor[1]}"
        if action == "mouse_move":
            return None
        if action in ("left_click", "right_click", "middle_click", "double_click", "triple_click"):
            button = {"right_click": "right", "middle_click": "middle"}.get(action, "left")
            count = {"double_click": 2, "triple_click": 3}.get(action, 1)
            self._with_modifier(p, lambda: m.click(*self._cursor, button=button, click_count=count))
        elif action == "left_click_drag":
            if "start_coordinate" not in p or "coordinate" not in p:
                raise ToolError("left_click_drag needs start_coordinate and coordinate")
            self._move(p["start_coordinate"])
            m.down()
            self._move(p["coordinate"])
            m.up()
        elif action == "left_mouse_down":
            m.down()
        elif action == "left_mouse_up":
            m.up()
        elif action == "scroll":
            if "coordinate" in p:
                self._move(p["coordinate"])
            direction, amount = p.get("scroll_direction"), int(p.get("scroll_amount", 3))
            step = 100 * amount
            dx, dy = {"up": (0, -step), "down": (0, step), "left": (-step, 0), "right": (step, 0)}.get(direction, (None, None))
            if dx is None:
                raise ToolError(f"scroll_direction must be up/down/left/right, got {direction!r}")
            self._with_modifier(p, lambda: m.wheel(dx, dy))
        elif action == "wheel":
            # Pixel deltas, as the OpenAI computer tool sends them.
            if "coordinate" in p:
                self._move(p["coordinate"])
            self._with_modifier(p, lambda: m.wheel(int(p.get("dx", 0)), int(p.get("dy", 0))))
        elif action == "drag_path":
            points = p["path"]
            if len(points) < 2:
                raise ToolError("drag path needs at least two points")
            for pt in points:
                self.check_xy(pt)

            def drag():
                self._move(points[0])
                m.down()
                for pt in points[1:]:
                    self._move(pt)
                m.up()
            self._with_modifier(p, drag)
        elif action == "type":
            kb.type(p["text"], delay=10)
        elif action == "key":
            kb.press(to_playwright_key(p["text"]))
        elif action == "hold_key":
            keys = to_playwright_key(p["text"]).split("+")
            for k in keys:
                kb.down(k)
            time.sleep(min(float(p.get("duration", 1)), 10))
            for k in reversed(keys):
                kb.up(k)
        elif action == "wait":
            time.sleep(min(float(p.get("duration", 1)), 30))
        return None

    def zoom_png(self, region) -> bytes:
        x0, y0, x1, y1 = region
        return self.page.screenshot(type="png", clip={"x": x0, "y": y0, "width": x1 - x0, "height": y1 - y0})
