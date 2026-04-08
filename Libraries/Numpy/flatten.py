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

b = a.flatten()
print(b)

c = a.reshape(2,3,2)
print(c)