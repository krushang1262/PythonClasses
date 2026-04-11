import pandas as pd

# 2. What are the column names and their data types?
df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')

columnNm = df.columns
dataType = df.dtypes
print(columnNm, "\n", dataType)