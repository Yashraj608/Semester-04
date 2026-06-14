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
        self.goal = "Clean all rooms"

    def run(self):
        step = 1
        while not self.env.goal_achieved():
            print("Step:", step)
            print("Percept:", (self.pos, self.env.rooms[self.pos]))
            print("Goal:", self.goal)

            if self.env.rooms[self.pos] == "Dirty":
                action = "Clean"
                self.env.rooms[self.pos] = "Clean"
            else:
                if self.pos < len(self.env.rooms) - 1:
                    action = "Move Right"
                    self.pos += 1
                else:
                    action = "Move Left"
                    self.pos -= 1

            print("Action:", action)
            self.env.show()
            print()
            step += 1


rooms = ["Dirty", "Clean", "Dirty"]
env = Environment(rooms)
agent = Agent(env)
agent.run()
