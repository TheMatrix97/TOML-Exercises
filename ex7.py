import numpy as np
from cvxpy import Variable, log, Minimize, Problem


def solve_cvxpy():
    # Create one scalar optimization variables.
    x = Variable(3, name='x')

    # Constraints
    f1 = x[0] + x[2]
    f2 = x[0] + x[1]
    f3 = x[2]
    constraints = [f1 <= 1., f2 <= 2., f3 <= 1.,
                   x[0] >= 0., x[1] >= 0., x[2] >= 0.]

    # Form objective.
    f0 = -log(x[0]) - log(x[1]) - log(x[2]) # negative for minimize
    obj = Minimize(f0)

    prob = Problem(obj, constraints)
    print("solve", prob.solve())  # Returns the optimal value.
    print("status:", prob.status)
    print("optimal value p* = ", prob.value)
    print("optimal var: x1 = ", x[0].value)
    print("optimal var: x2 = ", x[1].value)
    print("optimal var: x3 = ", x[2].value)
    print("optimal dual variables lambda1 = ", constraints[0].dual_value)
    print("optimal dual variables lambda2 = ", constraints[1].dual_value)
    print("optimal dual variables lambda3 = ", constraints[2].dual_value)
    print("optimal dual variables lambda4 = ", constraints[3].dual_value)
    print("optimal dual variables lambda5 = ", constraints[4].dual_value)

solve_cvxpy()