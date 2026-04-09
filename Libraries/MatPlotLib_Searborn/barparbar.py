import matplotlib.pyplot as plt
import seaborn as sbn
import numpy as np 

x = ['A','B','C','D']
y1 = [10,50,90,40]
y2 = [20,60,10,50]
y3 = [30,70,20,60]
y4 = [40,80,30,70]

y5 = np.add(y2,y3)

plt.bar(x,y1, color='r')
plt.bar(x,y2, bottom=y1, color='g')
plt.bar(x, y3, bottom=y2, color='purple')
plt.bar(x,y4, bottom=y5, color='orange')
# plt.grid(True)
plt.show()