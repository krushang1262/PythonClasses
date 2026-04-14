import pandas as pd 

# 12. Which state has the highest number of orders?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

dt = df.groupby('State')[['Order No','Order Date']].max()
print(dt)