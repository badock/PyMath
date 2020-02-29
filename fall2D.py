import sys
import numpy as np
from sympy import *
import matplotlib.pyplot as plt

INITIAL_SPEED = 8
INITIAL_HEIGHT = 1.5
GRAVITY_CONSTANT = 9.81

t = symbols("t")
g = symbols("g")
vx0 = symbols("vX0")
vy0 = symbols("vy0")
y0 = symbols("y0")
x0 = symbols("x0")


ACCELERATION_Y_FUNCTION = -g
ACCELERATION_X_FUNCTION = 0
VELOCITY_X_FUNCTION = integrate(ACCELERATION_X_FUNCTION, t) + vx0
VELOCITY_Y_FUNCTION = integrate(ACCELERATION_Y_FUNCTION, t) + vy0
POSITION_X_FUNCTION = integrate(VELOCITY_X_FUNCTION, t) + x0
POSITION_Y_FUNCTION = integrate(VELOCITY_Y_FUNCTION, t) + y0


def estimate_position(vx0_f, vy0_f, x0_f, y0_f):
    fx = POSITION_X_FUNCTION.subs(vx0, vx0_f).subs(x0, x0_f).subs(g, GRAVITY_CONSTANT).evalf()
    fy = POSITION_Y_FUNCTION.subs(vy0, vy0_f).subs(y0, y0_f).subs(g, GRAVITY_CONSTANT).evalf()
    return fx, fy


def main():
    fig = plt.figure()
    time_steps = np.arange(start=0, stop=3.0, step=0.001)

    angles = np.arange(start=0, stop=90, step=5)

    for initial_angle in angles:
        angle_radian = (1.0 * initial_angle / 180) * pi
        fx, fy = estimate_position(cos(angle_radian) * INITIAL_SPEED, sin(angle_radian) * INITIAL_SPEED, 0, INITIAL_HEIGHT)
        xs = []
        ys = []
        for (x, y) in [(fx.subs(t, ts), fy.subs(t, ts)) for ts in time_steps]:
            if y > 0.0:
                xs += [x]
                ys += [y]
        plt.plot(xs, ys, label=f'initial_angle={initial_angle}')

    plt.legend(loc='upper right')
    plt.savefig("result.pdf")
    return True


if __name__ == "__main__":
    main()
    sys.exit(0)
