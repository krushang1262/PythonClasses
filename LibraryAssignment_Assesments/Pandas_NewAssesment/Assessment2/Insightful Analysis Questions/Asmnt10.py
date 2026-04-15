import pandas as pd 

# 10. Which shipping mode is most cost-effective (lowest avg. shipping)?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

df['Shipping Cost'] = df['Shipping Cost'].str.replace('$','',regex=False)
df['Shipping Cost'] = pd.to_numeric(df['Shipping Cost'], errors='coerce')

x = df.groupby('Ship Mode')['Shipping Cost'].mean()
print(x)