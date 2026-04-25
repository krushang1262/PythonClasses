import pandas as pd 
import plotly.express as px

# 3) A heat map overlaid on the map of the United States 

df = pd.read_csv('~/Desktop/AssignmentData/U.S.Death.csv')
dth = df.groupby('state').size().reset_index(name='total_death')
print(dth)

fig = px.choropleth(dth,
              locations='state',
              locationmode='USA-states',
              color='total_death',
              scope='usa',
               color_continuous_scale="Reds",
              title='Heatmap of Deaths Across US States')

fig.show()