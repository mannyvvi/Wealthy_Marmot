from Tkinter import *

class Application(Frame):
    "Gui application with buttons"

    def __init__(self, master):
        "Initalize frame"
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        "create button"
        self.button1 = Button(self, text = "Button")
        self.button1.grid()

root = Tk()
root.title("Title")
root.geometry("500x300")

app = Application(root)
root.mainloop()
