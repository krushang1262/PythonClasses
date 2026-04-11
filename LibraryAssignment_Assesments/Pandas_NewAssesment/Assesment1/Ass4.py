import pandas as pd

# 4. What is the date range of the dataset?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
print(f"Range: {df['Date'].min()} to {df['Date'].max()}")