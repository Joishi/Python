from unittest import TestCase
from tower_defense.database import orm


class TestCreep(TestCase):

    def test_orm(self):
        creepToTest = orm.Creep(creep_id=1, name="Test Creep")
        self.assertEqual(creepToTest.name, "Test Creep", 'Test Creep name should be "Test Creep"')

