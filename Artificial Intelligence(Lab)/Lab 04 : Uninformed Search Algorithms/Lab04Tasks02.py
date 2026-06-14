graph = {
    "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Zerind": [("Arad", 75), ("Oradea", 71)],
    "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu", 80)],
    "Timisoara": [("Arad", 118), ("Lugoj", 111)],
    "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
    "Mehadia": [("Lugoj", 70), ("Drobeta", 75)],
    "Drobeta": [("Mehadia", 75), ("Craiova", 120)],
    "Craiova": [("Drobeta", 120), ("Rimnicu", 146), ("Pitesti", 138)],
    "Rimnicu": [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)],
    "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
    "Pitesti": [("Rimnicu", 97), ("Craiova", 138), ("Bucharest", 101)],
    "Bucharest": []
}


def ucs(start, goal):
    queue = [(start, 0, [start])]
    visited = []

    while len(queue) > 0:

        min_index = 0
        for i in range(len(queue)):
            if queue[i][1] < queue[min_index][1]:
                min_index = i

        node, cost, path = queue.pop(min_index)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.append(node)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, cost + weight, path + [neighbor]))

    return None



result = ucs("Arad", "Bucharest")

print("Path:", result[0])
print("Total Cost:", result[1])