#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Dependencies
import csv
import pandas as pd
import numpy as np
from pathlib import Path
import sys


# In[2]:


# Create a reference the CSV file desired
csv_path = "Resources/election_data.csv"

# Read the CSV into a Pandas DataFrame
pole_df = pd.read_csv(csv_path)

# Print the data just to get look and feel
pole_df


# In[3]:


#Define required outputs, remove counties, rename column, add percent column column, and select a winner

#number of votes
cnt_pole_df = pole_df['Voter ID'].nunique()

#Reduce pole_df to two columns and rename Voter Id to Vote Count
pole_df = pole_df.rename(columns={'Candidate':'Candidate','Voter ID':'Vote Count'})
pole_df = pole_df[['Candidate', 'Vote Count']]

#Group by candidate and count voter id (Vote Count)
pole_df_can_vtr_cnt = pole_df.groupby(['Candidate']).count()

#Add percent of Vote as a column in the dataframe 
pole_df_can_vtr_cnt['pct of vote'] = pole_df_can_vtr_cnt['Vote Count']/[cnt_pole_df]

#Sort decending by vote count
Election_Results = pole_df_can_vtr_cnt.sort_values(['Vote Count'], ascending=[0])

#Sort high to low on vote caunt to pick winning candidate
Winner = pole_df_can_vtr_cnt.sort_values(['Vote Count'], ascending=[0]).iloc[:1]


# In[4]:


#Print results
print(' EXTRA EXTRA EXTRA')
print('-------------------')
print(' Election Results ')
print('-------------------')
print('Total Votes: ' + str(cnt_pole_df))
print('-------------------')
print(' Invidual Results ')
print('-------------------')
print(Election_Results)
print('-------------------')
print('And the Winner is . . . ')
print(Winner)


# In[4]:


#Save results to a file
Path("Analysis/Results.txt").touch()
stdout_obj = sys.stdout             # store original stdout 
sys.stdout = open("Analysis/Results.txt", "w")
print(' EXTRA EXTRA EXTRA')
print('-------------------')
print(' Election Results ')
print('-------------------')
print('Total Votes: ' + str(cnt_pole_df))
print('-------------------')
print(' Invidual Results ')
print('-------------------')
print(Election_Results)
print('-------------------')
print('And the Winner is . . . ')
print(Winner)
sys.stdout.close()
sys.stdout = stdout_obj             # restore print commands to to interactive prompt


# In[ ]:




