def dfs_limited(maze, start, goal, limit):
    stack = [(start, [start], 0)]

    while stack:
        (x, y), path, depth = stack.pop()

        if (x, y) == goal:
            return path

        if depth < limit:
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                    if maze[nx][ny] != 1 and (nx, ny) not in path:
                        stack.append(((nx, ny), path + [(nx, ny)], depth + 1))

    return None


def iterative_deepening_search(maze, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Trying depth limit = {depth}")
        result = dfs_limited(maze, start, goal, depth)
        if result:
            return result
    return None


maze = [
    ['S', 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 'G'],
    [1, 1, 0, 1, 1]
]

start = None
goal = None

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 'S':
            start = (i, j)
        elif maze[i][j] == 'G':
            goal = (i, j)

max_depth = 20
solution = iterative_deepening_search(maze, start, goal, max_depth)

if solution:
    print("\nGoal Found!")
    print(solution)
    print("Path length:", len(solution) - 1)
else:
    print("\nGoal not found within depth limit.")
