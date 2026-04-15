import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

df1 = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

ct = df1['cut'].value_counts()
plt.pie(ct, labels=ct.index, autopct='%0.2f%%')
plt.show()

df = df1.groupby('cut')['price'].sum().reset_index()
print(df)
plt.pie(df['price'], labels=df['cut'],autopct='%.0f%%')
plt.show()