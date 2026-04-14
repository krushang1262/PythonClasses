import pandas as pd 

# 9. Which account manager generated the most revenue?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')
mostRevenue = df.groupby('Account Manager')['Total'].max().reset_index()
print(mostRevenue)