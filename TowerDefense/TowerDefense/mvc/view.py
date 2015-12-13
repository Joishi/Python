
import sys
import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

class ModelListener(object):
    '''To properly implement this class, you will need to add the following functions to your class:
    gameStagesChanged(self, model)'''
    def __init__(self):
        None

    def modelChanged(self, model):
        self.gameStagesChanged(model)

    def gameStagesChanged(self, model):
        raise NotImplementedError("This method has not been implemented yet")


class MainView(ModelListener):

    def __init__(self):
        ModelListener.__init__(self)
        self._model = None

        sphereCenter = Point3D(0, 0, 0)
        sphereColor = Color(255, 127, 0, 255)
        self.sphere = Sphere(sphereCenter, 2, sphereColor)

    def show(self):
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
        gl.lightZeroPosition = [10., 4., 10., 1.]
        gl.lightZeroColor = [0.8, 1.0, 0.8, 1.0] #green tinged
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, gl.lightZeroPosition)
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_DIFFUSE, gl.lightZeroColor)
        gl.glLightf(gl.GL_LIGHT0, gl.GL_CONSTANT_ATTENUATION, 0.1)
        gl.glLightf(gl.GL_LIGHT0, gl.GL_LINEAR_ATTENUATION, 0.05)
        gl.glEnable(gl.GL_LIGHT0)
        glut.glutDisplayFunc(self.paint)
        glut.glutIdleFunc(self.repaint)
        gl.glMatrixMode(gl.GL_PROJECTION)
        glu.gluPerspective(40., 1., 1., 40.)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        eyePosition = Point3D(0, 0, 10)
        watchingPosition = Point3D(0, 0, 0)
        upVector = Point3D(0, 1, 0)
        glu.gluLookAt(eyePosition.x, eyePosition.y, eyePosition.z, watchingPosition.x, watchingPosition.y, watchingPosition.z, upVector.x, upVector.y, upVector.z)
        gl.glPushMatrix()
        glut.glutMainLoop()

    def setModel(self, model):
        if self._model is not None:
            self._model.removeModelListener(self)
        self._model = model
        self._model.addModelListener(self)

    model = property(None, setModel, None, "The model used for this view")

    def gameStagesChanged(self, model):
        self.updateGameStages(model.gameStages)

    def paint(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glPushMatrix()
        sphereCenter = self.sphere.center
        sphereRadius = self.sphere.radius
        sphereColor = self.sphere.color
        gl.glTranslate(sphereCenter.x, sphereCenter.y, sphereCenter.z)
        gl.glMaterialfv(gl.GL_FRONT, gl.GL_DIFFUSE, [sphereColor.getRedAsPercent(), sphereColor.getGreenAsPercent(), sphereColor.getBlueAsPercent(), sphereColor.getAlphaAsPercent()])
        glut.glutSolidSphere(sphereRadius, 50, 50)
        gl.glPopMatrix()
        glut.glutSwapBuffers()
        self.sphere.rotateColor()
        self.sphere.rotateCenter()
        return

    def repaint(self):
        glut.glutPostRedisplay()

    def updateGameStages(self, gameStages):
        # Do stuff here to populate some UI element with game stages...
        for gameStage in gameStages:
            print(gameStage)
            print("  " + str(gameStage.path))
            for point in gameStage.path.points:
                print("    " + str(point))


class Sphere(object):

    def __init__(self, center, radius, color):
        self._center = center
        self._radius = radius
        self._color = color
        self.redGrow = True
        self.greenGrow = True
        self.blueGrow = True
        self.xGrow = True
        self.yGrow = True
        self.zGrow = True

    def getCenter(self):
        return self._center

    def setCenter(self, center):
        self._center = center

    def getRadius(self):
        return float(self._radius)

    def setRadius(self, radius):
        self._radius = radius

    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color

    center = property(getCenter, setCenter, None, "")
    radius = property(getRadius, setRadius, None, "")
    color = property(getColor, setColor, None, "")

    def rotateCenter(self):
        x = self._center.x
        y = self._center.y
        z = self._center.z
        if x >= 10:
            self.xGrow = False
        if x <= -10:
            self.xGrow = True
        if y >= 10:
            self.yGrow = False
        if y <= -10:
            self.yGrow = True
        if z >= 10:
            self.zGrow = False
        if z <= -10:
            self.zGrow = True
        if self.xGrow:
            x = x + .1
        else:
            x = x - .1
        if self.yGrow:
            y = y + .05
        else:
            y = y - .05
        if self.zGrow:
            z = z + .025
        else:
            z = z - .025
        self._center.x = x
        self._center.y = y
        self._center.z = z

    def rotateColor(self):
        red = self._color.r
        green = self._color.g
        blue = self._color.b
        if red >= 255:
            self.redGrow = False
        if red <= 0:
            self.redGrow = True
        if green >= 255:
            self.greenGrow = False
        if green <= 0:
            self.greenGrow = True
        if blue >= 255:
            self.blueGrow = False
        if blue <= 0:
            self.blueGrow = True
        if self.redGrow:
            red = red + 1
        else:
            red = red - 1
        if self.greenGrow:
            green = green + 1
        else:
            green = green - 1
        if self.blueGrow:
            blue = blue + 1
        else:
            blue = blue - 1
        self._color.r = red
        self._color.g = green
        self._color.b = blue

class Point3D(object):

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def getX(self):
        return float(self._x)

    def setX(self, x):
        self._x = x

    def getY(self):
        return float(self._y)

    def setY(self, y):
        self._y = y

    def getZ(self):
        return float(self._z)

    def setZ(self, z):
        self._z = z

    x = property(getX, setX, None, "The X value for the point")
    y = property(getY, setY, None, "The Y value for the point")
    z = property(getZ, setZ, None, "The Z value for the point")


class Color(object):

    def __init__(self, red, green, blue, alpha):
        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = alpha

    def getRedAsPercent(self):
        return self._red / 255.

    def getGreenAsPercent(self):
        return self._green / 255.

    def getBlueAsPercent(self):
        return self._blue / 255.

    def getAlphaAsPercent(self):
        return self._alpha / 255.

    def getRed(self):
        return self._red

    def setRed(self, red):
        if red >= 0 and red <= 255:
            self._red = red
        else:
            raise ValueError("Red attribute of color must be at least 0 and at most 255")

    def getGreen(self):
        return self._green

    def setGreen(self, green):
        if green >= 0 and green <= 255:
            self._green = green
        else:
            raise ValueError("Green attribute of color must be at least 0 and at most 255")

    def getBlue(self):
        return self._blue

    def setBlue(self, blue):
        if blue >= 0 and blue <= 255:
            self._blue = blue
        else:
            raise ValueError("Blue attribute of color must be at least 0 and at most 255")

    def getAlpha(self):
        return self._alpha

    def setAlpha(self, alpha):
        if alpha >= 0 and alpha <= 255:
            self._alpha = alpha
        else:
            raise ValueError("Alpha attribute of color must be at least 0 and at most 255")

    r = property(getRed, setRed, None, "The red value of the color")
    g = property(getGreen, setGreen, None, "The green value of the color")
    b = property(getBlue, setBlue, None, "The blue value of the color")
    a = property(getAlpha, setAlpha, None, "The opaqueness value of the color")

