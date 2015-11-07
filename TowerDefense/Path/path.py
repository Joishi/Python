import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, x, y):
        self.x += x
        self.y += y

    def hypotenuse(self, otherPoint):
        dx = self.x - otherPoint.x
        dy = self.y - otherPoint.y
        return math.hypot(dx, dy)


class Path:
    def __init__(self):
        self.a = []

    def addPoint(self, point):
        self.a.append(point)

    def totalDistance(self):
        totalDistance = 0
        if len(self.a) > 0:
            previousPoint = self.a[0]
            for x in self.a:
                totalDistance += x.hypotenuse(previousPoint)
        return totalDistance
