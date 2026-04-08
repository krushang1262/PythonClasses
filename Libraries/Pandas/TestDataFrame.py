import pandas as pd

df = pd.DataFrame({'Name': ['Ajay','Sunil','Jatin'], 'age': [20,21,10],'contact': [9913141301, 9173789108, 8469558093]})
print(df)
df.to_json("~/Desktop/DataSheet/myData.json")

# print("===========================================================================================================================")

dfcsv = pd.read_csv("~/Desktop/DataSheet/diamonds.csv")
print(dfcsv)

# print("===========================================================================================================================")

dfcsv2 = pd.read_csv("~/Desktop/DataSheet/Sample - Superstore - full.csv", encoding='latin-1')
print(dfcsv2.head())  
print(dfcsv2.tail())
print(dfcsv2.info())
print(dfcsv2.describe())
print(dfcsv2.shape)
print(dfcsv2.columns)
print(dfcsv2.dtypes)