import pandas as pd 
import numpy as np

df = pd.read_csv('~/Downloads/spotify_timeseries_dataset.csv')

df1 = df.groupby('Song Name')['Play Count per Day'].sum().reset_index()
df1.rename(columns={'Play Count per Day':'Total Plays'}, inplace=True)
print(df1)