import pandas as pd

df = pd.DataFrame({'Name':["Krushang","Raj","Sachin","Dhoni"], 'age':[23,pd.NaT,45,pd.NaT], 'Phone':[9173789108,pd.NaT,9913141301, pd.NaT]})
df1 = pd.DataFrame({'number':[9,pd.NaT,6,5], 'age':[23,pd.NaT,45,pd.NaT]})

x = df.fillna(1)
y = df.fillna('-')
z = df1.fillna(df1.mean())

print(x,"\n")
print(y,"\n")
print(z,"\n")