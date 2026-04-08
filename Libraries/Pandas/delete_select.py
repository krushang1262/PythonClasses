import pandas as pd

df = pd.read_csv("~/Desktop/DataSheet/Sample - Superstore - full.csv", encoding='latin-1').head()

deleteData = df.drop(columns=['Order ID','Customer ID'])
selectData = df[["Region","Sales"]]
print("Delete-Rocords \n\n",deleteData)
print("Selected-Records \n\n",selectData)