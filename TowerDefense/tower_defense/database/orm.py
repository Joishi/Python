from sqlalchemy import Table, Column, Integer, String, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from math import hypot

SQLAlchemyBase = declarative_base()

# Many-to-many table/pattern with SQLAlchemy
pathPoint = Table("path_point", SQLAlchemyBase.metadata,
    Column("path_id", Integer, ForeignKey("path.path_id")),
    Column("point_id", Integer, ForeignKey("point.point_id")),
)


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


class Path(SQLAlchemyBase):
    __tablename__ = "path"

    path_id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(String(60), nullable=False)

    points = relationship("Point", secondary=pathPoint, backref="paths")

    def getTotalDistance(self):
        runningTotal = 0
        if len(self.points) > 0:
            point = self.points[0]
            for nextPoint in self.points:
                runningTotal += point.distance(nextPoint)
                point = nextPoint

        return runningTotal

    totalDistance = property(getTotalDistance, None, None, "The total distance contained by the path")

    def __repr__(self):
        return "<Path(path_id=%r, name=%r)>" %(self.path_id, self.name)


# Association table/pattern with SQLAlchemy
class WaveCreep(SQLAlchemyBase):
    __tablename__ = "wave_creep"
    wave_id = Column(Integer, ForeignKey("wave.wave_id"))
    creep_id = Column(Integer, ForeignKey("creep.creep_id"))
    position = Column(Integer, nullable=False)
    PrimaryKeyConstraint(wave_id, creep_id, position)

    creep = relationship("Creep")

    def __repr__(self):
        return "<WaveCreep(Creep=%r, position=%r)>" %(self.creep, self.position)


class Wave(SQLAlchemyBase):
    __tablename__ = "wave"

    wave_id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(String(60), nullable=False)

    creeps = relationship("WaveCreep", order_by="WaveCreep.position")

    def __repr__(self):
        return "<Wave(wave_id=%r, name=%r)>" %(self.wave_id, self.name)


class Creep(SQLAlchemyBase):
    __tablename__ = "creep"

    creep_id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(String(60), nullable=False)

    def __repr__(self):
        return "<Creep(creep_id=%r, name=%r)>" %(self.creep_id, self.name)

