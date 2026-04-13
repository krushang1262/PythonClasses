import pandas as pd 
import matplotlib.pyplot as plt

# 5. What’s the trend of crude oil prices over time?
df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')

df['Date'] = pd.to_datetime(df['Date'])
plt.figure(figsize=(10,5))
plt.plot(df['Date'],df['Crude Oil Price (USD per Barrel)'], marker='o', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('crude oil prices over time')
plt.show()