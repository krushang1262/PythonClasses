import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

sbn.pairplot(df, vars=['carat','depth','table','price'], palette='Set2', hue='cut')
plt.show()