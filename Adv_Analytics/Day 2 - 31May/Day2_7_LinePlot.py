# -*- coding: utf-8 -*-
"""
Created on Fri May 31 20:06:19 2024

@author: RS
"""

import numpy as np
import matplotlib.pyplot as plt

# generate x-axis values (1-9)
x = np.arange(1,10)

# generate y-axis values (1-18)
y = np.arange(1,19)

# Select the first 9 elements from y to match x-axis length
y = y[:9]   # Slicing to get elements from index 0 (inclusive) to 9 (exclusive)

# Create the line plot
plt.plot(x,y)
plt.scatter(x,y, s=50)      # Increase marker size to 50
plt.show()

# Add labels and title
plt.xlabel('X Axis title here')
plt.ylabel('Y Axis title here')
plt.title('Plot Title here')
plt.scatter(x,y, s=50)      # Increase marker size to 50
plt.show()