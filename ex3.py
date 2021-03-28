import numpy as np
from cvxpy import Variable, quad_form, Minimize, Problem
from scipy.optimize import minimize


def objective(x):
    # Objective function
    return pow(x[0], 2) + pow(x[1], 2)


def objective_jacob(x):  # TODO REVISAR!
    # Objective function
    dx = 2 * x[0]
    dy = 2 * x[1]
    return np.array((dx, dy))


def ineq_const():
    # I'm negating funs because minimize expects x >= 0

    return {'type': 'ineq',
            'fun': lambda x: np.array([-(pow(x[0], 2) + x[0] * x[1] + pow(x[1], 2) - 3),
                                       (3 * x[0] + 2 * x[1] - 3)])
            }


def run_minimize(x0):
    return minimize(objective, x0, method='SLSQP',
                    constraints=[ineq_const()], options={'ftol': 1e-9, 'disp': True},
                    )


def run_minimize_jacob(x0):
    return minimize(objective, x0, method='SLSQP', jac=objective_jacob, constraints=[ineq_const()])

def solve_cvxpy():
    # Create two scalar optimization variables.
    x = Variable(2, name='x')

    # Constraints
    P1 = np.array(np.mat('1. 0.5; 0.5 1.'))
    f1 = quad_form(x, P1)
    f2 = 3. * x[0] + 2. * x[1]
    constraints = [f1 <= 3., f2 >= 3.]

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
    # Initial points x0
    x0_points = [[0, 1], [6, 10]]
    for point in x0_points:
        print("X0 -> " + str(np.array(point)))
        res = run_minimize_jacob(np.array(point))
        print(res)
        print("---------------------------------\n")
    #CVXPY
    print("---------CVXPY--------")
    solve_cvxpy()


main()
