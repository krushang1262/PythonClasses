import matplotlib.pyplot as plt
import seaborn as sbn
import seaborn.objects as obj
import pandas as pd 

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

df1 = df.groupby(['cut','clarity'])['price'].count().reset_index()

plt.bar(df1['cut'],df1['price'])
plt.show()

sbn.barplot(data=df1, x='cut',y='price',hue='clarity', palette='viridis')
plt.show()

obj.Plot(df1, x='clarity',y='price',color='cut').add(obj.Bar()).scale(color="Set1")