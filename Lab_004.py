# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 09:54:44 2018

@author: CJ O'Sullivan
"""
# Importing data analysis packages. 
import pandas 
import numpy 
import seaborn
import matplotlib.pyplot as plot

# Set PANDAS to show all columns in Data frame
pandas.set_option('display.max_columns', None)

# Set PANDAS to show all rows in Data frame
pandas.set_option('display.max_rows', None)


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



## -------------------------------------- Lab 03 --------------------------------- ##

### --- Part 01 - Managing Data - Creating Secondary Variables - Combining Two Variables --- ###

# Multipling USFRWQMO * S3AQ3C1 to find the number of cigaretts smoked per month.
subset2['NUMCIGMO_EST'] = subset2['USFREQMO'] * subset2['S3AQ3C1']

# Macking sure S3AQ3C1 is a number 
subset2['S3AQ3C1'] = pandas.to_numeric(subset2['S3AQ3C1'])

# Creating a ouytput tha shows us only the variables we wish to see.
subset3=subset2[['IDNUM','S3AQ3C1','USFREQMO', 'NUMCIGMO_EST']]
subset3.head(25)

### --- Part 04 - Managing Data - Binning Variables --- ###

# Using QCut function to group ages into four quartiles.
print('AGE - 4 Categories - quartiles')
subset2['AGEGROUP'] = pandas.qcut(subset2.AGE, 4, labels=['1=25%tile','2=50%tile','3=75%tile','4=100%tile'])
c17 = subset2['AGEGROUP'].value_counts(sort=False, dropna=True)
print(c17)

# Categorise variable based on customised splits using the cut() functions,  splits into three groups, 18-20, 21-22, and 23-25
subset2['AGEGROUP2']= pandas.cut(subset2.AGE, [17, 20, 22, 25], labels=['18-20','21-22','23-25'])
c17 = subset2['AGEGROUP2'].value_counts(sort=False, dropna=True)
print(c17)

# Printing a cross tab on the AGEGROUP2 variable
print(pandas.crosstab(subset2['AGEGROUP2'],subset2['AGE']))




## -------------------------------------- Lab 04 --------------------------------- ##

### --- Part 01 - Descriptive Statistics --- ###

#counts for TAB12MDX
print('count of TAB12MDX')
c1 = subset2.groupby('TAB12MDX').size()
print(c1)
print('same count different function used')
c2 = subset2['TAB12MDX'].value_counts(sort=False, dropna=True)
print(c2)

#percentages for TAB12MDX
print('percentages of counts')
p1 = subset2.groupby('TAB12MDX').size() * 100 /len(nesarc_data)
print(p1)

#counts for NUMCIGMO_EST
print('count of TAB12MDX')
c3 = subset2.groupby('NUMCIGMO_EST').size()
print(c3)
print('same count different function used')
c4 = subset2['NUMCIGMO_EST'].value_counts(sort=False, dropna=True)
print(c4)

#percentages for NUMCIGMO_EST
print('percentages of counts')
p2 = subset2.groupby('NUMCIGMO_EST').size() * 100 /len(nesarc_data)
print(p2)


#univariate graphing
bc1 = seaborn.countplot(x='TAB12MDX',data=subset2)
plot.xlabel('Nicotine Dependence past 12 months')
plot.title('Nicotine Dependence in the past 12 months among young adult smokers in the Nesarc study')


bc2 = seaborn.distplot(subset2['NUMCIGMO_EST'].dropna(),kde=False)
plot.xlabel('Number of cigarettes per month')
plot.title('Estimated number of cigarettes per month among young adult smokers in the Nesarc study')

### --- Part 02 - Univariate Graphing --- ###

#categorise variable based on customised splits using the cut() function
# splits into 6 groups, 1-200, 200-400, 400-600, 600-800, 800-1000, 1000-4000
print('Group the variable NUMCIGMO_EST into bins')
subset2['NUMCIGMO_EST_BINS'] = pandas.cut(subset2.NUMCIGMO_EST, [0,200,400,600,800,1000,4000], labels=['1-200','200-400','400-600','600-800','800-1000','1000-4000'])
c4 = subset2['NUMCIGMO_EST_BINS'].value_counts(sort=False,dropna=True)
print(c4)

# Generating Graph showing nicotine dependnce amoung young adults
bc3= seaborn.countplot(x='NUMCIGMO_EST_BINS', data=subset2)
plot.xlabel('Nicotine Dependence past 12 months by number of cigarettes')
plot.title('Nicotine Dependnce among young adults')

### --- Part 03 - Graphing DCategorical Response Variables --- ###

# Deviding NUMCIGMO_EST by 20 to estimate the PACKSPERMONTH
subset2['PACKSPERMONTH'] = subset2['NUMCIGMO_EST'] / 20

# The amount of packs people smoke in a month
c5 = subset2.groupby('PACKSPERMONTH').size()
print(c5)

# Dividing packs per month into groups
subset2['PACKCATEGORY'] = pandas.cut(subset2.PACKSPERMONTH, [0,5,10,20,30,147])

# Changing format of PACKCATEGORY to categorical. 
subset2['PACKCATEGORY'] = subset2['PACKCATEGORY'].astype('category')

# Gettiung a count of people per bin.
print('describe nicotine dependence')
count1 = subset2.groupby('PACKCATEGORY').size()
print(count1)

# Converting TAB12MDX to numeric 
subset2['TAB12MDX'] = pandas.to_numeric(subset2['TAB12MDX'],errors='ignore')

# Creating bivariate car chat for PACKCATEGORY & TAB12MDX 
seaborn.factorplot(x='PACKCATEGORY', y='TAB12MDX', data=subset2, kind='bar', ci=None)
plot.xlabel('Packs per month')
plot.ylabel('Proportion Nicotine Dependence')

### --- Part 04 - Bivariate graph with response variable containing more than 2 categories. --- ###

# Creating a new variable called SMOKEGRP
def SMOKEGRP (row):
  if row['TAB12MDX'] == 1:
    return 1
  elif row['USFREQMO'] == 30:
    return 2
  else:
    return 3

subset2['SMOKEGRP'] = subset2.apply(lambda row: SMOKEGRP (row), axis=1)

# Count the occurance of the values in SMOKEGROUPS
c21=subset2['SMOKEGRP'].value_counts(normalize=True)
print(c21)

# Graphing the smkoking groups.
bc1 = seaborn.countplot(x='SMOKEGRP',data=subset2)
plot.xlabel('Smoking Groups')

# Collapsing the variable into daily and non-daily smokers 
def DAILY (row): 
    if row['USFREQMO'] == 30:
        return 1
    elif row['USFREQMO'] != 30:
        return 0

subset2['DAILY'] = subset2.apply(lambda row: DAILY (row), axis=1)

# Counting daily and non daily smokers
c22 = subset2.groupby('DAILY').size()
print(c22)

# Converting the ETHRACE2A to a categorical variable.
subset2['ETHRACE2A'] = subset2['ETHRACE2A'].astype('category')

# Relaybalying the x axis.
subset2['ETHRACE2A'] = subset2['ETHRACE2A'].cat.rename_categories(['White','Black','NatAm','Asian','Hispanic'])

# Graphing the proportion of smokers for each ethnic race.
seaborn.factorplot(x='ETHRACE2A', y='DAILY', data=subset2, kind='bar', ci=None)
plot.xlabel('Ethnic Group')
plot.ylabel('Proportion Daily Smokers')


























