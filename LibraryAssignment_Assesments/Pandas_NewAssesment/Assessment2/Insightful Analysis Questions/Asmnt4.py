import pandas as pd 

# 4. What is the average profit margin by product category?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')


prfmrg = df.groupby('Product Category')['Profit Margin'].mean()

print(prfmrg)