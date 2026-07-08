import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

cl = df.groupby('cut')['price'].count()
print(cl)

plt.pie(cl,labels=cl.index,autopct='%.2f%%')
plt.show()