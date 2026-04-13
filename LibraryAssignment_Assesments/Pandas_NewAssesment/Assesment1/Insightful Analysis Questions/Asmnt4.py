import pandas as pd

# 4. Do higher corporate profits align with higher consumer confidence?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')

align = df['Corporate Profits (Billion USD)'].align(df['Consumer Confidence Index'])
print(align)