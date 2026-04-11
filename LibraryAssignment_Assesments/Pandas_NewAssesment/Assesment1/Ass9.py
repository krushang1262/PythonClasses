import pandas as pd

# Are there any duplicate rows?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
print(df.duplicated())