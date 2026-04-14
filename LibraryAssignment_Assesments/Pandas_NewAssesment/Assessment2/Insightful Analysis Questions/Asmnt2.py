import pandas as pd 

# 2. Which customer type generates more revenue?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')
moreRev = df.groupby('Customer Type')['Total'].max()

print(moreRev)