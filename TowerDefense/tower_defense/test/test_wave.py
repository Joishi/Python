from unittest import TestCase
from tower_defense.database import orm
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, contains_eager


class TestWave(TestCase):

    def test_orm(self):
        waveToTest = orm.Wave(wave_id=1, name="Test Wave")

        dbEngine = create_engine("sqlite://")
        orm.SQLAlchemyBase.metadata.create_all(dbEngine)
        session = Session(bind=dbEngine)
        session.add_all([waveToTest])

        waveToTest = session.query(orm.Wave).filter(orm.Wave.wave_id == 1).one()
        self.assertEqual(waveToTest.name, "Test Wave", 'Test Wave name should be "Test Wave"')

    def test_wave_creeps(self):
        waveToTest = orm.Wave(wave_id=1, name="Test Wave")
        creep1 = orm.Creep(creep_id=1, name="C1")
        creep2 = orm.Creep(creep_id=2, name="C2")
        waveCreep1 = orm.WaveCreep(wave_id=waveToTest.wave_id, creep_id=creep1.creep_id, position=1)
        waveCreep2 = orm.WaveCreep(wave_id=waveToTest.wave_id, creep_id=creep2.creep_id, position=2)
        waveCreep3 = orm.WaveCreep(wave_id=waveToTest.wave_id, creep_id=creep1.creep_id, position=3)
        waveCreep4 = orm.WaveCreep(wave_id=waveToTest.wave_id, creep_id=creep2.creep_id, position=4)
        waveCreep5 = orm.WaveCreep(wave_id=waveToTest.wave_id, creep_id=creep1.creep_id, position=5)
        waveCreep6 = orm.WaveCreep(wave_id=waveToTest.wave_id, creep_id=creep2.creep_id, position=6)
        waveCreep7 = orm.WaveCreep(wave_id=waveToTest.wave_id, creep_id=creep1.creep_id, position=7)
        waveCreep8 = orm.WaveCreep(wave_id=waveToTest.wave_id, creep_id=creep2.creep_id, position=8)
        waveCreep9 = orm.WaveCreep(wave_id=waveToTest.wave_id, creep_id=creep1.creep_id, position=9)
        waveCreep0 = orm.WaveCreep(wave_id=waveToTest.wave_id, creep_id=creep2.creep_id, position=10)
        waveToTest.wave_creeps = [waveCreep1, waveCreep2, waveCreep3, waveCreep4, waveCreep5, waveCreep6, waveCreep7, waveCreep8, waveCreep9, waveCreep0]

        dbEngine = create_engine("sqlite://")
        orm.SQLAlchemyBase.metadata.create_all(dbEngine)
        session = Session(bind=dbEngine)
        session.add_all([waveToTest, creep1, creep2, waveCreep1, waveCreep2, waveCreep3, waveCreep4, waveCreep5, waveCreep6, waveCreep7, waveCreep8, waveCreep9, waveCreep0])

        waveToTest = session.query(orm.Wave).\
            join(orm.WaveCreep, orm.Wave.wave_id == orm.WaveCreep.wave_id).\
            join(orm.Creep, orm.WaveCreep.creep_id == orm.Creep.creep_id).\
            filter(orm.Wave.wave_id == 1).\
            options(contains_eager(orm.Wave.wave_creeps)).\
            one()
        self.assertEqual(len(waveToTest.wave_creeps), 10, "Test Wave should have 10 creeps total")

