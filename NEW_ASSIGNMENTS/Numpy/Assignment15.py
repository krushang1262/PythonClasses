import numpy as np 

# 15. Create a 2D array of shape (3, 1) and a 1D array of length 3. Perform
# element-wise addition using broadcasting. Explain how broadcasting rules apply
# in this scenario.

arr = np.arange(1,4)

shp = arr.reshape(3,1)
arr1 = np.arange(1,4)
print(shp + arr1)