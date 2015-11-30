from unittest import TestCase
from tower_defense.database import orm
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, contains_eager


class TestCreep(TestCase):

    def test_orm(self):
        creepToTest = orm.Creep(creep_id=1, name="Test Creep")

        dbEngine = create_engine("sqlite://")
        orm.SQLAlchemyBase.metadata.create_all(dbEngine)
        session = Session(bind=dbEngine)
        session.add_all([creepToTest])

        creepToTest = session.query(orm.Creep).filter(orm.Creep.creep_id == 1).one()
        self.assertEqual(creepToTest.name, "Test Creep", 'Test Creep name should be "Test Creep"')

