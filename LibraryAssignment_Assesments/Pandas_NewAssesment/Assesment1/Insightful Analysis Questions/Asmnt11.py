import pandas as pd

# 11. Which stock index had the highest average closing price ?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
hgavg = df.groupby('Stock Index')['Close Price'].mean().max()
print(hgavg)