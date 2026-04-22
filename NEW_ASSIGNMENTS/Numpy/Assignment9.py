import numpy as np 

# 9. Limit the number of items printed in python NumPy array a to a maximum of 6 elements.

a = np.arange(15)
np.set_printoptions(threshold=6)
print(a)