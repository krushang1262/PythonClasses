import pandas as pd

# 13. Do lower consumer confidence values coincide with higher bankruptcy rates?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
abc = df['Consumer Confidence Index'].corr(df['Bankruptcy Rate (%)'])

print(abc)