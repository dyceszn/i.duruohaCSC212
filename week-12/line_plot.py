import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
# Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.figure()
plt.plot(x, y)
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()