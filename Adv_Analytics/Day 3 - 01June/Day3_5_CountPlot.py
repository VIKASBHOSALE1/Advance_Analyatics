# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 09:39:43 2024

@author: dbda
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Countplot : A simple plot, it merely shows the total count of rows per category
# A histogram across a categorical, instead of quantitative, variable 

df = pd.read_csv("D:/Adv_Analytics/Day 3 - 01June/dm_office_sales.csv")

plt.figure(figsize=(10,4), dpi=200)
sns.countplot(x=  'level of education', data = df)
plt.show()

# Breakdown within another category with hue
plt.figure(figsize=(10,4), dpi=200)
sns.countplot(x=  'level of education', data = df, hue = 'training level')
plt.show()

# Using palette
plt.figure(figsize=(10,4), dpi=200)
sns.countplot(x=  'level of education', data = df, hue = 'training level', palette = 'Set1')
plt.show()

plt.figure(figsize=(10,4), dpi=200)
# Paired would be a good choice if there was a distinct jump from 0 and 1 to 2 and 3
sns.countplot(x=  'level of education', data = df, hue = 'training level', palette = 'Paired')
plt.show()