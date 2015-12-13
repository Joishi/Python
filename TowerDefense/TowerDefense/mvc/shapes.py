# This file contains shapes to draw with openGL

from collections import deque
import math

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

    def distance(self, point):
        dx = self._x - point.x
        dy = self._y - point.y
        dz = self._z - point.z
        return math.hypot(math.hypot(dx, dy), math.hypot(dy, dz))

    def translate(self, dx, dy, dz):
        self._x += dx
        self._y += dy
        self._z += dz


class Movable(object):

    def __init__(self, startPoint, startingVelocity, maximumVelocity, acceleration):
        self._currentLocation = startPoint
        self._currentDestination = None
        self._destinations = deque()
        self._currentVelocity = startingVelocity
        self._maximumVelocity = maximumVelocity
        self._acceleration = acceleration

    def addDestination(self, destinationPoint):
        self._destinations.append(destinationPoint)

    def move(self, elapsedTime):
        doneMoving = True
        if self._currentDestination is not None:
            # adjust velocity
            if self._currentVelocity < self._maximumVelocity:
                self._currentVelocity += (self._acceleration * elapsedTime)
            if self._currentVelocity > self._maximumVelocity:
                self._currentVelocity = self._maximumVelocity
            distanceToDestination = self._currentLocation.distance(self._currentDestination)
            if distanceToDestination == 0:
                self._currentDestination = None
                doneMoving = self.move(elapsedTime)
            else:
                maxDistanceCanTravelThisFrame = self._currentVelocity * elapsedTime
                ratio = maxDistanceCanTravelThisFrame / distanceToDestination
                if ratio >= 1:
                    # Set to destination, figure out how long that took, and move again with remaining time .. also adjust velocity so that acceleration isn't accidentally doubled
                    self._currentLocation = self._currentDestination
                    self._currentDestination = None
                    remainingDistanceToTravel = maxDistanceCanTravelThisFrame - distanceToDestination
                    ratio = remainingDistanceToTravel / maxDistanceCanTravelThisFrame
                    newElapsedTime = elapsedTime * ratio
                    self._currentVelocity -= (self._acceleration * newElapsedTime)
                    doneMoving = self.move(newElapsedTime)
                else:
                    # Just move and be done .. return False because not done moving yet .. calculations based off of similar triangles
                    bigDX = self._currentDestination.x - self._currentLocation.x
                    bigDY = self._currentDestination.y - self._currentLocation.y
                    bigDZ = self._currentDestination.z - self._currentLocation.z
                    self._currentLocation.translate(bigDX * ratio, bigDY * ratio, bigDZ * ratio)
                    doneMoving = False
        else:
            if len(self._destinations) > 0:
                self._currentDestination = self._destinations.popleft()
                doneMoving = self.move(elapsedTime)
        return doneMoving

    def getCurrentLocation(self):
        return self._currentLocation

    currentLocation = property(getCurrentLocation, None, None, "The current location of the movable shape")


class Sphere(Movable):

    def __init__(self, center, radius, color):
        Movable.__init__(self, center, 10, 30, 2)
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

