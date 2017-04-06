
# coding: utf-8

# # Q2_Part ONE
# - use employee_compensation dataset.
# - Calculate mean of total compensation for every department
# - Groupby the result with Organization droup with highest total compensation
# - Generate CSV with 3 columns(Organization Group, department and Total Compensation)

# In[1]:

import os
import pandas as pd
import numpy as np


# In[3]:

#getting current working directory
b = os.getcwd()

#reading the csv file
df = pd.read_csv(b+"\\"+"Data\\employee_compensation.csv", usecols=[3,5,21]) #, parse_dates=['DATE']), usecols=[0,1,3,19,20,21,22,23]) #usecols=[0,1,3]) #vehicle_collisions.csv, , delim_whitespace=True, , header=None


# In[4]:

#printing the first 5 rows of the dataset
df.head()


# In[5]:

#Calculating the mean of total compensation group by Organization and Department
AvgComp = df.groupby(['Organization Group','Department']).mean()
AvgComp.head()


# In[6]:

#resetting the index to bring hierarchical index to flat index
AvgComp = AvgComp.reset_index()
AvgComp.head()


# In[8]:

#sorting the value in descending order based on Total Compensation
AvgComp = AvgComp.sort_values(['Organization Group','Total Compensation'], ascending=[True,False])

AvgComp.head()


# In[9]:

#function to check is directory exists
def funCheckDir(path):
    directory = os.path.dirname(path) # defining directory path
    if not os.path.exists(directory): # checking if directory already exists
        os.makedirs(directory) # making a directory
        
resultsPath = b+"/Q2_Part_1.csv"
funCheckDir(resultsPath)

# Saving our result dataFrame to csv file.
AvgComp.to_csv(resultsPath, index=False, encoding='utf-8')


# In[ ]:



