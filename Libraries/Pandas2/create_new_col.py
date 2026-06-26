import pandas as pd 

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')
print(df)


df['double_price'] = df['price']*2
print(df)

df['percent_ten'] = df['price']*0.1
print(df)

df['add_percent_ten'] = df['price']*1.10
print(df)