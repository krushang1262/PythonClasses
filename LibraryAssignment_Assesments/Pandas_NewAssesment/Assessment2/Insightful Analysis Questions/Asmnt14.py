import pandas as pd
# 14. What is the average total spend per order?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

dta = df.groupby('Order No')['Total'].mean()
print(dta)