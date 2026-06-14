from collections import defaultdict

class Node:
    def __init__(self, node, cost, path):
        self.node = node
        self.cost = cost
        self.path = path

def beam_search(graph, start, goal):
    beam_width = 2
    max_beam_width = 5
    level = 0

    beam = [Node(start, 0, [start])]

    while beam:
        print("Level", level, "| Beam Width:", beam_width)
        print("Beam Nodes:", [n.node for n in beam])

        candidates = []

        for node in beam:
            if node.node == goal:
                print("Goal Found")
                print("Path:", node.path)
                print("Cost:", node.cost)
                return

            for neighbor, cost in graph[node.node]:
                new_node = Node(
                    neighbor,
                    node.cost + cost,
                    node.path + [neighbor]
                )
                candidates.append(new_node)

        candidates.sort(key=lambda x: x.cost)
        beam = candidates[:beam_width]

        level += 1

        if level % 3 == 0 and beam_width < max_beam_width:
            beam_width += 1

    print("Goal not found")

graph = defaultdict(list)

graph[0] = [(1,2),(2,4)]
graph[1] = [(3,3),(4,2)]
graph[2] = [(5,5),(6,1)]
graph[3] = [(7,4)]
graph[4] = [(7,2),(8,3)]
graph[5] = [(9,2)]
graph[6] = [(9,3),(10,6)]
graph[7] = [(11,1)]
graph[8] = [(11,5),(12,2)]
graph[9] = [(13,4)]
graph[10] = [(13,2)]
graph[11] = [(14,3)]
graph[12] = [(14,6)]
graph[13] = [(14,1)]

beam_search(graph, 0, 14)