import pandas as pd 

# 13. What is the average discount % across all orders?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

df['Discount %'] = df['Discount %'].str.replace('%','', regex=False)
df['Discount %'] = pd.to_numeric(df['Discount %'], errors='coerce')

m = df.groupby(['Order No','Order Date'])['Discount %'].mean()
print(m)