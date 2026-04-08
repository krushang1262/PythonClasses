import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

plt.boxplot(df['price'])
plt.show()

sbn.boxplot(df['price'])
plt.show()