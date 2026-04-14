import pandas as pd 

# 7. Do longer shipping times impact profit margins?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')


df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days

result = df['Shipping Days'].corr(df['Profit Margin'])
print(result)