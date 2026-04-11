import pandas as pd

# 20. What is the average corporate profit?
df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
avgProf = df['Corporate Profits (Billion USD)'].mean()
print(avgProf)