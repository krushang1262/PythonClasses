import numpy as np 

a = np.array([[1,5,7],[9,8,7]])

b = np.array([[8,4,3],[5,9,1]])

x = np.concatenate((a,b), axis=0)
y = np.concatenate((a,b), axis=1)
print("\n",x)
print("\n",y)

x1 = np.stack((a,b),axis=0)
y1 = np.stack((a,b),axis=1)
print("\n",x1)
print("\n", y1)
