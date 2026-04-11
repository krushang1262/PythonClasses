import pandas as pd

# 18. What is the highest gold price recorded?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
hg = df['Gold Price (USD per Ounce)'].max()
print(hg)