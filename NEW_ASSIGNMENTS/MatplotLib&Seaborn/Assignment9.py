import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sbn
import plotly.express as  px

# 9) A tree map with three levels: state, city (description), cause 

df = pd.read_csv('~/Desktop/AssignmentData/U.S.Death.csv')

x = df.groupby(['state','cause']).size().reset_index(name='total_death_per_state')
print(x)

fig = px.treemap(x,
                 path=['state'],
                 values='total_death_per_state',
                 title='Total Deaths by State')

fig.show()
