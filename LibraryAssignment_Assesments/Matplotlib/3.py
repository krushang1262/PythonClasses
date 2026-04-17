import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

# Q 3: Use the functionality of Seaborn Library to create a visualization to compare
# the sales trend per vehicle type for a recession period with a non- recession
# period. 

df = pd.read_csv('~/Desktop/AssignmentData/historical_automobile_sales.csv')
df['Period'] = df['Recession'].map({1: 'Recession', 0: 'Non-Recession'})
sales_compare = df.groupby(['Year', 'Vehicle_Type', 'Period'])['Automobile_Sales'].sum().reset_index()

sbn.relplot(data=sales_compare,
            x='Year',
            y='Automobile_Sales',
            hue='Vehicle_Type',
            kind='line',
            col='Period',
            marker='o',
            height=6)
plt.show()