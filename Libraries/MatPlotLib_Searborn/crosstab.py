import pandas as pd

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

df0 = pd.crosstab(df['cut'], df['color'])
print(df0)