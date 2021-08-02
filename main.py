import yfinance as yf


stockInput = input("enter your tickers symbol: ").upper()
print("valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max")
periodInput = input("enter desired period:").lower()
print()


def getLastPrice(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history()
    last_price = (data.tail(1)['Close'].iloc[0])
    print(last_price)





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
    print("high:", finalhighdate, "@ $", high)
    print("low:", finallowdate, "@ $", low)
    print("if you had bought on", finallowdate, "you would have had a", gain * 100, "% gain")
    print("if you had invested $1,000 for", pot_shares, "shares, it would be worth $", gain * 1000)

print("current price of", stockInput, "is: $", end="", flush=True), getLastPrice(stockInput)
stockDateRange(stockInput, periodInput)

