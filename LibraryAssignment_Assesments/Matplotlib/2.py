import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sbn

# Q 2: Plot different lines for categories of vehicle type and analyze the trend
# to answer the question Is there a noticeable difference in sales trends
# between different vehicle types during recession periods?

df = pd.read_csv('~/Desktop/AssignmentData/historical_automobile_sales.csv')

recession = df[df['Recession']==1]
table = recession.groupby(['Year','Vehicle_Type'])['Automobile_Sales'].sum().reset_index()

plt.figure(figsize=(10,5))

sbn.lineplot(data=table, x='Year', y='Automobile_Sales', hue='Vehicle_Type', marker='o')

plt.title('Sales Trend by Vehicle Type During Recession Periods')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.grid(True)
plt.legend(title='Vehicle Type')
plt.show()

print(table)
