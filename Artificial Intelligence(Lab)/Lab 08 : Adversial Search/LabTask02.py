import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minimax_value = None

class AlphaBeta:
    def __init__(self, depth):
        self.depth = depth

    def act(self, node, environment):
        environment.alpha_beta(node, self.depth, -math.inf, math.inf, True)
        return f"Optimal value at root node is: {node.minimax_value}"

class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.visited = 0

    def alpha_beta(self, node, depth, alpha, beta, maximizing_player):
        if depth == 0 or not node.children:
            node.minimax_value = node.value
            self.visited += 1
            return node.minimax_value

        if maximizing_player:
            value = -math.inf
            for child in node.children:
                value = max(value, self.alpha_beta(child, depth-1, alpha, beta, False))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            node.minimax_value = value
            return value
        else:
            value = math.inf
            for child in node.children:
                value = min(value, self.alpha_beta(child, depth-1, alpha, beta, True))
                beta = min(beta, value)
                if alpha >= beta:
                    break
            node.minimax_value = value
            return value

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
agent = AlphaBeta(depth=3)

result = agent.act(A, env)

print(result)
print("\nVisited leaf nodes:", env.visited)

print("\nInternal Node Values:")
print(f"D = {D.minimax_value}")
print(f"E = {E.minimax_value}")
print(f"F = {F.minimax_value}")
print(f"G = {G.minimax_value}")
print(f"B = {B.minimax_value}")
print(f"C = {C.minimax_value}")
print(f"A = {A.minimax_value}")