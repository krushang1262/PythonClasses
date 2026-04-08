import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

df1 = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

df = df1.groupby('carat')['price'].mean().reset_index()
plt.scatter(df['carat'],df['price'], marker='o', color='orange')
plt.title('carat wise average price')
plt.xlabel('carat')
plt.ylabel('price')
plt.grid(True)

plt.show()

sbn.scatterplot(data=df, x='carat', y='price', marker='o',color='purple')
plt.grid(True)
plt.show()