import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp
import json

# Set a random seed for reproducibility
np.random.seed(2)

# Number of participants in each group
num_participants = 40

# # Create a DataFrame for the dark theme group
# dark_theme = pd.DataFrame({
#     'Theme': ['Dark'] * num_participants,
#     'Rating': np.random.randint(1, 11, num_participants),  # Ratings from 1 to 10
#     'EngagementTime': np.random.randint(30, 91, num_participants),  # Engagement time in seconds (30s to 300s)
# })
#
# # Writing to json
# with open("dark.json", "w") as outfile:
#     dark_theme.to_json(outfile)

dark_theme = pd.read_json('dark2.json')

# # Create a DataFrame for the light theme group
# light_theme = pd.DataFrame({
#     'Theme': ['Light'] * num_participants,
#     'Rating': np.random.randint(1, 11, num_participants),
#     'EngagementTime': np.random.randint(30, 91, num_participants),
# })
#
# # Writing to json
# with open("light.json", "w") as outfile:
#     light_theme.to_json(outfile)

light_theme = pd.read_json('light2.json')

# Concatenate the two DataFrames to create the full dataset
dataset = pd.concat([dark_theme, light_theme], ignore_index=True)

# Create separate data for "Light" and "Dark" themes
dark_ratings = dataset[dataset['Theme'] == 'Dark']['Rating']
light_ratings = dataset[dataset['Theme'] == 'Light']['Rating']

# Calculate rating distributions for each theme
dark_rating_counts = dark_ratings.value_counts().sort_index()
light_rating_counts = light_ratings.value_counts().sort_index()

# Create a bar chart to compare website ratings by theme
width = 0.4  # Width of the bars

# fig, ax = plt.subplots(figsize=(8, 6))
# ax.bar(dark_rating_counts.index - width/2, dark_rating_counts.values, width, color='#000000', label='Dark Theme', alpha=0.7)
# ax.bar(light_rating_counts.index + width/2, light_rating_counts.values, width, color='#bbbbbb', label='Light Theme', alpha=0.7)

plt.figure(figsize=(9, 7))
plt.bar(dark_rating_counts.index - width / 2, dark_rating_counts.values, width, color='#000000', label='Dark Theme',
        alpha=0.7)
plt.bar(light_rating_counts.index + width / 2, light_rating_counts.values, width, color='#bbbbbb', label='Light Theme',
        alpha=0.7)

# ax.set_title('Website Rating Comparison by Theme')
# ax.set_xlabel('Rating (1-10)')
# ax.set_ylabel('Number of People')
# ax.set_xticks(range(1, 11))
# ax.legend()
# ax.grid(True)

plt.title('Website Rating Comparison by Theme')
plt.xlabel('Rating (1-10)')
plt.ylabel('Number of People')
plt.xticks(range(1, 11))
plt.legend()
plt.grid(True)

# Calculate smoothed curves for dark and light themes
x = dark_rating_counts.index
dark_curve = interp.make_smoothing_spline(dark_rating_counts.index, dark_rating_counts.values)
light_curve = interp.make_smoothing_spline(light_rating_counts.index, light_rating_counts.values)

# Plot the smoothed curves
x_smooth = np.linspace(x.min(), x.max(), 100)
# ax.plot(x_smooth, dark_curve(x_smooth), linestyle='-', color='#222222', label='Dark Theme Curve')
# ax.plot(x_smooth, light_curve(x_smooth), linestyle='-', color='#aaaaaa', label='Light Theme Curve')
plt.plot(x_smooth, dark_curve(x_smooth), linestyle='-', color='#222222', label='Dark Theme Curve')
plt.plot(x_smooth, light_curve(x_smooth), linestyle='-', color='#aaaaaa', label='Light Theme Curve')

# ax.legend()
plt.legend()

# plt.show()

### Times

# Concatenate the two DataFrames to create the full dataset
dataset = pd.concat([dark_theme, light_theme], ignore_index=True)

# Create separate data for "Light" and "Dark" themes
dark_engagement_times = dataset[dataset['Theme'] == 'Dark']['EngagementTime']
light_engagement_times = dataset[dataset['Theme'] == 'Light']['EngagementTime']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 9))
bin_width = 1.5
ax1.hist(dark_engagement_times.values, int((max(dark_engagement_times.values) - min(dark_engagement_times.values)) / bin_width), color='#000000', edgecolor='#bbbbbb')
ax2.hist(light_engagement_times.values, int((max(light_engagement_times.values) - min(light_engagement_times.values)) / bin_width), color='#bbbbbb', edgecolor='#000000')

ax1.set_title('Website Engagement Times Comparison by Theme')
ax1.set_xlabel('Engagement Time (seconds)')
ax1.set_ylabel('Number of People')
ax1.grid(True)

ax2.set_title('Website Engagement Times Comparison by Theme')
ax2.set_xlabel('Engagement Time (seconds)')
ax2.set_ylabel('Number of People')
ax2.grid(True)

ax1.set_xlim(30, 60)
ax2.set_xlim(30, 60)

plt.show()

# Calculate and compare the mean engagement times
mean_engagement_times = dataset.groupby('Theme')['EngagementTime'].mean().reset_index()

print(mean_engagement_times)
