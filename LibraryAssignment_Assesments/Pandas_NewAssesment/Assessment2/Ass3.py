import pandas as pd 

# 3. Are there any duplicate records?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')
print(df.duplicated().any())