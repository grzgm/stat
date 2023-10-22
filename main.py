import matplotlib.pyplot as plt
import scipy.interpolate as interp
import numpy as np

dark_rating_mean_value = 5.65
dark_rating_std_deviation = 2.554897258208243
light_rating_mean_value = 5.5
light_rating_std_deviation = 3.024896692450835

dark_engagement_time_mean_value = 41.225
dark_engagement_time_std_deviation = 4.198139468859985
light_engagement_time_mean_value = 35.325
light_engagement_time_std_deviation = 2.601802259972883


def generate_positive_normal_distribution(mean_value, std_dev, population_size):
    samples = []
    while len(samples) < population_size:
        value = np.random.normal(loc=mean_value, scale=std_dev)
        if 10 >= value >= 0:
            samples.append(value)
    return np.array(samples)

def simulate_plots(mean_value1, std_dev1, mean_value2, std_dev2,
                   title, color1, color2, sample_size=40,
                   population_size=1000, simulation_amount=10):
    # Generate sample data for all graphs
    generated_data = []
    for i in range(simulation_amount):
        # Get 40 values from 1000 generated
        sample1 = generate_positive_normal_distribution(mean_value1, std_dev1, population_size)[:sample_size]
        sample2 = generate_positive_normal_distribution(mean_value2, std_dev2, population_size)[:sample_size]
        generated_data.append((sample1, sample2))

    # Plot settings
    COLS = 2
    # ROWS = int((simulation_amount / COLS) + 1)
    ROWS = 5
    width = 0.4
    # Create subplots for histograms on one canvas
    fig, axes = plt.subplots(ROWS, COLS, figsize=(12, 18))  # 5 rows, 2 columns

    # Iterate through the subplots and plot histograms
    for i, ax in enumerate(axes.flatten()):
        ax.bar(list(j - width / 2 for j in range(1, 41)), generated_data[i][0], width, color=color1, alpha=0.7)
        ax.bar(list(j + width / 2 for j in range(1, 41)), generated_data[i][1], width, color=color2, alpha=0.7)
        ax.set_title(f"Simulation {i + 1}")
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Frequency")
        ax.set_xlim(0, 10)
        ax.grid(True)

    # Add a title to the whole canvas
    plt.suptitle(title)

    # Adjust layout
    plt.tight_layout()

    # Show the plot
    plt.show()


def simulate_hists(mean_value, std_dev, title, color,
                   edgecolor, sample_size=40, population_size=1000, simulation_amount=10):
    # Generate sample data for all graphs
    generated_data = []
    for i in range(simulation_amount):
        # generated_data.append(
        #     np.random.normal(loc=mean_value, scale=std_dev, size=40))
        generated_data.append(
            np.random.normal(loc=mean_value, scale=std_dev, size=population_size)[:sample_size])

    # Plot settings
    COLS = 2
    # ROWS = int((simulation_amount / COLS) + 1)
    ROWS = 5
    bin_width = 1.5
    # Create subplots for histograms on one canvas
    fig, axes = plt.subplots(ROWS, COLS, figsize=(12, 18))  # 5 rows, 2 columns

    # Iterate through the subplots and plot histograms
    for i, ax in enumerate(axes.flatten()):
        ax.hist(generated_data[i],
                int((max(generated_data[i]) - min(generated_data[i])) / bin_width), color=color,
                edgecolor=edgecolor)
        ax.set_title(f"Simulation {i + 1}")
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Frequency")
        ax.set_xlim(30, 60)
        ax.grid(True)

    # Add a title to the whole canvas
    plt.suptitle(title)

    # Adjust layout
    plt.tight_layout()

    # Show the plot
    plt.show()


simulate_plots(dark_rating_mean_value, dark_rating_std_deviation, light_rating_mean_value, light_rating_std_deviation,
               "Rating Simulations", "#000000", "#bbbbbb")
simulate_hists(dark_engagement_time_mean_value, dark_engagement_time_std_deviation,
               "Dark Theme Engagement Time Simulations", "#000000", "#bbbbbb")
simulate_hists(light_engagement_time_mean_value, light_engagement_time_std_deviation,
               "Light Theme Engagement Time Simulations", "#bbbbbb", "#000000")
