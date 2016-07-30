import ystockquote
import time

tickerSymbol = 'FCX'
while True:
    allInfo = ystockquote.get_all(tickerSymbol)
    print tickerSymbol + " Price = " + allInfo["price"]
    time.sleep(0.3)
