import pandas as pd

# 14. Which indicator has the highest correlation with stock close price?
df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')

corval = df.corr(numeric_only=True)['Close Price']
print(corval)