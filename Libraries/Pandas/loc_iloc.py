import pandas as pd 

df = pd.read_csv("~/Desktop/DataSheet/diamonds.csv").head(100)
newloc = df.loc[2:5,["cut","color"]]
print(newloc)

newiloc = df.iloc[5:9,9:10]
print(newiloc)
