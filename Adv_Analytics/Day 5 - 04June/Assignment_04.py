# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:11:33 2024

@author: Sakshi & Ruta
"""

# Assignment 4 : Descriptive Statistics, Skewness, Kurtosis - 4 June 2024


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the datasets for each year
df_2015 = pd.read_csv("D:/Adv_Analytics/Day 5 - 04June/marathon_results_2015.csv")
df_2016 = pd.read_csv("D:/Adv_Analytics/Day 5 - 04June/marathon_results_2016.csv")
df_2017 = pd.read_csv("D:/Adv_Analytics/Day 5 - 04June/marathon_results_2017.csv")

# Concatenate the datasets into a single dataframe
df = pd.concat([df_2015, df_2016, df_2017])

''' 
Calculate various descriptive statistics and visualize the distribution for 
the Official Time column of Boston Marathon 2015, 2016, 2017 as a single dataset 
(Dataset names: marathon_results_2015.csv, marathon_results_2016.csv, marathon_results_2017.csv)
'''


