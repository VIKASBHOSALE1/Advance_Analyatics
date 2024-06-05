# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 09:06:38 2024

@author: RS
"""

import pandas as pd

df_2015=pd.read_csv("marathon_results_2015.csv")
df_2016=pd.read_csv("marathon_results_2016.csv")
df_2017=pd.read_csv("marathon_results_2017.csv")

df=pd.concat([df_2015,df_2016,df_2017])

#split the'official time' column into hours,minute and seconds
#expand=true menas split into different columns
df[['Hours','Minutes','Seconds']]=df['Official Time'].str.split(':',expand=True)

#convert hours,minute,and seconds columns to integers
df['Hours']=df['Hours'].astype(int)
df['Minutes']=df['Minutes'].astype(int)
df['Seconds']=df['Seconds'].astype(int)

#manually calculate total time in secons
df['finish_time_in_seconds']=df['Hours']*3600+df['Minutes']*60+df['Seconds']

#repeat for the 'pace' column
#split the 'official tme' column into hours, minutes,seconds
#expand=True means split into different columns
df[['Hours','Mintutes','Seconds']]=df['Pace'].str.split(':',expand=True)

#conver hours,minutes,seconds columns to integers
df['Hours']=df['Hours'].astype(int)
df['Minutes']=df['Minutes'].astype(int)
df['Seconds']=df['Seconds'].astype(int)

df['pace_in_seconds']=df['Hours']*3600+df['Minutes']*60+df['Seconds']

#define the condition
condition_A=df['finish_time_in_seconds']<=3*60*60#finish within 3 hours
condition_B=df['pace_in_seconds']<8*60#pace less than 8 minutes per km

#calculate the probabilities
P_B=len(df[condition_B])/len(df)
P_A_and_B=len(df[condition_A & condition_B])/len(df)

#condition probability P(A | B)
P_A_given_B=P_A_and_B / P_B

print(f"(A | B)={P_A_given_B:.4f}")