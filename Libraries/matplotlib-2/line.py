import matplotlib.pyplot as plt
import seaborn as sbn
import pandas as pd 

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

df1 = df.groupby('cut')['price'].count().reset_index()
plt.plot(df1['cut'],df1['price'],marker="*", linestyle='-' )
plt.show()

sbn.lineplot(data=df1,x='cut',y='price', marker='o',color='green')
plt.show()