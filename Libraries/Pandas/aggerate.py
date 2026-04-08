import pandas as pd 

df = pd.DataFrame({'RollNo':[1,2,3,4],'Name':['Krushang','raj','hasan','sagar'],'Marks':[45,12,12,89]})

df1 = df.groupby(['RollNo','Marks']).agg({'RollNo':'sum', 'Marks':'mean'})
# df1 = df.groupby(['RollNo']).agg({'RollNo':'sum'})
# df2 = df.groupby(['Marks']).agg({'Marks':'mean'})
print(df1)