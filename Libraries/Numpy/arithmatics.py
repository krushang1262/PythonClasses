import numpy as np 

a = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

b = np.array([
   [10,20,30,40],
    [50,60,70,80]
])

c = np.sum((a,b), axis=2)
print(c)