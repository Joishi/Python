from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from math import hypot

SQLAlchemyBase = declarative_base()

class Path(SQLAlchemyBase):
    __tablename__ = "path"

    path_id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(String(60), nullable=False)

    def getTotalDistance(self):
        runningTotal = 0
        if len(self.path_points) > 0:
            point = self.path_points[0].point
            for nextPathPoint in self.path_points:
                nextPoint = nextPathPoint.point
                runningTotal += point.distance(nextPoint)
                point = nextPoint

        return runningTotal

    totalDistance = property(getTotalDistance, None, None, "The total distance contained by the path")

    def __repr__(self):
        return "<Path(path_id=%r, name=%r)>" %(self.path_id, self.name)


class Point(SQLAlchemyBase):
    __tablename__ = "point"

    point_id = Column(Integer, autoincrement=True, primary_key=True)

    x = Column(Integer, nullable=False)
    y = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Point(point_id=%r, x=%r, y=%r)>" %(self.point_id, self.x, self.y)

    def distance(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        return hypot(dx, dy)


class PathPoint(SQLAlchemyBase):
    __tablename__ = "path_point"

    path_id = Column(Integer, ForeignKey(Path.path_id), nullable=False)
    point_id = Column(Integer, ForeignKey(Point.point_id), nullable=False)
    __table_args__ = (
        PrimaryKeyConstraint(path_id, point_id),
    )

    path = relationship("Path", backref="path_points")
    point = relationship("Point", backref="path_points")

    def __repr__(self):
        return "<PathPoint(path_id=%r, point_id=%r)>" %(self.path_id, self.point_id)


class Wave(SQLAlchemyBase):
    __tablename__ = "wave"

    wave_id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(String(60), nullable=False)

    def __repr__(self):
        return "<Wave(wave_id=%r, name=%r>)" %(self.wave_id, self.name)


class Creep(SQLAlchemyBase):
    __tablename__ = "creep"

    creep_id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(String(60), nullable=False)

    def __repr__(self):
        return "<Creep(creep_id=%r, name=%r)>" %(self.creep_id, self.name)


class WaveCreep(SQLAlchemyBase):
    __tablename__ = "wave_creep"

    wave_id = Column(Integer, ForeignKey(Wave.wave_id), nullable=False)
    creep_id = Column(Integer, ForeignKey(Creep.creep_id), nullable=False)
    position = Column(Integer, nullable=False)
    __table_args__ = (
        PrimaryKeyConstraint(wave_id, creep_id, position),
    )

    wave = relationship("Wave", backref="wave_creeps")
    creep = relationship("Creep", backref="wave_creeps")

    def __repr__(self):
        return "<WaveCreep(wave_id=%r, creep_id=%r)>" %(self.wave_id, self.creep_id)


