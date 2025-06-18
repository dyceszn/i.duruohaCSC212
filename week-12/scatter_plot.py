import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()