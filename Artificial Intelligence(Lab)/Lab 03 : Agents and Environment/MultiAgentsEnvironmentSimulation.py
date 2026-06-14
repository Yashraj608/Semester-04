class Environment:
    def __init__(self, rooms):
        self.rooms = rooms.copy()

    def goal_achieved(self):
        return all(r == "Clean" for r in self.rooms)

    def show(self):
        print(self.rooms)


class ReflexAgent:
    def __init__(self, env):
        self.env = env
        self.pos = 0
        self.steps = 0

    def run(self):
        while not self.env.goal_achieved():
            self.steps += 1
            if self.env.rooms[self.pos] == "Dirty":
                self.env.rooms[self.pos] = "Clean"
            else:
                self.pos = min(self.pos + 1, len(self.env.rooms) - 1)
        return self.steps


class LearningAgent:
    def __init__(self, env):
        self.env = env
        self.pos = 0
        self.q_table = {}

    def choose_action(self):
        if self.env.rooms[self.pos] == "Dirty":
            return "Clean"
        else:
            return "Move"

    def run(self):
        steps = 0
        while not self.env.goal_achieved():
            steps += 1
            action = self.choose_action()
            state = (self.pos, tuple(self.env.rooms))
            if action == "Clean":
                self.env.rooms[self.pos] = "Clean"
                reward = 10
            else:
                self.pos = min(self.pos + 1, len(self.env.rooms) - 1)
                reward = -1
            self.q_table.setdefault(state, {})[action] = reward
        return steps


rooms = ["Dirty", "Dirty", "Dirty"]

env1 = Environment(rooms)
reflex = ReflexAgent(env1)
reflex_steps = reflex.run()
print("Reflex Agent Steps:", reflex_steps)

env2 = Environment(rooms)
learning = LearningAgent(env2)
learning_steps = learning.run()
print("Learning Agent Steps:", learning_steps)

print("Learning Agent Q-Table:")
for s, a in learning.q_table.items():
    print(s, a)
