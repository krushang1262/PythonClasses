import numpy as np 

# 14. Given two arrays, a = np. array ([1, 2, 3]) and b = np. array ([4,
# 5, 6]), perform element-wise addition, subtraction, multiplication, and
# division. Explain the behavior when dividing by zero

a = np.array([1, 2, 3]) 
b = np.array([4, 5, 6])

print("Addition ", np.add(a,b))
print("Subtraction ", np.subtract(a,b))
print("Multiply ", np.multiply(a,b))
print("Division ", np.divide(a,b))
