from database import orm

class SeedData(object):

    def createSeedData(self, session):
        self.createPaths(session)
        self.createPoints(session)
        self.createPathPoints(session)
        session.commit()

    def createPaths(self, session):
        p1 = orm.Path(name="Test Path")
        session.add(p1)

    def createPoints(self, session):
        p1 = orm.Point(x=0, y=0)
        p2 = orm.Point(x=200,  y=200)
        session.add_all([p1, p2])

    def createPathPoints(self, session):
        pp1 = orm.PathPoint(path_id=1, point_id=1)
        pp2 = orm.PathPoint(path_id=1, point_id=2)
        session.add_all([pp1, pp2])
