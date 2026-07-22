import yfinance as yf
import pandas as pd
import json
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
pio.renderers.default = "iframe"
import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)
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

import pandas as pd
import requests
from bs4 import BeautifulSoup

# The working URL for this data on the course platform is often this one:
url = " https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

# 1. Use pandas to read all tables from the URL.
# Note: The .html file is often redirected or deleted, but the .htm file 
# often remains active for these labs.
try:
    tables = pd.read_html(url)
except ValueError:
    print("Error: No tables found at the URL. Please verify the URL is correct and active.")
    exit()

# The Tesla Quarterly Revenue table is the second table (index 1).
gme_revenue = tables[1]
gme_revenue.columns = ["Date", "Revenue"] # Assign column names

# 2. Post-processing
# Clean the 'Revenue' column: remove $ and ,
# .astype(str) ensures the operation works even if the column type is mixed.
gme_revenue["Revenue"] = gme_revenue['Revenue'].astype(str).str.replace(r'[\$,]', "", regex=True)

# Remove rows with empty strings or NaN values
gme_revenue.dropna(inplace=True)
tesla_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

print(tesla_revenue.tail())


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    
    # Removed infer_datetime_format=True to fix warnings
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    
    # Removed infer_datetime_format=True to fix warnings
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    
    # 🌟 FIX: Updated the title to be more descriptive using an f-string 🌟
    fig.update_layout(showlegend=False,
    height=900,
    title=f'Historical Share Price and Revenue for {stock}', # Descriptive Title
    xaxis_rangeslider_visible=True)
    
    fig.show()
    from IPython.display import display, HTML
    fig_html = fig.to_html()
    display(HTML(fig_html))

print("----------Historical Share Price", "Historical Revenue----------")
make_graph(game_stop_data, gme_revenue, 'GameStop')