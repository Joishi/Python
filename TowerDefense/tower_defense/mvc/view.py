import tkinter as glib

class MainView(glib.Frame):

    def print_out(self):
        print("%s, %s!" %(self.greeting_var.get().title(), self.recipient_var.get()))

    def run(self):
        self.mainloop()

    def __init__(self, master):
        glib.Frame.__init__(self, master, width=800, height=600)
        self.master.title("PyDefense")
        self.pack_propagate(0)
        self.pack()

        self.greeting_var = glib.StringVar()
        self.greeting = glib.OptionMenu(self, self.greeting_var, "Hello", "Goodbye", "Heyo")
        self.greeting_var.set("Hello")

        self.recipient_var = glib.StringVar()
        self.recipient = glib.Entry(self, textvariable=self.recipient_var)
        self.recipient_var.set("World")

        self.go_button = glib.Button(self, text="Go", command=self.print_out)

        self.go_button.pack(fill=glib.X, side=glib.BOTTOM)
        self.greeting.pack(fill=glib.X, side=glib.TOP)
        self.recipient.pack(fill=glib.X, side=glib.TOP)

        self._model = None
        self._gameStages = None

    def setModel(self, model):
        self._model = model

    def setAvailableGameStages(self, gameStages):
        self._gameStages = gameStages

    model = property(None, setModel, None, "The model associated with this view")
    gameStages = property(None, setAvailableGameStages, None, "The game stages that are available to be played in this view")
