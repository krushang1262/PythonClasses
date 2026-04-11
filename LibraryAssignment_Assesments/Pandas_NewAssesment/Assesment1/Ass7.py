import pandas as pd

# 7. What is the summary of GDP Growth (%)?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
summary = df['GDP Growth (%)'].describe()
print(summary)