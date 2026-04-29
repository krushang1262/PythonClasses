import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sbn

# 10) A rug plot showing a timeline of canine deaths.

df = pd.read_csv('~/Desktop/AssignmentData/U.S.Death.csv')
print(df)

canine_df = df[df['canine'] == True]

canine_df['date'] = df['date'] = pd.to_datetime(df['date'], format='mixed')

plt.figure(figsize=(12,4))
sbn.rugplot(x=canine_df['date'], height=0.4)

plt.title("Timeline of Canine Deaths")
plt.xlabel("Date")
plt.yticks([])

plt.show()