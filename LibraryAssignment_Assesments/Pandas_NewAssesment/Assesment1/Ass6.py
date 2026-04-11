import pandas as pd

# 6. Are there negative values in columns that should be non-negative?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')

numeric_dt = df.select_dtypes(include='number')
negative_count = (numeric_dt <= -numeric_dt).any()
print(negative_count)