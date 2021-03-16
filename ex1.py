import numpy as np
from scipy.optimize import minimize


def objective(x):
    # Objective function
    return np.exp(x[0]) * (4 * pow(x[0], 2) + 2 * pow(x[1], 2) + 4 * x[0] * x[1] +
                           2 * x[1] + 1)

def objective_der(x): #TODO REVISAR!
    # Objective function
    der = np.zeros_like(x)
    der[0] = np.exp(x[0])*(8*x[0] + 2*pow(x[1], 2) + 4*x[1] + 2*x[1])
    der[1] = np.exp(x[0]) * (4*pow(x[0], 2) + 4*x[1] + 4*x[0] + 2)
    return der
    #ERROR! derivada en base x[0] y x[1]!


def ineq_const():
    # I'm negating funs because minimize expects x >= 0

    return {'type': 'ineq',
            'fun': lambda x: np.array([-(x[0] * x[1] - x[0] - x[1] + 1.5),
                                       -(-x[0] * x[1] - 10)])
            }


def run_minimize(x0):
    return minimize(objective, x0, method='SLSQP',
                    constraints=[ineq_const()], options={'ftol': 1e-9, 'disp': True},
                    )
def run_minimize_jacob(x0):
    return minimize(objective, x0, method='SLSQP', jac=objective_der,
                    constraints=[ineq_const()], options={'ftol': 1e-9, 'disp': True},
                    )

def main():
    # Initial points x0
    x0_points = [[0, 0], [10, 20], [-10, 1], [-30, -30]]
    for point in x0_points:
        print("X0 -> " + str(np.array(point)))
        res = run_minimize_jacob(np.array(point))
        print(res)
        print("---------------------------------\n")


main()
