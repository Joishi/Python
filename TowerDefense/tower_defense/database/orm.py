from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

SQLAlchemyBase = declarative_base()

class Path(SQLAlchemyBase):
    __tablename__ = "path"

    path_id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(String(60), nullable=False)

    def __repr__(self):
        return "<Path(path_id=%r, name=%r)>" %(self.path_id, self.name)


class Point(SQLAlchemyBase):
    __tablename__ = "point"

    point_id = Column(Integer, autoincrement=True, primary_key=True)

    x = Column(Integer, nullable=False)
    y = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Point(point_id=%r, x=%r, y=%r)>" %(self.point_id, self.x, self.y)


class PathPoint(SQLAlchemyBase):
    __tablename__ = "path_point"

    path_id = Column(Integer, ForeignKey(Path.path_id), nullable=False)
    point_id = Column(Integer, ForeignKey(Point.point_id), nullable=False)
    __table_args__ = (
        PrimaryKeyConstraint(path_id, point_id),
    )

    path = relationship("Path", backref="points")
    point = relationship("Point", backref="paths")

    def __repr__(self):
        return "<PathPoint(path_id=%r, point_id=%r)>" %(self.path_id, self.point_id)
