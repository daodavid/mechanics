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

    def calculate_speed_points(self, end_time=100, h=0.1):
        times = []
        t = 0
        c = 0.5
        for t in range(end_time):
            for i in range(len(self.points)):
                is_has_collision = False
                for j in range(len(self.points)):
                    p = self.points[i]
                    p1 = self.points[j]
                    if i != j and ((abs(p.last_x - p1.last_x)) <= c) and (abs(p.last_y - p1.last_y) <= c):
                        #self.calculate_momentum_conservation(p, p1)
                        #is_has_collision = True
                        #break
                        pass
                if not is_has_collision:
                   self.__update_coordinates(p)

        t = t + h
        times.append(t)

    def calculate_momentum_conservation(self, point1, point2, limit=[10, 10, 0.0]):
        v_11 = point1.last_vx
        v_12 = point1.last_vy
        v_21 = point2.last_vx

        v_22 = point2.last_vy
        m1 = point1.get_mass()
        m2 = point1.get_mass()

        E1 = point1.get_energy()


        E2 = point2.get_energy()
        H = E1 + E2  # all energy
        v1 = H / (2 * m1)  # volume of speed v1
        v2 = H / (2 * m2)

        p1 = m1 * v_11 + m2 * v_21
        p2 = m1 * v_12 + m2 * v_22

        k = (-v_11 - v_21) / (-v_21 - v_22)  ## tg calculate propertion between x and y coordinates

        v_11 = v1 * (k ** 2) / (1 + k ** 2)
        v_12 = v_11 / k

        k = (-v_21 - v_11) / (-v_22 - v_12)
        v_21 = v2 * (k ** 2) / (1 + k ** 2)
        v_22 = v_21 / k

        self.update_coor(point1, v_11, v_12)
        self.update_coor(point2, v_21, v_22)


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


    def update_coor(self, point, v1, v2, h=0.1):
        x = point.last_x
        y = point.last_y
        vx = v1
        vy = v2

        x = x + h * vx
        y = y + h * vy
        point.append_coordinates(x, y)

    def plot_motion(self):
        size = len(self.points[0].x_args)
        for i in range(size):
            for p in self.points:
                x0=p.x_args[i]
                y0=p.y_args[i]
                plt.plot(x0.y0)

    def get_size(self):
        size = len(self.points[0].x_args)
        return size

    def update_HTML_animation(self, i, arg):
        ax = plt.gca()

        # q =ax.quiver(0, 0, self.r[i,2],  self.r[i,3], pivot='mid', color='r', units='inches')
        # q = ax.quiver(0, 0, self.r[i, 2], self.r[i, 3], pivot='mid', color='r', units='inches')
        i = i * self.z

        arg.clf()
        ax.spines['top'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.set_aspect('equal')
        particles, = ax.plot([], [], 'bo', ms=6)
        particles.set_data([], [])
        particles.set_data(self.r[i, 0], self.r[i, 1])
        particles.set_markersize(20)

        particles, = ax.plot([], [], 'bo', ms=6)

        for p in self.points:
            x0 = p.x_args[i]
            y0 = p.y_args[i]
            q = plt.scatter(x0.y0, color='black', linewidths=5)
            particles.set_data([], [])
            particles.set_data(x0, y0)

            rezult = particles

            z = plt.plot(self.r[:, 0], self.r[:, 1], color='blue')
            plt.draw()

        return particles



g = Ground()
g.add_point(MaterialPoint(x0=1, y0=5, mass=3, v_x0=1, v_y0=2))
g.add_point(MaterialPoint(x0=4, y0=6, mass=3, v_x0=3, v_y0=4))
g.add_point(MaterialPoint(x0=3.1, y0=3.1, mass=3, v_x0=3, v_y0=4))
g.add_point(MaterialPoint(x0=3, y0=6, mass=3, v_x0=2, v_y0=5))
g.calculate_speed_points()
plt.show()

points = g.points
for p in points:
    print(p.get_coordinates())
