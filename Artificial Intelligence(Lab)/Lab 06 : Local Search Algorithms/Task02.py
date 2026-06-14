import random
N = 8

def conflicts(state):
    count = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                count += 1
    return count

def get_neighbors(state):
    neighbors = []
    for col in range(N):
        for row in range(N):
            if state[col] != row:
                new_state = list(state)
                new_state[col] = row
                neighbors.append(new_state)
    return neighbors

def hill_climbing():
    state = [random.randint(0, N - 1) for _ in range(N)]

    while True:
        current_conflict = conflicts(state)
        neighbors = get_neighbors(state)

        best_neighbor = min(neighbors, key=conflicts)
        best_conflict = conflicts(best_neighbor)

        if best_conflict >= current_conflict:
            return state, current_conflict

        state = best_neighbor

def random_restart(max_restarts=20):
    for i in range(max_restarts):
        state, conf = hill_climbing()
        print("Restart", i + 1, "Conflicts:", conf)

        if conf == 0:
            print("Solution Found")
            print("State:", state)
            return

    print("No solution found after 20 restarts")


random_restart()