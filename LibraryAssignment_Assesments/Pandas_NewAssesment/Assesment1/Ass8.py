import numpy as np
import pandas as pd

# 8. Are there rows with zero or near-zero trading volume?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
z = np.where((df['Trading Volume']==0) | (df['Trading Volume'] <=1))
print(z)