import pandas as pd 

# dept size 60 more 70 less or cart 1.5 caat bigger

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

df1 = df[((df['depth'] > 60)&
        (df['depth'] < 70) )|
        (df['carat'] > 1.5)]
print(df1)

# arithmetics

df['DiscountPrice'] = df['price'] * 0.90
print(df)