import matplotlib.pyplot as plt
import seaborn as sbn
import pandas as pd 

df1 = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

sbn.violinplot(data=df1, x='clarity',y='price', hue='clarity')

plt.show()
