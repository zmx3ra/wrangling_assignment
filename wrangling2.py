#!/usr/bin/env python3

# Question 2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# importing the necessary packages 

# Part 1
df4 = pd.read_excel("/mnt/c/Users/rache/Downloads/GSAF5.xls") #reading in the file
#https://www.geeksforgeeks.org/python/reading-excel-file-using-python/

pd.set_option('display.max_rows', None)


pd.set_option('display.max_columns', None)
#https://builtin.com/data-science/pandas-show-all-columns

#Part 2
#print(df4.columns)
length=len(df4['Time'])
print(length)

c=df4.isna().sum()
print(c)
# i dropped the unnamed columns because they weren't in the excel dataset and I wasn't sure what they meant, otherwise all of the columns had data in them

df4 = df4.drop(['Unnamed: 21', 'Unnamed: 22'], axis=1)
print(df4.columns)
#https://www.geeksforgeeks.org/python/how-to-drop-one-or-multiple-columns-in-pandas-dataframe/

#Part 3
print(df4['Year'].unique())

print(df4['Year'].head(20))

# I see a range of values going from 0000-2025. To clean the column, I did the following code to remove missing values.
df4['Year'] = df4['Year'].replace(' ',np.nan)
filtered_df4 = df4[df4['Year'] > 1939]
print(filtered_df4['Year'].unique())


#https://www.geeksforgeeks.org/pandas/ways-to-filter-pandas-dataframe-by-column-values/
filtered_df4['Year'].hist(bins=50)
plt.show()

plt.savefig("year_hist.png")
# i did a histogram and judging from the histogram, the shark attacks are increasing as the years progress

# Part 4
df4['Age'] = pd.to_numeric(df4['Age'], errors='coerce') # Coerce the variable to numeric

# Create a missing dummy:
df4['age_nan'] = df4['Age'].isnull()
df4['Age'] = df4['Age'].replace([' ','nan','NA','N/A'], np.nan)

df4['Age'].hist(bins=50)
plt.show()
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
# from the histogram, it appears the ages with the higher shark attacks is 20-30s

plt.savefig("AGE.png")
# saving the histogram to a picture

#Part 5


x=len(df4[df4['Sex']=='M'])
y=len(df4[df4['Sex']=='F'])
print(x/(x+y))

#male proportion is .88 for the unfiltered data

# Part 6

print(df4['Type'].unique()) #seeing all the unique types of entries in the column

df4['Type'] = df4['Type'].replace(['Watercraft', 'Sea Disaster','Boat','unprovoked'], 'Unprovoked')
df4['Type'] = df4['Type'].replace(' Provoked', 'Provoked')
df4['Type'] = df4['Type'].replace(['Questionable','?','Unconfirmed','Unverified','Invalid','Under investigation'], 'Unknown')
df4['Type'] = df4['Type'].replace([' ', 'nan'], np.nan)
print(df4['Type'].unique())
#this is me removing the extra words and narrowing it down to three different categories, and I did a print statement to check my work

a=len(df4['Type'])
b=len(df4[df4['Type']=='Unprovoked'])
ratio=b/a
print(ratio)

# 0.82 of the attacks were unprovoked

#Part 7

print(df4['Fatal Y/N'].unique()) #seeing the unique values in the column


df4['Fatal Y/N']=df4['Fatal Y/N'].replace(['F','M','Nq','UNKNOWN',2017,'Y x 2'],np.nan)
df4['Fatal Y/N']=df4['Fatal Y/N'].replace(['n',' N', 'N '], 'N')
df4['Fatal Y/N']=df4['Fatal Y/N'].replace('y','Y')

print(df4['Fatal Y/N'].unique())
# cleaning the column with .replace and then checking my work to make sure there are only Y or N

#Part 8

q1=df4[['Type','Sex']]
q2=df4[['Type','Fatal Y/N']]
q3=df4[['Fatal Y/N', 'Sex']]
# making three subsets
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

# Part 9

gw=df4['Species '].str.count('Great White')
print(gw.count())
gw1=df4['Species '].str.count('white')
gw2=df4['Species '].str.count('great')
print(gw1.count())
print(gw2.count())
# all of these print statements produced 3911
# https://www.w3schools.com/python/ref_string_count.asp
print(len(df4['Species ']))
# 3911/7042 is the proportion of attacks from white sharks 
