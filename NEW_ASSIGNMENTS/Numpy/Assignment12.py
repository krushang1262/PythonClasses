import numpy as np 

# 12. Given a 3D NumPy array of shape (2, 3, 4), find its shape, size,
# number of dimensions, and data type. Change its data type to float64 and verify
# the change. 

a = np.zeros((2,3,4), dtype=np.int32)
print(f"Shape: {a.shape}")
print(f"Size: {a.size}")
print(f"Dimension: {a.ndim}")
print(f"dtype: {a.dtype} \n")

b = a.astype(np.float64)
print(b.dtype)


