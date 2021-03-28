from cvxopt import solvers, matrix, spdiag, log
import numpy as np
from scipy.optimize import minimize

#https://courses.csail.mit.edu/6.867/wiki/images/a/a7/Qp-cvxopt.pdf

def objective(x):
    # Objective function
    return pow(x[0], 2) + pow(x[1], 2)


def ineq_const():
    # I'm negating funs because minimize expects x >= 0

    return {'type': 'ineq',
            'fun': lambda x: np.array([-(pow(x[0], 2) + x[0]*x[1] + pow(x[1], 2) - 3),
                                       (3*x[0] + 2*x[1] - 3)])
            }


def run_minimize(x0):
    return minimize(objective, x0, method='SLSQP',
                    constraints=[ineq_const()], options={'ftol': 1e-9, 'disp': True},
                    )


# Ni idea de como convertirlo a cvx... no es un QCQP x1*x2?
# https://github.com/cvxopt/cvxopt/issues/81
"""""
def F(x=None, z=None):
    if x is None: return 0, matrix(1.0, (n, 1))
    if min(x) <= 0.0: return None
    f = -sum(log(x))
    Df = -(x ** -1).T
    if z is None: return f, Df
    H = spdiag(z[0] * x ** -2)
    return f, Df, H
"""""



#Why jacobian is giving more iterations??
def main():
    # Initial points x0
    x0_points = [[0, 1], [6, 10]]
    for point in x0_points:
        print("X0 -> " + str(np.array(point)))
        res = run_minimize(np.array(point))
        print(res)
        print("---------------------------------\n")

main()