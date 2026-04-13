import pandas as pd 

# 1. View the structure of the dataset (columns, types, missing values).

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')
print(df.info())