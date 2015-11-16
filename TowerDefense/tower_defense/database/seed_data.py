from database import orm

class SeedData(object):

    def createSeedData(self, session):
        self.createPaths(session)
        session.commit()

    def createPaths(self, session):
        p1 = orm.Path(name="Test Path")
        session.add(p1)
