import pandas as pd 

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')
# print(df)

df1 = df.groupby('cut')['price'].mean().reset_index()
print(df1,'\n')

df2 = df.groupby(['cut','color'])[['table','depth']].mean().reset_index()
print(df2,'\n')

df3 = df.groupby('clarity')['price'].agg(['min','max']).reset_index()
print(df3,'\n')