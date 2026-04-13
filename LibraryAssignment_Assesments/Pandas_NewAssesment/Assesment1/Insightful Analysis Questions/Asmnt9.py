import pandas as pd 

# 9. Is retail sales growth associated with GDP growth?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')

xy = df['Retail Sales (Billion USD)'].corr(df['GDP Growth (%)'])
print(xy)