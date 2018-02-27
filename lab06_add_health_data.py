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

