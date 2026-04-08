import pandas as pd 
import numpy as np

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

df['carat'] = np.where(df['carat']<=0.2,"Less then 0.2",
            np.where((df['carat']<=0.5) & (df['carat']>=0.2),"0.2-0.5",
            np.where((df['carat']>=0.5) & (df['carat']<=1),"0.5 - 1",
            np.where(df['carat']>=1,"1+",df['carat']))))

print(df.head(25))