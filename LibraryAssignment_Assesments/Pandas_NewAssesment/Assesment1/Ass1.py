# Financial Analysis
import numpy as np
import pandas as pd

# 1. What is the shape of the dataset?
df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')

sh = np.shape(df)
print(sh)