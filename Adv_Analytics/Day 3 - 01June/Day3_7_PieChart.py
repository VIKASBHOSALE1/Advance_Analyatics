# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:40:54 2024

@author: dbda
"""

import matplotlib.pyplot as plt
import seaborn as sns

data = [30, 20, 50]
labels = ["Java", "C++", "Python"]

# Create a pastel color palette
colors = sns.color_palette("pastel")[1:4]

# Create the pie chart
plt.pie(data, labels = labels, colors = colors, autopct = "%.1f%%")     # Show percentage with one decimal
plt.title("Pie Chart Exmaple")
plt.show()