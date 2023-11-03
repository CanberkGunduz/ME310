import math


def f(x):
    return 8*math.sin(x)*math.e**(-x)-1
    # return math.e**(x**2+7*x-30)-1
    # return 1/x - math.sin(x)+1
    # return math.cos(x)-x**3
    # return math.log(x) # NEWTON METHOD GIVES X_ROOT -0.03 SO OUT OF BOUNDS
    # return x**2-(1-x)**5
    # return x**5-8*x**4+44*x**3-91*x**2+85*x-26
    # return math.e**(-x) -x
