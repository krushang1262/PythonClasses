import pandas as pd 

# 4. Are there any missing or corrupted entries in Ship Date, Order Date, or numeric columns?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')
mse = df[['Ship Date','Order Date']].isnull().sum()


print(mse,"\n")