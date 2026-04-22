import numpy as np

# 22. Create a 3D array of shape (2, 1, 4) and a 2D array of shape (4,
# 1). Perform an element-wise operation using broadcasting and explain the
# result. Use np. new axis to achieve the same result without broadcasting.

a = np.arange(1,9).reshape(2,1,4)
c = np.arange(1,5).reshape(4,1)

result = a + c
print("Result shape",result.shape)