import pandas as pd 

# 8. Which city brings in the highest revenue?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

result = df.groupby('City')['Total'].max()
print(result)