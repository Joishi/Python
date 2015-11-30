from unittest import TestCase
from database import orm


class TestPath(TestCase):

    def test_orm(self):
        pathToTest = orm.Path(path_id=1, name="Test Path")
        self.assertEqual(pathToTest.name, "Test Path", 'Test Path name should be "Test Path"')

    def test_horizontal_distance(self):
        pathToTest = orm.Path(path_id=1, name="Test Path")
        point1 = orm.Point(point_id=1, x=0, y=0)
        point2 = orm.Point(point_id=2, x=100, y=0)
        pathToTest.points = [point1, point2]
        self.assertEqual(pathToTest.totalDistance, 100, "Test Path total distance should be 100")

    def test_vertical_distance(self):
        pathToTest = orm.Path(path_id=1, name="Test Path")
        point1 = orm.Point(point_id=1, x=0, y=0)
        point2 = orm.Point(point_id=2, x=0, y=100)
        pathToTest.points = [point1, point2]
        self.assertEqual(pathToTest.totalDistance, 100, "Test Path total distance should be 100")

    def test_diagonal_distance(self):
        pathToTest = orm.Path(path_id=1, name="Test Path")
        point1 = orm.Point(point_id=1, x=0, y=0)
        point2 = orm.Point(point_id=2, x=300, y=400)
        pathToTest.points = [point1, point2]
        self.assertEqual(pathToTest.totalDistance, 500, "Test Path total distance should be 500")

    def test_total_distance(self):
        pathToTest = orm.Path(path_id=1, name="Test Path")
        point1 = orm.Point(point_id=1, x=0, y=0)
        point2 = orm.Point(point_id=2, x=300, y=400)
        point3 = orm.Point(point_id=3, x=700, y=100)
        point4 = orm.Point(point_id=4, x=400, y=-300)
        point5 = orm.Point(point_id=5, x=0, y=0)
        pathToTest.points = [point1, point2, point3, point4, point5]
        self.assertEqual(pathToTest.totalDistance, 2000, "Test Path total distance should be 2000")

