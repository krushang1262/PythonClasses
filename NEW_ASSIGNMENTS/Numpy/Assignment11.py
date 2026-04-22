import numpy as np 

# 11. Create a 1D NumPy array of the first 20 natural numbers and a
# 2D NumPy array of shape (4, 5) with values ranging from 1 to 20. 

a = np.arange(1,21)
print("1d array:",a,'\n')

b = a.reshape(4,5)
print("2d array:",b)