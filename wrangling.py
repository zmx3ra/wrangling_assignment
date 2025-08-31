#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("data/airbnb_hw.csv") #importing the data airbnb



#print("df.shape:")
#print(df.shape, '\n') # List the dimensions of df

#print("df.dtypes:")
#print(df.dtypes, '\n') # The types of the variables; `object` is a bad sign

#print("df.columns:")
#print(df.columns, '\n')

pd.set_option('display.max_rows', None)

# Optional: show all columns too
pd.set_option('display.max_columns', None)



x=df.isnull()
#print(x)
#https://www.geeksforgeeks.org/data-analysis/working-with-missing-data-in-pandas/ (citations for my work, it printed out no null values)

# there are some commas when the price goes over 1,000, so we need to remove these commas so the variable is numeric

#df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Price']=df['Price'].str.replace(",", "") #removing the commas, did a print statement later to check and the comma was gone


# Part 2

df2=pd.read_csv("data/mn_police_use_of_force.csv") #reading in the second dataset


df2['subject_injury'] = df2['subject_injury'].replace(' ',np.nan) #replacing the missing values with np.nan
#print(df2.head(50)) #shows the NaNs are in there
na=(df2['subject_injury'].isna().sum())
length=len(df2['subject_injury'])
#print(na/length)
# equals .76; this is concerning because there are a lot of missing values, and this column only has 1/4 actual data. it is not very reliable.
#https://stackoverflow.com/questions/26266362/how-do-i-count-the-nan-values-in-a-column-in-pandas-dataframe
#print(df2['subject_injury'].sum())

#print(pd.crosstab(df2['subject_injury'],df2['force_type']))
# baton, firearms, less lethal projectiles are the very concerning ones because they don't have many issues


# Question 3
url = 'http://www.vcsc.virginia.gov/pretrialdataproject/October%202017%20Cohort_Virginia%20Pretrial%20Data%20Project_Deidentified%20FINAL%20Update_10272021.csv'
df3 = pd.read_csv(url,low_memory=False)



#NA=(df3['WhetherDefendantWasReleasedPretrial'].isna().sum())
#print(NA)
#print(df3['WhetherDefendantWasReleasedPretrial'].unique())
# both of these codes showed that 1) there were no NA values, and 2) there is a 9 in the data column so we need to remove that
#df3['WhetherDefendantWasReleasedPretrial']=df3['WhetherDefendantWasReleasedPretrial'].replace('9',np.nan) #this will replace the 9 with an NAN


# Part 4


df3['ImposedSentenceAllChargeInContactEvent'] = df3['ImposedSentenceAllChargeInContactEvent'].replace(' ',np.nan)

df3['ImposedSentenceAllChargeInContactEvent']=pd.to_numeric(df3['ImposedSentenceAllChargeInContactEvent'], errors='coerce')

#here, I am getting rid of the blank values and coercing it to numeric
print(df3['ImposedSentenceAllChargeInContactEvent'].head(20))
# checking to see if NANs are in the right spots
