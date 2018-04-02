# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 13:10:23 2018

@author: CJ O'Sullivan
"""

import pandas
import numpy

data = pandas.read_csv('addhealth_pds.csv')

## -------------------------------------- Lab 03 --------------------------------- ##

### --- Part 02 - Managing Data - Creating Secondary Variables - Combining More Than Two Variables --- ###

# Making sure all variables are numbers.
data['H1GI4'] = pandas.to_numeric(data['H1GI4'])
data['H1GI6A'] = pandas.to_numeric(data['H1GI6A'])
data['H1GI6B'] = pandas.to_numeric(data['H1GI6B'])
data['H1GI6C'] = pandas.to_numeric(data['H1GI6C'])
data['H1GI6D'] = pandas.to_numeric(data['H1GI6D'])

# Removing values 6 and 8, setting to NaN.
data['H1GI4'] = data['H1GI4'].replace([6,8], numpy.nan)
data['H1GI6A'] = data['H1GI6A'].replace([6,8], numpy.nan)
data['H1GI6B'] = data['H1GI6B'].replace([6,8], numpy.nan)
data['H1GI6C'] = data['H1GI6C'].replace([6,8], numpy.nan)
data['H1GI6D'] = data['H1GI6D'].replace([6,8], numpy.nan)

# Summing each of the variables and placing the answer in a new variables called NUMETHNIC 
data['NUMETHNIC'] = data['H1GI4'] + data['H1GI6A'] + data['H1GI6B'] + data['H1GI6C'] + data['H1GI6D']

# Frequency counts for NUMETHNIC.
print('counts for NUMETHNIC')
c1= data['NUMETHNIC'].value_counts(sort=True)
print (c1)

### --- Part 03 - Managing Data - Creating Secondary Variables - Characterizing each ethnicity. --- ###

# Using the define function to create a new variable called Ethnicity.
# Row is a temporary variable to be used in the function. 
# Apply function is uysed to actually create the new variable.
# Axis = 1 tells python to applly the finction to each row.
def ETHNICITY (row):
    if row['NUMETHNIC']>1:
        return 1
    if row['H1GI4'] ==1:
        return 2
    if row['H1GI6A'] ==1:
        return 3
    if row['H1GI6B'] ==1:
        return 4
    if row['H1GI6C']==1:
        return 5
    if row['H1GI6D']==1:
        return 6

data['ETHNICITY'] = data.apply(lambda row: ETHNICITY (row), axis=1)

# Outputting a grid that shows 25 random rows and what ethnicity they were identified as.
ETHNICITY_SUB = data[['H1GI4','H1GI6A','H1GI6B','H1GI6C','H1GI6D','NUMETHNIC','ETHNICITY']]  
print(ETHNICITY_SUB.head(n=25))


















