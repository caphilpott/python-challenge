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
csv_path = 'Resources/budget_data.csv'

# Read the CSV into a Pandas DataFrame
bgt_df = pd.read_csv(csv_path)

# Print the data just to get look and feel
bgt_df


# In[3]:


#Define required outputs, formula feeds, new column, and index

#number of months
count_bgt_df=bgt_df['Date'].count()

#Sum of profit and loss
sum_bgt_df=bgt_df['Profit/Losses'].sum()

#add change column
bgt_df['Chg'] = bgt_df['Profit/Losses'].diff()

#Average Change calc
chg_bgt_df=bgt_df['Chg'].mean()

#Set Index for estblishing min/max change
bgt_df_with_index = bgt_df.set_index('Profit/Losses')

#Maximum in change column
Max_change= bgt_df_with_index.sort_values(['Chg'], ascending=[0]).iloc[0]


#Minimum in change column
Min_change = bgt_df_with_index.sort_values(['Chg'], ascending=[1]).iloc[0]


# In[4]:


#Print results
print('Total Months: ' + str(count_bgt_df))
print('Total: $'+ str(sum_bgt_df))
print('Average Change: $'+ str('{:.2f}'.format(chg_bgt_df)))
print('Greatest Increase in Profits: '+ Max_change['Date'] + '  $' + str(+ Max_change['Chg']))
print('Greatest Decrease in Profits: '+ Min_change['Date'] + '  $' + str(+ Min_change['Chg']))


# In[5]:


#Save results to a file
Path("Analysis/Results.txt").touch()
stdout_obj = sys.stdout             # store original stdout 
sys.stdout = open("Analysis/Results.txt", "w")
print('Total Months: ' + str(count_bgt_df))
print('Total: $'+ str(sum_bgt_df))
print('Average Change: $'+ str('{:.2f}'.format(chg_bgt_df)))
print('Greatest Increase in Profits: '+ Max_change['Date'] + '  $' + str(+ Max_change['Chg']))
print('Greatest Decrease in Profits: '+ Min_change['Date'] + '  $' + str(+ Min_change['Chg']))
sys.stdout.close()
sys.stdout = stdout_obj             # restore print commands to to interactive prompt


# In[ ]:




