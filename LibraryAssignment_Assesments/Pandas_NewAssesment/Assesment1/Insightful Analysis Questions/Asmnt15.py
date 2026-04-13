import pandas as pd

# 15. Are unemployment rates lower when corporate profits are high?
df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')

abc = df['Unemployment Rate (%)'].corr(df['Corporate Profits (Billion USD)'])
print(abc)