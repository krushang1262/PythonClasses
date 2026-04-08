import pandas as pd

df = pd.DataFrame({'Name':["Krushang","Raj","Sachin","Dhoni"], 'age':[23,pd.NaT,45,pd.NaT], 'Phone':[9173789108,pd.NaT,9913141301, pd.NaT]})

df['age'] = df["age"].fillna(df["age"].mean())
df['Phone'] = df["Phone"].fillna('-')
print(df)