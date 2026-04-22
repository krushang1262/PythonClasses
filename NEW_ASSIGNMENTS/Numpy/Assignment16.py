import numpy as np 

# 16. Generate a random 2D array of integers between 0 and 10.
# Use conditional operators to create a Boolean mask identifying elements greater than
# 5. Replace all elements greater than 5 with the value 5


arr = np.random.randint(0,10,(2,3))
print("Original array:\n", arr)

arr = np.where(arr>5, 5, arr)
print("Updated array:\n", arr)