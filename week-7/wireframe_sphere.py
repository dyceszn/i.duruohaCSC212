from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	glTranslatef(0, 0, -5)
	glColor3f(1, 1, 1)
	glutWireSphere(1, 20, 20)
	glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(400, 400)
glutCreateWindow(b"wireframe Sphere")
glEnable(GL_DEPTH_TEST)
glutDisplayFunc(draw)
glutMainLoop()