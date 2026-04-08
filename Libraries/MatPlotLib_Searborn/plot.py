import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

df1 = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

df = df1.groupby('cut')['price'].sum().reset_index()
plt.figure(figsize=(5,5))
plt.plot(df['cut'], df['price'], marker='o',color='green', linestyle='--')
plt.title('cut wise price')
plt.xlabel('Cut')
plt.ylabel('total price')
plt.grid(True)

plt.show()

sbn.lineplot(data=df, x='cut',y='price', marker='o', color='red', linestyle='--')
plt.title('cut wise price')
plt.grid(True)

plt.show()