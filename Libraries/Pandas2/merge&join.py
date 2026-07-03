import pandas as pd 

# df1 = pd.DataFrame({'ID':[1,2,3], 'Name':['Krushang','Raj','Om']})
# df2 = pd.DataFrame({'ID':[2,3,4], 'Makrs':[20,30,40]})
# res = pd.merge(df1,df2,on='ID',how='inner')
# res1 = pd.merge(df1,df2,on='ID',how='outer')
# res2 = pd.merge(df1,df2,on='ID',how='left')
# res3 = pd.merge(df1,df2,on='ID',how='right')
# print(res,'\n')
# print(res1,'\n')
# print(res2,'\n')
# print(res3,'\n')

res1 = pd.DataFrame({'ID':[1,2,3], 'Name':['Krushang','Raj','Om']},index=[20,10,23])
res2 = pd.DataFrame({'IDs':[2,3,4], 'Makrs':[20,30,40]}, index=[20,10,15])

op = res1.join(res2,how='inner')
print(op)
