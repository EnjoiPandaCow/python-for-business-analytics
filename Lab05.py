# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# ------------------------ lab 04 Start --------------------------------- # 

import pandas
import numpy

#load dataset from the csv file in the dataframe called nesarc_data
nesarc_data = pandas.read_csv('nesarc_pds.csv',low_memory=False)

#convert all columns names to uppercase
nesarc_data.columns = map(str.upper, nesarc_data.columns)
#nesarc_data.columns = map(str.lower, nesarc_data.columns)

#bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format',lambda x:'%f'%x)

print (len(nesarc_data)) 
print (len(nesarc_data.columns))

#converting strings to numeric data for better output

nesarc_data['S3AQ3B1'] = pandas.to_numeric(nesarc_data['S3AQ3B1'], errors='ignore')
nesarc_data['S3AQ3C1'] = pandas.to_numeric(nesarc_data['S3AQ3C1'], errors='ignore')

#Count and percentage for each variable using value_counts function
print('counts for TAB12MDX - nicotine dependence in the past 12 months, yes=1')
c1= nesarc_data["TAB12MDX"].value_counts(sort=True)
print (c1)

print('percentages for TAB12MDX - nicotine dependence in the past 12 months, yes=1')
p1= nesarc_data["TAB12MDX"].value_counts(sort=True, normalize=True)
print (p1)

print('counts for CHECK321 - smoked in the past year, yes=1')
c2= nesarc_data["CHECK321"].value_counts(sort=True)
print (c2)

print('percentages for CHECK321 - smoked in the past year, yes=1')
p2= nesarc_data["CHECK321"].value_counts(sort=True, normalize=True)
print (p2)

print('counts for S3AQ3B1 - usual frequency when smoked cigarettes')
c3= nesarc_data["S3AQ3B1"].value_counts(sort=True)
print (c3)

print('percentages for S3AQ3B1 - usual frequency when smoked cigarettes')
p3= nesarc_data["S3AQ3B1"].value_counts(sort=True, normalize=True)
print (p3)

print('counts for S3AQ3C1 - usual quanitity when smoked cigarettes')
c4= nesarc_data["S3AQ3C1"].value_counts(sort=True)
print (c4)

print('percentages for S3AQ3C1 - usual quanitity when smoked cigarettes')
p4= nesarc_data["S3AQ3C1"].value_counts(sort=True, normalize=True)
print (p4)

#count and percentage for TAB12MDX using the groupby function

ct1 = nesarc_data.groupby('TAB12MDX').size()
print(ct1)

pt1 = nesarc_data.groupby('TAB12MDX').size() * 100 / len(nesarc_data)
print(pt1)

# ------------------------ lab 05 Start --------------------------------- # 

# Finding the number of adults between 18 and 25 that have smoked in the last 12 months. 
print('The number of rows in the subset of adults between 18 and 25 that have smoked in the past 12 months')
subset1 = nesarc_data[(nesarc_data['AGE']>=18) & (nesarc_data['AGE']<=25) & (nesarc_data['CHECK321']=='1')]
print(len(subset1))

# Count the amount of people at each age 
print('The count of each age value')
c5 = subset1['AGE'].value_counts(sort='TRUE')
print(c5)

# Find the percentage each age has of the dataset. 
print('The percentage of each age value')
p5 = subset1['AGE'].value_counts(sort='TRUE', normalize=True)
print (p5)

# Print the amount of people that have smoked in the last 12 months. 
print('The count of those who have smoked in the past 12 months')
c6=subset1['CHECK321'].value_counts(sort='TRUE')
print(c6)

# Copying subset1 to subset2 
subset2 = subset1.copy()

print('Number of observations in subset 2')
print (len(subset2))

# Checking if S3AQ3B1 in subset2 is actually a number 
subset2['S3AQ3B1']=pandas.to_numeric(subset2['S3AQ3B1'])

