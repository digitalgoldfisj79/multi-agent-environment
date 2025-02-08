class MultiAgentEnvironment:
    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def update(self):
        for agent in self.agents:
            agent.update()

    def get_state(self):
        return [agent.get_state() for agent in self.agents]
