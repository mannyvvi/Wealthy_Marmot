import ystockquote
import time

tickerSymbol = raw_input("Enter Code: ",)
user_money = input("Enter starting money: $",)
stock = 0
n = 1
stock_price = 0
margin = 1.03
while True:
    allInfo = ystockquote.get_all(tickerSymbol)
    price_old = float(allInfo["price"])
    avg = float(allInfo["fifty_day_moving_avg"])

        
    time.sleep(0.3)
    allInfo = ystockquote.get_all(tickerSymbol)
    avg_new = float(allInfo["fifty_day_moving_avg"])
    price_new = float(allInfo["price"])
    if price_old < price_new:
        if avg_new > avg:
            n = user_money/price_new
            stock += n
            user_money = user_money - (n * price_new)
            stock_price = price_new
    if price_new > (stock_price * margin):
            if stock > 0:
                user_money = user_money + (price_new * stock)
                stock -= stock
          
        
    else:
        pass
    if price_old != price_new:
        print "Balance: $", user_money
        print stock
        print avg
        print "---"
    else:
        pass
