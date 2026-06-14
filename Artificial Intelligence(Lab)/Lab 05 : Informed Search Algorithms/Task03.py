import heapq

def a_star_search(graph, start, goal, heuristics, blocked=[]):
    open_list = []
    closed_list = set()
    g_scores = {start: 0}
    
    heapq.heappush(open_list, (heuristics[start], start, [start]))
    
    while open_list:
        f, current, path = heapq.heappop(open_list)
        if current == goal:
            return path
        
        closed_list.add(current)
        
        for neighbor, cost in graph.get(current, {}).items():
            if neighbor in closed_list or neighbor in blocked:
                continue
            tentative_g = g_scores[current] + cost
            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristics[neighbor]
                heapq.heappush(open_list, (f_score, neighbor, path + [neighbor]))
                
    return None

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 7, 'E': 1},
    'C': {'E': 3},
    'D': {},
    'E': {'D': 2}
}
heuristics = {'A': 10, 'B': 7, 'C': 5, 'D': 0, 'E': 2}
blocked = ['C']  

path = a_star_search(graph, 'A', 'D', heuristics, blocked)
print("A* Path:", path)