# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:29:43 2024

@author: RS
"""

# PMF on the Age column of diabetes dataset

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("D:/Adv_Analytics/Day 6 - 05June/diabetes.csv")

age_data = df['Age']

plt.hist(age_data, bins = 'auto', color = 'lightgray', edgecolor = 'black', alpha = 0.7, label = 'PMF')
# Use 'auto' for bins selection
plt.xlabel("Age")
plt.ylabel("Probability Mass")
plt.title("Probability Mass Function of Age in thr Dataset")
plt.legend()
plt.show()