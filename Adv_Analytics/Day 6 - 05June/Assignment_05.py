# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:17:57 2024

@author: Sakshi & Ruta
"""

# Assignment 5 - 5 June 2024
'''
Find (a) the conditional probability that a person's Glucose levels are > 110  
given that the person’s BMI >= 25 and (b) the conditional probability of BMI >= 25  
given that Glucose > 110.
'''

import pandas as pd

df = pd.read_csv('D:/Adv_Analytics/Day 6 - 05June/diabetes.csv')

condition_A = df['Glucose'] > 110
condition_B = df['BMI'] >= 25

P_A = len(df[condition_A]) / len(df)
P_B = len(df[condition_B]) / len(df)

P_A_and_B= len(df[condition_A & condition_B]) / len(df)

P_A_given_B = P_A_and_B / P_B
P_B_given_A = P_A_and_B / P_A

print(f"P(Glucose|BMI) = {P_A_given_B:.4f}")
print(f"P(BMI|Glucose) = {P_B_given_A:.4f}")