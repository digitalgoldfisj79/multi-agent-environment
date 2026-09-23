import unittest

from agent import Agent
from environment import MultiAgentEnvironment


class AgentTests(unittest.TestCase):
    def test_initial_state(self):
        a = Agent("A", (2, 3))
        self.assertEqual(a.name, "A")
        self.assertEqual(a.get_position(), (2, 3))
        self.assertEqual(a.get_state(), {})

    def test_update_state_merges(self):
        a = Agent("A", (0, 0))
        a.update_state({"x": 1})
        a.update_state({"y": 2})
        self.assertEqual(a.get_state(), {"x": 1, "y": 2})

    def test_base_update_is_noop(self):
        a = Agent("A", (0, 0))
        a.update()
        self.assertEqual(a.get_position(), (0, 0))
        self.assertEqual(a.get_state(), {})


class EnvironmentTests(unittest.TestCase):
    def test_add_and_get_state(self):
        env = MultiAgentEnvironment()
        a, b = Agent("A", (0, 0)), Agent("B", (1, 1))
        env.add_agent(a)
        env.add_agent(b)
        a.update_state({"k": "v"})
        self.assertEqual(env.get_state(), [{"k": "v"}, {}])

    def test_update_calls_every_agent_in_order(self):
        calls = []

        class Recorder(Agent):
            def update(self):
                calls.append(self.name)

        env = MultiAgentEnvironment()
        for n in "ABC":
            env.add_agent(Recorder(n, (0, 0)))
        env.update()
        env.update()
        self.assertEqual(calls, list("ABCABC"))

    def test_main_setup_runs(self):
        env = MultiAgentEnvironment()
        env.add_agent(Agent("Agent1", (0, 0)))
        env.add_agent(Agent("Agent2", (1, 1)))
        for _ in range(10):
            env.update()
        self.assertEqual(env.get_state(), [{}, {}])


if __name__ == "__main__":
    unittest.main()
