import numpy as np

a = np.array([
    [1,2],
    [3,4]
])

b = np.array([
    [11,12],
    [13,14]
])

c = np.stack((a,b), axis=2)
print(c)