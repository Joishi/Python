import tkinter

class MainGUI(tkinter.Frame):

    def print_out(self):
        print("%s, %s!" %(self.greeting_var.get().title(), self.recipient_var.get()))

    def run(self):
        self.mainloop()

    def __init__(self, master):
        tkinter.Frame.__init__(self, master, width=300, height=200)
        self.master.title("PyDefense")
        self.pack_propagate(0)
        self.pack()

        self.greeting_var = tkinter.StringVar()
        self.greeting = tkinter.OptionMenu(self, self.greeting_var, "Hello", "Goodbye", "Heyo")
        self.greeting_var.set("Hello")

        self.recipient_var = tkinter.StringVar()
        self.recipient = tkinter.Entry(self, textvariable=self.recipient_var)
        self.recipient_var.set("World")

        self.go_button = tkinter.Button(self, text="Go", command=self.print_out)

        self.go_button.pack(fill=tkinter.X, side=tkinter.BOTTOM)
        self.greeting.pack(fill=tkinter.X, side=tkinter.TOP)
        self.recipient.pack(fill=tkinter.X, side=tkinter.TOP)

