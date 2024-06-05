# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 09:16:10 2024

@author: RS
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:/Adv_Analytics/Day 3 - 01June/dm_office_sales.csv")

sns.scatterplot(x='salary', y='sales', data=df)
plt.show()      # Note that seaborn is linked to matplotlib underneath

plt.figure(figsize=(12,8))
sns.scatterplot(x='salary', y='sales', data=df)
plt.show() 

# hue: color points based off a categorical feature in the dataframe , differntiate columns
plt.figure(figsize=(12,8))
sns.scatterplot(x='salary', y='sales', data=df, hue = 'division')
plt.show()

plt.figure(figsize=(12,8))
sns.scatterplot(x='salary', y='sales', data=df, hue = 'work experience')
plt.show() 

'''
# Choosing a palette from matplotlib's cmap:
    https://matplotlib.org/tutorials/colors/colormaps.html
'''

plt.figure(figsize=(12,8))
sns.scatterplot(x='salary', y='sales', data=df, hue = 'work experience', palette = 'viridis')
plt.show()

# Use s= if you want to change the marker size to be some uniform integer value
plt.figure(figsize=(12,8))
sns.scatterplot(x='salary', y='sales', data=df, s=200)
plt.show() 

plt.figure(figsize=(12,8))
sns.scatterplot(x='salary', y='sales', data=df, s=200, linewidth=0, alpha=0.2)
plt.show() 

plt.figure(figsize=(12,8))
sns.scatterplot(x='salary', y='sales', data=df, style='level of education')
plt.show() 

plt.figure(figsize=(12,8))
sns.scatterplot(x='salary', y='sales', data=df, s=100, style='level of education', hue='level of education')
plt.show() 

