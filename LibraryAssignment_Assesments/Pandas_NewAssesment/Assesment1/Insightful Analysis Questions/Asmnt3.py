import pandas as pd

# 3. Is there a relationship between unemployment and consumer spending?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')

relation = df['Unemployment Rate (%)'].corr(df['Consumer Spending (Billion USD)'])
print(relation)