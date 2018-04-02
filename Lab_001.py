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


