import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sbn

# 7) Bar chart comparing the no. of deaths due to different causes, animated
# by year.

df = pd.read_csv('~/Desktop/AssignmentData/U.S.Death.csv')

noDeath = df.groupby(['year','cause']).size().reset_index(name='death')
print(noDeath)