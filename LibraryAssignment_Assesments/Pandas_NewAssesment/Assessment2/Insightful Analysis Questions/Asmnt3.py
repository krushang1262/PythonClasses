import pandas as pd 

# 3. How does order priority affect revenue?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')
rev = df.groupby(['Order Priority'])['Total'].sum()
print(rev)