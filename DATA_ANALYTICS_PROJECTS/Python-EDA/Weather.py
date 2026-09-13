import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sbn 

df = pd.read_csv('~/Desktop/ClassExcelData/weather_classification_data.csv')
print(df)

df = df[df['Temperature'] > 0]
df1 = df.groupby('Weather Type')['Temperature'].mean().reset_index()
print(df1,'\n')

df1 = df1[df['Temperature']> 0]
plt.figure(figsize=(10,6))
plt.title('Weather Type wise Average Temperature')
sbn.barplot(data=df1, x='Weather Type', y='Temperature',hue='Weather Type')
plt.show()

df2 = df.groupby('Weather Type')['Precipitation (%)'].mean()
df2 = df2.fillna(df['Precipitation (%)'].mean())
print(df2, '\n')

plt.figure(figsize=(10,6))
plt.title('Weather Type wise Average Precipitation in (%)')
plt.pie(df2, labels=df2.index, autopct='%.2f%%')
plt.legend(df['Season'])
plt.show()

df3 = df.groupby(['Location','Weather Type'])['Atmospheric Pressure'].count().reset_index()
print(df3)

plt.figure(figsize=(10,6))
plt.title('Location wise Average Atmospheric Pressure by Different Weather Type')
sbn.barplot(data=df3, x=df3['Location'], y=df3['Atmospheric Pressure'], hue='Weather Type')
plt.show()

df4 = df.groupby(['Season','Weather Type'])['Temperature'].mean().unstack()
df4 = df4.fillna(df['Temperature'].mean())
print(df4,'\n')

plt.figure(figsize=(10,6))
plt.title('Season and Weather Type Wise Average Temperature.')
sbn.heatmap(data=df4,cmap='coolwarm', annot=True, fmt='.0f', linewidths=1)
plt.show()