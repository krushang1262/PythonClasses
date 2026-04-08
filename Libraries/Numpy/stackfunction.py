import numpy as np 

a = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [10,20,30],
        [40,50,60]
    ]
])

print(np.hstack(a)) # left to right
print(np.vstack(a)) # up to down 