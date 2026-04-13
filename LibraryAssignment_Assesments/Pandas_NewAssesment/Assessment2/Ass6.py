import pandas as pd

# 6. Check for future or inconsistent shipping dates.

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

tod = pd.Timestamp.today()

future = df[ df['Ship Date'] > tod ]
print(future)
