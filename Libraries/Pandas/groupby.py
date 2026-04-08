import pandas as pd 

data = {
    'Category':['A','B','C','A','B','C','A','B','C'],
    'Region':["East","West","East","West","East","West","East","West","East"],
    'Sales':[100,200,50,500,1000,780,963,1200,752],
    'Quantity':[10,20,3,50,45,65,89,90,16]
}

df = pd.DataFrame(data)
df1 = df.groupby('Category')['Sales'].sum().reset_index()
df2 = df.groupby(['Category'])[['Quantity','Sales']].sum()
print(df1,"\n")
print(df2)