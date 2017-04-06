
# coding: utf-8

# # Q1_Part TWO
# 
# - use vehicle_collision data.
# - For each borough, find out distribution of each collision scale. (One car involved? Two? Three? or more?) (From 2015 to present)
# - Display a few rows of the output use df.head().
# - Generate a csv output with five columns ('borough', 'one-vehicle', 'two-vehicles','three-vehicles', 'more-vehicles')

# In[36]:

#from pandas import Series, DataFrame
import os
import pandas as pd


# In[37]:

#getting current working directory
b = os.getcwd()


#reading the csv file
df = pd.read_csv(b+"\\"+"Data\\vehicle_collisions.csv", parse_dates=['DATE'], usecols=[0,1,3,19,20,21,22,23]) #vehicle_collisions.csv, , delim_whitespace=True, , header=None


# In[39]:

df.head()


# In[63]:

df['DATE'] = pd.to_datetime(df.DATE)
#df


# In[64]:

# getting data from the year of 2015 until now and storing it in new dataframe
df_2015 = df[df.DATE.dt.year >= 2015]
#df_2015


# In[65]:

dfl = df[['UNIQUE KEY','BOROUGH']]
dfv = df[['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]
dfv = dfv.notnull()
dfv = dfv.applymap(lambda x:1 if x else 0)
new_df = pd.concat([dfl,dfv],axis=1)

new_df.head()


# In[66]:

dfc = new_df.groupby('BOROUGH').sum()
dfc.head()


# In[67]:

#Calculate number of vehicles
dfc['ONE_VEHICLE_INVOLVED'] =  dfc['VEHICLE 1 TYPE']-dfc['VEHICLE 2 TYPE']

dfc['TWO_VEHICLES_INVOLVED'] =  dfc['VEHICLE 2 TYPE']-dfc['VEHICLE 3 TYPE']

dfc['THREE_VEHICLES_INVOLVED'] =  dfc['VEHICLE 3 TYPE']-dfc['VEHICLE 4 TYPE']


dfc['MORE_VEHICLES_INVOLVED'] = dfc['VEHICLE 4 TYPE'] + dfc['VEHICLE 5 TYPE'] - dfc['VEHICLE 5 TYPE']

dfc = dfc[['ONE_VEHICLE_INVOLVED','TWO_VEHICLES_INVOLVED','THREE_VEHICLES_INVOLVED','MORE_VEHICLES_INVOLVED']]
dfc.head()


# In[70]:

#function to check is directory exists
def funCheckDir(path):
    directory = os.path.dirname(path) # defining directory path
    if not os.path.exists(directory): # checking if directory already exists
        os.makedirs(directory) # making a directory
        
resultsPath = b+"/Q1_Part_2.csv"
funCheckDir(resultsPath)

# Saving our dataFrame to csv file.
#Percent_df[Columns].to_csv(resultsPath, index=False, encoding='utf-8')
dfc.to_csv(resultsPath, index=True, encoding='utf-8')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[14]:



