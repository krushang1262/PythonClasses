import numpy as np

# 26. Given an array of shape (10, 20), reshape it to (20, 10) and (5,
# 40). Discuss the impact on the array's shape, size, and dimensionality.

arr = np.random.randint(10,90,(10,20))
print(arr)
print(arr.shape)
print(arr.size)
print(arr.ndim)
arr1 = arr.reshape(20,10)
print(arr1)
print(arr1.shape)
print(arr1.size)
print(arr1.ndim)
arr2 = arr.reshape(5,40)
print(arr2)
print(arr2.shape)
print(arr2.size)
print(arr2.ndim)