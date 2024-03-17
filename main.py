import requests
import time
import admin

currTicker = "MSFT"

api_key = admin.getTicker()

def getStockPrice(ticker_symbol, api):
    url = f"https://api.twelvedata.com/time_series?symbol={ticker_symbol}&interval=1min&apikey={api}"
    response = requests.get(url).json()
    return response

print(getStockPrice(currTicker,api_key))
