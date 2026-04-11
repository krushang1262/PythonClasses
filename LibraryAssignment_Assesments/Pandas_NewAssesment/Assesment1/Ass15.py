import pandas as pd

# 15. What is the correlation between inflation and interest rate?
df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
corr = df['Inflation Rate (%)'].corr(df['Interest Rate (%)'])
print(corr)