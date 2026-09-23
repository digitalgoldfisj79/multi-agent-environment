"""CLI: ``python -m harness`` runs every scenario; ``python -m harness serve`` starts the UI."""

import argparse
import sys

from harness.runner import run_all, run_scenario
from harness.scenarios import SCENARIOS


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python -m harness")
    sub = parser.add_subparsers(dest="cmd")
    run = sub.add_parser("run", help="run scenarios (default)")
    run.add_argument("scenario", nargs="?", choices=sorted(SCENARIOS))
    run.add_argument("--steps", type=int)
    run.add_argument("--seed", type=int, default=0)
    srv = sub.add_parser("serve", help="start the web UI")
    srv.add_argument("--host", default="127.0.0.1")
    srv.add_argument("--port", type=int, default=8000)
    args = parser.parse_args(argv)

    if args.cmd == "serve":
        from harness.server import serve
        serve(args.host, args.port)
        return 0

    seed = getattr(args, "seed", 0)
    if getattr(args, "scenario", None):
        traces = [run_scenario(args.scenario, args.steps, seed)]
    else:
        traces = run_all(seed)
    for t in traces:
        print(f"{'PASS' if t['passed'] else 'FAIL'}  {t['scenario']}")
        for c in t["checks"]:
            print(f"    {'ok ' if c['passed'] else 'BAD'} {c['name']}: {c['detail']}")
    return 0 if all(t["passed"] for t in traces) else 1


if __name__ == "__main__":
    sys.exit(main())
