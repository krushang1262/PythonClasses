import pandas as pd
import numpy as np

x = pd.Series([1,2,3,4])
print(x)

y =  pd.Series([1,3,5,np.nan, pd.NaT,None])
y1 = pd.Series({2:'a', 1:'b', 3:'c'}, index=[33,1,2])
print(y1)
print(y)

z = pd.Series([10,12], index=[100,200])
z1 = pd.Series(5, index=[100,200,500,6,7])
print(z)
print(z1)