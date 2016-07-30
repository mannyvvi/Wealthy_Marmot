import ystockquote
import time

from Tkinter import *

tickerSymbol = "SPY"
user_money = 500
stock = 0
price_new = 20
      

class Application(Frame):
    "Gui application with buttons"
    tickerSymbol = "SPY"
    user_money = 500
    stock = 0
    price_new = 20
    
    def __init__(self, master):
        "Initalize frame"
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.run_sim(user_money,stock,price_new)
                 
        

    def create_widgets(self):
        self.button = Button(self)
        self.button["text"] = "Run"
        self.button.grid()

        self.balance = Label(self, text = ("Balance: $", user_money))
        self.balance.grid()

        self.stock = Label(self, text = ("Stock:", stock))
        self.stock.grid()

        self.price = Label(self, text = ("Price: $", price_new))
        self.price.grid()
 


    def run_sim(self,user_money,stock,price_new):
        allInfo = ystockquote.get_all(tickerSymbol)
        price_old = float(allInfo["price"])
        time.sleep(0.3)
        allInfo = ystockquote.get_all(tickerSymbol)
        price_new = float(allInfo["price"])
        print price_new
        if price_old > price_new:
            if user_money > (2*price_new):
                stock += 2
                user_money = user_money - (2 * price_new)
        if price_old < price_new:
            if stock > 0:
                stock -= 1
                user_money = user_money + price_new
    
        else:
            pass
        print "I'm still running!"
        self.balance = Label(self, text = ("Balance: $", user_money))
        self.stock = Label(self, text = ("Stock:", stock))
        self.price = Label(self, text = ("Price:", price_new))
        self.after(2000, self.run_sim(user_money,stock,price_new))



root = Tk()
root.title("Stock Market Simulator")
root.geometry("500x300")
app = Application(root)
root.mainloop()

    
