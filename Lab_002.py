# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 09:54:44 2018

@author: CJ O'Sullivan
"""
# Importing data analysis packages. 
import pandas 
import numpy 

# Importing nesarc csv file.
nesarc_data = pandas.read_csv('nesarc_pds.csv', low_memory=False)

## -------------------------------------- Lab 01 --------------------------------- ##

### --- Part 03 --- ###

# Number of observations (rows) in the dataset.
print('Number of rows in the dataset.')
print(len(nesarc_data))

# Number of variables (columns) in the dataset.
print('Number of columns in the dataset.')
print(len(nesarc_data.columns))

### --- Part 04 --- ### 

# Generating frequency distribution for TAB12MDX
print('counts for TAB12MDX - nicotine dependence in the past 12 months, yes=1')
count1 = nesarc_data["TAB12MDX"].value_counts(sort=False)
print(count1)

print('percentages for TAB12MDX - nicotine dependence in the past 12 months, yes=1')
percentage1 = nesarc_data['TAB12MDX'].value_counts(sort=False, normalize=True)
print(percentage1)

### --- Part 05 --- ### 

# Generating frequency distribution for CHECK321
print('counts for CHECK321 - smoked in the past year, yes=1')
count2 = nesarc_data["CHECK321"].value_counts(sort=False)
print (count2)

print('percentages for CHECK321 - smoked in the past year, yes=1')
percentage2 = nesarc_data["CHECK321"].value_counts(sort=False, normalize=True)
print (percentage2)

# Generating frequency distribution for S3AQ3B1
print('counts for S3AQ3B1 - usual frequency when smoked cigarettes')
count3= nesarc_data["S3AQ3B1"].value_counts(sort=True)
print (count3)

print('percentages for S3AQ3B1 - usual frequency when smoked cigarettes')
percentage3= nesarc_data["S3AQ3B1"].value_counts(sort=True, normalize=True)
print (percentage3)

# Generating frequency distribution for S3AQ3B1
print('counts for S3AQ3C1 - usual quanitity when smoked cigarettes')
count4= nesarc_data["S3AQ3C1"].value_counts(sort=True)
print (count4)

print('percentages for S3AQ3C1 - usual quanitity when smoked cigarettes')
percentage4= nesarc_data["S3AQ3C1"].value_counts(sort=True, normalize=True)
print (percentage4)



## -------------------------------------- Lab 02 --------------------------------- ##

### --- Part 01 - Selecting Rows --- ###

# Reducing the size of the dataset to 18 - 25 year olds.
print('The number of rows in the subset of adults between 18 and 25 that have smoked in the past 12 months')
subset1 = nesarc_data[(nesarc_data['AGE']>=18) & (nesarc_data['AGE']<=25) & (nesarc_data['CHECK321']=='1')]
print(len(subset1))

# Printing the counts for the AGE variable.
print('counts for AGE ')
c1 = subset1['AGE'].value_counts(sort=True)
print (c1)

# Printing the percentages for the AGE variable.
print('percentages for AGE ')
c2 = subset1['AGE'].value_counts(sort=True, normalize=True)
print (c2)

# Counting 18 - 25 year olds who have snoked in the past 12 months. 
print('The count of those who have smoked in the past 12 months')
c6=subset1['CHECK321'].value_counts(sort='TRUE')
print(c6)

# Copying subset1 to subset2 
subset2 = subset1.copy()

# Printing the length of subset 2.
print('Number of observations in subset 2')
print (len(subset2))

### --- Part 02 - Missing Data --- ###

# Making sure that the variable S3AQ3B1 in subset2 is actually a number. 
subset2['S3AQ3B1']=pandas.to_numeric(subset2['S3AQ3B1'])

# Frequency counts for S3AQ3B1
print('counts for S3AQ3B1 - usual frequency when smoked cigarettes')
c7= subset2["S3AQ3B1"].value_counts(sort=True)
print (c7)

# Replacing the 9 values with NaN using the Numpy library.
subset2['S3AQ3B1']=subset2['S3AQ3B1'].replace(9,numpy.nan)

# Checking to see if there is any values equal to 9 still remaning.
print((subset2['S3AQ3B1']==9).sum())

# Checking how many varables are NaN or null. 
print(subset2['S3AQ3B1'].isnull().sum())

# Frequency counts for S3AQ3B1 without 9 value.
print('counts for S3AQ3B1 - usual frequency when smoked cigarettes')
c8= subset2['S3AQ3B1'].value_counts(sort=True, dropna=False)
print (c8)

### --- Part 03 - Retriving Useful Data --- ###

# Making sure that the variable S3AQ3C1 in subset2 is actually a number. 
subset2['S3AQ3C1']=pandas.to_numeric(subset2['S3AQ3C1'])

# Frequency counts for S3AQ3C1
print('counts for S3AQ3C1 - usual quantity when smoked cigarettes')
c8= subset2["S3AQ3C1"].value_counts(sort=True)
print (c8)

# Replacing the 99 values with NaN using the Numpy library.
subset2['S3AQ3C1']=subset2['S3AQ3C1'].replace(99,numpy.nan)

# Checking to see if there is any values equal to 9 still remaning.
print((subset2['S3AQ3C1']==99).sum())

# Checking how many varables are NaN or null. 
print(subset2['S3AQ3C1'].isnull().sum())

# Frequency counts for S3AQ3C1 without 99 value.
print('counts for S3AQ3C1 - usual qunatity when smoked cigarettes')
c9= subset2['S3AQ3C1'].value_counts(sort=True, dropna=False)
print (c9)

# Frequency counts for S2AQ3.
print('counts for S2AQ3 - drank at least one alcoholic drink in the past 12 months')
c10= subset2['S2AQ3'].value_counts(sort=True, dropna=False)
print (c10)

# Frequency counts for S2AQ8A.
print('counts for S2AQ8A - how often drink any alcohol in the past 12 months')
c11= subset2['S2AQ8A'].value_counts(sort=True, dropna=False)
print (c11)

# Checking for null's in S2AQ8A
print((subset2['S2AQ8A'].isnull()).sum())

# Checking for empty values in S2AQ8A
print((subset2['S2AQ8A']=="").sum())

# Checking for values that contain a space in S2AQ8A
print((subset2['S2AQ8A']==" ").sum())

# Replacing blank data with NaN
subset2['S2AQ8A']=subset2['S2AQ8A'].replace(' ', numpy.NaN)

# Frequency counts for S2AQ8A with NaN.
print('counts for S2AQ8A - how often drink any alcohol in the past 12 months')
c12= subset2['S2AQ8A'].value_counts(sort=True, dropna=False)
print (c12)

# Replacing NaN in S2AQ8A with 11 if S2AQ3 is also not equal to 9. 
subset2.loc[(subset2['S2AQ3']!=9) & (subset2['S2AQ8A'].isnull()),'S2AQ8A']=11

# Frequency counts for S2AQ8A with 11 option added.
print('counts for S2AQ8A - how often drink any alcohol in the past 12 months')
c13= subset2['S2AQ8A'].value_counts(sort=True, dropna=False)
print (c13)

### --- Part 04 - Recoding Responses --- ###

# Building a dictionary that recodes each value.
recode1= {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

# Using the map function to point to recode1 and applying it to S3AQ3B1. Creating the new variable USFREQ
subset2['USFREQ'] = subset2['S3AQ3B1'].map(recode1)

# Building a dictionary that recodes each value.
recode2 = {1: 30, 2: 22, 3: 14, 4: 5, 5: 2.5, 6: 1}

# Using the map function to point to recode2 and applying it to S3AQ3B1. Creating the new variable USFREQMO
subset2['USFREQMO'] = subset2['S3AQ3B1'].map(recode2)

# Frequency counts for S3AQ3B1.
print('counts for S3AQ3B1 - usual frequency when smoked cigarettes')
c14= subset2['S3AQ3B1'].value_counts(sort=True, dropna=False)
print (c14)

# Frequency counts for USFREQ.
print('counts for USFREQ - usual frequency when smoked cigarettes')
c15= subset2['USFREQ'].value_counts(sort=True, dropna=False)
print (c15)

# Frequency counts for USFREQMO.
print('counts for USFREQMO - usual frequency when smoked cigarettes')
c16= subset2['USFREQMO'].value_counts(sort=True, dropna=False)
print (c16)













































