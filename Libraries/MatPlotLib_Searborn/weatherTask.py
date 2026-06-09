import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

# Load Dataset
df = pd.read_csv('~/Desktop/ClassExcelData/weather_classification_data.csv')

# ==========================================
# 1. Weather Type Records Count
# ==========================================
weather_count = df['Weather Type'].value_counts().reset_index()
weather_count.columns = ['Weather Type', 'Count']

print("Weather Type Records Count:")
print(weather_count)

plt.figure(figsize=(8, 5))
plt.title('Weather Type Records Count')
sbn.barplot(data=weather_count, x='Weather Type', y='Count', palette='viridis')
plt.xlabel('Weather Type')
plt.ylabel('Count')
plt.show()

# ==========================================
# 2. Location-wise Highest Temperature
# ==========================================
max_temp = df.groupby('Location')['Temperature'].max().reset_index()

print("\nLocation-wise Highest Temperature:")
print(max_temp)

plt.figure(figsize=(8, 5))
plt.title('Location-wise Highest Temperature Comparison')
sbn.barplot(data=max_temp, x='Location', y='Temperature', palette='magma')
plt.xlabel('Location')
plt.ylabel('Maximum Temperature')
plt.show()

# ==========================================
# 3. Temperature Frequency Distribution
# ==========================================
plt.figure(figsize=(8, 5))
sbn.histplot(df['Temperature'], bins=20, color='orange', edgecolor='black')
plt.title('Temperature Frequency Distribution')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.show()

# ==========================================
# 4. Wind Speed Frequency Distribution
# ==========================================
plt.figure(figsize=(8, 5))
sbn.histplot(df['Wind Speed'], bins=20, color='green', edgecolor='black')
plt.title('Wind Speed Frequency Distribution')
plt.xlabel('Wind Speed')
plt.ylabel('Frequency')
plt.show()

# ==========================================
# 5. Season & Location-wise Average Atmospheric Pressure
# ==========================================
avg_atm = (
    df.groupby(['Season', 'Location'])['Atmospheric Pressure']
    .mean()
    .reset_index()
)

print("\nSeason & Location-wise Average Atmospheric Pressure:")
print(avg_atm)

plt.figure(figsize=(10, 5))
plt.title('Season & Location-wise Average Atmospheric Pressure')
sbn.barplot(
    data=avg_atm,
    x='Location',
    y='Atmospheric Pressure',
    hue='Season',
    palette='magma'
)
plt.xlabel('Location')
plt.ylabel('Average Atmospheric Pressure')
plt.show()

# ==========================================
# 6. Humidity Density Plot
# ==========================================
plt.figure(figsize=(8, 5))
sbn.kdeplot(df['Humidity'], fill=True, color='red')
plt.title('Humidity Density Distribution')
plt.xlabel('Humidity')
plt.ylabel('Density')
plt.show()

# ==========================================
# 7. UV Index vs Average Temperature
# ==========================================
uv_temp_avg = (
    df.groupby('UV Index')['Temperature']
    .mean()
    .reset_index()
)

print("\nUV Index vs Average Temperature:")
print(uv_temp_avg)

plt.figure(figsize=(8, 5))
plt.title('UV Index vs Average Temperature')
sbn.scatterplot(
    data=uv_temp_avg,
    x='UV Index',
    y='Temperature',
    marker='o',
    color='purple'
)
plt.show()

# ==========================================
# 8. UV Index vs Temperature (Raw Data)
# ==========================================
plt.figure(figsize=(8, 5))
plt.title('UV Index vs Temperature Relationship')
sbn.scatterplot(
    data=df,
    x='UV Index',
    y='Temperature',
    marker='o',
    color='purple'
)
plt.show()