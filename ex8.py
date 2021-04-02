import cvxpy
import numpy as np
from cvxpy import Variable, log, Minimize, Problem


def solve_cvxpy():
    # Create one scalar optimization variables.
    x = Variable(3, name='x')
    r = Variable(3, name='r')

    # Constraints
    f1 = x[0] + x[1] - r[0]
    f2 = x[0] - r[1]
    f3 = x[2] - r[2]
    f4 = r[0] + r[1] + r[2]
    constraints = [f1 <= 0, f2 <= 0, f3 <= 0, f4 <= 1]

    # Form objective.
    f0 = -cvxpy.sum(cvxpy.log(x)) # negative for minimize

    obj = Minimize(f0)

    prob = Problem(obj, constraints)
    print("solve", prob.solve())  # Returns the optimal value.
    print("status:", prob.status)
    print("optimal value p* = ", prob.value)
    print("optimal var: x1 = ", x[0].value)
    print("optimal var: x2 = ", x[1].value)
    print("optimal var: x3 = ", x[2].value)
    print("optimal var: r12 = ", r[0].value)
    print("optimal var: r23 = ", r[1].value)
    print("optimal var: r32 = ", r[2].value)
    print("optimal dual variables lambda1 = ", constraints[0].dual_value)
    print("optimal dual variables lambda2 = ", constraints[1].dual_value)
    print("optimal dual variables lambda3 = ", constraints[2].dual_value)
    print("optimal dual variables lambda4 = ", constraints[3].dual_value)

solve_cvxpy()