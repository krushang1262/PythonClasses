import pandas as pd 

data = {
    'Category':['A','A','A','B','B','B','C','C','C'],
    'Region':['East','East','East','West','West','West','North','North','North'],
    'Sales':[100,200,100,400,500,600,800,900,1000],
    'Qty':[20,30,50,40,60,80,5,90,120]
}

df = pd.DataFrame(data)
# print(df)

df1 = df.groupby('Region')['Sales'].sum().reset_index()
print(df1)

df2 = df.groupby(['Region','Category'])[['Sales','Qty']].sum().reset_index()
print(df2)

df3 = df.groupby('Category')['Sales'].agg(['sum','min','max','count','mean'])
print(df3)

df4 = df.groupby('Category').agg({'Sales':'mean','Qty':'sum'}).reset_index()
print(df4)