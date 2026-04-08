import pandas as pd 

df = pd.read_csv("~/Desktop/DataSheet/diamonds.csv").head()
df['Total'] = df['x']+df['y']+df['z']
df['Half_price'] = df['price']/2
# df['increment_percentage'] = df['price']*20/100+df['price']
df['increment_percentage'] = df['price']*1.20
print(df)