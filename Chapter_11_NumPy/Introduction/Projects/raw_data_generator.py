import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Seed set kiya taaki har baar same random data generate ho
np.random.seed(42)
n_rows = 200

# 1. Transaction ID (Duplicates aur Missing values ke sath)
tx_ids = np.arange(1000, 1000 + n_rows).astype(float)
# Duplicates inject kiye (taaki deduplication check ho sake)
tx_ids[15:20] = tx_ids[5:10] 
# NaNs inject kiye
tx_ids[np.random.choice(n_rows, 8, replace=False)] = np.nan

# 2. Product Names (Gande spacing aur inconsistent casing ke sath)
products_pool = [' Laptop ', 'smartphone', ' HEADPHONES', 'SmartWatch', '  charger ']
products = np.random.choice(products_pool, size=n_rows)

# 3. Prices (Negatives aur NaNs ke sath)
prices = np.random.uniform(15.0, 1200.0, size=n_rows)
# Sensor error/invalid price inject kiya (-999.0)
prices[np.random.choice(n_rows, 10, replace=False)] = -999.0
# Missing prices (NaNs)
prices[np.random.choice(n_rows, 8, replace=False)] = np.nan

# 4. Quantities (Float aur Negative values ke sath)
quantities = np.random.randint(1, 10, size=n_rows).astype(float)
# Invalid negative quantity inject ki
quantities[np.random.choice(n_rows, 5, replace=False)] = -2.0
# Missing quantities
quantities[np.random.choice(n_rows, 6, replace=False)] = np.nan

# 5. Dates (Inconsistent formats ke sath - standard vs local format)
base_date = datetime(2026, 1, 1)
dates = []
for i in range(n_rows):
    current_date = base_date + timedelta(days=int(np.random.randint(0, 180)))
    if i % 12 == 0:
        dates.append(current_date.strftime('%d/%m/%Y')) # British/Pakistani Format
    elif i % 25 == 0:
        dates.append(np.nan) # Missing date
    else:
        dates.append(current_date.strftime('%Y-%m-%d')) # ISO Format

# DataFrame banana
df = pd.DataFrame({
    'Transaction_ID': tx_ids,
    'Product_Name': products,
    'Price': prices,
    'Quantity': quantities,
    'Date': dates
})

# CSV File save karna
df.to_csv('raw_sales_data.csv', index=False)
print("🔥 Mubarak ho! 'raw_sales_data.csv' file tayyar hai.")
print("Isme data engineering pipeline test karne ke liye poora masala maujood hai!")