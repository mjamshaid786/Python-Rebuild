import yfinance as yf
import pandas as pd
import json 

apple = yf.Ticker("AAPL")

with open('apple.json') as json_file :
    apple_info = json.load(json_file)
    print(type(apple_info))
    print(apple_info['country']) # It will print country of in which apple office is located

# Extracting Share Price
apple_share_price_data = apple.history(period = "max")
#print(apple_share_price_data.head())
apple_share_price_data.reset_index(inplace=True)
print(apple_share_price_data.plot(x="Date", y="Open"))

print(apple.dividends)
print(apple.dividends.plot())

