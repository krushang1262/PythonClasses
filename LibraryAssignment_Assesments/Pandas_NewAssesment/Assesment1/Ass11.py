import pandas as pd

# 11. What is the summary of Inflation Rate (%)?
df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
print(df['Inflation Rate (%)'].describe())