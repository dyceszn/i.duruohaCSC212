from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

angle = 0

def draw_cube():
	global angle
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	glTranslatef(0.0, 0.0, -5)
	glRotatef(angle, 1, 1, 1)

	glBegin(GL_QUADS)
	# Top face (red)
	glColor3f(1, 0, 0)
	glVertex3f( 1, 1,-1)
	glVertex3f(-1, 1,-1)
	glVertex3f(-1, 1, 1)
	glVertex3f( 1, 1, 1)
	# Bottom face (green)
	glColor3f(0, 1, 0)
	glVertex3f( 1,-1, 1)
	glVertex3f(-1,-1, 1)
	glVertex3f(-1,-1,-1)
	glVertex3f( 1,-1,-1)
	# Front face (blue)
	glColor3f(0, 0, 1)
	glVertex3f( 1, 1, 1)
	glVertex3f(-1, 1, 1)
	glVertex3f(-1,-1, 1)
	glVertex3f( 1,-1, 1)
	# Back face (yellow)
	glColor3f(1, 1, 0)
	glVertex3f( 1,-1,-1)
	glVertex3f(-1,-1,-1)
	glVertex3f(-1, 1,-1)
	glVertex3f( 1, 1,-1)
	# Left face (magenta)
	glColor3f(1, 0, 1)
	glVertex3f(-1, 1, 1)
	glVertex3f(-1, 1,-1)
	glVertex3f(-1,-1,-1)
	glVertex3f(-1,-1, 1)
	# Right face (cyan)
	glColor3f(0, 1, 1)
	glVertex3f( 1, 1,-1)
	glVertex3f( 1, 1, 1)
	glVertex3f( 1,-1, 1)
	glVertex3f( 1,-1,-1)
	glEnd()

	angle += 1
	glutSwapBuffers()

def timer(i):
	glutPostRedisplay()
	glutTimerFunc(16, timer, 1)

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(600, 600)
	glutCreateWindow(b"Rotating 3D Cube")
	glEnable(GL_DEPTH_TEST)
	glutDisplayFunc(draw_cube)
	glutTimerFunc(16, timer, 1)
	glutMainLoop()

main()