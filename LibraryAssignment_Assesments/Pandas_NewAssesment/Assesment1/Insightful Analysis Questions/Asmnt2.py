import pandas as pd

# 2. Does high inflation correspond to higher interest rates?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')

corr = df['Inflation Rate (%)'].corr(df['Interest Rate (%)'])
print(corr)