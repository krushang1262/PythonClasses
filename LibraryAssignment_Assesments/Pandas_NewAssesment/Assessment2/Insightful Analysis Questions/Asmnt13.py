import pandas as pd 

# 13. What is the average discount % across all orders?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

m = df.groupby(['Order No','Order Date'])['Discount %'].mean()
print(m)