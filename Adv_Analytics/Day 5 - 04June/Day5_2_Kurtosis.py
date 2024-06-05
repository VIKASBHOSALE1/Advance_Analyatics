# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:49:11 2024

@author: RS
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("D:/Adv_Analytics/Day 5 - 04June/tips.csv")

# Calculate descriptive statistics for the 'tip' column
tip_stats = data['tip'].describe()
print("Descriptive Statistics for the 'tip' column : ")
print(tip_stats)


# Additional statistic
mean_tip = data['tip'].mean()
median_tip = data['tip'].median()
std_tip = data['tip'].std()
var_tip = data['tip'].var()
skew_tip = data['tip'].skew()
kurtosis_tip = data['tip'].kurtosis()
cv_tip = std_tip/mean_tip

print("\nAdditional Statistics for the 'tip' column : ")
print(f"Mean : {mean_tip}")
print(f"Median : {median_tip}")
print(f"Standard Deviation : {std_tip}")
print(f"Variance : {var_tip}")
print(f"Skewness : {skew_tip}")
print(f"Kurtosis : {kurtosis_tip}")
print(f"Coefficient of Variation : {cv_tip}%")

# Plotting the distribution of the 'tip' column
plt.figure(figsize=(14,6))

# Histogram
plt.subplot(1,2,1)      # Number of rows, Number of Columns, Current subplot number
sns.histplot(data['tip'], bins = 20, kde = True)
#sns.histplot(data['tip'], bins = 20, kde = False)
plt.title("Distribution of Tips")
plt.xlabel("Tip Amount")
plt.ylabel("Frequency")


# Box plot
plt.subplot(1,2,2)
sns.boxplot(y = data['tip'])
plt.title("Box Plot of Tips")
plt.xlabel("Tip Amount")

# Show the plots
plt.tight_layout()
plt.show()