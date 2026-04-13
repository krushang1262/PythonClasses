import pandas as pd

# 12. What is the relationship between interest rate and unemployment?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
relationship = df['Interest Rate (%)'].corr(df['Unemployment Rate (%)'])
print(relationship)