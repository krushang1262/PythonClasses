import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sbn

# 2) Line chart comparing the yearly deaths in different states 

df = pd.read_csv('~/Desktop/AssignmentData/U.S.Death.csv')

dt = df.groupby(['year','state']).size().reset_index(name='yearly_death')
print(dt)

plt.figure(figsize=(12,6))
sbn.lineplot(data=dt, x='year', y='yearly_death', hue='state')

plt.title('Yearly Deaths in Different States')
plt.xlabel('States')
plt.ylabel('Number of Deaths')
plt.xticks(rotation=80)

plt.show()