import pandas as pd 

# 14. Are all discount percentages matching discount dollar amounts?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

# Clean columns
df['Cost Price'] = df['Cost Price'].str.replace('$', '', regex=False)
df['Cost Price'] = pd.to_numeric(df['Cost Price'], errors='coerce')

df['Discount %'] = df['Discount %'].str.replace('%', '', regex=False)
df['Discount %'] = pd.to_numeric(df['Discount %'], errors='coerce')

df['Discount $'] = df['Discount $'].str.replace('$', '', regex=False)
df['Discount $'] = pd.to_numeric(df['Discount $'], errors='coerce')

# Expected discount
df['Exp Discount'] = df['Cost Price'] * df['Discount %'] / 100

# Check mismatch
check = df[df['Exp Discount'] != df['Discount $']]

print(check)