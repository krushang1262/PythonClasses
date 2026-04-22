import numpy as np

# 23. Generate a 2D array of random floats between 0 and 1. Use
# conditional operators to create a Boolean mask for values less than 0.5.
# Replace these values with their squares and leave the rest unchanged. 

arr = np.random.rand(3,3)
arr = np.where(arr <0.5, arr*2, arr)
print(arr)