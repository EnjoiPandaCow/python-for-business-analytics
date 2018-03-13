# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas
import numpy
import seaborn
import matplotlib.pyplot as plot

#set PANDAS to show all columns in Data frame
pandas.set_option('display.max_columns', None)

#set PANDAS to show all rows in Data frame
pandas.set_option('display.max_rows', None)

#load dataset from the csv file in the dataframe called nesarc_data
nesarc_data = pandas.read_csv('nesarc_pds.csv',low_memory=False)

#converting strings to numeric data for better output

nesarc_data['TAB12MDX'] = pandas.to_numeric(nesarc_data['TAB12MDX'],errors='ignore')
nesarc_data['CHECK321'] = pandas.to_numeric(nesarc_data['CHECK321'],errors='ignore')
nesarc_data['S3AQ3B1'] = pandas.to_numeric(nesarc_data['S3AQ3B1'], errors='ignore')
nesarc_data['S3AQ3C1'] = pandas.to_numeric(nesarc_data['S3AQ3C1'], errors='ignore')

#step 1
# restrict to those observations that are between 18 and 25 and smoke now
subset1 = nesarc_data[(nesarc_data['AGE']>=18) & (nesarc_data['AGE']<=25) & (nesarc_data['CHECK321']=='1')]


subset2 = subset1.copy()

#step 2 replacing missing data
#counts for S3AQ3B1
print('counts for S3AQ3B1 - usual frequency when smoked cigarettes')
c7= subset1['S3AQ3B1'].value_counts(sort=True)
print (c7)


#ensure the variable is number data type first
subset2['S3AQ3B1']=pandas.to_numeric(subset2['S3AQ3B1'])
#replace the value 9 in S3AQ3B1 with Nan to signify missing data

subset2['S3AQ3B1']=subset2['S3AQ3B1'].replace(9, numpy.NaN)

print((subset2['S3AQ3B1']==9).sum())
print(subset2['S3AQ3B1'].isnull().sum())

#counts for S3AQ3B1 after set to Nan
print(subset2.describe())
print('counts for S3AQ3B1 - usual frequency when smoked cigarettes')
c8= subset2['S3AQ3B1'].value_counts(sort=True, dropna=False)
print (c8)

#step 3 data management missing values
subset2['S2AQ3']=pandas.to_numeric(subset2['S2AQ3'])

c9=subset2['S2AQ3'].value_counts(sort=True, dropna=False)
print(c9)


c10=subset2['S2AQ8A'].value_counts(sort=True, dropna=False)
print(c10)

print((subset2['S2AQ8A']=="").sum())
print((subset2['S2AQ8A'].isnull()).sum())
print((subset2['S2AQ8A']==" ").sum())

subset2['S2AQ8A']=subset2['S2AQ8A'].replace(' ', numpy.NaN)

print(subset2['S2AQ8A'].isnull().sum())

subset2.shape
subset2.isnull().sum()

subset2.loc[(subset2['S2AQ3']!=9) & (subset2['S2AQ8A'].isnull()),'S2AQ8A']=11


print((subset2['S2AQ8A']==11).sum())

#step 4, recoding values

#first create the dictionary to recode
recode1= {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

#next use the map funciton to replace values using the recode dictionary
subset2['USFREQ'] = subset2['S3AQ3B1'].map(recode1)

#Now recode to a quantitative value based on an estimate of how many times per month each person smokes

recode2 = {1: 30, 2: 22, 3: 14, 4: 5, 5: 2.5, 6: 1}

subset2['USFREQMO'] = subset2['S3AQ3B1'].map(recode2)


c11=subset2['S3AQ3B1'].value_counts(sort=True, dropna=False)
print(c11)

c12=subset2['USFREQ'].value_counts(sort=True, dropna=False)
print(c12)

c13=subset2['USFREQMO'].value_counts(sort=True, dropna=False)
print(c13)

### ------------------------------------------------ Lab 06 Start Point ----------------------------------------------- ###
subset2['S3AQ3C1']=pandas.to_numeric(subset2['S3AQ3C1'])

subset2['NUMCIGMO_EST'] = subset2['USFREQMO']*subset2['S3AQ3C1']

subset3 = subset2[['IDNUM', 'S3AQ3C1', 'USFREQMO', 'NUMCIGMO_EST']]
subset3.head(25)

### ------------------------------------------------ Lab 07 Start Point ----------------------------------------------- ###
### --- Part 1 --- ###
print('Count')
count1 = subset2['NUMCIGMO_EST'].count()
print(count1)

print('Mean')
mean1 = subset2['NUMCIGMO_EST'].mean()
print(mean1)

print('Std Deviation') 
std1 = subset2['NUMCIGMO_EST'].std()
print(std1)

print('Min')
min1 = subset2['NUMCIGMO_EST'].min()
print(min1)

print('Max')
max1 = subset2['NUMCIGMO_EST'].max()
print(max1)

print('Median')
median1 = subset2['NUMCIGMO_EST'].median()
print(median1)

print('Mode')
mode1 = subset2['NUMCIGMO_EST'].mode()
print(mode1)

### --- Part 2 --- ###

# Converting categorical variables to a format Python recognises as categorical.
subset2['TAB12MDX'] = subset2['TAB12MDX'].astype('category')

# Counting both of the variables in TAB12MDX
seaborn.countplot(x='TAB12MDX', data=subset2)
# Adding the X label
plot.xlabel('Nicotine Dependence past 12 months')
# Adding the graph title
plot.title('Nicotine Dependence in the past 12 months amoung young adult smokers in the Nesarc study')

# Creating a graph for numberic data.
seaborn.distplot(subset2['NUMCIGMO_EST'].dropna(),kde=False)
plot.xlabel('Number of cigarettes per month')
plot.title('Estimated number of cigarettes per month among young adult smokers in the Nesarc study')

print('Group the variable NUMCIGMO_EST into bins')
subset2['NUMCIGMO_EST_BINS']=pandas.cut(subset2.NUMCIGMO_EST,[0, 200, 400, 600, 800, 1000, 4000], labels=['1-200', '200-400', '400-600', '600 - 800', '800 - 1000', '1000 - 4000'])
count2 = subset2['NUMCIGMO_EST_BINS'].value_counts(sort=False, dropna= True)
print(count2)

chart3 = seaborn.countplot(x='NUMCIGMO_EST_BINS', data=subset2)
plot.xlabel('Nicotine Dependence past 12 months by number of cigarettes')
plot.title('Nicotine Dependnce among young adults')

print ('describe number of cigarettes smoked per month')
desc1 = subset2['NUMCIGMO_EST'].describe()
print(desc1)

### --- Part 3 --- ###
subset2['PACKSPERMONTH'] = subset2['NUMCIGMO_EST']/20

c5 = subset2.groupby('PACKSPERMONTH').size()
print(c5)

subset2['PACKCATEGORY'] = pandas.cut(subset2.PACKSPERMONTH, [0,5,10,20,30,147])

#change format of variable from numerical to Categorical 
subset2['PACKCATEGORY'] = subset2['PACKCATEGORY'].astype('category')

print('Describe nicotine dependence')
desc3 = subset2.groupby('PACKCATEGORY').size()
print(desc3)

subset2['TAB12MDX'] = pandas.to_numeric(subset2['TAB12MDX'],errors='ignore')

#bivariate bar chart
seaborn.factorplot(x='PACKCATEGORY',y='TAB12MDX',data=subset2, kind='bar',ci=None)
plot.xlabel('Packs per month')
plot.ylabel('Proportion Nicotine Dependence')

















