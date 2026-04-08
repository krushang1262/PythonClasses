import pandas as pd

# 8) How many banks has the State Bank of Texas acquired? How many of them were actually in Texas?

df = pd.read_csv('~/Desktop/AssignmentData/banklist.csv')

df1 = df[(df['Acquiring Institution']=='State Bank of Texas')]
print("State Bank of Texas acquired :- \n",df1['Bank Name'])


df2 = df1[(df1['ST']=='TX')]
print("State Bank of Texas acquired and actually in Texas:- \n",df2['Bank Name'])