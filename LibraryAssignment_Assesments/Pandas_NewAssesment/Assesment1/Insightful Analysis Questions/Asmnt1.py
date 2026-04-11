# Insightful Analysis Questions
import pandas as pd

# 1. What percentage of the dataset shows negative GDP growth?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
negVal = (df['GDP Growth (%)']<0).sum()
totalRecords = df['GDP Growth (%)'].count()
percentage = (negVal / totalRecords) * 100

print(percentage)