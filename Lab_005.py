# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 18:06:24 2018

@author: CJ O'Sullivan
"""
import pandas 
import numpy 
import seaborn
import matplotlib.pyplot as plot

# Set PANDAS to show all columns in Data frame
pandas.set_option('display.max_columns', None)

# Set PANDAS to show all rows in Data frame
pandas.set_option('display.max_rows', None)

# Importing nesarc csv file.
gapminder = pandas.read_csv('gapminder.csv', low_memory=False)

## -------------------------------------- Lab 01 --------------------------------- ##

### --- Part 01 - Exercise --- ###

# Making sure that the variable urbanrate is numeric. 
gapminder['urbanrate']=pandas.to_numeric(gapminder['urbanrate'])

# Checking for null's in urbanrate
print((gapminder['urbanrate'].isnull()).sum())

# Checking for empty values in urbanrate
print((gapminder['urbanrate']=="").sum())

# Checking for values that contain a space in urbanrate
print((gapminder['urbanrate']==" ").sum())

# Replacing blank data with NaN
gapminder['urbanrate']=gapminder['urbanrate'].replace(' ', numpy.NaN)

desc1 = gapminder['urbanrate'].describe()
print(desc1)

# Making sure that the variable internetuserate is numeric. 
gapminder['internetuserate']=pandas.to_numeric(gapminder['internetuserate'])

# Checking for null's in internetuserate
print((gapminder['internetuserate'].isnull()).sum())

# Checking for empty values in internetuserate
print((gapminder['internetuserate']=="").sum())

# Checking for values that contain a space in internetuserate
print((gapminder['internetuserate']==" ").sum())

# Replacing blank data with NaN
gapminder['internetuserate']=gapminder['internetuserate'].replace(' ', numpy.NaN)

desc2 = gapminder['internetuserate'].describe()
print(desc2)

### --- Part 02 - Graphing Scatterplot --- ###

# Graphing a basic scatter plot. 
scat1 = seaborn.regplot(x="urbanrate", y="internetuserate", fit_reg=True, data=gapminder)
plot.xlabel('Urban Rate')
plot.ylabel('Internet Use Rate')
plot.title('Scatterplot for the Association between Urban Rate and Internet Use Rate')

# Making sure that the variable incomeperperson is numeric. 
gapminder['incomeperperson']=pandas.to_numeric(gapminder['incomeperperson'])

# Checking for null's in incomeperperson
print((gapminder['incomeperperson'].isnull()).sum())

# Checking for empty values in incomeperperson
print((gapminder['incomeperperson']=="").sum())

# Checking for values that contain a space in incomeperperson
print((gapminder['incomeperperson']==" ").sum())

# Replacing blank data with NaN
gapminder['incomeperperson']=gapminder['incomeperperson'].replace(' ', numpy.NaN)

desc3 = gapminder['incomeperperson'].describe()
print(desc3)

# Graphing a basic scatter plot. 
scat2 = seaborn.regplot(x="incomeperperson", y="internetuserate", fit_reg=True, data=gapminder)
plot.xlabel('Income per person')
plot.ylabel('Internet Use Rate')
plot.title('Scatterplot for the Association between Income Per Person and Internet Use Rate')

### --- Part 03 - Graphing Scatterplot --- ###

# Making sure that the variable hivrate is numeric. 
gapminder['hivrate']=pandas.to_numeric(gapminder['hivrate'])

# Checking for values that contain a space in hivrate
print((gapminder['hivrate']==" ").sum())

# Replacing blank data with NaN
gapminder['hivrate']=gapminder['hivrate'].replace(' ', numpy.NaN)

desc4 = gapminder['hivrate'].describe()
print(desc4)

# Graphing a basic scatter plot. 
scat2 = seaborn.regplot(x="incomeperperson", y="hivrate", fit_reg=True, data=gapminder)
plot.xlabel('Income per person')
plot.ylabel('HIV Rate')
plot.title('Scatterplot for the Association between Income Per Person and HIV Rate')

# Using QCut function to group INCOME into four quartiles.
gapminder['incomegrp4'] = pandas.qcut(gapminder.incomeperperson, 4, labels=['1=25%tile','2=50%tile','3=75%tile','4=100%tile'])
c17 = gapminder['incomegrp4'].value_counts(sort=False, dropna=True)
print(c17)

#bivariate bar graph C->Q
seaborn.factorplot(x='incomegrp4',y='hivrate',data=gapminder,kind='bar',ci=None)
plot.xlabel('income group')
plot.ylabel('mean HIV rate')
















