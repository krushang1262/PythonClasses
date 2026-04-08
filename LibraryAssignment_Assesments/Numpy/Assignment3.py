import numpy as np

# Q.3 Get all items between 5 and 10 from a.

a = np.array([2,6, 1, 9, 10, 3, 27]) 

alitm = (a[(a>5) & (a<=10)],)
print(alitm)