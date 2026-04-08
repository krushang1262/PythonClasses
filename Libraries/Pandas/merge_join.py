import pandas as pd

df1 = pd.DataFrame({'ID':[1,2,3],'Name':['Raj','Hiren','Sachin']})
df2 = pd.DataFrame({'ID':[2,3,4],'Score':[20,25,36]})

df = pd.merge(df1,df2, on='ID', how='inner')
ndf1 = pd.merge(df1,df2, on='ID', how='outer')
ndf2 = pd.merge(df1,df2, on='ID', how='left')
ndf3 = pd.merge(df1,df2, on='ID', how='right')
print("merge",df)
print("merge",ndf1)
print("merge",ndf2)
print("merge",ndf3)


jdf1 = pd.DataFrame({'Name':['Raj','Hiren','Sachin']}, index=[1,2,3])
jdf2 = pd.DataFrame({'Score':[20,25,36]}, index=[2,3,4])

# jdf = jdf1.join(jdf2, how='inner')
# jdf2 = jdf1.join(jdf2, how='outer')
# jdf3 = jdf1.join(jdf2, how='left')
jdf4 = jdf1.join(jdf2, how='right')
# print("join",jdf)
# print("join",jdf2)
# print("join",jdf3)
print("join",jdf4)