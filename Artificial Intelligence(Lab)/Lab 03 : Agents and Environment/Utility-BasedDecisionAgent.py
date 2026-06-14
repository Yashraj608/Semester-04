class Environment:
    def __init__(self, rooms):
        self.rooms = rooms

    def goal_achieved(self):
        return all(r == "Clean" for r in self.rooms)

    def show(self):
        print(self.rooms)


class Agent:
    def __init__(self, env):
        self.env = env
        self.pos = 0
        self.total_utility = 0

    def utility(self, action):
        if action == "Clean" and self.env.rooms[self.pos] == "Dirty":
            return 10
        if action == "Move":
            return -1
        return -5

    def run(self):
        step = 1
        while not self.env.goal_achieved():
            actions = ["Clean", "Move", "Do Nothing"]
            utilities = {a: self.utility(a) for a in actions}
            best_action = max(utilities, key=utilities.get)

            print("Step:", step)
            print("Action:", best_action)
            print("Utility:", utilities[best_action])

            self.total_utility += utilities[best_action]

            if best_action == "Clean":
                self.env.rooms[self.pos] = "Clean"
            elif best_action == "Move":
                self.pos = min(self.pos + 1, len(self.env.rooms) - 1)

            print("Total Utility:", self.total_utility)
            self.env.show()
            print()
            step += 1


rooms = ["Dirty", "Dirty", "Clean"]
env = Environment(rooms)
agent = Agent(env)
agent.run()
