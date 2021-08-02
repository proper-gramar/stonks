import pandas as pd
import yfinance as yf

stockInput = input("enter your tickers symbol: ").upper()
testGME = "GME"


def getLastPrice(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history()
    last_price = (data.tail(1)['Close'].iloc[0])
    print(last_price)


getLastPrice(stockInput)
