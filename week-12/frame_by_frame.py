# FRAME BY FRAME

import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

point, =  ax.plot([], [], 'bo', markersize = 10)

frames = 100

def init():
    point.set_data([], [])
    return point,

def update(frame):
    angle = 2 * np.pi * frames / frames
    x = np.cos(angle)
    y = np.sin(angle)
    point.set_data(x, y)
    return point,


ani = FuncAnimation(fig, update, frames=frames, init_func=init , blit=True, interval=50)

plt.show()