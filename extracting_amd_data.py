import yfinance as yf
import pandas as pd
import json

amd = yf.Ticker("AMD")

with open('amd.json') as json_file :
    amd_info = json.load(json_file)
    print(type(json_file))
    print(amd_info['country'])
    print(amd_info['sector'])

amd_stock_data = amd.history(period = "max")
print(amd_stock_data)