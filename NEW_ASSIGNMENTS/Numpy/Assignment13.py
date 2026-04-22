import numpy as np 

# 13. Reshape a 1D array of 12 elements into a 3x4 2D array and then
# flatten it back into a 1D array using ravel (). Verify that the flattened array
# matches the original. 

arr = np.arange(1,13)
rshp = arr.reshape(3,4)
rv = rshp.ravel()
print(arr)
print(rv)