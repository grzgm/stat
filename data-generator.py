import numpy as np
import json

# Define the desired range and distribution
lower_bound = 30
upper_bound = 60
peak_mean = 35  # The peak of the distribution (most values around 45 seconds)
std_deviation = 3  # Standard deviation for the distribution (controls the spread)

# Generate engagement times with a normal distribution
engagement_times = np.random.normal(loc=peak_mean, scale=std_deviation, size=1000)

# Clip values to ensure they are within the desired range
engagement_times = np.clip(engagement_times, lower_bound, upper_bound)

# Round the values to integers if needed
engagement_times = np.round(engagement_times).astype(int)

# Print a sample of the generated engagement times
print(list(engagement_times[:40]))
# print(json.dumps(engagement_times[:40]))

import matplotlib.pyplot as plt

# Sample data (replace with your data)
# engagement_times = engagement_times[:40]
# engagement_times = [36, 31, 36, 36, 35, 35, 33, 35, 32, 35, 40, 38, 34, 33, 38, 36, 38, 35, 39, 33, 42, 31, 36, 32, 35, 40, 34, 32, 37, 35, 32, 38, 32, 35, 37, 37, 33, 33, 37, 37]
engagement_times = [44, 31, 42, 44, 38, 41, 44, 45, 42, 42, 46, 34, 37, 42, 44, 39, 37, 41, 48, 44, 44, 40, 41, 40, 39, 42, 38, 48, 45, 54, 42, 42, 43, 38, 33, 38, 40, 41, 40, 36]

# Create a histogram
plt.hist(engagement_times, bins=15, color='blue', edgecolor='black')

# Customize the plot
plt.title('Engagement Time Histogram')
plt.xlabel('Engagement Time (seconds)')
plt.ylabel('Number of People')
plt.grid(True)

# Show the histogram
plt.show()


# # Black
# black = [44, 31, 42, 44, 38, 41, 44, 45, 42, 42, 46, 34, 37, 42, 44, 39, 37, 41, 48, 44, 44, 40, 41, 40, 39, 42, 38, 48, 45, 54, 42, 42, 43, 38, 33, 38, 40, 41, 40, 36]
# # White
# white = [36, 31, 36, 36, 35, 35, 33, 35, 32, 35, 40, 38, 34, 33, 38, 36, 38, 35, 39, 33, 42, 31, 36, 32, 35, 40, 34, 32, 37, 35, 32, 38, 32, 35, 37, 37, 33, 33, 37, 37]
# d = {}
# d2 = {}
# for x in range(40):
#     d[str(x)] = black[x]
#     d2[str(x)] = white[x]
#
# print(d)
# print(d2)