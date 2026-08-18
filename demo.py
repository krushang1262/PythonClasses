import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sbn

df1 = pd.read_csv('~/Desktop/gameAdd/gaming_addiction.csv')
df = pd.DataFrame(df1)
df2 = df.groupby('Month')[['App_Downloads', 'Ad_Spend_Lakhs']].sum().reset_index()

print(df2)

sbn.barplot(
    data=df2,
    x='Month',
    y='Ad_Spend_Lakhs',
    hue='App_Downloads'
)

plt.show()