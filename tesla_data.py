import yfinance as yf
import pandas as pd
import json
TICKER_SYMBOL = "TSLA"
JSON_FILENAME = "tesla_historical_data.json"
tesla = yf.Ticker(TICKER_SYMBOL)
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
tesla_data.to_json(
    path_or_buf=JSON_FILENAME,
    orient='records',
    date_format='iso',
    indent=4
)
print(tesla_data.head())

