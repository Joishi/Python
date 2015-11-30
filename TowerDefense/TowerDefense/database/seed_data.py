from database import orm

class SeedData(object):

    def createSeedData(self, session):
        point1 = orm.Point(x=0, y=0)
        point2 = orm.Point(x=200,  y=200)
        path1 = orm.Path(name="Test Path")
        path1.points = [point1, point2]

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

        gameStage1 = orm.GameStage(name="Test Stage1")
        gameStage1.path = path1
        gameStageWave1 = orm.GameStageWave(level=1); gameStageWave1.wave = wave1
        gameStageWave2 = orm.GameStageWave(level=2); gameStageWave2.wave = wave1
        gameStage1.waves = [gameStageWave1, gameStageWave2]
        session.add_all([gameStage1])
        session.commit()

