import pandas as pd

df = pd.read_csv('~/Downloads/insurance.csv')

print(df['smoker'].value_counts())
print(df['sex'].value_counts())

rnm = df.rename(columns={'age':'Age', 'sex':'Sex', 'bmi':'Bmi', 'children':'Children', 'smoker':'Smoker', 'region':'Region', 'charges':'Charges'})
print(rnm)

df3 = df[df['smoker'] == 'yes']
print(df3['sex'].value_counts())

df4 = df3[df3['smoker']=='yes']
df4 = df4[(df4['region']=='southeast') | (df4['region']=='southwest')]
print(df4.value_counts())
