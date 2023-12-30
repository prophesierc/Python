import pandas as pd
import random
from datetime import datetime, timedelta
from openpyxl import Workbook
from openpyxl.styles import Font

# Sample data
data = ["Groceries", "Fuel", "Shopping", "Dining", "Electronics", "Health", "AMZN Mktp Amzn.com/bill", "SQ *MEXIOTE Hollywood FL", "PUBLIX SUPER MAR PEMBROKE PINE"]

# Repeat random values to fill 365 cells
repeated_data = random.choices(data, k=365)

# Generate date range from today to (today - 364 days)
date_range = [datetime.today() - timedelta(days=i) for i in range(365)]

# Generate random prices between -1 and -100
random_prices = [round(random.uniform(-1, -60), 2) for _ in range(365)]

# Create a DataFrame with columns "Date", "Transaction Description", and "Price"
df = pd.DataFrame({'Date': date_range, 'Transaction Description': repeated_data, 'Price': random_prices})

# Replace every 30th cell with "Rent"
df.loc[df.index % 30 == 0, 'Transaction Description'] = 'Rent'

# Set every cell in Column C where 'Rent' is present to -1350
df.loc[df['Transaction Description'] == 'Rent', 'Price'] = -1350

# Set every 14th cell in Column B to 'Paycheck' and set the corresponding cells in Column C to 1700
df.loc[df.index % 14 == 0, 'Transaction Description'] = 'Paycheck'
df.loc[df.index % 14 == 0, 'Price'] = 1700

# Create a new row every 31 rows
new_row_indices = range(30, len(df), 31)
new_row_values = [f'Month {i // 31 + 1}' if i % 31 == 0 else None for i in range(len(df.columns))]  
 

# Insert new rows
for index in new_row_indices:
    df = pd.concat([df.iloc[:index], pd.DataFrame([new_row_values], columns=df.columns), df.iloc[index:]], ignore_index=True)

# Calculate C values for the new rows based on the sum of the previous 31 C cells
for i in new_row_indices:
    df.loc[i, 'Price'] = df.loc[max(0, i-31):i-1, 'Price'].sum()

# Limit the DataFrame to the first 365 rows
df = df.head(365)

# Specify the Excel file path
excel_file_path = r'C:\Users\bwkno\Downloads\AssignmentModule_5.xlsx'

# Write DataFrame to Excel
df.to_excel(excel_file_path, index=False)

print(f'Data exported to {excel_file_path}')
