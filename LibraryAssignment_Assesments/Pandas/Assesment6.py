import pandas as pd
# 6) What are the top 5 states with the most failed banks?
df = pd.read_csv('~/Desktop/AssignmentData/banklist.csv')
df1 = df['ST'].value_counts().head(5)
print(df1)
