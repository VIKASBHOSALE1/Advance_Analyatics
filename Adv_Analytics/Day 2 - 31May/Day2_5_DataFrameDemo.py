# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:12:59 2024

@author: RS
"""

import numpy as np
import pandas as pd

# Create a simple dataframe from an existing Python List
np.random.seed(101)
mydata = np.random.randint(0,101,(4,3))
print(mydata)

myindex = ['CA','NY','AZ','TX']
mycolumns = ['Jan', 'Feb', 'Mar']

df = pd.DataFrame(data = mydata)
print(df)

df = pd.DataFrame(data = mydata, index = myindex)
print(df)

df = pd.DataFrame(data = mydata, index = myindex, columns = mycolumns)
print(df)

print(df.info())

# Create a dataframe from a CSV File

df = pd.read_csv('D:/Adv_Analytics/Day 2 - 31May/tips.csv')
print(df)

print(df.columns)   # column names
print(df.index)     # index 
print(df.head(3))   # First 3 rows
print(df.tail(3))   # Last 3 rows
print(df.info())    # Information about df including data types and memory used
print(len(df))      # Number of rows
print(df.describe())    # Statistical summary
print(df.describe().transpose())    # Statistical summary better organized

# Select a single column
print(df['total_bill'])
print(df.total_bill)  # will not work if the column name contains a space
print(type(df['total_bill']))

# Select multiple columns
# Note how its a python list of column names ! Thus the double brackets
print(df[['total_bill', 'tip']])

# create new columns
df['tip_percentage'] = 100 * df['tip'] / df['total_bill']
print(df.head())

df['price_per_person'] = df['total_bill'] / df['size']
print(df.head())

# Adjust existing columns 
df['price_per_person'] = np.round(df['price_per_person'], 2)
print(df.head())

# Remove Coulmns 
df = df.drop('tip_percentage', axis = 1)
print(df.head())


# Index
print(df.head())
print(df.index)

df.set_index('Payment ID')
print(df.head())
print(df.index)

df = df.set_index('Payment ID')
print(df.head())
print(df.index)

df = df.reset_index()
print(df.head())

# Another index sample - Air BNB dataset from kaggle

# Default inedx
df_airbnb = pd.read_csv("D:/Adv_Analytics/Day 2 - 31May/AB_NYC_2019.csv")
print(df_airbnb.head(3))

# Make id column the index
df2 = df_airbnb.set_index("id")
print(df2.head(3))
print(df2.name[3647])   # Get the name for id = 3647

pd.set_option('display.max_columns', None)
print(df2.head(3))
print(df2.index)
# Note that room_type has become to index - we can again convert it into a normal column
df2 = df2.reset_index()
pd.reset_option('display.max_columns')      # Also reset the column display to default
print(df2.head(3))

# Rows 
# Get a single row
# Integer based
print(df.iloc[0])

# Name based
# First set the index to the column which will be used in locating the row
df2 = df2.set_index('id')
print(df2.loc['2595'])

# Remove a row
print(df2.head())
df2 = df2.drop('2595', axis = 0)
print(df2.head())


# Conditions

print(df['total_bill'] < 30)            # True / False
bool_series = df['total_bill'] > 30     # Save in variable

print(bool_series)                      # True / False
print(df[bool_series])                  # Actual results, applying the true/false conditions

print(df[df['total_bill'] > 30])

# Another syntax
print(df.total_bill > 30)
print(df[df.total_bill > 30])

print(df[df['gender'] == 'Male'])

# Multiple conditions
df_new = df[(df['total_bill'] > 30) & (df['gender'] == 'Male')]
print(df_new.head())

df_new = df[(df['total_bill'] > 30) & ~(df['gender'] == 'Male')]
print(df_new.head())

df_new = df[(df['total_bill'] > 30) & (df['gender'] != 'Male')]
print(df_new.head())

df_new = df[(df['total_bill'] > 30) | (df['tip'] > 5)]
print(df_new.head())

# conditional 'is in' operator
options = ['Sat', 'Sun']
print(df['day'].isin(options))
print(df[df['day'].isin(['Sat', 'Sun'])])

# value_counts - get count on categorical columns
print(df['smoker'].value_counts())      # Smokers and non-smokers
print(df['gender'].value_counts())      # Males and Females

# unique 
print(df['size'].unique())      # all the unique values as an array
print(df['size'].nunique())     # number of unique values (i.e. count of the above array)
print(df['time'].unique())      # for a character column 

# between : options for inclusive are both, left, right, neither
print(df['total_bill'].between(10, 20, inclusive = "both"))
print(df[df['total_bill'].between(10, 20, inclusive = "both")])
























