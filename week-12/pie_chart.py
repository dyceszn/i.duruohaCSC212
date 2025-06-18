import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

labels = ['Python', 'C++', 'Ruby', 'Java']
sizes = [215, 130, 245, 210]
plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart Example")
plt.show()