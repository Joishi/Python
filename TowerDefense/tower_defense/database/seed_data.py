from database import orm

class SeedData(object):

    def createSeedData(self, session):
        self.createPaths(session)
        self.createWaves(session)
        session.commit()

    def createPaths(self, session):
        point1 = orm.Point(x=0, y=0)
        point2 = orm.Point(x=200,  y=200)
        path1 = orm.Path(name="Test Path")
        path1.points = [point1, point2]
        session.add(path1)

    def createWaves(self, session):
        creep1 = orm.Creep(name="Test Creep1")
        creep2 = orm.Creep(name="Test Creep2")
        wave1 = orm.Wave(name="Test Wave1")
        waveCreep0 = orm.WaveCreep(position=0); waveCreep0.creep = creep1
        waveCreep1 = orm.WaveCreep(position=1); waveCreep1.creep = creep2
        waveCreep2 = orm.WaveCreep(position=2); waveCreep2.creep = creep1
        waveCreep3 = orm.WaveCreep(position=3); waveCreep3.creep = creep2
        waveCreep4 = orm.WaveCreep(position=4); waveCreep4.creep = creep1
        waveCreep5 = orm.WaveCreep(position=5); waveCreep5.creep = creep2
        waveCreep6 = orm.WaveCreep(position=6); waveCreep6.creep = creep1
        waveCreep7 = orm.WaveCreep(position=7); waveCreep7.creep = creep2
        waveCreep8 = orm.WaveCreep(position=8); waveCreep8.creep = creep1
        waveCreep9 = orm.WaveCreep(position=9); waveCreep9.creep = creep2
        wave1.creeps = [waveCreep0, waveCreep1, waveCreep2, waveCreep3, waveCreep4, waveCreep5, waveCreep6, waveCreep7, waveCreep8, waveCreep9]
        session.add(wave1)
