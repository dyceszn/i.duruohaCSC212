import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

data = np.random.randn(1000)
plt.figure()
plt.hist(data, bins=30)
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()