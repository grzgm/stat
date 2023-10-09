import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()
data = iris.data[:, 0]  # Selecting the first feature (sepal length)

# Calculate the mean of the population (sepal length)
population_mean = np.mean(data)
print(f"Population Mean: {population_mean:.2f}")

# Initialize an array to store the population and sample data
population_data = data
sample_data = []

# Number of random samples and sample size
num_samples = 100
sample_size = 10

# Initialize an array to store the sample means
sample_means = []

# Perform random sampling and calculate means
for _ in range(num_samples):
    # Randomly select indices for the sample
    sample_indices = np.random.choice(len(data), size=sample_size, replace=False)

    # Extract the sample data
    sample = data[sample_indices]
    sample_data.extend(sample)

    # Calculate the mean of the sample and append to the list
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)

# Convert the list of sample means to a numpy array
sample_means = np.array(sample_means)

# Plot both the population distribution (histogram) and sample distribution (curve)
plt.figure(figsize=(10, 6))

# Plot the population distribution (histogram)
plt.hist(sample_means, bins=30, alpha=0.5, color='b', label='Population Distribution')

# Fit and plot a normal distribution curve for the sample distribution
mu = np.mean(sample_means)
sigma = np.std(sample_means)
x = np.linspace(min(sample_data), max(sample_data), 100)
plt.plot(x, (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2), color='r', linewidth=2,
         label='Sample Distribution (Normal Curve)')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Population Distribution and Sample Distribution for Sepal Length (Feature 1)')
plt.legend(loc='upper right')

plt.show()
