import pandas as pd

# 15. Are certain containers (e.g., Small Box, Wrap Bag) more profitable?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

dta = df.groupby('Product Container')['Profit Margin'].max()
print(dta)