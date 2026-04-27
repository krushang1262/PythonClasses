import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sbn

# 7) Bar chart comparing the no. of deaths due to different causes, animated
# by year.

df = pd.read_csv('~/Desktop/AssignmentData/U.S.Death.csv')

noDeath = df.groupby('cause_short').size().reset_index(name='death')
noDeath = noDeath.sort_values(by='death', ascending=False)
print(noDeath)

plt.figure(figsize=(15,7))

sbn.barplot(data=noDeath, x='death',y='cause_short')

plt.title("Number of Deaths by Cause")
plt.xlabel("Total Deaths")
plt.ylabel("Cause")

plt.show()