from environment import MultiAgentEnvironment
from agent import Agent

# Create an instance of MultiAgentEnvironment
env = MultiAgentEnvironment()

# Add agents to the environment
agent1 = Agent("Agent1", (0, 0))
agent2 = Agent("Agent2", (1, 1))
env.add_agent(agent1)
env.add_agent(agent2)

# Implement a loop to update the environment and print the state
for _ in range(10):
    env.update()
    print(env.get_state())
