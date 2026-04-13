import pandas as pd 

# 7. Does government debt impact consumer confidence?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
x = df['Government Debt (Billion USD)'].corr(df['Consumer Confidence Index'])
print(x)