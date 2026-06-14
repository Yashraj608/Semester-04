from ortools.sat.python import cp_model

model = cp_model.CpModel()

grid = {}
for i in range(9):
    for j in range(9):
        grid[(i, j)] = model.NewIntVar(1, 9, f'cell_{i}_{j}')

puzzle = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

for i in range(9):
    for j in range(9):
        if puzzle[i][j] != 0:
            model.Add(grid[(i, j)] == puzzle[i][j])

for i in range(9):
    model.AddAllDifferent([grid[(i, j)] for j in range(9)])


for j in range(9):
    model.AddAllDifferent([grid[(i, j)] for i in range(9)])


for box_row in range(3):
    for box_col in range(3):
        cells = []
        for i in range(3):
            for j in range(3):
                cells.append(grid[(box_row*3+i, box_col*3+j)])
        model.AddAllDifferent(cells)


solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
    for i in range(9):
        print([solver.Value(grid[(i, j)]) for j in range(9)])