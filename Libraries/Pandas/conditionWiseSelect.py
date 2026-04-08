import pandas as pd

df = pd.read_csv("~/Desktop/DataSheet/diamonds.csv").head(10)
select_data = df[ (df['table'] > 50) & (df['color']=='E') ]
print(select_data)