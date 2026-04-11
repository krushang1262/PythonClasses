import pandas as pd

# 16. What is the average Consumer Confidence Index?
df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
xyz = df['Consumer Confidence Index'].mean()
print(xyz)