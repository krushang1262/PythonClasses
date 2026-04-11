import pandas as pd

# 14. How many stock records are from each index?
df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
print(df['Stock Index'].value_counts().reset_index(),"\n")

x = df.groupby('Stock Index')['Stock Index'].count()
print(x)