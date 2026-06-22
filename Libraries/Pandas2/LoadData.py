import pandas as pd 

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')
df.head(5)
df.tail(5)
df.describe()
print(df.shape)
print(df.columns)
print(df.index)
print(df.sample(5))
print(df.isnull().sum())