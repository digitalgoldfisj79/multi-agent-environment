"""Scenario registry.

A scenario builds a fresh environment and declares checks that are
evaluated against the recorded trace (a list of frames, see runner.py).
Each check is a function ``(trace) -> (passed, detail)``.
"""

from agent import Agent
from environment import MultiAgentEnvironment
from harness.behaviours import Chaser, Faulty, RandomWalker, Walker

SCENARIOS = {}


def scenario(name, description, steps=10):
    def register(fn):
        SCENARIOS[name] = {
            "name": name,
            "description": description,
            "default_steps": steps,
            "build": fn,
        }
        return fn

    return register


def positions(frame):
    return {a["name"]: tuple(a["position"]) for a in frame["agents"]}


def check_no_error(trace):
    return trace["error"] is None, trace["error"] or "no errors"


def check_static(trace):
    first = positions(trace["frames"][0])
    last = positions(trace["frames"][-1])
    moved = [n for n in first if first[n] != last[n]]
    return not moved, f"moved: {moved}" if moved else "all agents stayed put"


def check_unit_steps(trace):
    frames = trace["frames"]
    for prev, cur in zip(frames, frames[1:]):
        p, c = positions(prev), positions(cur)
        for name in c:
            dist = abs(c[name][0] - p[name][0]) + abs(c[name][1] - p[name][1])
            if dist != 1:
                return False, f"{name} moved {dist} cells at step {cur['step']}"
    return True, "every move was exactly one cell"


@scenario("baseline", "The main.py setup: two plain Agents that do nothing.")
def baseline(seed):
    env = MultiAgentEnvironment()
    env.add_agent(Agent("Agent1", (0, 0)))
    env.add_agent(Agent("Agent2", (1, 1)))
    return env, [check_no_error, check_static]


@scenario("walkers", "Two Walkers moving at constant velocity.")
def walkers(seed):
    env = MultiAgentEnvironment()
    env.add_agent(Walker("East", (0, 0), (1, 0)))
    env.add_agent(Walker("NorthEast", (0, 5), (1, -1)))

    def check_displacement(trace):
        steps = trace["frames"][-1]["step"]
        last = positions(trace["frames"][-1])
        expected = {"East": (steps, 0), "NorthEast": (steps, 5 - steps)}
        return last == expected, f"expected {expected}, got {last}"

    return env, [check_no_error, check_displacement]


@scenario("random_walk", "Three seeded RandomWalkers.", steps=25)
def random_walk(seed):
    env = MultiAgentEnvironment()
    for i in range(3):
        env.add_agent(RandomWalker(f"R{i}", (4 * i, 4), seed=seed + i))
    return env, [check_no_error, check_unit_steps]


@scenario("chase", "A Chaser pursues a stationary target 8 cells away.")
def chase(seed):
    env = MultiAgentEnvironment()
    target = Agent("Target", (5, 3))
    env.add_agent(target)
    env.add_agent(Chaser("Chaser", (0, 0), target))

    def check_caught(trace):
        for frame in trace["frames"]:
            if positions(frame)["Chaser"] == (5, 3):
                return True, f"caught at step {frame['step']}"
        return False, "target never reached"

    return env, [check_no_error, check_caught]


@scenario("faulty", "An agent raises on tick 3; the harness must report it.")
def faulty(seed):
    env = MultiAgentEnvironment()
    env.add_agent(Walker("Healthy", (0, 0)))
    env.add_agent(Faulty("Broken", (0, 2), fail_at=3))

    def check_error_reported(trace):
        err = trace["error"]
        ok = err is not None and "tick 3" in err and trace["frames"][-1]["step"] == 2
        return ok, err or "no error was reported"

    return env, [check_error_reported]
