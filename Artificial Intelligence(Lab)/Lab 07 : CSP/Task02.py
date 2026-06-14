from ortools.sat.python import cp_model

model = cp_model.CpModel()

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

shirt = {d: model.NewIntVar(0, 4, f"shirt_{d}") for d in days}
pant = {d: model.NewIntVar(0, 2, f"pant_{d}") for d in days}
sq = {d: model.NewIntVar(0, 1, f"sq_{d}") for d in days}

use_sq = {d: model.NewBoolVar(f"use_sq_{d}") for d in days}

for d in days:
    model.Add(use_sq[d] == 1).OnlyEnforceIf(use_sq[d])
    model.Add(use_sq[d] == 0).OnlyEnforceIf(use_sq[d].Not())

    model.Add(sq[d] >= 0).OnlyEnforceIf(use_sq[d])
    model.Add(sq[d] == 0).OnlyEnforceIf(use_sq[d].Not())

    model.Add(shirt[d] >= 0).OnlyEnforceIf(use_sq[d].Not())
    model.Add(pant[d] >= 0).OnlyEnforceIf(use_sq[d].Not())

model.Add(use_sq["Fri"] == 1)

model.Add(use_sq["Mon"] == 0)
model.Add(use_sq["Thu"] == 0)

for d in days:
    model.AddAllDifferent([shirt[d], pant[d], sq[d]])

model.AddAllDifferent(
    [shirt[d] * 10 + pant[d] for d in days]
)

solver = cp_model.CpSolver()

status = solver.Solve(model)

if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
    for d in days:
        if solver.Value(use_sq[d]) == 1:
            print(d, "→ SQ", solver.Value(sq[d]))
        else:
            print(d, "→ Shirt", solver.Value(shirt[d]), ", Pant", solver.Value(pant[d]))
else:
    print("No solution found")