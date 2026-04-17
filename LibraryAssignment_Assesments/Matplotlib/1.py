import pandas as pd 
import matplotlib.pyplot as plt 

# Q 1: Develop a Line chart using the functionality of pandas to show how
# automobile sales fluctuate from year to year. 

df = pd.read_csv('~/Desktop/AssignmentData/historical_automobile_sales.csv')

fluct1 = df.groupby('Year')['Automobile_Sales'].sum().reset_index()
print(fluct1)

plt.figure(figsize=(10,5))
plt.plot(fluct1['Year'], fluct1['Automobile_Sales'], marker='o', color='orange', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Automobile_sales')
plt.grid(True)
plt.show()