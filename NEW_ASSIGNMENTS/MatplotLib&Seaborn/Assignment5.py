import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sbn

# 5) A word cloud of the different causes of death (remove the string "Cause
# of Death:" for best results) 

df = pd.read_csv('~/Desktop/AssignmentData/U.S.Death.csv')
print(df)