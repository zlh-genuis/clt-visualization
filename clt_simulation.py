"""Simulate the Central Limit Theorem with an exponential population."""

import matplotlib.pyplot as plt
import numpy as np


# Use a fixed seed so the example creates the same random data each time.
rng = np.random.default_rng(seed=42)

# Compare the distributions of sample means for these sample sizes.
sample_sizes = [5, 30, 100]
num_simulations = 5000

# Create one chart for each sample size.
fig, axes = plt.subplots(1, len(sample_sizes), figsize=(15, 4))

for axis, sample_size in zip(axes, sample_sizes):
    # The exponential distribution is right-skewed, not normal.
    samples = rng.exponential(scale=1.0, size=(num_simulations, sample_size))

    # Each row is one sample. Calculate one mean for every sample.
    sample_means = samples.mean(axis=1)

    # Plot the distribution of the sample means.
    axis.hist(sample_means, bins=40, color="skyblue", edgecolor="black")
    axis.set_title(f"Sample size: n = {sample_size}")
    axis.set_xlabel("Sample mean")
    axis.set_ylabel("Frequency")

fig.suptitle("Central Limit Theorem: Sample Means from an Exponential Distribution")
fig.tight_layout()
plt.savefig("clt_visualization.png")
plt.show()
