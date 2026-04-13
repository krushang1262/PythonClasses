import pandas as pd

# 11. What’s the range of order quantities and prices?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')


ranges = df['Order Quantity'].min(),
ranges1 = df['Cost Price'].min(),
ranges2 = df['Order Quantity'].max(), 
ranges3 = df['Cost Price'].max()

print("min ",ranges)
print("min ",ranges1)
print("max ", ranges2)
print("max ",ranges3)