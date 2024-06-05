# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 13:14:42 2024

@author: RS
"""

import pandas as pd
 
wdi = pd.read_pickle('wdi.pkl')
print(wdi.info())   # Get tge non-null count for each column

print(wdi['alcohol_consumption_per_capita'])
print(wdi.isna())

# How many nulls in each column?
print(wdi.isna().sum())

# Unique counts for each value for the alcohol_consumption_per_capita column
# Note: This excludes nulls by default
print(wdi['alcohol_consumption_per_capita'].value_counts())
print(wdi['alcohol_consumption_per_capita'].value_counts(dropna = False))

# Find nulls by rows
print(wdi.isna())   # DataFrame containing boolean data fro nulls
print(wdi.isna().sum(axis=1))   # By default, it counts rows for columns, but now we want null column counts for each rows

# Store this as a series
num_missing_by_rows = wdi.isna().sum(axis=1)
print(num_missing_by_rows > 0)          # Which rows have 1 null column ?
print((num_missing_by_rows > 0).sum())  # How many rows have at least some missing data ?
print(wdi.shape)
print(wdi[num_missing_by_rows > 0])     # Rows with atleast some missing data

# Drop rows that contain missing values
# Show only non-null rows (Rows with even one null column value will be dropped)
print(wdi.dropna())
print(wdi.dropna().info())

# Drop columns that contain missing values
print(wdi.dropna(axis = 1))