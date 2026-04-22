import numpy as np 

# 17. Given a 4x4 array of random integers, use indexing and slicing
# to extract:
# -> The entire second row
# -> The last column
# -> The subarray consisting of the first two rows and first two columns

arr1 = np.random.randint(1,17, (4,4))
print(arr1,'\n')
print(arr1[1],'\n')
print(arr1[:, -1],'\n')
print(arr1[:2,:2],'\n')