#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df4 = pd.read_excel("/mnt/c/Users/rache/Downloads/GSAF5.xls")
#https://www.geeksforgeeks.org/python/reading-excel-file-using-python/

pd.set_option('display.max_rows', None)

# Optional: show all columns too
pd.set_option('display.max_columns', None)

#print(df4.columns)
length=len(df4['Time'])
print(length)

c=df4.isna().sum()
print(c)

df4 = df4.drop(['Unnamed: 21', 'Unnamed: 22'], axis=1)
print(df4.columns)


print(df4['Year'].unique())

print(df4['Year'].head(20))

# I see a range of values going from 0000-2025. To clean the column, I did the following code to remove missing values.
df4['Year'] = df4['Year'].replace(' ',np.nan)
filtered_df4 = df4[df4['Year'] > 1940]
print(filtered_df4['Year'].unique())

#https://www.geeksforgeeks.org/pandas/ways-to-filter-pandas-dataframe-by-column-values/
filtered_df4['Year'].hist(bins=50)
plt.show()

plt.savefig("year_hist.png")
# i did a histogram and judging from the histogram, the shark attacks are increasing as the years progress

filtered_df4['Age'] = filtered_df4['Age'].replace([' ','nan','NA','N/A'], np.nan)
filtered_df4['Age'] = pd.to_numeric(filtered_df4['Age'], errors='coerce')
filtered_df4['Age'].hist(bins=50)
plt.show()

plt.savefig("AGE_histo.png")


print(filtered_df4['Age'].describe())
print(filtered_df4['Age'].unique())

print(len(filtered_df4[filtered_df4['Sex']=='M']))
print(len(filtered_df4[filtered_df4['Sex']=='F']))

x=len(df4[df4['Sex']=='M'])
y=len(df4[df4['Sex']=='F'])
print(x/(x+y))
#male is 4311/5026, and the 5026 comes from just entries of "M" or "F" (for the 1940 filtered data)
#male proportion is .88 for the unfiltered data
print(df4['Type'].unique())

df4['Type'] = df4['Type'].replace(['Watercraft', 'Sea Disaster','Boat','unprovoked'], 'Unprovoked')
df4['Type'] = df4['Type'].replace(' Provoked', 'Provoked')
df4['Type'] = df4['Type'].replace(['Questionable','?','Unconfirmed','Unverified','Invalid','Under investigation'], 'Unknown')
df4['Type'] = df4['Type'].replace([' ', 'nan'], np.nan)
print(df4['Type'].unique())

a=len(df4['Type'])
b=len(df4[df4['Type']=='Unprovoked'])
ratio=b/a
print(ratio)

# 0.82 of the attacks were unprovoked

print(df4['Fatal Y/N'].unique())


df4['Fatal Y/N']=df4['Fatal Y/N'].replace(['F','M','Nq','UNKNOWN',2017,'Y x 2'],np.nan)
df4['Fatal Y/N']=df4['Fatal Y/N'].replace(['n',' N', 'N '], 'N')
df4['Fatal Y/N']=df4['Fatal Y/N'].replace('y','Y')

print(df4['Fatal Y/N'].unique())

q1=df4[['Type','Sex']]
q2=df4[['Type','Fatal Y/N']]
q3=df4[['Fatal Y/N', 'Sex']]

print(len(q1[(q1['Type']=='Unprovoked') & (q1['Sex']=='M')]))
print(len(q1[(q1['Type']=='Unprovoked') & (q1['Sex']=='F')]))
# there are much more males with unprovoked shark attacks than females

print(len(q2[(q2['Type']=='Unprovoked') & (q2['Fatal Y/N']=='Y')]))
print(len(q2[(q2['Type']=='Provoked') & (q2['Fatal Y/N']=='Y')]))
#it is more likely to be fatal when it is unprovoked (1441 vs. 21)

print(len(q3[(q3['Sex']=='M') & (q3['Fatal Y/N']=='Y')]))
print(len(q3[(q3['Sex']=='F') & (q3['Fatal Y/N']=='Y')]))
# it is more likely to be fatal when it is a male

# I still don't like sharks but I feel better because I am a female

gw=df4['Species '].str.count('Great White')
print(gw.count())
gw1=df4['Species '].str.count('white')
gw2=df4['Species '].str.count('great')
print(gw1.count())
print(gw2.count())
# all of these print statements produced 3911

print(len(df4['Species ']))
# 3911/7042 is the proportion of attacks from white sharks 
