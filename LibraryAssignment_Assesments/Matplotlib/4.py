import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

# Q 4: Now you want to compare the sales of different vehicle types
# during a recession and a non-recession period 

df = pd.read_csv('~/Desktop/AssignmentData/historical_automobile_sales.csv')

new_df = df.groupby(['Recession', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()

# Plot bar chart
plt.figure(figsize=(5,6))
sbn.barplot(data=new_df,
            x='Vehicle_Type',
            y='Automobile_Sales',
            hue='Recession')

plt.show()