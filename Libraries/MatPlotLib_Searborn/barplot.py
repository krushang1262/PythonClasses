import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

df1 = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')
df = df1.groupby(['clarity','cut'])['price'].sum().reset_index()

sbn.barplot(data=df, x='cut', y='price', hue='clarity', palette='viridis')

plt.show()