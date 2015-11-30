from unittest import TestCase
from tower_defense.database import orm
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, contains_eager


class TestPoint(TestCase):

    def test_orm(self):
        pointToTest = orm.Point(x=2, y=4)
        self.assertEqual(pointToTest.x, 2, "X should be at 2")
        self.assertEqual(pointToTest.y, 4, "Y should be at 4")

    def test_distance(self):
        pointToTest = orm.Point(x=2, y=4)
        otherPointToTest = orm.Point(x=5, y=8)
        self.assertEqual(pointToTest.distance(otherPointToTest), 5, "Distance Between should be 5")


class TestPath(TestCase):

    def test_orm(self):
        pathToTest = orm.Path(path_id=1, name="Test Path")

        dbEngine = create_engine("sqlite://")
        orm.SQLAlchemyBase.metadata.create_all(dbEngine)
        session = Session(bind=dbEngine)
        session.add_all([pathToTest])

        pathToTest = session.query(orm.Path).filter(orm.Path.path_id == 1).one()
        self.assertEqual(pathToTest.name, "Test Path", 'Test Path name should be "Test Path"')

    def test_horizontal_distance(self):
        pathToTest = orm.Path(path_id=1, name="Test Path")
        point1 = orm.Point(point_id=1, x=0, y=0)
        point2 = orm.Point(point_id=2, x=100, y=0)
        pathPoint1 = orm.PathPoint(path_id=pathToTest.path_id, point_id=point1.point_id)
        pathPoint2 = orm.PathPoint(path_id=pathToTest.path_id, point_id=point2.point_id)
        pathToTest.path_points = [pathPoint1, pathPoint2]

        dbEngine = create_engine("sqlite://")
        orm.SQLAlchemyBase.metadata.create_all(dbEngine)
        session = Session(bind=dbEngine)
        session.add_all([pathToTest, point1, point2, pathPoint1, pathPoint2])

        pathToTest = session.query(orm.Path).\
            join(orm.PathPoint, orm.Path.path_id == orm.PathPoint.path_id).\
            join(orm.Point, orm.PathPoint.point_id == orm.Point.point_id).\
            filter(orm.Path.path_id == 1).\
            options(contains_eager(orm.Path.path_points)).\
            one()
        self.assertEqual(pathToTest.totalDistance, 100, "Test Path total distance should be 100")

    def test_vertical_distance(self):
        pathToTest = orm.Path(path_id=1, name="Test Path")
        point1 = orm.Point(point_id=1, x=0, y=0)
        point2 = orm.Point(point_id=2, x=0, y=100)
        pathPoint1 = orm.PathPoint(path_id=pathToTest.path_id, point_id=point1.point_id)
        pathPoint2 = orm.PathPoint(path_id=pathToTest.path_id, point_id=point2.point_id)
        pathToTest.path_points = [pathPoint1, pathPoint2]

        dbEngine = create_engine("sqlite://")
        orm.SQLAlchemyBase.metadata.create_all(dbEngine)
        session = Session(bind=dbEngine)
        session.add_all([pathToTest, point1, point2, pathPoint1, pathPoint2])

        pathToTest = session.query(orm.Path).\
            join(orm.PathPoint, orm.Path.path_id == orm.PathPoint.path_id).\
            join(orm.Point, orm.PathPoint.point_id == orm.Point.point_id).\
            filter(orm.Path.path_id == 1).\
            options(contains_eager(orm.Path.path_points)).\
            one()
        self.assertEqual(pathToTest.totalDistance, 100, "Test Path total distance should be 100")

    def test_diagonal_distance(self):
        pathToTest = orm.Path(path_id=1, name="Test Path")
        point1 = orm.Point(point_id=1, x=0, y=0)
        point2 = orm.Point(point_id=2, x=300, y=400)
        pathPoint1 = orm.PathPoint(path_id=pathToTest.path_id, point_id=point1.point_id)
        pathPoint2 = orm.PathPoint(path_id=pathToTest.path_id, point_id=point2.point_id)
        pathToTest.path_points = [pathPoint1, pathPoint2]

        dbEngine = create_engine("sqlite://")
        orm.SQLAlchemyBase.metadata.create_all(dbEngine)
        session = Session(bind=dbEngine)
        session.add_all([pathToTest, point1, point2, pathPoint1, pathPoint2])

        pathToTest = session.query(orm.Path).\
            join(orm.PathPoint, orm.Path.path_id == orm.PathPoint.path_id).\
            join(orm.Point, orm.PathPoint.point_id == orm.Point.point_id).\
            filter(orm.Path.path_id == 1).\
            options(contains_eager(orm.Path.path_points)).\
            one()
        self.assertEqual(pathToTest.totalDistance, 500, "Test Path total distance should be 500")

    def test_total_distance(self):
        pathToTest = orm.Path(path_id=1, name="Test Path")
        point1 = orm.Point(point_id=1, x=0, y=0)
        point2 = orm.Point(point_id=2, x=300, y=400)
        point3 = orm.Point(point_id=3, x=700, y=100)
        point4 = orm.Point(point_id=4, x=400, y=-300)
        point5 = orm.Point(point_id=5, x=0, y=0)
        pathPoint1 = orm.PathPoint(path_id=pathToTest.path_id, point_id=point1.point_id)
        pathPoint2 = orm.PathPoint(path_id=pathToTest.path_id, point_id=point2.point_id)
        pathPoint3 = orm.PathPoint(path_id=pathToTest.path_id, point_id=point3.point_id)
        pathPoint4 = orm.PathPoint(path_id=pathToTest.path_id, point_id=point4.point_id)
        pathPoint5 = orm.PathPoint(path_id=pathToTest.path_id, point_id=point5.point_id)
        pathToTest.path_points = [pathPoint1, pathPoint2, pathPoint3, pathPoint4, pathPoint5]

        dbEngine = create_engine("sqlite://")
        orm.SQLAlchemyBase.metadata.create_all(dbEngine)
        session = Session(bind=dbEngine)
        session.add_all([pathToTest, point1, point2, point3, point4, point5, pathPoint1, pathPoint2, pathPoint3, pathPoint4, pathPoint5])

        pathToTest = session.query(orm.Path).\
            join(orm.PathPoint, orm.Path.path_id == orm.PathPoint.path_id).\
            join(orm.Point, orm.PathPoint.point_id == orm.Point.point_id).\
            filter(orm.Path.path_id == 1).\
            options(contains_eager(orm.Path.path_points)).\
            one()
        self.assertEqual(pathToTest.totalDistance, 2000, "Test Path total distance should be 2000")

