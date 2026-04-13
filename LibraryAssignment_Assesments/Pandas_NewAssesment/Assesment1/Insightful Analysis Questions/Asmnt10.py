import pandas as pd

# 10. Is stock market performance linked to consumer spending?
df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')

grp = df['Close Price'].corr(df['Consumer Spending (Billion USD)'])
print(grp)