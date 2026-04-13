import pandas as pd 

# 9. What are the most common shipping modes?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')
common = df['Ship Mode'].duplicated()
print(common)