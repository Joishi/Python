import logging, time, sys
import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
from mvc.shapes import *

class ModelListener(object):
    '''To properly implement this class, you will need to add the following functions to your class:
    gameStagesChanged(self, model)'''
    def __init__(self):
        return

    def modelChanged(self, model):
        self.gameStagesChanged(model)

    def gameStagesChanged(self, model):
        raise NotImplementedError("This method has not been implemented yet")


class MainView(ModelListener):

    def __init__(self, name):
        self._name = name
        logging.debug("Initializing %r" %(self))
        ModelListener.__init__(self)
        self._model = None
        self._eyePosition = None
        self._watchingPosition = None
        self._upVector = None
        self._lastTime = None
        self._spheres = []
        logging.debug("%r variables declared" %(self))

        sphereCenter = Point3D("Sphere 1 Center")
        sphereRadius = 20
        sphereColor = Color("Sphere 1 Color", 255, 127, 0, 255)
        sphere = Sphere("Sphere 1")
        sphere.center = sphereCenter
        sphere.radius = sphereRadius
        sphere.color = sphereColor
        sphere.addDestination(Point3D("Sphere 1 Destination 1").translate(50, 50, 50))
        sphere.addDestination(Point3D("Sphere 1 Destination 2").translate(-50, -50, -50))
        sphere.addDestination(Point3D("Sphere 1 Destination 3"))
        self._spheres.append(sphere)
        logging.debug("First Sphere added")
        sphereCenter = Point3D("Sphere 2 Center").translate(50, -20, -50)
        sphereRadius = 10
        sphereColor = Color("Sphere 2 Color", 127, 0, 255, 255)
        sphere = Sphere("Sphere 2")
        sphere.center = sphereCenter
        sphere.radius = sphereRadius
        sphere.color = sphereColor
        sphere.addDestination(Point3D("Sphere 2 Destination 1").translate(-50, 50, 50))
        sphere.addDestination(Point3D("Sphere 2 Destination 2").translate(50, 50, -50))
        sphere.addDestination(Point3D("Sphere 2 Destination 3").translate(10, 10, 10))
        self._spheres.append(sphere)
        logging.debug("Second Sphere added")
        logging.debug("Done initializing %r" %(self))
        return

    def __repr__(self):
        return "<MainView %r>" %(getattr(self, '_name', None))

    def show(self):
        self.initOpenGLMatrix()
        glut.glutMainLoop()
        return

    def setModel(self, model):
        if self._model is not None:
            self._model.removeModelListener(self)
        self._model = model
        self._model.addModelListener(self)
        return

    model = property(None, setModel, None, "The model used for this view")

    def gameStagesChanged(self, model):
        self.updateGameStages(model.gameStages)
        # this is only a temporary solution until UI element to select a game stage is done..
        model.activeGameStage = model.gameStages[0]
        return

    def initOpenGLMatrix(self):
        # FROM http://code.activestate.com/recipes/325391-open-a-glut-window-and-draw-a-sphere-using-pythono/
        glut.glutInit(sys.argv)
        glut.glutInitDisplayMode(glut.GLUT_RGBA | glut.GLUT_DOUBLE | glut.GLUT_DEPTH)
        glut.glutInitWindowSize(400, 400)
        glut.glutCreateWindow(b'PyTowerDefense')

        gl.glClearColor(0., 0., 0., 1.)
        gl.glShadeModel(gl.GL_SMOOTH)
        gl.glEnable(gl.GL_CULL_FACE)
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glEnable(gl.GL_LIGHTING)
        gl.lightZeroPosition = [100., 40., 100., 1.]
        gl.lightZeroColor = [0.8, 1.0, 0.8, 1.0] #green tinged
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, gl.lightZeroPosition)
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_DIFFUSE, gl.lightZeroColor)
        gl.glLightf(gl.GL_LIGHT0, gl.GL_CONSTANT_ATTENUATION, 0.01)
        gl.glLightf(gl.GL_LIGHT0, gl.GL_LINEAR_ATTENUATION, 0.005)
        gl.glEnable(gl.GL_LIGHT0)
        glut.glutDisplayFunc(self.paint)
        glut.glutIdleFunc(self.repaint)
        gl.glMatrixMode(gl.GL_PROJECTION)
        glu.gluPerspective(30., 1., 1., 1000.)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        self._eyePosition = Point3D("Camera Eye Location").translate(0, 0, 400)
        self._watchingPosition = Point3D("Camera Watching Position")
        self._upVector = Point3D("Camera Up Vector").translate(0, 1, 0)
        glu.gluLookAt(self._eyePosition.x, self._eyePosition.y, self._eyePosition.z,
                      self._watchingPosition.x, self._watchingPosition.y, self._watchingPosition.z,
                      self._upVector.x, self._upVector.y, self._upVector.z)
        gl.glPushMatrix()
        return

    def paint(self):
        elapsedTime = 0
        currentTime = time.clock()
        if self._lastTime is not None:
            elapsedTime = currentTime - self._lastTime
        self._lastTime = currentTime
        if self._model is not None:
            if self._model.activeGameStage is not None:
                path = self._model.activeGameStage.path
#                for point in path.points:
#                    print(point)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        self._drawSpheres(elapsedTime)
        glut.glutSwapBuffers()
        return

    def _drawSpheres(self, elapsedTime):
        for sphere in self._spheres:
            gl.glPopMatrix()
            gl.glPushMatrix()
            sphereCenter = sphere.currentLocation
            sphereRadius = sphere.radius
            sphereColor = sphere.color
            gl.glTranslate(sphereCenter.x, sphereCenter.y, sphereCenter.z)
            gl.glMaterialfv(gl.GL_FRONT, gl.GL_DIFFUSE, [sphereColor.getRedAsPercent(), sphereColor.getGreenAsPercent(), sphereColor.getBlueAsPercent(), sphereColor.getAlphaAsPercent()])
            glut.glutSolidSphere(sphereRadius, 15, 15)
            sphere.move(elapsedTime)
        return


    def repaint(self):
        glut.glutPostRedisplay()
        return

    def updateGameStages(self, gameStages):
        # Do stuff here to populate some UI element with game stages...
        for gameStage in gameStages:
            print(gameStage)
            print("  " + str(gameStage.path))
            for point in gameStage.path.points:
                print("    " + str(point))
        return

