import numpy as np

# 18. Describe a practical example where NumPy can be used in EDA,
# AI, ML, and DL, and implement a NumPy solution for a simple task in each
# area1

data = np.array([100,200,300,400,500,600,700,800])

mean = np.mean(data)
median = np.median(data)
std = np.std(data)

print("mean: ", mean)
print("median: ", median)
print("standard deviation: ", std)