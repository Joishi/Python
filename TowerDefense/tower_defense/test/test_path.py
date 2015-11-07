from unittest import TestCase
from tower_defense.path import Point


class TestPoint(TestCase):

    def test_translate(self):
        pointToTest = Point(2, 4)
        pointToTest.translate(5, 10)
        self.assertEqual(pointToTest.x, 7, "X should be at 7")
        self.assertEqual(pointToTest.y, 14, "Y should be at 14")

    def test_hypotenuse(self):
        pointToTest = Point(2, 4)
        otherPointToTest = Point(5, 8)
        self.assertEqual(pointToTest.hypotenuse(otherPointToTest), 5, "Distance Between should be 5")
