# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:34:41 2024

@author: dbda
"""

##### Data Cleaning #####

import numpy as np
import pandas as pd
#import datetime
#import matplotlib.pyplot as plt
#import seaborn as sns

df=pd.read_csv("D:/Adv_Analytics/Day 1 - 30May/MS_Dhoni_ODI_record.csv")

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

fours = df_new['fours'].sum()
print("Number of 4[s] : ", fours)

sixes = df_new['sixes'].sum()
print("Number of 6[s] : ", sixes)