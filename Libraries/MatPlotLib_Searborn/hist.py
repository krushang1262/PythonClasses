import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

df1 = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

plt.hist(df1['price'], bins=20, color='orange', edgecolor='red')
plt.title('Histogram')
plt.xlabel('Price')
plt.ylabel('Frequency')

plt.show()

sbn.histplot(data=df1['depth'], bins=50, color='purple', edgecolor='black', kde=True)

plt.show()
