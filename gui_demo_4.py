from Tkinter import *

class Application(Frame):
    "Gui application with buttons"

    def __init__(self, master):
        "Initalize frame"
        Frame.__init__(self, master)
        self.grid()
        self.button_clicks = 0 #number of clicks
        self.create_widgets()

    def create_widgets(self):
        "create button"
        self.button = Button(self)
        self.button["text"] = "Total Clicks: 0"
        self.button["command"] = self.update_count
        self.button.grid()

    def update_count(self):
        "increases count"
        self.button_clicks += 1
        self.button["text"] = "total Clicks: " + str(self.button_clicks)

root = Tk()
root.title("Title")
root.geometry("500x300")

app = Application(root)
root.mainloop()
