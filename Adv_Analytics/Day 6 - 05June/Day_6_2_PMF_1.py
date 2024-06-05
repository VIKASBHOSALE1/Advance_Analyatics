# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:18:10 2024

@author: RS
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate random weight data for 1000 people between 50 and 100 kg
np.random.seed(42)  # Set seed for reproducibility
weights = np.random.uniform(50, 100, 1000)

# Plotting the histogram as the PMF
plt.hist(weights, bins = np.arange(50, 101, 2), color = 'lightgray', edgecolor = 'black', alpha = 0.7, label = 'PMF', density = False)

plt.xlabel('Weight (kg)')
plt.ylabel('Probabillity Mass')
plt.title('Probability Mass function for 1000 People')
plt.legend()

# Show the plot
plt.show()