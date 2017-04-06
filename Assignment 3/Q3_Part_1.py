
# coding: utf-8

# # Q3_PART ONE
# - Use ‘cricket_matches’ data set.
# - Calculate the average score for each team which host the game and win the game.
# - Remember that if a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. You have to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. The final answer is the average score of each team satisfying the above condition.
# - Display a few rows of the output use df.head()
# - Generate a csv output
# 

# In[2]:

#from pandas import Series, DataFrame
import os
import pandas as pd
import numpy as np


# In[12]:

#getting current working directory
b = os.getcwd()


#reading the csv file
df = pd.read_csv(b+"\\"+"Data\\cricket_matches.csv", usecols=[6,8,12,13,17,18])


# In[13]:

df.head()


# In[14]:

df1 = df[df['home'] == df['winner']]
df1.head()


# In[15]:

df1['score'] = np.where(df1['home'] == df1['innings1'], df1['innings1_runs'], df1['innings2_runs'])
df1.head()


# In[16]:

total_avg = df1['score'].groupby(df1['home']).mean()
total_avg.head()


# In[18]:

df2 = pd.DataFrame({ 'score' : total_avg})
df2.head()


# In[19]:

df3 = pd.DataFrame({'home' : df2.index,'score' : total_avg })
df3.head()


# In[20]:

#function to check is directory exists
def funCheckDir(path):
    directory = os.path.dirname(path) # defining directory path
    if not os.path.exists(directory): # checking if directory already exists
        os.makedirs(directory) # making a directory
        
resultsPath = b+"/Q3_Part_1.csv"
funCheckDir(resultsPath)

# Saving our dataFrame to csv file.
#Percent_df[Columns].to_csv(resultsPath, index=False, encoding='utf-8')
df3.to_csv(resultsPath, index=False, encoding='utf-8')

