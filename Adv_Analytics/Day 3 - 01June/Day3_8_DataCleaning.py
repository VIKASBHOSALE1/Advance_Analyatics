# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 12:47:03 2024

@author: RS
"""

import pandas as pd

wdi = pd.read_csv("D:/Adv_Analytics/Day 3 - 01June/world_development_indicators.csv")
wdi.info()

# Column analysis
# Some columns seem to be repeating

# Verify that some columns are possible duplicates
print(wdi[['country_name', 'Country Name', 'Country Code', 'planet']].head())
print(wdi.nunique())

# Needed?
print(wdi['planet'].value_counts())
wdi['planet'].value_counts(normalize=True)
# Comparing values/data in both the columns (If the data is same in both the columns then it will show the result/output as -> Empty DataFrame)
print(wdi[wdi['country_name'] != wdi['Country Name']])  
print(wdi['country_name'].compare(wdi['Country Code']))


# Ok to drop these.....
wdi = wdi.drop(columns=['Country Name', 'Country Code', 'planet'])
print(wdi.info())


# Row analysis
print(wdi.duplicated())
print(wdi[wdi.duplicated()])
print(wdi.drop_duplicates(ignore_index = True))
wdi = wdi.drop_duplicates(ignore_index = True)

# Verify that duplicates are gone
print(wdi.shape)
print(wdi[wdi.duplicated()])

# Save the dataframe so that we can reopen from this stage in the next code example
wdi.to_pickle('wdi.pkl')