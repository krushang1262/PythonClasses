import numpy as np

# 27. Generate a large 2D array and demonstrate the use of np.reshape() and unravel()
# to manipulate its shape for various linear algebra operations. 

arr = np.arange(100).reshape(4,25)
print(arr.shape)