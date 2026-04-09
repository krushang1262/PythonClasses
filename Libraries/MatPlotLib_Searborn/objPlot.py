import matplotlib.pyplot as plt
import seaborn.objects as so
import pandas as pd 

df1 = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

df = df1.groupby(['cut','clarity'])['price'].sum().reset_index()

so.Plot(df, x='clarity',y='price', color='cut').add(so.Bar()).scale(color='Set2').show()
plt.show()