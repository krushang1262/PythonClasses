import numpy as np 

a = np.array([
    [
        [1,2,3],
        [11,12,13],
        [21,22,23]
    ]
])

b = np.array([
    [
        [100,200,300],
        [400,500,600],
        [700,800,900]
    ]
])

c = np.concatenate((a,b), axis=2)
print(c.ndim)
print(c)