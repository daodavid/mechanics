import numpy as np
import matplotlib.pyplot as plt
from daomath.numdao import *
from matplotlib import animation, rc
from IPython.display import HTML
import math
from daomath.daomechanics import MaterialPoint
from daomath.numdao import *


class Ground:
    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def calculate_speed_points(self, end_time=1000, h=0.1):
        times = []
        c = 0.5

        for i in range(len(self.points)):
            is_has_collision = False
            for j in range(len(self.points)):
                p = self.points[i]
                p1 = self.points[j]
                if i != j and ((abs(p.last_x - p1.last_x)) <= c) and (abs(p.last_y - p1.last_y) <= c):
                    self.calculate_momentum_conservation(p, p1)
                    is_has_collision = True
                    break

            if not is_has_collision:
                self.__update_coordinates(p)

    def calculate_momentum_conservation(self, p, p1):
        pass

    def __update_coordinates(self, p, h=0.1):
        """
        update cordinate with one incremented(integrated) step

        :param p: Material point
        :param vx_0: init value for vx cordinate
        :param vy_0: init value for vy cordinate
        :param h: increment integration step
        :return:
        """
        x = p.last_x
        y = p.last_y
        vx = p.last_vx
        vy = p.last_vy

        x = x + h * vx
        y = y + h * vy
        p.append_coordinates(x, y)


g = Ground()
g.add_point(MaterialPoint(x0=0, y0=0, mass=3, v_x0=1, v_y0=2))
g.add_point(MaterialPoint(x0=3, y0=3, mass=3, v_x0=3, v_y0=4))
g.add_point(MaterialPoint(x0=3.1, y0=3.1, mass=3, v_x0=3, v_y0=4))
g.add_point(MaterialPoint(x0=7, y0=7, mass=3, v_x0=1, v_y0=-2))
g.calculate_speed_points()

points = g.points
for p in points:
    print(p.get_coordinates())
