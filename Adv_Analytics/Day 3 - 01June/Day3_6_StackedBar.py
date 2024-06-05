# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:31:33 2024

@author: RS
"""

import matplotlib.pyplot as plt

fruits = ['Apples', 'Pineapples', 'Oranges']
sales_2023 = [1000, 800, 600]
sales_2024 = [1200, 900, 700]

# Stack the data (sales_2023 in the lower half)
data = [sales_2023, sales_2024]

# Create the stcked bar plot
plt.bar(fruits, data[0], label = '2023 Sales')
plt.bar(fruits, data[1], bottom = data[0], label = '2024 Sales')
plt.xlabel("Fruits")
plt.ylabel("Sales")
plt.title("Fruit Sales Comparison (2023 vs 2024)")
plt.legend()
plt.show()