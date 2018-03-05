# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:36:58 2018

@author: CJ O'Sullivan
"""

import pandas
import numpy 

data = pandas.read_csv('addhealth_pds.csv');

#### Lab06 Section 2 ####

## Checking the variables are of numerical data type. 
data['H1GI4'] = pandas.to_numeric(data['H1GI4'])
data['H1GI6A'] = pandas.to_numeric(data['H1GI6A'])
data['H1GI6B'] = pandas.to_numeric(data['H1GI6B'])
data['H1GI6C'] = pandas.to_numeric(data['H1GI6C'])
data['H1GI6D'] = pandas.to_numeric(data['H1GI6D'])

## Removing values of 6 and 8 because they are not useful. 
data['H1GI4'] = data['H1GI4'].replace([6,8], numpy.nan)
data['H1GI6A'] = data['H1GI6A'].replace([6,8], numpy.nan)
data['H1GI6B'] = data['H1GI6B'].replace([6,8], numpy.nan)
data['H1GI6C'] = data['H1GI6C'].replace([6,8], numpy.nan)
data['H1GI6D'] = data['H1GI6D'].replace([6,8], numpy.nan)

## Summing each of the variables and placing them in a new variables called NUMETHNIC
data['NUMETHNIC'] = data['H1GI4'] + data['H1GI6A'] + data['H1GI6B'] + data['H1GI6C'] + data['H1GI6D']

## Counting all instances of each value for NUMTHNIC vriable. 
count1=data['NUMETHNIC'].value_counts(sort=True)
print(count1)

#### Lab06 Section 3 ####

def ETHNICITY (row):
    if row['NUMETHNIC'] > 1:
        return 1
    if row['H1GI4'] == 1:
        return 2
    if row['H1GI6A'] == 1:
        return 3
    if row['H1GI6B'] == 1:
        return 4
    if row['H1GI6C'] == 1:
        return 5
    if row['H1GI6D'] == 1:
        return 6
    
data['ETHNICITY'] = data.apply(lambda row: ETHNICITY (row), axis=1)

subset1 = data[['AID', 'H1GI4', 'H1GI6A', 'H1GI6B', 'H1GI6C', 'H1GI6D', 'NUMETHNIC', 'ETHNICITY']]
subset1.head(25)

#### Lab06 Section 4 ####

## Quartile split qcut function into four groups.
print('AGE - 4 Categories - Quartiles')
subset2['AGEGROUP'] = pandas.qcut(subset2.AGE, 4, labels=['1=25%tile','2=50%tile','3=75%tile','4=100%tile'])
c14 = subset2['AGEGROUP'].value_counts(sort=False, dropna=True)
print(c14)

## Categorise variable based on customised splits using the cut() functions. 
## Splits into three groups, 18 - 20, 21 - 22 and 23- 25
subset2['AGEGROUP2']=pandas.cut(subset2.AGE,[17, 20, 22, 25], labels=['18-20','21-22','23-25'])
c15 = subset2['AGEGROUP2'].value_counts(sort=False, dropna= True)
print(c15)

subset2['AGEGROUP2']=pandas.cut(subset2.AGE,[17, 20, 22, 25], labels=['18-20','21-22','23-25'])
c16 = subset2['AGEGROUP2'].value_counts(sort=True, dropna= True, normalize= True)
print(c16)



        
        

