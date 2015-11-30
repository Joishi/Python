import tkinter as glib

class MainView(glib.Frame):

    def __init__(self, master):
        glib.Frame.__init__(self, master, width=800, height=600)
        self.createMenu(master)
        self.master.title("PyDefense")
        self.pack_propagate(0)
        self.pack()

        self.gameStageListSelectedValue = glib.StringVar()
        self.gameStageList = [""]
        self.gameStageListSelectionBox = glib.OptionMenu(self, self.gameStageListSelectedValue, *self.gameStageList)
        self.gameStageListSelectedValue.trace("w", self.updateBackground)
        self.gameStageListSelectedValue.set("")

        self.recipient_var = glib.StringVar()
        self.recipient = glib.Entry(self, textvariable=self.recipient_var)
        self.recipient_var.set("World")

        self.go_button = glib.Button(self, text="Go", command=self.startGame)

        self.go_button.pack(fill=glib.X, side=glib.BOTTOM)
        self.gameStageListSelectionBox.pack(fill=glib.X, side=glib.TOP)
        self.recipient.pack(fill=glib.X, side=glib.TOP)

        self._model = None
        self._gameStages = None

    def createMenu(self, master):
        masterMenuBar = glib.Menu(master)

        fileMenu = glib.Menu(masterMenuBar, tearoff=0)
        fileMenu.add_command(label="Exit", command=self.shutdown)
        masterMenuBar.add_cascade(label="File", menu=fileMenu)

        editMenu = glib.Menu(masterMenuBar, tearoff=0)
        masterMenuBar.add_cascade(label="Edit", menu=editMenu)

        helpMenu = glib.Menu(masterMenuBar, tearoff=0)
        masterMenuBar.add_cascade(label="Help", menu=helpMenu)

        master.config(menu=masterMenuBar)

    def run(self):
        self.mainloop()

    def shutdown(self):
        print("SHUTDOWN")

    def updateBackground(self, *args):
        print("UPDATE BACKGROUND")
        gameStage = self.gameStageListSelectedValue.get()

    def updateGameStageSelection(self):
        print("UPDATE GAME STAGE SELECTION")
        self.gameStageList.clear()
        for gameStage in self._gameStages:
            self.gameStageList.append(gameStage)
        self.gameStageListSelectionBox.
        self.gameStageListSelectedValue.set(self.gameStageList[0])

    def startGame(self):
        print("START GAME")

    def setModel(self, model):
        self._model = model

    def setAvailableGameStages(self, gameStages):
        self._gameStages = gameStages
        self.updateGameStageSelection()

    model = property(None, setModel, None, "The model associated with this view")
    gameStages = property(None, setAvailableGameStages, None, "The game stages that are available to be played in this view")
