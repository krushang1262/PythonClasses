import pandas as pd

# 8. What are the unique values in Customer Type and Order Priority?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

uv1 = df['Customer Type'].unique()
uv2 = df['Order Priority'].unique()

print(uv1,"\n \n", uv2)