# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:56:51 2024

@author: RS
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'D:/Adv_Analytics/Day 4 - 03June/temp.csv'
df = pd.read_csv(file_path)
print(df.head())

df['date'] = pd.to_datetime(df['datetime'])


# Identify outliers using IQR method
def identify_outliers_iqr(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return np.where((data < lower_bound) | (data > upper_bound))[0]

# Visualize the data using BoxPlots
plt.figure(figsize = (12,6))

# LA Temperatures
plt.subplot(1,2,1)
sns.boxplot(y = df['LA'])
plt.title('LA Temperatures')

# NY Temperatures
plt.subplot(1,2,2)
sns.boxplot(y = df['NY'])
plt.title('NY Temperatures')
plt.show()


# Outliers Detection
LA_outliers_iqr = identify_outliers_iqr(df['LA'])
NY_outliers_iqr = identify_outliers_iqr(df['NY'])

print("Outliers in LA Temperatures using IQR method : ")
print(df.iloc[LA_outliers_iqr])

print("Outliers in NY Temperatures using IQR method : ")
print(df.iloc[NY_outliers_iqr])