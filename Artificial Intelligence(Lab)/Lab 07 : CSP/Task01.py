from ortools.sat.python import cp_model

model = cp_model.CpModel()
nodes = ['A', 'B', 'C', 'D']
node_vars = {n: model.NewIntVar(0, 2, n) for n in nodes}


edges = [('A','B'), ('A','C'), ('B','C'), ('B','D'), ('C','D')]

for u, v in edges:
    model.Add(node_vars[u] != node_vars[v])


solver = cp_model.CpSolver()

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.variables = variables

    def on_solution_callback(self):
        print({v: self.Value(self.variables[v]) for v in self.variables})

solver.SearchForAllSolutions(model, SolutionPrinter(node_vars))