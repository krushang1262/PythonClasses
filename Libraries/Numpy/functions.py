import numpy as np

x = np.zeros((1,10,2),int)
print("Zeros:",x)

y = np.ones((1,20,2),int)
print("ones :",y)

z = np.linspace(1,50,10)
print("linespace:",z)

a = np.arange(1,10)
b = np.arange(11,20)
print("Addition:", np.add(a,b))
print("subtract:", np.subtract(a,b))
print("divide:", np.divide(a,b))
print("multiply:", np.multiply(a,b))

ey = np.eye(20,10,k=1)
print(ey)