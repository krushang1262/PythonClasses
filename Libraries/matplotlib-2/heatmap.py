import pandas as pd 
import seaborn as sbn
import matplotlib.pyplot as plt

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

df1 = df.groupby(['cut','color'])['price'].count().unstack()
print(df1)

# sbn.heatmap(data=df1,cmap='coolwarm', annot=True, fmt='.0f', linewidths=1)
# plt.show()

sbn.pairplot(df,vars=['carat','depth','table','price'],palette='Set2', hue='cut')
plt.show()

sbn.jointplot(data=df,x='depth',y='table', kind='scatter',hue='cut')
plt.show()