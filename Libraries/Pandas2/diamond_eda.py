import pandas as pd 
import numpy as np

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')
# print(df)

df['new'] = np.where(df['color']=='E','yes','no')
print(df)

df['new_multi'] = np.where((df['color']=='E') | (df['color']=='D'),'yes','no' )
print(df)

df['price_inc_ideal'] = np.where( (df['cut']=='Ideal'), (df['price']*1.20), df['price'] )
print(df)

df['carat_group'] = np.where(df['carat']<0.5, '0 - 0.5', np.where(df['carat']<1,'0.5 - 1','1+') )
print(df)