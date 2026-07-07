import matplotlib.pyplot as plt
import seaborn as sbn
import pandas as pd 

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

df1 = df.groupby(['cut','clarity'])['price'].count().reset_index()

plt.bar(df1['cut'],df1['price'])
plt.show()

sbn.barplot(data=df1, x='cut',y='price',hue='clarity', palette='viridis')
plt.show()