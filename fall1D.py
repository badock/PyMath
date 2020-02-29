import sys
import numpy as np
from sympy import *
import matplotlib.pyplot as plt


GRAVITY_CONSTANT = 9.81

t = symbols("t")
g = symbols("g")
v0 = symbols("v0")
y0 = symbols("y0")


ACCELERATION_FUNCTION = -g
VELOCITY_FUNCTION = integrate(ACCELERATION_FUNCTION, t) + v0
POSITION_FUNCTION = integrate(VELOCITY_FUNCTION, t) + y0


def estimate_position(initial_speed, initial_height):
    result = POSITION_FUNCTION.subs(v0, initial_speed).subs(y0, initial_height).evalf()
    return result


def main():
    fig = plt.figure()
    x = np.arange(start=0, stop=10, step=0.1)
    y = 2.5 * np.sin(x / 20 * np.pi)

    for initial_height in [0, 100, 200, 400]:
        for initial_speed in [0, 10, 20, 40]:
            result = estimate_position(initial_speed, initial_height)
            values = [result.subs(t, xt).subs(g, GRAVITY_CONSTANT) for xt in x]
            plt.plot(x, values, label=f'initial_speed={initial_speed} initial_height={initial_height}')
            print(values)

    plt.legend(loc='lower right')
    plt.savefig("result.pdf")
    return True


if __name__ == "__main__":
    main()
    sys.exit(0)
