# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:40:56 2024

@author: RS
"""


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random weight data for 1000 people between 50 and 100 kg
np.random.seed(42)  # Set seed for reproducibility
weights = np.random.uniform(50, 100, 1000)

# Filter weights within the range 65-67 kg for KDE visualization
weights_kde_range = weights[(weights >= 65) & (weights <= 67)]

# Plotting the histogram as the PMF
plt.hist(weights, bins = np.arange(50, 101, 2), color = 'lightgray', edgecolor = 'black', alpha = 0.7, label = 'Overalll Distribution', density = True)

# Plotting the KDE (PDF) for the weight data in the specified range with common_norm
sns.kdeplot(weights_kde_range, bw_method = 0.5, fill = True, color = 'skyblue', alpha = 0.7, linewidth = 2, label = 'KDE (65-67 Kg)', common_norm = False)
# common_norm = True (default) : Total area under all the curves should be 1
# common_norm = False :Area under our own curve should be 1

plt.xlabel('Weight (kg)')
plt.ylabel('Probabillity Mass')
plt.title('Probability Mass function for 1000 People')
plt.legend()

# Show the plot
plt.show()