from daomath.daomechanics import VectorField
from daomath.daomechanics import MaterialPoint
from daomath.ground import Ground
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML
import numpy as np


fig = plt.figure(figsize=(6, 6))
fig = plt.figure(figsize=(6, 6))
g = Ground()
g.add_point(MaterialPoint(x0=0, y0=5, mass=5, v_x0=3, v_y0=0))
g.add_point(MaterialPoint(x0=10, y0=5, mass=15, v_x0=-3, v_y0=0))

g.calculate_speed_points(end_time=80)
points = g.points
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
size = len(g.points[0].x_args)
anim = animation.FuncAnimation(fig, g.update_HTML_animation,interval=80,fargs=(fig,),frames=size, blit=False)
#HTML(anim.to_html5_video())

anim.save('sources/2-bodies-convservation.mp4', writer=writer)