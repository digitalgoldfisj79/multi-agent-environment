import traceback

from harness.scenarios import SCENARIOS


def snapshot(env, step):
    return {
        "step": step,
        "agents": [
            {
                "name": a.name,
                "type": type(a).__name__,
                "position": list(a.get_position()),
                "state": dict(a.get_state()),
            }
            for a in env.agents
        ],
    }


def run_scenario(name, steps=None, seed=0):
    """Run a scenario and return its trace plus check results.

    Frame 0 is the initial state; an exception during a tick stops the run
    and is recorded in ``error`` rather than raised.
    """
    spec = SCENARIOS[name]
    steps = spec["default_steps"] if steps is None else steps
    env, checks = spec["build"](seed)

    trace = {"scenario": name, "seed": seed, "steps": steps,
             "frames": [snapshot(env, 0)], "error": None, "traceback": None}
    for step in range(1, steps + 1):
        try:
            env.update()
        except Exception as exc:
            trace["error"] = f"step {step}: {type(exc).__name__}: {exc}"
            trace["traceback"] = traceback.format_exc()
            break
        trace["frames"].append(snapshot(env, step))

    results = []
    for check in checks:
        try:
            passed, detail = check(trace)
        except Exception as exc:
            passed, detail = False, f"check raised {type(exc).__name__}: {exc}"
        results.append({"name": check.__name__, "passed": bool(passed), "detail": detail})
    trace["checks"] = results
    trace["passed"] = all(r["passed"] for r in results)
    return trace


def run_all(seed=0):
    return [run_scenario(name, seed=seed) for name in SCENARIOS]
