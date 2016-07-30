from Tkinter import *

root = Tk()

root.title("GUI")
root.geometry("500x300")

app = Frame(root)
app.grid()
label = Label(app, text = "Label")
label.grid()
button1 = Button(app, text = "Button")
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text = "Button2")

root.mainloop()
