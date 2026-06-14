import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minimax_value = None

class Minimax:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        return "goal reached" if node.minimax_value is not None else "Searching"
    
    def act(self, node, environment):
        goal_status = self.formulate_goal(node)
        if goal_status == "goal reached":
            return f"Minimax value for root node is: {node.minimax_value}"
        else:
            environment.compute_minimax(node, self.depth, True)
            return f"Minimax value for root node is: {node.minimax_value}"

class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []

    def compute_minimax(self, node, depth, maximizing_player=True):
        if depth == 0 or not node.children:
            node.minimax_value = node.value
            self.computed_nodes.append(node.minimax_value)
            return node.minimax_value
        
        if maximizing_player:
            max_eval = -math.inf
            for child in node.children:
                eval = self.compute_minimax(child, depth-1, False)
                max_eval = max(max_eval, eval)
            node.minimax_value = max_eval
            return max_eval
        else:
            min_eval = math.inf
            for child in node.children:
                eval = self.compute_minimax(child, depth-1, True)
                min_eval = min(min_eval, eval)
            node.minimax_value = min_eval
            return min_eval

n1 = Node(3)
n2 = Node(5)
n3 = Node(6)
n4 = Node(9)
n5 = Node(1)
n6 = Node(2)
n7 = Node(0)
n8 = Node(-1)

D = Node(); D.children = [n1, n2]
E = Node(); E.children = [n3, n4]
F = Node(); F.children = [n5, n6]
G = Node(); G.children = [n7, n8]

B = Node(); B.children = [D, E]
C = Node(); C.children = [F, G]

A = Node(); A.children = [B, C]

env = Environment(A)
agent = Minimax(depth=3)

result = agent.act(A, env)

print(result)

print("\nInternal Node Values:")
print(f"D = {D.minimax_value}")
print(f"E = {E.minimax_value}")
print(f"F = {F.minimax_value}")
print(f"G = {G.minimax_value}")
print(f"B = {B.minimax_value}")
print(f"C = {C.minimax_value}")
print(f"A = {A.minimax_value}")