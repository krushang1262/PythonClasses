import pandas as pd 

# 18. What is the average shipping cost by mode?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

df['Shipping Cost'] = pd.to_numeric(df['Shipping Cost'], errors='coerce')
avg = df.groupby('Ship Mode')['Shipping Cost'].mean()
print(avg)