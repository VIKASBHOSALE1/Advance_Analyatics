# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:38:18 2024

@author: Sakshi & Ruta
"""

# Assignment 3 : Outlier Detection using IQR - 3 June 2024

'''
Do outlier analysis using IQR method for males and females 
separately for a dataset weight-height.csv.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'D:/Adv_Analytics/Day 4 - 03June/weight-height.csv'
df = pd.read_csv(file_path)
print(df.head())

# Identify outliers using IQR method
def identify_outliers_iqr(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return np.where((data < lower_bound) | (data > upper_bound))[0]

df_males = df.loc[(df['Gender'] == 'Male')]
df_males.head()

df_females = df.loc[(df['Gender'] == 'Female')]
df_females.head()

# Visualize the data using BoxPlots
plt.figure(figsize = (6,4))

# Males Height
plt.subplot(2,2,1)
sns.boxplot(y = df_males['Height'])
plt.title('Males Height')

# Males Weight
plt.subplot(2,2,2)
sns.boxplot(y = df_males['Weight'])
plt.title('Males Weight')
plt.show()

# Females Height
plt.subplot(2,2,3)
sns.boxplot(y = df_females['Height'])
plt.title('Females Height')

# Females Weight
plt.subplot(2,2,4)
sns.boxplot(y = df_females['Weight'])
plt.title('Females Weight')
plt.show()

# Outliers Detection
Males_Height_outliers_iqr = identify_outliers_iqr(df_males['Height'])
Males_Weigth_outliers_iqr = identify_outliers_iqr(df_males['Weight'])

Females_Height_outliers_iqr = identify_outliers_iqr(df_females['Height'])
Females_Weigth_outliers_iqr = identify_outliers_iqr(df_females['Weight'])

print("Outliers in Male Heights using IQR method : ")
print(df.iloc[Males_Height_outliers_iqr])

print("Outliers in Male Weights using IQR method : ")
print(df.iloc[Males_Weigth_outliers_iqr])

print("Outliers in Female Heights using IQR method : ")
print(df.iloc[Females_Height_outliers_iqr])

print("Outliers in Female Weights using IQR method : ")
print(df.iloc[Females_Weigth_outliers_iqr])