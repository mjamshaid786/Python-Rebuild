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

# The working URL for this data on the course platform is often this one:
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

# 1. Use pandas to read all tables from the URL.
try:
    tables = pd.read_html(url)
except ValueError:
    print("Error: No tables found at the URL. Please verify the URL is correct and active.")
    exit()

# The Tesla Quarterly Revenue table is the second table (index 1).
tesla_revenue = tables[1]
tesla_revenue.columns = ["Date", "Revenue"] # Assign column names

# 2. Post-processing
# Clean the 'Revenue' column: remove $ and ,
# Note: To avoid potential ValueErrors from non-numeric strings, it's best practice
# to use pd.to_numeric with errors='coerce' here, but keeping the original logic 
# and adding a final coercion step.
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].astype(str).str.replace(r'[\$,]', "", regex=True)

# Coerce any remaining non-numeric values to NaN, and then drop them
tesla_revenue["Revenue"] = pd.to_numeric(tesla_revenue['Revenue'], errors='coerce') 

# Remove rows with empty strings or NaN values
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

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
make_graph(tesla_data, tesla_revenue, 'Tesla')