# Frequency counts for S3AQ3B1
print('Counts for S3AQ3B1 - Usual frequency when smoked cigaretts')
c7 = subset2 ["S3AQ3B1"].value_counts(sort = True)
print (c7)

# Replaces all the 9 values with NaN.
subset2['S3AQ3B1'] = subset2['S3AQ3B1'].replace(9,numpy.nan)
print((subset2['S3AQ3B1'] == 9).sum())

# Print how many values are NaN
print(subset2['S3AQ3B1'].isnull().sum())

# Frequency counts for S3AQ3B1
print('Counts for S3AQ3B1 - Usual frequency when smoked cigaretts')
c8 = subset2 ["S3AQ3B1"].value_counts(sort = True, dropna = False)
print (c8)

# --------- Part 03 - S3AQ3C1 variable. ----------- # 

# Copying subset1 to subset2 
subset3 = subset1.copy()

print('Number of observations in subset 3')
print (len(subset3))

# Checking if S3AQ3C1 in subset2 is actually a number 
subset3['S3AQ3C1']=pandas.to_numeric(subset3['S3AQ3C1'])

# Frequency counts for S3AQ3C1
print('Counts for S3AQ3C1 - Usual quantity when smoked cigaretts')
c9 = subset3 ["S3AQ3C1"].value_counts(sort = True)
print (c9)

# Replaces all the 9 values with NaN.
subset3['S3AQ3C1'] = subset3['S3AQ3C1'].replace(99,numpy.nan)
print((subset3['S3AQ3C1'] == 99).sum())

# Print how many values are NaN
print(subset3['S3AQ3C1'].isnull().sum())

# Frequency counts for S3AQ3C1
print('Counts for S3AQ3C1 - Usual quantity when smoked cigaretts')
c10 = subset3 ["S3AQ3C1"].value_counts(sort = True, dropna = False)
print (c10)

# --------- Part 03 - S2AQ3 - S2AQ8A variables. ----------- # 
print('Counts for S2AQ3 - Drank at least 1 alcoholic drink in the last 12 months')
c11 = subset3 ["S2AQ3"].value_counts(sort = True)
print (c11)

print('Counts for S2AQ8A - How often drank any alcohol in the last 12 months')
c12 = subset3 ["S2AQ8A"].value_counts(sort = True)
print (c12)

# First see if there are any nulls. 
print((subset3['S2AQ8A'].isnull()).sum())

# Next see if there are any empty values. 
print((subset3['S2AQ8A']=="").sum())

# Next see if there are any that contain a space.
print((subset3['S2AQ8A']==" ").sum())

# Replacing the blank data with NaN
subset3['S2AQ8A']=subset3['S2AQ8A'].replace(' ', numpy.NaN)

print('Counts for S2AQ8A - How often drank any alcohol in the last 12 months')
c13 = subset3 ["S2AQ8A"].value_counts(sort = True, dropna = False)
print (c13)

# Or count the nulls.
print(subset3['S2AQ8A'].isnull().sum())

subset3.loc[(subset3['S2AQ3']!=9) & (subset3['S2AQ8A'].isnull()),'S2AQ8A'] = 11

print('Counts for S2AQ8A - How often drank any alcohol in the last 12 months')
c14 = subset3 ["S2AQ8A"].value_counts(sort = True, dropna = False)
print (c14)

# --------- Part 04 - Recoding Resposnes - S3AQ3B1 ----------- #
recode1 = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
subset2['USFREQ'] = subset2['S3AQ3B1'].map(recode1)
c15 = subset2 ['USFREQ'].value_counts(sort = True)
print (c15)

recode2 = { 1:30, 2:22, 3:14, 4:5, 5:2.5, 6:1}
subset2['USFREQMO'] = subset2['S3AQ3B1'].map(recode2)
c16 = subset2['USFREQMO'].value_counts(sort = True, dropna = False)
print (c16)

c17 = subset2 ['S3AQ3B1'].value_counts(sort = True)
print (c17)



























































