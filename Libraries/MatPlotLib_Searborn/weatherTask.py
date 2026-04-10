import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

df = pd.read_csv('~/Desktop/ClassExcelData/weather_classification_data.csv')

# weather type records count

df1 = df['Weather Type'].value_counts().reset_index()
print(df1)
sbn.barplot(data=df1, x='Weather Type', y='count', hue='Weather Type', palette='viridis')
plt.show()

# location wise higest temperature comparision.

df1 = df.groupby('Location')['Temperature'].max().reset_index()
print(df1)

sbn.barplot(data=df1, x='Location', y='Temperature', hue='Temperature', palette='viridis')
plt.show()

# Temperature and wind speed frequency

temp = df['Temperature']
print(temp,"\n")

sbn.histplot(data=df['Temperature'], color='orange', edgecolor='black')
plt.title('Temperature Frequency')
plt.xlabel('Temperature')
plt.show()

windspeed = df['Wind Speed']
print(windspeed)

sbn.histplot(data=df['Wind Speed'], color='green', edgecolor='black')
plt.title('windspeed Frequency')
plt.xlabel('Windspeed')
plt.show()

# season location wise average atmosphere

avgatm = df.groupby(['Season','Location'])['Atmospheric Pressure'].mean().reset_index().drop_duplicates()
print(avgatm)

sbn.barplot(data=avgatm, x='Location', y='Atmospheric Pressure', hue='Season', palette='magma')
plt.show()

# humidity and density

print(df['Humidity'])
sbn.kdeplot(data=df['Humidity'], color='red', fill=True)
plt.title('Density')
plt.show()

plt.boxplot(df['Humidity'])
plt.show()

# UV index and Temperature relation 

df_group = df.groupby('UV Index')['Temperature'].mean().reset_index()
print(df_group)

sbn.scatterplot(data=df_group, x='UV Index', y='Temperature', markers='o', color='purple')
plt.show()

dg = df[['UV Index','Temperature']]
sbn.scatterplot(data=dg, x='UV Index', y='Temperature', markers='o', color='purple')
plt.show()