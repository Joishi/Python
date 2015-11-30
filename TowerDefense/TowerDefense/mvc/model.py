class MainModel(object):

    def __init__(self):
        self._gameStage = None
        self._towers = []

    def getGameStage(self):
        return self._gameStage

    def setGameStage(self, gameStage):
        self._gameStage = gameStage
        self._towers.clear()

    def delGameStage(self):
        self._gameStage = None
        self._towers.clear()

    def getTowers(self):
        return self._towers

    def addTower(self, tower):
        self._towers.append(tower)

    gameStage = property(getGameStage, setGameStage, delGameStage, "The Current Game Stage that is loaded and playable")
    towers = property(getTowers)

