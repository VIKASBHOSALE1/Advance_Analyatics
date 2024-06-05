# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:55:37 2024

@author: RS
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

airline_df = pd.read_csv("D:/Adv_Analytics/Day 5 - 04June/airline_dec_2008_50k.csv")
distance = airline_df['Distance']

mean_distance = distance.mean()
median_distance = distance.median()
skewness_distance = distance.skew()
kurtosis_distance = distance.kurt()     # Calculate kurtosis using 'kurt'

plt.figure(figsize = (8,6))
sns.histplot(distance, kde=True, color='skyblue', bins=30)
plt.axvline(mean_distance, color="red", linestyle='--', label=f'Mean:{mean_distance:.2f}')
plt.axvline(median_distance, color="black", linestyle='--', label=f'Median:{median_distance:.2f}')
plt.title(f'Distribution of distance \nSkewness : {skewness_distance:.2f}, Kurtosis : {kurtosis_distance:.2f}')
plt.xlabel("Distance")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()