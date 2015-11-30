from unittest import TestCase
from tower_defense.database import orm


class TestPoint(TestCase):

    def test_orm(self):
        point1 = orm.Point(point_id=1, x=2, y=4)
        self.assertEqual(point1.x, 2, "X should be at 2")
        self.assertEqual(point1.y, 4, "Y should be at 4")

    def test_distance(self):
        point1 = orm.Point(point_id=1, x=2, y=4)
        point2 = orm.Point(point_id=2, x=5, y=8)
        self.assertEqual(point1.distance(point2), 5, "Distance Between should be 5")

