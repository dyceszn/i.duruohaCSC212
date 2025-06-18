
# BOUNCING BALL

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation



g = 9.81
frames = 200
dt = 0.05
y = 1.0
v = 0.0
positions  = []

for _ in range(frames):
    v -= g * dt
    y += v * dt
    if y < 0:
        y = 0
        v = -v  * 0.9
    positions.append(y)

fig, ax = plt.subplots()
ax.set_xlim(0, frames)
ax.set_ylim(0, 2)
ball, = ax.plot([], [], 'ro', markersize = 20)

def init():
    ball.set_data([], [])
    return ball,

def update(frame):
    ball.set_data([frame], [positions[frame]])
    return ball,

ani = FuncAnimation(fig, update, frames=frames, init_func=init , blit=True, interval=50)
plt.title("Bouncing ball")
plt.show()
