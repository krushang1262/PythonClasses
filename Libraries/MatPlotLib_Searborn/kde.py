import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

df1 = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

sbn.kdeplot(df1['depth'], color='darkblue', fill=True)
plt.title('Density')

plt.show()