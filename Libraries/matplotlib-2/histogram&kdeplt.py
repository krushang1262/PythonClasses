import matplotlib.pyplot as plt
import seaborn as sbn
import pandas as pd 

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

plt.hist(df['price'], bins=50,color='skyblue', edgecolor='black')
plt.show()

sbn.histplot(df['depth'], bins=50, color='purple', kde=True)
plt.show()

sbn.kdeplot(data=df['depth'],color='green', fill=True)
plt.title("Density of table")
plt.show()

sbn.boxplot(df['table'])
plt.show()

sbn.boxplot(data=df, x=df['cut'], y=df['price'], hue='cut', palette='Set3')
plt.show()