import requests
import time
import admin
import json



currTicker = "MSFT"

api_key = admin.getTicker()

def getStockPrice(ticker_symbol, api):
    url = f"https://api.twelvedata.com/time_series?symbol={ticker_symbol}&interval=1min&apikey={api}"
    response = requests.get(url).json()
    return response

def getStockList():
    url = f"https://api.twelvedata.com/stocks"
    response = requests.get(url).json()
    try:
        with open("stocklist.txt", "w") as file:
            json.dump(response, file)
            print("data stored successfully")
    except:
        print("An Error Occured")
    return response

getStockList()
