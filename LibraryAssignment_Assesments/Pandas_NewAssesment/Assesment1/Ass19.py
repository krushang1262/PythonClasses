import pandas as pd

# 19. Which date had the highest crude oil price?
df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
hcop = df.loc[df['Crude Oil Price (USD per Barrel)'] == df['Crude Oil Price (USD per Barrel)'].max()]
print(hcop[['Date','Crude Oil Price (USD per Barrel)']])