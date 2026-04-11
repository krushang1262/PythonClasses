import pandas as pd

# 17. Which column has the highest standard deviation?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
x = df.std(numeric_only=True)
print("Column:", x.idxmax())
print("Std Value:", x.max())