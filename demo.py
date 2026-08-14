import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Create Z values
z = np.linspace(-4, 4, 1000)

# Standard normal distribution
y = norm.pdf(z, 0, 1)

# Plot the curve
plt.plot(z, y)

# Shade area between Z = -1 and Z = 1
z_fill = np.linspace(-1, 1, 500)
y_fill = norm.pdf(z_fill, 0, 1)

plt.fill_between(z_fill, y_fill, alpha=0.5)

# Add lines at Z = -1 and Z = 1
plt.axvline(-1, linestyle='--')
plt.axvline(1, linestyle='--')

# Labels
plt.xlabel("Z-score")
plt.ylabel("Probability Density")
plt.title("Standard Normal Distribution")

plt.show()