import pandas as pd 

# 10. Which shipping mode is most cost-effective (lowest avg. shipping)?

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

x = df['Ship Mode'].corr(df['Shipping Cost'].min())
print(x)