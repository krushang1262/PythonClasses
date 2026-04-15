import pandas as pd
# 14. What is the average total spend per order?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

df['Total'] = df['Total'].str.replace('$','', regex=False)
df['Total'] = pd.to_numeric(df['Total'], errors='coerce')

dta = df.groupby('Order No')['Total'].mean()
print(dta)