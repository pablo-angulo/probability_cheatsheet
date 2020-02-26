from optlang import Model, Variable, Constraint, Objective

model = Model(name='optlang model')

### Decision variables, positive (lb is lower bound)
#   x is real, y is interger
x = Variable('x',lb=0,type='continuous')
y = Variable('y',lb=0,type='integer')

### Constraints, x+2*y<=4, 5*x-y>=8
model.add([
    Constraint(x+2*y, ub=4),
    Constraint(5*x-y, lb=8)
])

### Objetive function to be maximixed
model.objective = Objective(x+2*y-2, direction='max')

### Solve
status = model.optimize()

### status can be "optimal", "infeasible", "unbounded"
#   or "undefined", if the solver decides there is no
#   optimal value, but cannot decide why
print("status:", model.status)

### optimal value
#   (only acceptable if status is "optimal")
print("objective value:", model.objective.value)
### print the value of each decision variable
#   for the optimal solution
#   (only acceptable if status is "optimal")
for var_name, var in model.variables.iteritems():
    print(var_name, "=", var.primal)
