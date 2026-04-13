import pandas as pd 

# 5. Convert Order Date and Ship Date to datetime

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

df['Order Date'] = pd.to_datetime(df['Order Date'],dayfirst=True, errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'],dayfirst=True, errors='coerce')
print(df['Order Date'],'\n',df['Ship Date'])