import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

"""
some verry usefull math tools
as integration ,diferenciación ..
"""


def solveODE(u, v, u0, v0, t0=0, h=0.001, n=10000):
    """
    Runge Kutta method for solving system ode

    see https://people.ucsc.edu/~mmrosent/talks_notes/num_int_pres.pdf


    solve system ode
    :param u: u(x,y,t) e1
    :param v: v(x,y,t) e2
    :param u0: initial value
    :param v0: initial value
    :param t0: initial value
    :param h:  increment step
    :param n:  interval multiple by h give the interval for integration
    :return:
    """

    y_args = [v0]  # y_args array for y arguments
    x_args = [u0]  # x_args array for arguments
    t_args = [t0]  # time interval
    x = u0
    y = v0
    t = t0
    for i in range(n):
        k1 = h * u(t, x, y)
        l1 = h * v(t, x, y)
        k2 = h * u(t + h / 2, x + k1 / 2, y + l1 / 2)
        l2 = h * v(t + h / 2, x + k1 / 2, y + l1 / 2)
        k3 = h * u(t + h / 2, x + k2 / 2, y + l2 / 2)
        l3 = h * v(t + h / 2, x + k2 / 2, y + l2 / 2)
        k4 = h * u(t + h, x + k3, y + l3)
        l4 = h * v(t + h, x + k3, y + l3)
        k = (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        l = (1 / 6) * (l1 + 2 * l2 + 2 * l3 + l4)
        x = x + k
        y = y + l
        t = t + h
        x_args.append(x)
        y_args.append(y)
        t_args.append(t)

        # ax.plot(x_args, y_args, label="solved", color="black")

    return np.array([x_args, y_args, t_args]).T


def integrate(x0, dxdt, t):
    """
    simple methpod for inegration


    :param x0: initial value
    :param dxdt: first derivative
    :param t: time
    :return: result of integration
    """
    x_args = [x0]
    t_args = [0]

    f = x0
    for i in range(len(t) - 1):
        dt = t[i + 1] - t[i]
        f = f + dxdt[i] * dt

        x_args.append(f)
        t_args.append(t)
    return np.array([x_args, t]).T


def leapFrog(u, v, x0, y0, vx_0, vy_0, n=1000, h=0.1,c = 1):
    """
      verry important numerical method for ode
      can be use well for solving system ode second order
      leapfrog algoritam is improved euler method verry usefull ecspecialy in computing

        see  #https://people.ucsc.edu/~mmrosent/talks_notes/num_int_pres.pdf

    :param u:  u = u(t,x,y) = e1
    :param v:   u = v(t,x,y) = e2
    :param x0:
    :param y0:
    :param vx_0:
    :param vy_0:
    :param n:  numbet of step
    :param h:  step
    :param c = can be some constant as mass
    :return:
    """

    x = x0
    y = y0
    vx = vx_0
    vy = vy_0
    t = 0
    y_args = [y]  # y_args array for y arguments
    x_args = [x]  # x_args array for arguments
    t_args = [t]  # time interval
    x_speed = [vx]
    y_speed = [vy]

    for i in range(n):
        x = x + vx * (h / 2)/c
        y = y + vy * (h / 2)/c

        vx = (vx + h * u(t, x, y))/c
        vy = (vy + h * v(t, x, y))/c

        x = x + vx * (h / 2)
        y = y + vy * (h / 2)

        t = t + h
        x_speed.append(vx)
        y_speed.append(vy)
        t_args.append(t)
        x_args.append(x)
        y_args.append(y)
    return np.array([x_args, y_args, x_speed, y_speed, t_args]).T


def reduce_array(arr,by_step):
    """
    this method reduce the number of cordinates
    can be use for plotitng  graph to be more notably

    :param arr:
    :param by_step:
    :return:
    """
    i=0
    result = []
    leng = arr.shape
    p  = leng[0]
    while i < p:
        result.append(arr[i])
        i = i+by_step

    return np.array(result)