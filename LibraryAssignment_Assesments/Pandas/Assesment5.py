import pandas as pd
# 5) Get a list or array of all the states in the data set.


df = pd.read_csv('~/Desktop/AssignmentData/banklist.csv')
st = df['ST'].unique().tolist()
print(st)