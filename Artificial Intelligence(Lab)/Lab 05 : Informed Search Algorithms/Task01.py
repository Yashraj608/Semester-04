import heapq

def best_first_search(graph, heuristics, start, goal):
    open_list = []
    closed_list = set()
    
    heapq.heappush(open_list, (heuristics[start], start, [start]))
    
    while open_list:
        h, current, path = heapq.heappop(open_list)
        if current == goal:
            return path
        
        closed_list.add(current)
        
        for neighbor in graph.get(current, []):
            if neighbor not in closed_list:
                heapq.heappush(open_list, (heuristics[neighbor], neighbor, path + [neighbor]))
                
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
heuristics = {'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3, 'F': 0}

path = best_first_search(graph, heuristics, 'A', 'F')
print("Best-First Search Path:", path)