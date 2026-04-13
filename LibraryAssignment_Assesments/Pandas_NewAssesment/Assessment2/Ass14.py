import pandas as pd 

# 14. Are all discount percentages matching discount dollar amounts?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

df['Cost Price'] = pd.to_numeric(df['Cost Price'], errors='coerce')
df['Discount %'] = pd.to_numeric(df['Discount %'], errors='coerce')
df['Discount $'] = pd.to_numeric(df['Discount $'], errors='coerce')

df['Exp Discount'] =  df['Cost Price'] * df['Discount %'] / 100
check = df[df['Exp Discount'] != df['Discount $']]

print(check)