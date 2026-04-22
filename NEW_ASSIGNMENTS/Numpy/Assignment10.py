import numpy as np 

# 10. Drop all nan values from a 1D NumPy 

val = np.array([1,2,3, np.nan,5,6,7, np.nan]) 

dt = val[np.logical_not(np.isnan(val))]
print(dt)