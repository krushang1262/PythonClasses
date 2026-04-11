import pandas as pd

# 3. How many unique stock indices are there?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')

uniqueStock = df['Stock Index'].unique()
print(uniqueStock)