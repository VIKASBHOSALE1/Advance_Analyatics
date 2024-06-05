# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:48:31 2024

@author: Sakshi & Ruta
"""

# Assignment 2 : Data Visualization - 01 June 2024

import matplotlib.pyplot as plt
import pandas as pd

# Draw a stacked bar plot as shown below in the MS Dhoni example.
df = pd.read_csv("D:/Adv_Analytics/Day 3 - 01June/MS_Dhoni_ODI_record.csv")
df['opposition']=df['opposition'].apply(lambda x: x[2:])

df['fours'] = df['fours'].replace("-", 0)
df['sixes'] = df['sixes'].replace("-", 0)
df['runs_scored'] = df['runs_scored'].replace("-", 0)

df['runs_scored'] = df['runs_scored'].astype(int)
df['fours'] = df['fours'].astype(int)
df['sixes'] = df['sixes'].astype(int)

df['runs_with_boundaries'] = (df['fours'] * 4) + (df['sixes'] * 6)

df['runs_without_boundaries'] = df['runs_scored'] - df['runs_with_boundaries']

opposition_list = ['Australia', 'Bangladesh', 'England', 'New Zealand', 'Pakistan', 'South Africa', 'Sri Lanka', 'West Indies']

df_filtered = df[df['opposition'].isin(opposition_list)]

grouped_by_opposition = df_filtered.groupby('opposition')
sum_of_runs_scored_with_boundaries = grouped_by_opposition['runs_with_boundaries'].sum()
sum_of_runs_scored_without_boundaries = grouped_by_opposition['runs_without_boundaries'].sum()

data = [sum_of_runs_scored_with_boundaries, sum_of_runs_scored_without_boundaries]
plt.bar(opposition_list, data[1], label = 'Runs Scored')
plt.bar(opposition_list, data[0], bottom = data[1], label = 'Runs with boundaries')
plt.title("Runs Scored and Runs in Boundaries by Opposition")
plt.xlabel('Opposition')
plt.ylabel('Runs')
plt.legend()
plt.xticks(rotation=45)
plt.show()


# ---------------------------------------------------------------------------------------------------------------------------------------
# Then show a pie chart as follows - 


labels = ['Runs in Sixes', 'Runs in Fours', 'Runs not in Boundaries']
 
for country in opposition_list:
    sixes = ((grouped_by_opposition['sixes']).sum()).where(grouped_by_opposition['opposition'] == country)
    fours = ((grouped_by_opposition['fours']).sum()).where(grouped_by_opposition['opposition'] == country)
    runs_without_boundaries = (sum_of_runs_scored_without_boundaries.sum()).where(sum_of_runs_scored_without_boundaries['opposition'] == country)
    
    data = [sixes, fours, runs_without_boundaries]
    
    plt.pie(data, labels = labels)
    plt.title(country)
    plt.show()