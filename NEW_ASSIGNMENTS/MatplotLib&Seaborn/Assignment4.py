import pandas as pd 
import plotly.express as px

# 4) A Choropleth comparing the number of police deaths in different states 

df = pd.read_csv('~/Desktop/AssignmentData/U.S.Death.csv')

statedeath = df.groupby('state').size().reset_index(name='total_death')
print(statedeath)

fg = px.choropleth(statedeath,
              locations='state',
              locationmode='USA-states',
              color='total_death',
              scope='usa',
              title='police death by state')

fg.show()