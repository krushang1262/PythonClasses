import pandas as pd

# 12. What is the average unemployment rate?
df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
print(df['Unemployment Rate (%)'].mean())