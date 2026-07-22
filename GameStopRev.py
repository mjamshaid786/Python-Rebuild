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
