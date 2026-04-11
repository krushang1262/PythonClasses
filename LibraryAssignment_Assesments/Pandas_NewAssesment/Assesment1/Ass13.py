import pandas as pd

# 13. Which index has the highest trading volume?
df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
inds = df.loc[df['Trading Volume'] == df['Trading Volume'].max()]
print(inds['Trading Volume'],"\n")