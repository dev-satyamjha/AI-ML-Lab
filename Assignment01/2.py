import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

data = np.random.normal(loc=0, scale=1, size=1000)


plt.figure(figsize=(8, 5))
count, bins, ignored = plt.hist(data, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')

x = np.linspace(min(bins), max(bins), 100)
plt.plot(x, norm.pdf(x, np.mean(data), np.std(data)), 'r', linewidth=2)

plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.title("Histogram of Normally Distributed Data (Bell Curve)")

plt.show()
