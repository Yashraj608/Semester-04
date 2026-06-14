class Environment:
    def __init__(self, rooms):
        self.rooms = rooms

    def goal_achieved(self):
        return all(r == "Clean" for r in self.rooms)


class Agent:
    def __init__(self, env):
        self.env = env
        self.pos = 0
        self.q_table = {}
        self.actions = ["Clean", "Move"]

    def state(self):
        return (self.pos, tuple(self.env.rooms))

    def choose_action(self, state):
        # Choose Clean if dirty, otherwise Move
        if self.env.rooms[self.pos] == "Dirty":
            return "Clean"
        else:
            return "Move"

    def update_q(self, state, action, reward, next_state):
        self.q_table.setdefault(state, {})
        self.q_table[state][action] = reward

    def run(self):
        self.pos = 0
        self.env.rooms = ["Dirty", "Dirty", "Dirty"]

        while not self.env.goal_achieved():
            state = self.state()
            action = self.choose_action(state)

            if action == "Clean":
                self.env.rooms[self.pos] = "Clean"
                reward = 10
            else:
                self.pos = min(self.pos + 1, len(self.env.rooms) - 1)
                reward = -1

            next_state = self.state()
            self.update_q(state, action, reward, next_state)

        print("Final Q-Table:")
        for s, a in self.q_table.items():
            print(s, a)


env = Environment(["Dirty", "Dirty", "Dirty"])
agent = Agent(env)
agent.run()
