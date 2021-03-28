import numpy as np
from scipy.optimize import minimize


def objective(x):
    # Objective function
    return pow(x[0], 2) + pow(x[1], 2)

def objective_der(x): #TODO REVISAR!
    # Objective function
    der = np.zeros_like(x)
    der[0] = 2*x[0]
    der[1] = 2*x[1]
    return der


def ineq_const():
    # I'm negating funs because minimize expects x >= 0

    return {'type': 'ineq',
            'fun': lambda x: np.array([(x[0]-0.5),
                                       -(-x[0] - x[1] + 1),
                                       -(-pow(x[0], 2) - pow(x[1], 2) + 1),
                                       -(-9*pow(x[0], 2) - pow(x[1], 2) + 9),
                                       -(-pow(x[0], 2) + x[1]),
                                       -(-pow(x[1], 2) + x[0])])
            }


def run_minimize(x0):
    return minimize(objective, x0, method='SLSQP',
                    constraints=[ineq_const()], options={'ftol': 1e-9, 'disp': True},
                    )
def run_minimize_jacob(x0):
    return minimize(objective, x0, method='SLSQP', jac=objective_der,
                    constraints=[ineq_const()], options={'ftol': 1e-9, 'disp': True},
                    )

#Why jacobian is giving more iterations??
def main():
    # Initial points x0
    x0_points = [[0, 1], [6, 10]]
    for point in x0_points:
        print("X0 -> " + str(np.array(point)))
        res = run_minimize(np.array(point))
        #res = run_minimize_jacob(np.array(point))
        print(res)
        print("---------------------------------\n")

main()
