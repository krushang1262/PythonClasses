import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

heatmap = df.groupby(['cut','color'])['price'].count().unstack()
sbn.heatmap(heatmap, annot=True, cmap='coolwarm', fmt='d', linewidths=3)
plt.show()
print(heatmap)