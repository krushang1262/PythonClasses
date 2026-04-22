import numpy as np

# 19. Create a random 4x4 matrix and use NumPy to compute its
# eigenvalues and eigenvectors. Verify the eigenvalues by reconstructing the
# matrix. 

A = np.random.randint(1, 10, (4, 4))
print("Matrix A:\n", A)

eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:\n", eigenvalues)
print("\nEigenvectors:\n", eigenvectors)

D = np.diag(eigenvalues)        
V = eigenvectors               

A_reconstructed = V @ D @ np.linalg.inv(V)

print("\nReconstructed Matrix:\n", A_reconstructed)

print("\nVerification:", np.allclose(A, A_reconstructed))