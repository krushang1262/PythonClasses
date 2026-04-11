import pandas as pd

# 5. Are there any missing values?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
print(df.isnull())