import numpy as np
import matplotlib.pyplot as plt
from daomath.numdao import *


class VectorField:

    def __init__(self, x_function, y_function, z_function=None, range=[1, 10]):
        """

        :param x_function: e1 = U(x,y)
        :param y_function: e2 = V(x,y)
        :param z_function: e3 = P(x,y)
        :param range:
        """
        self.U = x_function
        self.V = y_function
        self.z = z_function
        self.rng = range
        self.evaluate_cord_field()

    def plot_field(self, matrix, color='b', reduce=20, scale=5, width=0.003):
        v = matrix
        x0 = v[:, 0]
        y0 = v[:, 1]
        x = v[:, 2]
        y = v[:, 3]
        x0 = reduce_array(x0, reduce)
        y0 = reduce_array(y0, reduce)
        x = reduce_array(x, reduce)
        y = reduce_array(y, reduce)

        q = plt.quiver(x0, y0, x, y, angles='xy', scale_units='xy', scale=scale, color=color, width=width)

    def evaluate_cord_field(self):
        x = np.linspace(self.rng[0], self.rng[1], 80)
        y = np.linspace(self.rng[0], self.rng[1], 80)
        self.field_cordinates = np.array([[x0, y0, self.U(0, x0, y0), self.V(0, x0, y0)] for y0 in y for x0 in x])

    def get_coridinates(self):
        return self.field_cordinates

    # def plot_p(self):
    #     self.ax = plt.gca()
    #     plt.title('Arrows scale with plot width, not view')
    #     self.ax.spines['top'].set_color('none')
    #     self.ax.spines['bottom'].set_position('zero')
    #     self.ax.spines['left'].set_position('zero')
    #     self.ax.spines['right'].set_color('none')
    #     plt.text(1, 1, r'$2 \frac{m}{s}$', fontsize=20, verticalalignment='center', transform=self.ax.transAxes)
    #     plt.xlim(-100, 100)
    #     plt.ylim(-100, 100)
    #     plt.axis('equal')

    def append_vector(self):
        pass

    def get_field_cordinates(self):
        return self.field_cordinates
