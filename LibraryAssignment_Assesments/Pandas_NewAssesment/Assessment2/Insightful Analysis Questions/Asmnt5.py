import pandas as pd 

# 5. What is the most profitable product overall?
df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')
dd = df.groupby('Product Name')['Profit Margin'].max().reset_index()
print(dd)