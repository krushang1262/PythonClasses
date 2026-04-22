import numpy as np 

# 7. How to get the common items between two pythons NumPy?

a = np. array ([1,2,3,2,3,4,3,4,5,6])
b = np. array ([7,2,10,2,7,4,9,4,9,8]) 

common = np.intersect1d(a,b)
print(common)