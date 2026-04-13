import pandas as pd 

# 12. Create a new column for shipping duration.

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

df['Shipping Duration'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce').dt.day
df['Shipping Duration'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce').dt.day

print(df)