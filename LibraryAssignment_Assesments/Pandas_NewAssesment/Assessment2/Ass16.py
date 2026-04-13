import pandas as pd 

# 16. Identify top 5 products by order quantity.
df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')
df['top5'] = df.groupby('Product Name')['Order Quantity'].head(5)
print(df)