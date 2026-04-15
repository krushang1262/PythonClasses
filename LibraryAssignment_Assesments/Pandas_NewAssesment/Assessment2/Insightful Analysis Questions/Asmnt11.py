import pandas as pd 

# 11. Do higher discounts reduce profits?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

df['Discount %'] = df['Discount %'].str.replace('%','', regex=False)
df['Discount %'] = pd.to_numeric(df['Discount %'], errors='coerce')
df['Profit Margin'] = df['Profit Margin'].str.replace('$','', regex=False)
df['Profit Margin'] = pd.to_numeric(df['Profit Margin'], errors='coerce')


result = df['Discount %'].corr(df['Profit Margin'])
print(result)