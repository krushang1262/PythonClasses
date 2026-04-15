import pandas as pd

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

df0 = pd.pivot_table(df, values='price', index='clarity', columns=['color'], aggfunc='count')
print(df0)