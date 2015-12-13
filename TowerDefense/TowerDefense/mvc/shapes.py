# This file contains shapes to draw with openGL

import logging, math
from collections import deque

class Movable(object):

    def __init__(self):
        self._startingPoint = None
        self._currentLocation = None
        self._currentDestination = None
        self._destinations = deque()
        self._currentVelocity = 0
        self._maximumVelocity = 0
        self._acceleration = 0
        return

    def addDestination(self, destinationPoint):
        logging.debug("%r Adding Destination %r" %(self, destinationPoint))
        self._destinations.append(destinationPoint)
        return

    def move(self, elapsedTime):
        doneMoving = True
        if self._currentLocation is None:
            self._currentLocation = self._startingPoint
        if self._currentLocation is not None and self._currentDestination is not None:
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
        elif self._currentLocation is not None:
            if len(self._destinations) > 0:
                self._currentDestination = self._destinations.popleft()
                doneMoving = self.move(elapsedTime)
        if doneMoving:
            logging.debug("%r IS DONE MOVING" %(self))
        return doneMoving

    def setStartingPoint(self, startingPoint):
        logging.debug("%r Setting Starting Point %r" %(self, startingPoint))
        self._startingPoint = startingPoint
        return

    def getCurrentLocation(self):
        return self._currentLocation

    def setCurrentLocation(self, location):
        logging.debug("%r Setting Current Location %r" %(self, location))
        self._currentLocation = location
        return

    def getCurrentVelocity(self):
        return self._currentVelocity

    def setCurrentVelocity(self, velocity):
        logging.debug("%r Setting Current Velocity %r" %(self, velocity))
        self._currentVelocity = velocity
        return

    def setMaximumVelocity(self, maximumVelocity):
        logging.debug("%r Setting Maximum Velocity %r" %(self, maximumVelocity))
        self._maximumVelocity = maximumVelocity
        return

    def getAcceleration(self):
        return self._acceleration

    def setAcceleration(self, acceleration):
        logging.debug("%r Setting Acceleration %r" %(self, acceleration))
        if acceleration >= 0:
            self._acceleration = acceleration
        return

    startingPoint = property(None, setStartingPoint, None, "The location this object will start at")
    currentLocation = property(getCurrentLocation, setCurrentLocation, None, "The current location of the movable shape")
    velocity = property(getCurrentVelocity, setCurrentVelocity, None, "The velocity that the object is currently moving at")
    maxVelocity = property(None, setMaximumVelocity, None, "The maximum speed that the object is allowed to move")
    acceleration = property(getAcceleration, setAcceleration, None, "The rate of change for the velocity - Must be positive")


class Point3D(object):
    '''A point in a 3D space. Every point starts at (0,0,0) .. to give it an initial location, use the translate method.'''

    def __init__(self, name):
        self._name = name
        logging.debug("Initializing %r" %(self))
        self._x = 0
        self._y = 0
        self._z = 0
        logging.debug("Done initializing %r" %(self))
        return

    def __repr__(self):
        return "<Point3D %r (x=%r, y=%r, z=%r)>" %(getattr(self, '_name', None), getattr(self, '_x', None), getattr(self, '_y', None), getattr(self, '_z', None))

    def getX(self):
        return float(self._x)

    def getY(self):
        return float(self._y)

    def getZ(self):
        return float(self._z)

    x = property(getX, None, None, "The X value for the point")
    y = property(getY, None, None, "The Y value for the point")
    z = property(getZ, None, None, "The Z value for the point")

    def translate(self, dx, dy, dz):
        logging.debug("%r Translating by %r, %r, %r" %(self, dx, dy, dz))
        self._x += dx
        self._y += dy
        self._z += dz
        return self

    def distance(self, point):
        dx = self._x - point.x
        dy = self._y - point.y
        dz = self._z - point.z
        return math.hypot(math.hypot(dx, dy), math.hypot(dy, dz))


class Rectangle(Movable):
    
    def __init__(self):
        None

class Sphere(Movable):

    def __init__(self, name):
        self._name = name
        logging.debug("Initializing %r" %(self))
        Movable.__init__(self)
        self._radius = None
        self._color = None
        logging.debug("Done initializing %r" %(self))
        return

    def __repr__(self):
        return "<Sphere %r (center=%r, radius=%r, color=%r)>" %(getattr(self, '_name', None), getattr(self, 'center', None), getattr(self, '_radius', None), getattr(self, '_color', None))

    def getCenter(self):
        return Movable.currentLocation.fget(self)

    def setCenter(self, center):
        logging.debug("%r Setting Center %r" %(self, center))
        Movable.startingPoint.fset(self, center)
        Movable.currentLocation.fset(self, center)
        return

    def getRadius(self):
        return float(self._radius)

    def setRadius(self, radius):
        logging.debug("%r Setting Radius %r" %(self, radius))
        self._radius = radius
        return

    def getColor(self):
        return self._color

    def setColor(self, color):
        logging.debug("%r Setting Color %r" %(self, color))
        self._color = color
        return

    center = property(getCenter, setCenter, None, "Identical to the current location. Sphere-friendly name, however.")
    radius = property(getRadius, setRadius, None, "The radius of the sphere.")
    color = property(getColor, setColor, None, "The color of the sphere.")


class Color(object):

    def __init__(self, name, red, green, blue, alpha):
        self._name = name
        logging.debug("Initializing %r" %(self))
        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = alpha
        logging.debug("Done initializing %r" %(self))
        return

    def __repr__(self):
        return "<Color %r (red=%r, green=%r, blue=%r, alpha=%r)>" %(getattr(self, '_name', None), getattr(self, '_red', None), getattr(self, '_green', None), getattr(self, '_blue', None), getattr(self, '_alpha', None))

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
            logging.debug("%r Setting Red %r" %(self, red))
            self._red = red
        else:
            raise ValueError("Red attribute of color must be at least 0 and at most 255")
        return

    def getGreen(self):
        return self._green

    def setGreen(self, green):
        if green >= 0 and green <= 255:
            logging.debug("%r Setting Green %r" %(self, green))
            self._green = green
        else:
            raise ValueError("Green attribute of color must be at least 0 and at most 255")
        return

    def getBlue(self):
        return self._blue

    def setBlue(self, blue):
        if blue >= 0 and blue <= 255:
            logging.debug("%r Setting Blue %r" %(self, blue))
            self._blue = blue
        else:
            raise ValueError("Blue attribute of color must be at least 0 and at most 255")
        return

    def getAlpha(self):
        return self._alpha

    def setAlpha(self, alpha):
        if alpha >= 0 and alpha <= 255:
            logging.debug("%r Setting Alpha %r" %(self, alpha))
            self._alpha = alpha
        else:
            raise ValueError("Alpha attribute of color must be at least 0 and at most 255")
        return

    r = property(getRed, setRed, None, "The red value of the color")
    g = property(getGreen, setGreen, None, "The green value of the color")
    b = property(getBlue, setBlue, None, "The blue value of the color")
    a = property(getAlpha, setAlpha, None, "The opaqueness value of the color")

