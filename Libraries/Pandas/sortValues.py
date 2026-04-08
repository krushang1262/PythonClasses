import pandas as pd

df = pd.DataFrame({'RollNo':[1,2,3,4],'Name':['Krushang','raj','hasan','sagar'],'Marks':[45,12,12,89]})

df1 = df.sort_values(by=['Marks','Name'], ascending=[True,True])
df2 = df.sort_values(by=['Name'])    
print(df1)

