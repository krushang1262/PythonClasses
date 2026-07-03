import pandas as pd 

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

df1 = df.loc[5:10,['carat','color','depth']]
print(df1,'\n')

df2 = df.iloc[10:15,1:5]
print(df2)