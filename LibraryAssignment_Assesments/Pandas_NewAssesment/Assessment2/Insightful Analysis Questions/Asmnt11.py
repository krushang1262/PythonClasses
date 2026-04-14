import pandas as pd 

# 11. Do higher discounts reduce profits?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')


result = df['Discount %'].corr(df['Profit Margin'])
print(result)