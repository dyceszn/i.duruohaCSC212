import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot([], [])
def init():
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    return line,
def update(frame):
    x_data.append(frame)
    y_data.append(random.randint(0, 100))
    line.set_data(x_data, y_data)
    return line,

ani = animation.FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True)
plt.show()