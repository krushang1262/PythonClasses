import pandas as pd 

# 13. Are there any orders with zero or negative total or quantity?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

records = df[(df['Total'] == 0) | (df['Order Quantity'] < 1)]
print(records)