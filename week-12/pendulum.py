# PENDULUM

import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation

length = 1
g = 9.81
theta = np.pi/ 6

frames = 200
t = np.linspace(0, 4, frames)
omega = np.sqrt(g / length)
theta = theta  * np.cos(omega * t)

fig, ax = plt.subplots()
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 0.2)
ax.set_aspect('equal')
line, =  ax.plot([], [], 'o-', lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    x = np.cos(theta[frame])
    y = np.sin(theta[frame])
    line.set_data([0, x], [0, y])
    return line,

ani = FuncAnimation(fig, update, frames=frames, init_func=init , blit=True, interval=50)
plt.title("Pendulum")
plt.show()
