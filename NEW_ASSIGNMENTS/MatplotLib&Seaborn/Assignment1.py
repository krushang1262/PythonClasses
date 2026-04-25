import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sbn

# 1) Bar chart showing the total deaths per year for 1984-2016 

df = pd.read_csv('~/Desktop/AssignmentData/U.S.Death.csv')

death = df[(df['year'] >= 1984) & (df['year'] <= 2016)]
death = death.groupby('year').size().reset_index(name='total_death')
print(death)

plt.figure(figsize=(10,6))
plt.title('showing the total deaths per year for 1984-2016')
sbn.barplot(data=death, x='year', y='total_death')
plt.xlabel('years')
plt.ylabel('total deaths per year')
plt.xticks(rotation=70)
plt.show()