# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:50:55 2024

@author: Sakshi & Ruta
"""

# Assignment 1 : NumPy - 31 May 2024

import numpy as np

# 1 - Create an array of 10 zeros
arr0 = np.zeros(10)
print(arr0)

# 2 - Create an array of 10 ones
arr1 = np.ones(10)
print(arr1)

# 3 - Create an array of 10 fives
arr5 = arr1 * 5
print(arr5)

# 4 - Create an array of the integers from 10 to 50
arr6 = np.arange(10,51)
print(arr6)

# 5 - Create an array of all the even integers from 10 to 50
arr7 = np.arange(10,51,2)
print(arr7)

# 6 - Use NumPy to generate a random number between 0 and 1
print(np.random.rand())

# 7 - Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
print(np.random.randn(25))

# 8 - Create an array of 20 linearly spaced points between 0 and 1
print(np.linspace(0,1,20))