
def bfs(graph, start, goal):
    visited = []
    queue = [[start]]

    while len(queue) > 0:
        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.append(node)

            for i in range(len(graph[node])):
                if graph[node][i] != 0:
                    queue.append(path + [i])

    return None




def dfs(graph, start, goal):
    visited = []
    stack = [[start]]

    while len(stack) > 0:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.append(node)

            for i in range(len(graph[node])):
                if graph[node][i] != 0:
                    stack.append(path + [i])

    return None



def dls(graph, node, goal, limit, path):
    if node == goal:
        return path

    if limit == 0:
        return None

    for i in range(len(graph[node])):
        if graph[node][i] != 0:
            result = dls(graph, i, goal, limit - 1, path + [i])
            if result is not None:
                return result

    return None



def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        result = dls(graph, start, goal, depth, [start])
        if result is not None:
            return result
    return None



def ucs(graph, start, goal):
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

            for i in range(len(graph[node])):
                weight = graph[node][i]
                if weight != 0:
                    queue.append((i, cost + weight, path + [i]))

    return None



graph = [
    [0, 1, 4, 0, 0, 0],   
    [0, 0, 2, 5, 0, 0],  
    [0, 0, 0, 1, 3, 0],   
    [0, 0, 0, 0, 0, 2],  
    [0, 0, 0, 0, 0, 1],  
    [0, 0, 0, 0, 0, 0]   
]

start_node = 0
goal_node = 5

print("BFS:", bfs(graph, start_node, goal_node))
print("DFS:", dfs(graph, start_node, goal_node))
print("DLS (limit=3):", dls(graph, start_node, goal_node, 3, [start_node]))
print("IDS:", ids(graph, start_node, goal_node, 5))
print("UCS:", ucs(graph, start_node, goal_node))