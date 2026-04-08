import numpy as np
import pandas as pd 

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')
# df['New'] = np.where(df['cut']=='Ideal', 'yes','no')
# df['New_price'] = np.where((df['cut']=='Ideal'), df['price']*2, df['price'])
# df['New_price'] = np.where((df['cut']=='Ideal') | (df['cut']=='Premium'), df['price']*2, df['price'])
# df['New1'] = np.where( (df['color'].isin(['D','E','F'])), "yes","no" )
# print(df)

df['dept_group'] = np.where(df['depth']<=60,"Less than 60",
                    np.where(df['depth']<65,"60-65",
                    np.where(df['depth']<70,"65-70","More than 70")))
print(df)