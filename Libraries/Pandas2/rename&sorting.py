import pandas as pd 

df = pd.DataFrame({'Roll No':[1,2,3,4,5], 
                   'Name':['Krushang','Raj','Preet','Sachin','Mahesh'],
                   'Marks':[79,97,94,68,98]})

dfrename = df.rename(columns={'Roll No':'RN', 'Marks':'marks'})
# print(dfrename, "\n")

df2 = dfrename.sort_values(by=['Name'], ascending=[True])
print(df2)

x = dfrename.set_index(keys='RN')
print(x)