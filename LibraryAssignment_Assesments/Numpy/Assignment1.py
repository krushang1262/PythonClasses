import numpy as np

# Q.1 Convert a 1D array to a 2D array with 2 rows 

a = np.array([1,2,3,4,5,6,7,8])
x = a.reshape(2,4)
print(x)