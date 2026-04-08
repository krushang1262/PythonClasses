import pandas as pd 

# 9) What is the most common city in California for a bank to fail in?

df = pd.read_csv('~/Desktop/AssignmentData/banklist.csv')

df1 = df[(df['ST']=='CA')]

banktoFail = df1['City'].value_counts()
print(banktoFail)