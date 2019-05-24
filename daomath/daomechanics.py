import numpy as np
import matplotlib.pyplot as plt
from daomath.numdao import *
from matplotlib import animation, rc
from IPython.display import HTML


class VectorField:

    def __init__(self, x_function, y_function, z_function=None, range=[-10, 10], coridinates=None):
        """

        :param x_function: e1 = U(x,y)
        :param y_function: e2 = V(x,y)
        :param z_function: e3 = P(x,y)
        :param range:
        """
        if coridinates is not None:
            self.field_cordinates = coridinates
        else:
            self.U = x_function
            self.V = y_function
            self.z = z_function
            self.rng = range
            self.evaluate_cord_field()

    def plot_field(self, color='b', reduce=20, scale=5, width=0.003, label=r'$\vec F$'):
        v = self.field_cordinates
        x0 = v[:, 0]
        y0 = v[:, 1]
        x = v[:, 2]
        y = v[:, 3]
        x0 = reduce_array(x0, reduce)
        y0 = reduce_array(y0, reduce)
        x = reduce_array(x, reduce)
        y = reduce_array(y, reduce)

        q = plt.quiver(x0, y0, x, y, angles='xy', scale_units='xy', scale=scale, color=color, width=width, label=label)
        # line3, = plt.plot([0, 0, 0], label=r'$\vec F$', linewidth=1, color=color)
        ax = plt.gca()
        # ax.plot([10, 6, 10])
        plt.legend(loc='upper left')
        ax.spines['top'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        # plt.text(self.rng[1], self.rng[1], label, fontsize=20, verticalalignment='center')
        plt.xlim(self.rng[0], self.rng[1])
        plt.ylim(self.rng[0], self.rng[1])

    def evaluate_cord_field(self):
        x = np.linspace(self.rng[0], self.rng[1], 50)
        y = np.linspace(self.rng[0], self.rng[1], 50)
        t = np.linspace(self.rng[0], self.rng[1], 50)
        self.field_cordinates = np.array([[x0, y0, self.U(t[0], x0, y0), self.V(t[0], x0, y0)] for y0 in y for x0 in x])

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

    def sum(vector_field1, vecor_field2):
        v1 = vector_field1
        v2 = vecor_field2

        x0 = v1[:, 0]
        y0 = v1[:, 0]
        x = v1[:, 1] + v2[:, 1]
        y = v1[:, 2] + v2[:, 2]
        return VectorField(np.array([x0, y0, x, y]).T)


# M = 10
# fx = lambda x, y: -M * x / ((x ** 2 + y ** 2) ** (3 / 2))
# fy = lambda x, y: -M * y / ((x ** 2 + y ** 2) ** (3 / 2))
# f = VectorField(fx, fy)
# f.plot_field(reduce=6, scale=10, width=0.003)
# plt.show()
class Force(VectorField):
    def __init__(self, x_function, y_function, z_function=None, range=[-10, 10], coridinates=None):
        super().__init__(x_function, y_function, z_function=None, range=[-10, 10], coridinates=None)


class MaterialPoint():

    def __init__(self, x0=0, y0=0, mass=1, v_x0=0, v_y0=0):
        self.x0 = x0
        self.y0 = y0
        self.v_x0 = v_x0
        self.v_y0 = v_y0
        self.mass = mass
        self.r = np.array([[x0], [y0], [v_x0], [v_y0], [0]])
        self.last_x = x0
        self.last_y = y0
        self.last_vx=v_x0
        self.last_vy=v_y0
        self.x_args = [x0]
        self.y_args = [y0]

    def __get_coordinate__(self, time):
        pass

    def __get_coordinate__(self):
        pass

    def get_speed(self):
        pass

    def get_acceleration(self):
        pass

    def get_mass(self):
        return self.mass
    def get_energy(self):
        return self.mass*(self.last_vx**2 + self.last_vy**2)/2

    def set_last_coor(self, x, y):
        self.last_x = x
        self.last_y = y

    def get_radius_vector(self):
        pass

    def add_force_field(self, f):
        self.force = f

    def add_force(self, force):
        self.force = force

    def get_init_speed(self):
        return np.array([self.v_x0, self.v_y0])

    def calculate_speed(self, vx0, vy0, time_range=[0, 100], step=60):
        self.vx0 = vx0
        self.vy0 = vy0
        self.speed_space = solveODE(self.force.U, self.force.V, vx0, vy0)

    def draw_speed(self):
        self.force.plot_field(self.speed_space, color='green')

    def calculate_radius_vector(self, vx0, vy0, n=10, h=0.01):
        # self.r = leapFrog(self.force.U,self.force.V,vx0,vy0,h=0.0001)
        # self.x_args = intergrate(self.x0,self.speed_space[:,0],self.speed_space[:,2])
        # self.y_args = intergrate(self.y0, self.speed_space[:,1], self.speed_space[:,2])
        # k = 7
        # fx = lambda t, x, y: -k * x / ((x ** 2 + y ** 2) ** (3 / 2))
        # fy = lambda t, x, y: -k * y / ((x ** 2 + y ** 2) ** (3 / 2))
        self.r = leapFrog(self.force.U, self.force.V, self.x0, self.y0, vx0, vy0, n=n, h=h, c=self.mass)
        last = self.r.shape[0]
        self.last_x = self.r[last:0]
        self.last_y = self.r[last:1]
        self.x_args = self.r[:, 0]
        self.x_args = self.r[:, 1]
        return self.r

    def set_radius_vector(self, arr):
        pass

    def append_coordinates(self,x,y):
        self.last_x=x
        self.last_x=y
        self.x_args.append(x)
        self.y_args.append(y)


    def get_radius_vector(self):
        return self.r

    def get_coordinates(self):
        return np.array([self.x_args,self.y_args]).T

    def plot_radios_vector(self,reduce=20):
        n = 10
        x = reduce_array(self.r[:, 0],reduce)
        y = reduce_array(self.r[:, 1], reduce)
        x0 = x*0

        q = plt.quiver(x0, x0, x, y, angles='xy', scale_units='xy', scale=1, color='r', width=0.003)
        plt.show()

    def plot_graph_motion(self, scale=6000):
        n = scale
        x = reduce_array(self.x_args[:, 0], n)
        y = reduce_array(self.y_args[:, 0], n)
        speed_x = reduce_array(self.speed_space[:, 0], n)
        speed_y = reduce_array(self.speed_space[:, 1], n)
        sp1x = derivate(self.x_args[:, 0], self.x_args[:, 1])
        sp1y = derivate(self.y_args[:, 0], self.y_args[:, 1])
        sp1x = reduce_array(sp1x, n)
        sp1y = reduce_array(sp1y, n)
        # x=self.x_args
        # y=self.y_args
        x0 = x * 0
        y0 = y * 0
        spe0 = plt.quiver(self.x0, self.y0, self.vx0, self.vy0, scale=40, color='violet', width=0.009)  # \vec a
        line, = plt.plot([4, 2, 1], label=r'$\vec v_0$', linewidth=1, color='violet')
        sp = plt.quiver(x, y, sp1x, sp1y, scale=60, color='green', width=0.003)
        line2, = plt.plot([4, 2, 1], label=r'$\vec v$', linewidth=1, color='green')
        q = plt.quiver(x0, x0, x, y, angles='xy', scale_units='xy', scale=1, color='r', width=0.003)
        line3, = plt.plot([4, 2, 1], label=r'$\vec r$', linewidth=1, color='r')

    def plot_graph(self):
        plt.plot(self.r[:, 0], self.r[:, 1])

    def get_size(self, z=1):
        self.z = z
        size = self.r.shape[0] / z
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

        q = plt.scatter(self.r[i, 0], self.r[i, 1], color='black', linewidths=5)
        q = plt.scatter(0, 0, color='black')

        rezult = particles

        z = plt.plot(self.r[:, 0], self.r[:, 1], color='blue')
        plt.draw()

        return particles
        #

# z = point.calculate_radius_vector(3,4)
# anim = animation.FuncAnimation(fig, point.update_HTML_animation, fargs=(Q, X, Y),
#
#                                interval=50, blit=False)

# k = 10
# u = lambda t, x, y: -400 * x / ((x ** 2 + y ** 2) ** (3 / 2))
# v = lambda t, x, y: -400 * y / ((x ** 2 + y ** 2) ** (3 / 2))
# u = lambda t, x, y: 0
# v = lambda t, x, y: -10
# point = MaterialPoint(x0=0, y0=0, mass=1)
# f = VectorField(u, v)
# point.add_force(f)
# z = point.calculate_radius_vector(20*np.cos(np.pi/4), +50*np.sin(np.pi/4),n=1000)

# point.plot_graph()
# size = int(point.get_size(1))
# point.update_HTML_animation(1)
# print(size)
# plt.show()


#
# fig = plt.figure(figsize=(6, 6))
# fig = plt.figure(figsize=(6, 6))
#
# u = lambda t, x, y: 0
# v = lambda t, x, y: -10
# point = MaterialPoint(x0=0, y0=0, mass=1)
# f = VectorField(u, v)
# point.add_force(f)
# z = point.calculate_radius_vector(20*np.cos(np.pi/4), +50*np.sin(np.pi/4),n=700)
# plt.plot(z[:,0],z[:,1])
# size = int(point.get_size(40))
# point.plot_radios_vector()
# print(size)
