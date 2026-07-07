import matplotlib.pyplot as plt
import seaborn as sbn
import pandas as pd 

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

df1 = df.groupby('carat')['price'].mean().reset_index()

sbn.scatterplot(data=df1,x=df1['carat'],y=df1['price'],color='purple', alpha=0.5 )
plt.show()