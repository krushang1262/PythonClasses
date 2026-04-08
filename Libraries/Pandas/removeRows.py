import pandas as pd

df = pd.read_csv("~/Desktop/DataSheet/diamonds.csv")
removeRows = df.drop([0,2,3,4], axis=0)
print(removeRows)