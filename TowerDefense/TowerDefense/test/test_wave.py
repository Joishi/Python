from unittest import TestCase
from database import orm


class TestWave(TestCase):

    def test_orm(self):
        waveToTest = orm.Wave(wave_id=1, name="Test Wave")
        self.assertEqual(waveToTest.name, "Test Wave", 'Test Wave name should be "Test Wave"')

    def test_wave_creeps(self):
        waveToTest = orm.Wave(wave_id=1, name="Test Wave")
        creep1 = orm.Creep(creep_id=1, name="C1")
        creep2 = orm.Creep(creep_id=2, name="C2")
        waveCreep1 = orm.WaveCreep(position=1); waveCreep1.creep = creep1
        waveCreep2 = orm.WaveCreep(position=2); waveCreep2.creep = creep2
        waveCreep3 = orm.WaveCreep(position=3); waveCreep3.creep = creep1
        waveCreep4 = orm.WaveCreep(position=4); waveCreep4.creep = creep2
        waveCreep5 = orm.WaveCreep(position=5); waveCreep5.creep = creep1
        waveCreep6 = orm.WaveCreep(position=6); waveCreep6.creep = creep2
        waveCreep7 = orm.WaveCreep(position=7); waveCreep7.creep = creep1
        waveCreep8 = orm.WaveCreep(position=8); waveCreep8.creep = creep2
        waveCreep9 = orm.WaveCreep(position=9); waveCreep9.creep = creep1
        waveCreep0 = orm.WaveCreep(position=10); waveCreep0.creep = creep2
        waveToTest.creeps = [waveCreep1, waveCreep2, waveCreep3, waveCreep4, waveCreep5, waveCreep6, waveCreep7, waveCreep8, waveCreep9, waveCreep0]
        self.assertEqual(len(waveToTest.creeps), 10, "Test Wave should have 10 creeps total")

