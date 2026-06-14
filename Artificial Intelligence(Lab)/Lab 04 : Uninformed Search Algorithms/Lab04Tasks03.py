start_state = (
    (7, 2, 4),
    (5, 0, 6),
    (8, 3, 1)
)

goal_state = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8)
)


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    neighbors = []
    row, col = find_blank(state)

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_state = [list(r) for r in state]

            new_state[row][col], new_state[new_row][new_col] = \
                new_state[new_row][new_col], new_state[row][col]

            neighbors.append(tuple(tuple(r) for r in new_state))

    return neighbors


def bfs(start, goal):
    queue = [(start, [start])]
    visited = set()

    while queue:
        state, path = queue.pop(0)

        if state == goal:
            return path

        if state not in visited:
            visited.add(state)

            for neighbor in get_neighbors(state):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None


solution = bfs(start_state, goal_state)

print("Total Moves:", len(solution) - 1)
print("Solution Path:")
for step_no, state in enumerate(solution):
    print(f"Step {step_no}:")
    for row in state:
        print(row)
    print()