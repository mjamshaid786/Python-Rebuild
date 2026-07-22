import yfinance as yf
import pandas as pd
import json
TICKER_SYMBOL = "GME"
JSON_FILENAME = "gamestop_historical_data.json"
gme = yf.Ticker(TICKER_SYMBOL) # Changed variable name for clarity
game_stop_data = gme.history(period="max")
game_stop_data.reset_index(inplace=True)
game_stop_data.to_json(
    path_or_buf=JSON_FILENAME,
    orient='records',
    date_format='iso',
    indent=4
)
print(game_stop_data.head())