from unittest import TestCase
from tower_defense.database import orm
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import Session, contains_eager


class TestPoint(TestCase):

    def test_orm(self):
        point1 = orm.Point(point_id=1, x=2, y=4)

        dbEngine = create_engine("sqlite://")
        orm.SQLAlchemyBase.metadata.create_all(dbEngine)
        session = Session(bind=dbEngine)
        session.add_all([point1])

        point1 = session.query(orm.Point).filter(orm.Point.point_id == 1).one()
        self.assertEqual(point1.x, 2, "X should be at 2")
        self.assertEqual(point1.y, 4, "Y should be at 4")

    def test_distance(self):
        point1 = orm.Point(point_id=1, x=2, y=4)
        point2 = orm.Point(point_id=2, x=5, y=8)

        dbEngine = create_engine("sqlite://")
        orm.SQLAlchemyBase.metadata.create_all(dbEngine)
        session = Session(bind=dbEngine)
        session.add_all([point1, point2])

        points = session.query(orm.Point).filter(or_(orm.Point.point_id == 1, orm.Point.point_id == 2)).all()
        point1 = points[0]
        point2 = points[1]
        self.assertEqual(point1.distance(point2), 5, "Distance Between should be 5")

