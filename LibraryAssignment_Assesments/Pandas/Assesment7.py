import pandas as pd

# 7) What are the top 5 acquiring institutions?

df = pd.read_csv('~/Desktop/AssignmentData/banklist.csv')
df1 = df.groupby(['Acquiring Institution'])['Bank Name'].count().sort_values(ascending=False).head(5)
print(df1)