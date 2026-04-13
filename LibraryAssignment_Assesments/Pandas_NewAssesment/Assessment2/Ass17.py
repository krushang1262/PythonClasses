import pandas as pd 

# 17. Which Account Manager handled the most revenue?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')
revenue = df.groupby('Account Manager')['Total'].sum()
print(revenue)