import numpy as np
import matplotlib.pyplot as plt

# Set random seed
np.random.seed(42)

# Number of samples
num_samples = 1000

# Sample size
sample_size = 30

# Generate sample means
sample_means = []

for i in range(num_samples):
    sample = np.random.exponential(scale=10, size=sample_size)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)

# Plot histogram of sample means
plt.figure(figsize=(10, 6))

plt.hist(sample_means, bins=30)

plt.title("Central Limit Theorem - Sampling Distribution of Mean")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")

plt.show()