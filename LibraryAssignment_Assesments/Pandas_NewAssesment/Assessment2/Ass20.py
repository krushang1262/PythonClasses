import pandas as pd 

# 19. Find the most profitable product.

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

profits = df.groupby('Product Name')['Profit Margin'].sum()
print(profits)