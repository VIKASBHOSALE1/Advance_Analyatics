# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:56:15 2024

@author: RS
"""

import numpy as np
import pandas as pd

# Creating a Series from a Python list
myindex = ['USA','Canada','England']
mydata = [1776,1876,1821]

# Just the numeric index
myser = pd.Series(data = mydata)
print(myser)

# Now the named index
myser = pd.Series(data = mydata, index = myindex)
print(myser)


# Creating a Series from NumPy array
# First create a NumPy array using the earlier list
ran_data = np.random.randint(0,100,4)
print(ran_data)
names = ['Alice','Bob','Charles','Dave']
ages = pd.Series(ran_data, names)
print(ages)

# Creating a series from a dictonary
ages = {'Sammy':5, 'Frank':10, 'Spike':7}
print(ages)
print(pd.Series(ages))

# Using named index
# Imaginary sales data for 1st and 2nd Quarters for a global company
q1 = {'Japan':80, 'China':450, 'India':200, 'USA':250}
q2 = {'Brazil':100, 'China':500, 'India':210, 'USA':260}
# Convert into Pandas Series
sales_Q1 = pd.Series(q1)
sales_Q2 = pd.Series(q2)

print(sales_Q1)

# Call values based on the Named index
print(sales_Q1['Japan'])

# Integer based Location Information also retained ! 
print(sales_Q1[0])


# Be careful with potential errors !

# Wrong name
# print(sales_Q1['France'])

# Accidental extra space
# print(sales_Q1['USA '])

# Text case mistake
# print(sales_Q1['usa'])