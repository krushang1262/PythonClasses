import numpy as np

# 21. Perform matrix multiplication of two 2D arrays using np.dot ()
# and @. Compare the results and performance of both methods using a large
# dataset. 

a = np.array([
    [
        [1,2,3],
        [4,5,6]
    ]
])

b = np.array([
    [
        [7,8,6],
        [9,10,6],
        [11,12,5]
    ]
])

c = np.dot(a,b)
print(c,'\n')
print(a @ b)