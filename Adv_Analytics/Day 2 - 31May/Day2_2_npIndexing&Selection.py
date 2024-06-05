# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:12:18 2024

@author: RS
"""

import numpy as np

# Creating sample array
arr = np.arange(0,11)
print(arr)

# Bracket indexing and selection -similar to python lists
# Get a value at an index
print(arr[8])
# Get values in a range
print(arr[1:5]) 
# Get values in a range
print(arr[0:5])

# Broadcasting 
# Setting a value with index range (Broadcasting)
arr[0:5]=100
print(arr)

# Reset array, why? will be clear soon
arr = np.arange(0,11)
print(arr)

# Important notes on Slices
slice_of_arr = arr[0:6]
print(slice_of_arr)

# Change slice 
slice_of_arr[:]=99
print(slice_of_arr)
print(arr)

# Changes made are also there in our original array!
# Data is not copied, it is a view of the original array!
# This avoids memory problems

# To get a copy, we need to be explicit
arr_copy = arr.copy()
print(arr_copy)

# Conditional selection
arr = np.arange(1,11)
print(arr)

# Check eeach element of the array against the condition arr > 4, which returns a boolean array where
# each element is Trueif the corresponding element in arr is greater than 4, and False otherwise
print(arr > 4)

# Store boolean results in another array
bool_arr = arr > 4
print(bool_arr)

# Select only those elements from the arr array where the corresponding element in boo_arr is True
# it effectively filters out the elements of arr where the condition arr > 4 is True
print(arr[bool_arr])
