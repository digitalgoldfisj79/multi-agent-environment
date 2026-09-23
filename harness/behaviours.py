import random

from agent import Agent


class Walker(Agent):
    """Moves by a fixed (dx, dy) each tick."""

    def __init__(self, name, position, velocity=(1, 0)):
        super().__init__(name, position)
        self.velocity = velocity

    def update(self):
        x, y = self.position
        dx, dy = self.velocity
        self.position = (x + dx, y + dy)
        self.update_state({"moves": self.state.get("moves", 0) + 1})


class RandomWalker(Agent):
    """Takes one random step in the 4-neighbourhood each tick (seeded)."""

    STEPS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self, name, position, seed=0):
        super().__init__(name, position)
        self.rng = random.Random(seed)

    def update(self):
        x, y = self.position
        dx, dy = self.rng.choice(self.STEPS)
        self.position = (x + dx, y + dy)
        self.update_state({"moves": self.state.get("moves", 0) + 1})


class Chaser(Agent):
    """Steps one cell per tick towards a target agent (x first, then y)."""

    def __init__(self, name, position, target):
        super().__init__(name, position)
        self.target = target

    def update(self):
        x, y = self.position
        tx, ty = self.target.get_position()
        if x != tx:
            x += 1 if tx > x else -1
        elif y != ty:
            y += 1 if ty > y else -1
        self.position = (x, y)
        self.update_state({"caught": self.position == (tx, ty)})


class Faulty(Agent):
    """Raises on a given tick, to check the harness reports agent errors."""

    def __init__(self, name, position, fail_at=3):
        super().__init__(name, position)
        self.fail_at = fail_at
        self.ticks = 0

    def update(self):
        self.ticks += 1
        if self.ticks == self.fail_at:
            raise RuntimeError(f"{self.name} failed on tick {self.ticks}")
