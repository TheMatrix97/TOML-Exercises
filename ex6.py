# https://scipy-lectures.org/advanced/mathematical_optimization/auto_examples/plot_gradient_descent.html


def main_a():
    print("A)")
    # alpha = 0.3 # between 0, 0.5
    beta = 0.8  # between 0, 1 (0.1 very crude search / 0.8 less crude)
    f = lambda x: (2 * x ** 2 - 0.5)
    fdx = lambda x: (4 * x)
    t = 1
    x0 = 3
    n = 1
    stop_criterion = 10 ** -4
    while (f(x0 + t * (-fdx(x0))) > stop_criterion):
        t = beta * t
        n += 1
    res = x0 + t * (-fdx(x0))
    print("N -> " + str(n))
    print("Final result -> " + str(res))
    print("Final accuracy -> " + str(f(res)))

def main_b():
    print("B)")
    # alpha = 0.3 # between 0, 0.5
    beta = 0.8  # between 0, 1 (0.1 very crude search / 0.8 less crude)
    f = lambda x: (2 * x ** 4 - 4*x**2 + x - 0.5)
    fdx = lambda x: (8*x**3 - 8*x + 1)
    stop_criterion = 10 ** -4
    for x0 in [-2, -0.5, 0.5, 2]:
        print("x0 -> " + str(x0))
        t = 1
        n = 0
        while (f(x0 + t * (-fdx(x0))) > stop_criterion):
            t = beta * t
            n += 1
        res = x0 + t * (-fdx(x0))
        print("N -> " + str(n))
        print("Final result -> " + str(res))
        print("Final accuracy -> " + str(f(res)))
        print("--------------------------")

def main_c(): #newtons method
    print("C)")
    f = lambda x: (2 * x ** 4 - 4 * x ** 2 + x - 0.5)
    fdx = lambda x: (8 * x ** 3 - 8 * x + 1)
    f2dx = lambda x: (24 * x ** 2 - 8)
    lambda_sq_fn = lambda x: (fdx(x) * f2dx(x)**-1 * fdx(x))
    new_step_fn = lambda x: (-f2dx(x)**-1 * fdx(x))
    stop_criterion = 10 ** -4
    for x0 in [-2, -0.5, 0.5, 2]:
        print("x0 -> " + str(x0))
        x = x0
        n = 0
        while lambda_sq_fn(x) > stop_criterion:
            new_step = new_step_fn(x)
            t = backtrack_t(x, f, fdx)
            x = x + t*new_step
            n += 1
        res = x
        print("N -> " + str(n))
        print("Final result -> " + str(res))
        print("Final accuracy -> " + str(f(res)))
        print("--------------------------")



def backtrack_t(x0,f,fdx):
    beta = 0.8
    t = 1
    stop_criterion = 10 ** -4
    while f(x0 + t * (-fdx(x0))) > stop_criterion:
        t = beta * t
    return t




main_a()
main_b()
main_c()

