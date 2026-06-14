import heapq

def greedy_bfs_collect(grid, start, objects):
    rows, cols = len(grid), len(grid[0])
    collected = set()
    path = [start]
    
    def heuristic(pos, targets):
        return min(abs(pos[0]-t[0]) + abs(pos[1]-t[1]) for t in targets if t not in collected)
    
    current = start
    while len(collected) < len(objects):
        open_list = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in path and (r, c) not in collected:
                    heapq.heappush(open_list, (heuristic((r, c), objects), (r, c)))
        
        if not open_list:
            break
        
        _, next_cell = heapq.heappop(open_list)
        if next_cell in objects:
            collected.add(next_cell)
        path.append(next_cell)
        current = next_cell
        
    return path, collected


grid = [[0]*5 for _ in range(5)]
start = (0, 0)
objects = [(2, 2), (4, 4), (1, 3)]

path, collected = greedy_bfs_collect(grid, start, objects)
print("Greedy BFS Path:", path)
print("Collected:", collected)