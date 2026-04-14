import pandas as pd 

# 1. What is the total revenue generated across all orders?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

dta = df['Total'].sum()
print(dta)