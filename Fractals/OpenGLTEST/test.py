from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 500, 500     # Width - Height

def drawMandlebrot():
    glBegin(GL_POINTS)
    glVertex2i(100, 100)
    glVertex2i(200, 100)
    glVertex2i(200, 200)
    glVertex2i(100, 200)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)              # Sets the default viewport
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear entire screen
    glLoadIdentity()                                    # Reset all graphic / shapes' position
    iterate()                                           #
    glColor3f(1.0, 0.0, 3.0)                            # Set the color to pink
    drawMandlebrot()                                            # Draw the screen using the square function
    glutSwapBuffers()                                   # Swaps buffers from front to back


glutInit()                      # Initialize display
glutInitDisplayMode(GLUT_RGBA)  # Set coloring mode
glutInitWindowSize(500, 500)    # Initial dimensions of window
glutInitWindowPosition(0, 0)    # Default window position?
wind = glutCreateWindow("Mandlebrot zoom")
glutDisplayFunc(showScreen)     # Method to be continuously called
glutIdleFunc(showScreen)        # Draw any graphics or shapes in the showScreen func at all times
glutMainLoop()                  # Keeps the window created running

