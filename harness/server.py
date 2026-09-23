"""Stdlib-only HTTP server for the harness UI.

GET  /                 -> the UI
GET  /api/scenarios    -> scenario list
POST /api/run          -> {"scenario", "steps"?, "seed"?} -> trace
POST /api/run_all      -> {"seed"?} -> [trace, ...]
POST /api/tests        -> run the unittest suite in tests/
"""

import io
import json
import os
import time
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from harness.runner import run_all, run_scenario
from harness.scenarios import SCENARIOS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UI_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui", "index.html")


class _Collector(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.records = []
        self._started = {}

    def startTest(self, test):
        self._started[test.id()] = time.perf_counter()
        super().startTest(test)

    def _record(self, test, status, detail=""):
        elapsed = time.perf_counter() - self._started.get(test.id(), time.perf_counter())
        self.records.append({"id": test.id(), "status": status,
                             "detail": detail, "ms": round(elapsed * 1000, 2)})

    def addSuccess(self, test):
        super().addSuccess(test)
        self._record(test, "pass")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self._record(test, "fail", self._exc_info_to_string(err, test))

    def addError(self, test, err):
        super().addError(test, err)
        self._record(test, "error", self._exc_info_to_string(err, test))

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self._record(test, "skip", reason)


def run_unit_tests():
    suite = unittest.defaultTestLoader.discover(os.path.join(ROOT, "tests"), top_level_dir=ROOT)
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, resultclass=_Collector, verbosity=0).run(suite)
    return {"tests": result.records, "ran": result.testsRun,
            "passed": result.wasSuccessful(), "output": stream.getvalue()}


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, content_type="application/json"):
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _body(self):
        length = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(length) or b"{}")

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            with open(UI_PATH, "rb") as f:
                self._send(200, f.read(), "text/html; charset=utf-8")
        elif self.path == "/api/scenarios":
            self._send(200, [{k: v for k, v in s.items() if k != "build"}
                             for s in SCENARIOS.values()])
        else:
            self._send(404, {"error": "not found"})

    def do_POST(self):
        try:
            body = self._body()
            if self.path == "/api/run":
                name = body.get("scenario")
                if name not in SCENARIOS:
                    return self._send(400, {"error": f"unknown scenario {name!r}"})
                steps = body.get("steps")
                steps = None if steps in (None, "") else max(0, min(int(steps), 1000))
                self._send(200, run_scenario(name, steps, int(body.get("seed", 0))))
            elif self.path == "/api/run_all":
                self._send(200, run_all(int(body.get("seed", 0))))
            elif self.path == "/api/tests":
                self._send(200, run_unit_tests())
            else:
                self._send(404, {"error": "not found"})
        except (ValueError, TypeError) as exc:
            self._send(400, {"error": str(exc)})

    def log_message(self, fmt, *args):
        pass


def serve(host="127.0.0.1", port=8000):
    httpd = ThreadingHTTPServer((host, port), Handler)
    print(f"Harness UI on http://{host}:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
