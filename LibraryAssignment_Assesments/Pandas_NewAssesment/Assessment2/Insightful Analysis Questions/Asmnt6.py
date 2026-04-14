import pandas as pd 

# 6. How many days does it usually take to ship an order?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

date = pd.to_datetime(df['Order Date'], dayfirst=True).dt.day
ship = pd.to_datetime(df['Ship Date'], dayfirst=True).dt.day

df['Days to Ship an Order'] = ship - date
print(df,"Days")