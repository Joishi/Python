class ModelSubject(object):
    
    def __init__(self):
        self._listeners = []

    def addModelListener(self, modelListener):
        if modelListener not in self._listeners:
            self._listeners.append(modelListener)
            modelListener.modelChanged(self)

    def removeModelListener(self, modelListener):
        if modelListener in self._listeners:
            self._listeners.remove(modelListener)


class MainModel(ModelSubject):

    def __init__(self):
        ModelSubject.__init__(self)
        self._gameStages = None
        self._activeGameStage = None
        self._towers = []
    
    def getGameStages(self):
        return self._gameStages

    def setGameStages(self, gameStages):
        self._gameStages = gameStages

    def getActiveGameStage(self):
        return self._activeGameStage

    def setActiveGameStage(self, gameStage):
        self._activeGameStage = gameStage
        self._towers.clear()

    def delActiveGameStage(self):
        self._activeGameStage = None
        self._towers.clear()

    def getTowers(self):
        return self._towers

    def addTower(self, tower):
        self._towers.append(tower)

    gameStages = property(getGameStages, setGameStages, None, "A list of available game stages")
    activeGameStage = property(getActiveGameStage, setActiveGameStage, delActiveGameStage, "The Current Game Stage that is loaded and playable")
    towers = property(getTowers, None, None, "A list of active towers in the current active game stage")

