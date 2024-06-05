# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 09:04:12 2024

@author: RS
"""

# Line plot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:/Adv_Analytics/Day 3 - 01June/patient.csv")

ages = df.groupby("age").median().reset_index()

# Simple Pandas
ages.plot.line("age", "chol");
plt.show()

# matplotlib
fig, ax = plt.subplots()
ax.plot(ages['age'], ages['chol'], ls = ":", lw = 1.7)
ax.set_xlabel('Age')
ax.set_ylabel('Cholesterol');
plt.show()

# seaborn
sns.lineplot(x='age', y='chol', data=ages, linestyle = ':', linewidth = 1.7)
plt.xlabel('Age')
plt.ylabel('Cholesterol')
plt.show()