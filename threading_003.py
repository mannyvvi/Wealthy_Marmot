import threading
import time
from Tkinter import *

exitflag = 0
counter = 1

class guithread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print "starting " + self.name
        start_gui(self, self.name)
        print "exiting " + self.name

class countthread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        

    def run(self):
        print "starting " + self.name
        global counter
        start_count(self)
        print "exiting " + self.name

def start_gui(self, name):
    root = Tk()
    root.title(name)
    root.geometry("500x200")
    app = Application(root)
    root.mainloop()

def start_count(self):
    while gui_thread.isAlive():
        time.sleep(1.5)
        print counter
        counter += 1
        global counter

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

        self.button2 = Button(self)
        self.button2["text"] = "Refresh"
        self.button2["command"] = self.update_refresh
        self.button2.grid()

    def update_count(self):
        "increases count"
        self.button_clicks += 1
        self.button["text"] = "total Clicks: " + str(self.button_clicks)

    def update_refresh(self):
        "refreshes"
        self.button2["text"] = counter

    
threads = []

gui_thread = guithread(1, "GUI THREAD")
count_thread = countthread(2, "Counting THREAD")

gui_thread.start()
count_thread.start()


print "Exiting Main Thread"
        
