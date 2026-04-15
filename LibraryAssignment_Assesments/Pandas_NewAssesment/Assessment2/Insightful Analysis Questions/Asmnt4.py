import pandas as pd 

# 4. What is the average profit margin by product category?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

df['Profit Margin'] = df['Profit Margin'].str.replace('$','', regex=False)
df['Profit Margin'] = pd.to_numeric(df['Profit Margin'], errors='coerce')

prfmrg = df.groupby('Product Category')['Profit Margin'].mean()

print(prfmrg)