import numpy as np

# 24. Given a 5x5 array of sequential integers, use slicing to:
# -> Extract the diagonal elements
# -> Replace the elements of the middle row with zeros
# -> Flip the array vertically and horizontally 

a = np.arange(1,26).reshape(5,5)
b = np.diag(a)
a[2]=0

vflip =  a[::-1]
hflip = a[:,::-1]

print(a,'\n')
print(hflip,'\n')
print(hflip,'\n')
