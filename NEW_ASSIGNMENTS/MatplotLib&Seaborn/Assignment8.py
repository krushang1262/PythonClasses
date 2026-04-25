import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sbn

# 8) A heatmap of total deaths per state per year i.e., showing "state" on one
# axis and "year" on the other axis. 

df = pd.read_csv('~/Desktop/AssignmentData/U.S.Death.csv')

hp = df.groupby(['state','year']).size().reset_index(name='total_death')
hpm = hp.pivot_table(index='state',columns='year', values='total_death')
print(hpm)

plt.figure(figsize=(10,6))
sbn.heatmap(data=hpm, cmap='coolwarm', linewidths=0.5)

plt.title("Heatmap of Total Deaths per State per Year")
plt.xlabel("Year")
plt.ylabel("State")

plt.show()