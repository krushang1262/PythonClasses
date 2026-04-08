import numpy as np 

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
print(c)