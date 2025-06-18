# SPRING

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

A = 0.5
k = 10
m = 1
omega = np.sqrt(k / m)

frames = 200
t = np.linspace(0, 4, frames)
x = A * np.cos(omega * t)

fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-0.5, 0.5)
mass, =  ax.plot([], [], 'bs', markersize = 20)

def init():
    mass.set_data([], [])
    return mass,

def update(frame):
    mass.set_data([x[frame]], [0])
    return mass,

ani = FuncAnimation(fig, update, frames=frames, init_func=init , blit=True, interval=50)
plt.title("Spring")
plt.show()












