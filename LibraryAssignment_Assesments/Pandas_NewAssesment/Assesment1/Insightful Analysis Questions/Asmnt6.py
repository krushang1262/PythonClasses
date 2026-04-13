import pandas as pd 

# 6. Are gold prices inversely related to stock performance?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
corr = df['Gold Price (USD per Ounce)'].corr(df['Close Price'])

print(corr)