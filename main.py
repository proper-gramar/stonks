import yfinance as yf

stockInput = input("enter your tickers symbol: ").upper()
print("valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max")
periodInput = input("enter desired period:").lower()
print()


def getLastPrice(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history()
    last_price = (data.tail(1)['Close'].iloc[0])
    print("{:.2f}".format(last_price))


def stockDateRange(ticker, period):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    highDate = ""
    lowDate = ""
    high = -999999.9
    low = 999999.9
    for index, row in data.iterrows():

        if float(row['High']) > high:
            high = float(row['High'])
            highDate = str(index)

        if float(row['Low']) < low:
            low = float(row['Low'])
            lowDate = str(index)
    finalhighdate = str.replace(highDate, "00:00:00", "")
    finallowdate = str.replace(lowDate, "00:00:00", "")
    gain = float(high / low)
    pot_shares = 1000 / low
    print("high:", finalhighdate, "@ $", "{:.2f}".format(high))
    print("low:", finallowdate, "@ $", "{:.2f}".format(low))
    print("if you had bought on", finallowdate, "at $", "{:.2f}".format(low) ,"you would have had a",
          "{:.2f}".format(gain * 100), "% gain")
    print("if you had invested $1,000 for", "{:.2f}".format(pot_shares), "shares at $", "{:.2f}".format(low),
          ", it would be worth $", "{:.2f}".format(gain * 1000))


print("current price of", stockInput, "is: $", end="", flush=True), getLastPrice(stockInput)
stockDateRange(stockInput, periodInput)
