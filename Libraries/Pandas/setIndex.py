import pandas as pd 

df = pd.DataFrame({'RollNo':[1,2,3,4],'Name':['Krushang','raj','hasan','sagar'],'Marks':[45,12,12,89]})
df1 = df.set_index('Marks')
print(df1)