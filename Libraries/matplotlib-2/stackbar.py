import numpy as np 
import matplotlib.pyplot as plt
x = ['A','B','C','D']
y1 = [10,20,10,30]
y2 = [20,25,15,25]
y3 = [11,12,13,15]

y4 = np.add(y1, y2).tolist()
# print(y)

plt.bar(x, y1, color='r')
plt.bar(x, y2, bottom=y1, color='g')
plt.bar(x, y3, bottom=y4, color='b')
plt.show()