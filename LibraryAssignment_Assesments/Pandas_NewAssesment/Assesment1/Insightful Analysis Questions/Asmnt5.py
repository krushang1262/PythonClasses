import pandas as pd 
import matplotlib.pyplot as plt

# 5. What’s the trend of crude oil prices over time?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')

df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.year.drop_duplicates()

plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Crude Oil Price (USD per Barrel)'],  marker='o', color='red', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Price')
plt.grid()
plt.show()