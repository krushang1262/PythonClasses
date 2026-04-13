import pandas as pd 

# 8. How do mergers & acquisitions (M&A) activity correlate with stock index closing prices?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')

grp = df['Mergers & Acquisitions Deals'].corr(df['Close Price'])
print(grp)