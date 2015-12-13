import logging

class ModelSubject(object):
    
    def __init__(self):
        logging.debug("Initializing ModelSubject for " + str(self))
        self._listeners = []
        logging.debug("Done initializing ModelSubject for " + str(self))
        return

    def addModelListener(self, modelListener):
        if modelListener not in self._listeners:
            self._listeners.append(modelListener)
            modelListener.modelChanged(self)
        return

    def removeModelListener(self, modelListener):
        if modelListener in self._listeners:
            self._listeners.remove(modelListener)
        return


class MainModel(ModelSubject):

    def __init__(self):
        logging.debug("Initializing MainModel for " + str(self))
        ModelSubject.__init__(self)
        self._gameStages = None
        self._activeGameStage = None
        self._towers = []
        logging.debug("Done initializing MainModel for " + str(self))
        return

    def __repr__(self):
        return "<MainModel>"
    
    def getGameStages(self):
        return self._gameStages

    def setGameStages(self, gameStages):
        self._gameStages = gameStages
        return

    def getActiveGameStage(self):
        return self._activeGameStage

    def setActiveGameStage(self, gameStage):
        self._activeGameStage = gameStage
        self._towers.clear()
        return

    def delActiveGameStage(self):
        self._activeGameStage = None
        self._towers.clear()
        return

    def getTowers(self):
        return self._towers

    def addTower(self, tower):
        self._towers.append(tower)
        return

    gameStages = property(getGameStages, setGameStages, None, "A list of available game stages")
    activeGameStage = property(getActiveGameStage, setActiveGameStage, delActiveGameStage, "The Current Game Stage that is loaded and playable")
    towers = property(getTowers, None, None, "A list of active towers in the current active game stage")

