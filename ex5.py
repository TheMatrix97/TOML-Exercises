import numpy as np
from cvxpy import Variable, Minimize, Problem, quad_form, Constant
# https://www.cvxpy.org/examples/basic/quadratic_program.html


def solve_cvxpy():
    # Create two scalar optimization variables.
    x = Variable(2, name='x')

    # Constraints
    P1 = np.array(np.mat('1. 0.; 0. 0.'))
    P2 = np.array(np.mat('0. 0.; 0. 1.'))
    a0 = quad_form(x, P1) - 2 * x[0] + 1  # (x1-1)**2
    a1 = quad_form(x, P2) - 2 * x[1] + 1  # (x2-1)**2
    a2 = quad_form(x, P2) + 2 * x[1] + 1  # (x2+1)**2
    cf0 = a0 + a1
    cf1 = a0 + a2
    constraints = [cf0 <= 1., cf1 <= 1.]

    # Form objective.
    P0 = np.array(np.mat('1. 0.; 0. 1.'))
    f0 = quad_form(x, P0)
    obj = Minimize(f0)

    prob = Problem(obj, constraints)
    print("solve", prob.solve())  # Returns the optimal value.
    print("status:", prob.status)
    print("optimal value p* = ", prob.value)
    print("optimal var: x1 = ", x[0].value, " x2 = ", x[1].value)
    print("optimal dual variables lanbda1 = ", constraints[0].dual_value)
    print("optimal dual variables lanbda2 = ", constraints[1].dual_value)

def main():
    solve_cvxpy()



main()


