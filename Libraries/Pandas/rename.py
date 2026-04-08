import pandas as pd

df = pd.DataFrame({'RollNo':[1,2,3,4],'Name':['Krushang','raj','hasan','sagar']})
df1 = df.rename(columns={'RollNo':'RN','Name':'Nm'})
print(df1)