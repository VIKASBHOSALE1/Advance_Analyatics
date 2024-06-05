# -*- coding: utf-8 -*-
"""
Created on Fri May 31 19:07:55 2024

@author: RS
"""
##### Data Cleaning #####

import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("D:/Adv_Analytics/Day 2 - 31May/MS_Dhoni_ODI_record.csv")

#Basic checks
print(df.head()) #By default it will print 5 rows
print(df.tail()) #By default it will print 5 rows


#data cleaning - opposition name says 'v Aus' etc, we can remove 'v '
df['opposition']=df['opposition'].apply(lambda x: x[2:])

#Add a 'feature'(column) - 'year' column using the match date column 
#First convert date column into datetime format 
df['date']=pd.to_datetime(df['date'], dayfirst=True)
df['year']=df['date'].dt.year.astype(int)
print(df.head())
#dt is function of pandas which will access datetime properties
#Using feature we predict label

#create a column to distinguish between out and not out

#The apply method in pandas allows you to apply a function to each element in a dataframe or series. 
#In this case, the function being applied is str, which is the built-in python function for converting values into string.
#By applying str to each element in the 'score' column, we are converting the numerical or other data types in that column into string data types.
df['score']=df['score'].apply(str)
df['not_out']=np.where(df['score'].str.endswith('*'),1,0)
type(df['score'])
type(df['not_out'])

#Dropping the odi_number feature because it adds no value to the analysis
df.drop(columns='odi_number', inplace=True)
#inplace=True is used for permenant change in DataFrame
#Alternate way -> df=df.drop(columns='odi_number')

#Dropping those innings where Dhoni did not bat and storing in a new DateFrame
#Take all the columns, starting with runs_scored
df_new = df.loc[((df['score']!='DNB') & (df['score']!='TDNB')), 'runs_scored':]
print(df_new.head())

#Fixing the data types of numerical columns
df_new['runs_scored']=df_new['runs_scored'].astype(int)
df_new['balls_faced']=df_new['balls_faced'].astype(int)
df_new['strike_rate']=df_new['strike_rate'].astype(float)
df_new['fours']=df_new['fours'].astype(int)
df_new['sixes']=df_new['sixes'].astype(int)
type(df_new['sixes'])

#Career stats 
first_match_date=df['date'].dt.date.min().strftime('%B %d, %Y') #first match
print('First match: ', first_match_date)

last_match_date=df['date'].dt.date.max().strftime('%B %d, %Y') #last match
print('Last match: ', last_match_date)

number_of_matches=df.shape[0] #number of matches played in career
#shape[0]->will give rows
print('Number of matches played: ', number_of_matches)

number_of_inns=df_new.shape[0] #number of innings played in career
#shape[0]->will give rows
print('Number of innings played: ', number_of_inns)

not_outs = df_new['not_out'].sum()
print("Not outs : ", not_outs)

runs_scored = df_new['runs_scored'].sum()
print("Runs scored in career : ", runs_scored)

balls_faced = df_new['balls_faced'].sum()
print("Balls faced  in career : ", balls_faced) 

career_sr = (runs_scored/balls_faced)*100
#print('Career strike rate', career_sr)
print('Career strike rate : {:.2f}'.format(career_sr))
print('Career strike rate : ', round(career_sr,2))

career_avg = (runs_scored/(number_of_inns - not_outs))
print('Career average : {:.2f}'.format(career_avg))

highest_score = df_new['runs_scored'].max()
not_out_for_highest = (df_new[df_new['runs_scored'] == highest_score]['not_out']
                       .replace([1,0], ["*", ""])
                       .iloc[0])
print("Highest score in career : ", highest_score,not_out_for_highest)

hundreds = (df_new['runs_scored'] >= 100).sum()
print("Number of 100[s] : ", hundreds)

fifties = (df_new['runs_scored'] >= 50).sum()
print("Number of 50[s] : ", fifties)

fours = df_new['runs_scored'].sum()
print("Number of 4[s] : ", fours)

sixes = df_new['runs_scored'].sum()
print("Number of 6[s] : ", sixes)


################################## day 2 ##################################################################

# Number of matches played against different oppositions 
# Count the occurrences of each unique value in the 'opposition' column
# opposition_counts will be the series with a labelled index as oppositions
opposition_counts = df['opposition'].value_counts()
print(opposition_counts)
opposition_counts.plot(kind='bar', title='Number of matches against different oppositions', figsize=(8,5))
plt.show()

# runs scored against each team
# group the dataframe by 'opposition' column
grouped_by_opposition = df_new.groupby('opposition')
# sum the 'runs_scored' column for each group
sum_of_runs_scored = grouped_by_opposition['runs_scored'].sum()
print(sum_of_runs_scored)

# sum_of_runs_scored is a series with a labelled index, which is opposition
# convert it into dataframe and remove the index
runs_scored_by_opposition = pd.DataFrame(sum_of_runs_scored).reset_index()
runs_scored_by_opposition.plot(x = 'opposition', kind = 'bar', title = "Runs scored against different oppositions", figsize = (8,5))
plt.xlabel(None)
plt.show()

# Does not look good
sorted = runs_scored_by_opposition.sort_values(by = 'runs_scored', ascending = False)
print(sorted)
sorted.plot(x = 'opposition', kind = 'bar', title = "Runs scored against different oppositions", figsize = (8,5))
plt.xlabel(None)
plt.show()

# Boxplot of runs against various oppositions
# BoxPlot will automatically show the outliers
sns.boxplot(x = 'opposition', y = 'runs_scored', data = df_new)
plt.show()

# looks crowded - Let us retain only major countries
# List of oppositions to filter
opposition_list = ['England', 'Australia', 'West Indies', 'South Africa', 'New Zealand', 'Pakistan', 'Sri Lanka', 'Bangladesh']

# Filter rows where 'opposition' is in the list
df_filtered = df_new[df_new['opposition'].isin(opposition_list)]

# sort the filtered dataframe in descending order of 'runs_scored'
df_filtered = df_filtered.sort_values(by = 'runs_scored', ascending = False)
print(df_filtered)

# redraw the boxplot 
sns.boxplot(x = 'opposition', y = 'runs_scored', data = df_filtered)
plt.xticks(rotation=45)
plt.show()

# Violin plot
plt.figure(figsize=(12,6))
sns.violinplot(x = 'opposition', y = 'runs_scored', data = df_filtered)
plt.xticks(rotation=45)
plt.show()

# distplot with and without kde
sns.displot(data = df_filtered, x = 'runs_scored', kde = False)
plt.show()

# we see that there is a right/positive skew, so there is a long tail to the right
sns.displot(data = df_filtered, x = 'runs_scored', kde = True)
plt.show()

# histogram with or without bins
sns.set(style = 'darkgrid')
sns.histplot(data = df_new, x = 'runs_scored', bins = 15)
plt.show()

# KDE plot
plt.figure(figsize = (12,8))
sns.kdeplot(data = df_new, x = 'runs_scored')
plt.show()

# jointplot
sns.jointplot(x = 'balls_faced', y = 'runs_scored', data = df_new, kind = 'scatter')
plt.show()

# Heat map
# calculate the correlation matrix
correlation_matrix = df_new[['balls_faced', 'runs_scored']].corr()

# Create the heatmap
plt.figure(figsize = (8,6))
sns.heatmap(data = correlation_matrix, annot = True, cmap = 'viridis', square = True, fmt = ".2f")

# Add title
plt.title('Correlation Heatmap between Balls Faced and Runs Scored')

# Show plot
plt.show()