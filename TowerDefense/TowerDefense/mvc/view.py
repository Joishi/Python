import sys
import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

class MainView(object):

    def __init__(self):
        # FROM http://code.activestate.com/recipes/325391-open-a-glut-window-and-draw-a-sphere-using-pythono/
        print("1")
        glut.glutInit(sys.argv)
        print("2")
        glut.glutInitDisplayMode(glut.GLUT_RGBA | glut.GLUT_DOUBLE | glut.GLUT_DEPTH)
        print("3")
        glut.glutInitWindowSize(400, 400)
        print("4")
        glut.glutCreateWindow(b'PyTowerDefense')

        print("5")
        gl.glClearColor(0., 0., 0., 1.)
        print("6")
        gl.glShadeModel(gl.GL_SMOOTH)
        print("7")
        gl.glEnable(gl.GL_CULL_FACE)
        print("8")
        gl.glEnable(gl.GL_DEPTH_TEST)
        print("9")
        gl.glEnable(gl.GL_LIGHTING)
        print("10")
        gl.lightZeroPosition = [10., 4., 10., 1.]
        print("11")
        gl.lightZeroColor = [0.8, 1.0, 0.8, 1.0] #green tinged
        print("12")
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, gl.lightZeroPosition)
        print("13")
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_DIFFUSE, gl.lightZeroColor)
        print("14")
        gl.glLightf(gl.GL_LIGHT0, gl.GL_CONSTANT_ATTENUATION, 0.1)
        print("15")
        gl.glLightf(gl.GL_LIGHT0, gl.GL_LINEAR_ATTENUATION, 0.05)
        print("16")
        gl.glEnable(gl.GL_LIGHT0)
        print("17")
        glut.glutDisplayFunc(self.paint)
        print("18")
        gl.glMatrixMode(gl.GL_PROJECTION)
        print("19")
        glu.gluPerspective(40., 1., 1., 40.)
        print("20")
        gl.glMatrixMode(gl.GL_MODELVIEW)
        print("21")
        glu.gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)
        print("22")
        gl.glPushMatrix()
        print("23")
        glut.glutMainLoop()

    def paint(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glPushMatrix()
        color = [1.0,0.,0.,1.]
        gl.glMaterialfv(gl.GL_FRONT, gl.GL_DIFFUSE, color)
        glut.glutSolidSphere(2, 20, 20)
        gl.glPopMatrix()
        glut.glutSwapBuffers()
        return

