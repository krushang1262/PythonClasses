import pandas as pd

# 10. Which cities have the highest number of orders?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

hg = df.groupby('City')['Order No'].max()
print(hg)