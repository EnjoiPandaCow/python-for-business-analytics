import pandas 
import numpy 

nesarc_data=pandas.read_csv('nesarc_pds.csv',low_memory=False)

pandas.set_option('display.float_format',lambda x:'%f'%x)

nesarc_data.columns = map(str.upper, nesarc_data.columns)
nesarc_data.columns = map(str.lower, nesarc_data.columns)

nesarc_data['S3AQ3C1'] = pandas.to_numeric(nesarc_data['S3AQ3C1'],errors='coerce')

print(len(nesarc_data))
print(len(nesarc_data.columns))

print('counts for TAB12MDX - nicotine dependence in the past 12 months, yes=1')
c1=nesarc_data["TAB12MDX"].value_counts(sort=False)
print(c1)

print('percentages for TAB12MDX - nicotine dependence in the past 12 months, yes=1')
p1=nesarc_data["TAB12MDX"].value_counts(sort=False, normalize=True)
print(p1)

print('counts for CHECK321 - smoked in the past year yes=1')
c2=nesarc_data["CHECK321"].value_counts(sort=False)
print(c2)

print('percentages for CHECK321 - smoked in the past year yes=1')
p2=nesarc_data["CHECK321"].value_counts(sort=False, normalize=True)
print(p2)

print('counts for S3AQ3B1 - usual frequency when smoking cigarettes')
c3=nesarc_data["S3AQ3B1"].value_counts(sort=False)
print(c3)

print('percentages for S3AQ3B1 - usual frequency when smoking cigarettes')
p3=nesarc_data["S3AQ3B1"].value_counts(sort=False, normalize=True)
print(p3)

print('counts for S3AQ3C1 - usual quantity when smoking cigarettes')
c4=nesarc_data["S3AQ3C1"].value_counts(sort=False)
print(c4)

print('percentages for S3AQ3C1 - usual quantity when smoking cigarettes')
p4= nesarc_data["S3AQ3C1"].value_counts(sort=False, normalize=True)
print(p4)

ct1 = nesarc_data.groupby('TAB12MDX').size()
print(ct1)