import numpy as np
from cvxpy import Variable, Minimize, Problem, quad_form, Constant
# https://www.cvxpy.org/examples/basic/quadratic_program.html


def solve_cvxpy():
    # Create one scalar optimization variables.
    x = Variable(1, name='x')

    # Constraints
    P1 = np.array(np.mat('1.'))
    #f1 = quad_form(x, P1)
    f1 = quad_form(x, P1) - 6*x[0] + Constant(8)
    constraints = [f1 <= 0.]

    # Form objective.
    f0 = quad_form(x, P1) + Constant(1)
    obj = Minimize(f0)

    prob = Problem(obj, constraints)
    print("solve", prob.solve())  # Returns the optimal value.
    print("status:", prob.status)
    print("optimal value p* = ", prob.value)
    print("optimal var: x1 = ", x[0].value)
    print("optimal dual variables lanbda1 = ", constraints[0].dual_value)

def main():
    solve_cvxpy()



main()


