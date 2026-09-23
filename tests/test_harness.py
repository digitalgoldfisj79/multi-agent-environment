import json
import threading
import unittest
import urllib.request
from http.server import ThreadingHTTPServer

from harness.runner import run_scenario
from harness.scenarios import SCENARIOS
from harness.server import Handler


class ScenarioTests(unittest.TestCase):
    def test_every_scenario_passes_its_checks(self):
        for name in SCENARIOS:
            with self.subTest(scenario=name):
                trace = run_scenario(name)
                self.assertTrue(trace["passed"], trace["checks"])

    def test_frame_count(self):
        trace = run_scenario("walkers", steps=4)
        self.assertEqual([f["step"] for f in trace["frames"]], [0, 1, 2, 3, 4])

    def test_random_walk_is_deterministic_per_seed(self):
        a = run_scenario("random_walk", seed=7)["frames"]
        b = run_scenario("random_walk", seed=7)["frames"]
        c = run_scenario("random_walk", seed=8)["frames"]
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)

    def test_faulty_error_is_captured_not_raised(self):
        trace = run_scenario("faulty")
        self.assertIn("RuntimeError", trace["error"])
        self.assertIn("Traceback", trace["traceback"])

    def test_failing_check_is_reported(self):
        # Too few steps for the chaser to reach its target
        trace = run_scenario("chase", steps=3)
        self.assertFalse(trace["passed"])


class ServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.base = f"http://127.0.0.1:{cls.httpd.server_address[1]}"
        threading.Thread(target=cls.httpd.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def request(self, path, body=None):
        data = None if body is None else json.dumps(body).encode()
        req = urllib.request.Request(self.base + path, data=data)
        try:
            with urllib.request.urlopen(req) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            return e.code, e.read()

    def test_index(self):
        status, body = self.request("/")
        self.assertEqual(status, 200)
        self.assertIn(b"<title>", body)

    def test_scenarios(self):
        status, body = self.request("/api/scenarios")
        self.assertEqual(status, 200)
        self.assertEqual({s["name"] for s in json.loads(body)}, set(SCENARIOS))

    def test_run(self):
        status, body = self.request("/api/run", {"scenario": "chase", "steps": 9})
        self.assertEqual(status, 200)
        self.assertEqual(len(json.loads(body)["frames"]), 10)

    def test_run_unknown_scenario(self):
        status, _ = self.request("/api/run", {"scenario": "nope"})
        self.assertEqual(status, 400)


if __name__ == "__main__":
    unittest.main()
