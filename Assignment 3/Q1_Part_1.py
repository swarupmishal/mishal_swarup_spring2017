
# coding: utf-8

# # Q1_Part ONE
# 
# - use vehicle_collision data.
# - For each month in 2016 calculate:
#     - Total accidents in NYC
#     - Total accidents in Manhattan
#     - Calculate the percentage of accidents in Manhattan over total in NYC
# - Generate CSV with 4 columns(Month, Manhattan, NYC, %)

# In[2]:

#from pandas import Series, DataFrame
import os
import pandas as pd


# In[3]:

#getting current working directory
b = os.getcwd()


#reading the csv file
df = pd.read_csv(b+"\\"+"Data\\vehicle_collisions.csv", parse_dates=['DATE'], usecols=[0,1,3]) #vehicle_collisions.csv, , delim_whitespace=True, , header=None


# In[4]:

#printing first 5 columns of the data frame
df.head(5)


# In[5]:

# getting data for only the year of 2016 and storing it in new dataframe
df_2016 = df[df.DATE.dt.year == 2016]

df_2016[:5]


# In[6]:

# Offsetting the warning
pd.options.mode.chained_assignment = None

# Extract month for each date in the dataframe containing 2016 data
df_2016['Month'] = df_2016['DATE'].dt.strftime('%b')

#gives the month in numbers
#df_2016['Month'] = pd.DatetimeIndex(df_2016['DATE']).month

df_2016.head()


# In[7]:

# counting the number of accidents in NYC by grouping it with months
NYC_Data = df_2016['UNIQUE KEY'].groupby(df_2016['Month']).count()

NYC_Data


# In[8]:

# Sorting month according to calendar
NYC_Data.index = pd.CategoricalIndex(NYC_Data.index, 
                               categories=['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'], 
                               sorted=True)
NYC_Data = NYC_Data.sort_index()

NYC_Data


# In[9]:

# grouping Data by month and counting the number of accidents in Manhattan
Manhattan_Data = df_2016['UNIQUE KEY'][df_2016['BOROUGH'] == "MANHATTAN"].groupby(df_2016['Month']).count()

# Sorting month according to calendar
Manhattan_Data.index = pd.CategoricalIndex(Manhattan_Data.index, 
                               categories=['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'], 
                               sorted=True)
Manhattan_Data = Manhattan_Data.sort_index()
Manhattan_Data


# In[15]:

# Create new Data frame with both NYC and Manhattan data
Columns = ["Month","Manhattan", "NYC", "Percentage"]
dataFrame = pd.DataFrame({'Month' : NYC_Data.index, 'Manhattan' : Manhattan_Data, 'NYC' : NYC_Data, 'Percentage' : Manhattan_Data / NYC_Data})
#Percent_df[Columns].head()
dataFrame


# In[19]:

#df1 = pd.merge(Manhattan, NYC, on='key',how='outer')
#merge is giving error as 
type(Manhattan_Data)


# In[21]:

#function to check is directory exists
def funCheckDir(path):
    directory = os.path.dirname(path) # defining directory path
    if not os.path.exists(directory): # checking if directory already exists
        os.makedirs(directory) # making a directory
        
resultsPath = b+"/Q1_Part_1.csv"
funCheckDir(resultsPath)

# Saving our dataFrame to csv file.
#Percent_df[Columns].to_csv(resultsPath, index=False, encoding='utf-8')
dataFrame.to_csv(resultsPath, index=False, encoding='utf-8')

