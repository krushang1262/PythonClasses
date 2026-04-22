import numpy as np

# 25. Create a 4D array of shape (2, 3, 4, 5) with random integers.
# Use advanced slicing to extract a subarray and compute the mean along a
# specified axis.

a = np.random.randint(1,25, (2,3,4,5))
print(np.mean(a[:2,:2], axis=1))