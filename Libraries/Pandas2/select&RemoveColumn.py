import pandas as pd 

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')
df_new = df[['cut','color','clarity']]
print(df_new)

x = df_new.drop(columns=['color','cut'])
print(x)

df2 = df.drop(['cut','color','clarity'], axis=1)
print("drop column ",df2)

df.drop(['cut','color','clarity'],axis=1, inplace=True)
print("Axis:1",df)

df.drop([0,2,4,6], axis=0, inplace=True)
print("Axis:0",df)

df1 = df[(df['color']=='D') & (df['price'] >= 10000)]
print(df1,"\n")

ndf = df[df['color'].isin(["D","F"])]
print(ndf)