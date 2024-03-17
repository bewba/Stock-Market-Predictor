import requests
import time
import admin
import json
import pandas as pd
import csv

currTicker = "MSFT"

api_key = admin.getTicker()
passer = "Hello"

# Finding Stock Price at a timeframe
# Incomplete
def getStockPrice(ticker_symbol, api):
    url = f"https://api.twelvedata.com/time_series?symbol={ticker_symbol}&interval=1min&apikey={api}"
    response = requests.get(url).json()
    return response


# Should send a CSV for the list of stocks
# Incomplete
def getStockList():
    url = f"https://api.twelvedata.com/stocks"
    response = requests.get(url).json()
    data = response['data']
    try:
        with open('stocklist.csv', 'w', newline="") as f:
            writer = csv.DictWriter(f,fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)
        print("success")
    except:
        print("An Error Occured")
    return response

getStockList()
