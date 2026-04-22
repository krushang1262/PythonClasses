import numpy as np

# 20. Create a 1D array of 27 elements and reshape it into a 3x3x3
# 3D array. Flatten it back into a 1D array and compare the flattened array
# with the original. 

arr = np.arange(1,28)
arr = arr.reshape(3,3,3)
arr = arr.flatten()
print(arr,'\n')
print(arr)