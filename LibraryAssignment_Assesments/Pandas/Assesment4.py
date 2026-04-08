import pandas as pd
# 4) How many States (ST) are represented in this data set?

df = pd.read_csv('~/Desktop/AssignmentData/banklist.csv').head(100).tail(100)
print(df['ST'].unique())