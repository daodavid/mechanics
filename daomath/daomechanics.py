import numpy as np
import matplotlib.pyplot as plt
from daomath.numdao import *


class VectorField:

    def __init__(self, x_function, y_function, z_function=None, range=[-10, 10],coridinates=None):
        """

        :param x_function: e1 = U(x,y)
        :param y_function: e2 = V(x,y)
        :param z_function: e3 = P(x,y)
        :param range:
        """
        if coridinates is not None:
            self.field_cordinates=coridinates
        else :
           self.U = x_function
           self.V = y_function
           self.z = z_function
           self.rng = range
           self.evaluate_cord_field()


    def plot_field(self, color='b', reduce=20, scale=5, width=0.003,label=r'$\vec F$'):
        v = self.field_cordinates
        x0 = v[:, 0]
        y0 = v[:, 1]
        x = v[:, 2]
        y = v[:, 3]
        x0 = reduce_array(x0, reduce)
        y0 = reduce_array(y0, reduce)
        x = reduce_array(x, reduce)
        y = reduce_array(y, reduce)

        q = plt.quiver(x0, y0, x, y, angles='xy', scale_units='xy', scale=scale, color=color, width=width,label=label,linewidth=1)
        #line3, = plt.plot([0, 0, 0], label=r'$\vec F$', linewidth=1, color=color)
        ax = plt.gca()
        #ax.plot([10, 6, 10])
        plt.legend(loc='upper left')
        ax.spines['top'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        plt.text(self.rng[1], self.rng[1], label, fontsize=20, verticalalignment='center')
        plt.xlim(self.rng[0], self.rng[1])
        plt.ylim(self.rng[0], self.rng[1])

    def evaluate_cord_field(self):
        x = np.linspace(self.rng[0], self.rng[1], 50)
        y = np.linspace(self.rng[0], self.rng[1], 50)
        self.field_cordinates = np.array([[x0, y0, self.U(x0, y0), self.V(x0, y0)] for y0 in y for x0 in x])

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


    def sum(vector_field1 ,vecor_field2):
        v1 = vector_field1
        v2 = vecor_field2

        x0 = v1[:,0]
        y0 = v1[:,0]
        x =  v1[:,1]+v2[:,1]
        y = v1[:, 2] + v2[:, 2]
        return VectorField(np.array([x0,y0,x,y]).T)


f = VectorField(lambda x,y : 0 , lambda x,y : -9.8)
f.plot_field(reduce=8,scale=10,width=0.003,label=r'$-g.\vec{j}$')
plt.show()
