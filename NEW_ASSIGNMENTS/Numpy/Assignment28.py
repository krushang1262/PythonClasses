import numpy as np

# 28. Given a 6x6 matrix, use advanced indexing and slicing to extract
# the upper triangular part of the matrix and set the lower triangular part to zero.
# Verify the result.

a = np.arange(1, 37).reshape(6, 6)
print("Original Matrix:\n", a)

result = a.copy()
result[np.tril_indices(6, -1)] = 0

print("\nUpper Triangular Matrix:\n", result)

print("\nVerified:", np.array_equal(result, np.triu(a)))