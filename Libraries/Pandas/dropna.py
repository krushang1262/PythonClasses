import pandas as pd

df = pd.DataFrame({'Name':["Krushang","Raj","Sachin","Dhoni"], 'age':[23,pd.NaT,45,pd.NaT], 'Phone':[9173789108,pd.NaT,9913141301, pd.NaT]})

x = df.dropna()
print(x)