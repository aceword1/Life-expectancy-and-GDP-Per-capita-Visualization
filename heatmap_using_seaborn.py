#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1 .Create a pivot table dataframe with year along x-axes, continent along y-axes and lifeExp filled within cells.
# 2. Plot a heatmap using seaborn for the pivot table that was just created.


# In[6]:


#import modules

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


# In[118]:


#Load and Read the Dataset using Pandas
dataset = pd.read_csv('gapminder-Five-Year-Data.csv')

#Convert to a Dataframe using Pandas
dataset_framed = pd.DataFrame(dataset)

#Split the column into multiple columns using pandas
dataset_split = pd.DataFrame(df['country,year,pop,continent,lifeExp,gdpPercap'].str.split(',',6).tolist(),columns=['Country','Year','Population','Continent','LifeExpectancy','GDP Per Capita'])

#Test to see if it works
dataset_split


# In[128]:


#Convert LifeExp from String to Number
dataset_split['LifeExpectancy'] = pd.to_numeric(dataset_split['LifeExpectancy'])

# Create a Pivot showing year along x-axes, continent along y-axes and lifeExp filled within the cells
dataset_pivot = dataset_split.pivot_table(index='Continent',columns='Year',values=('LifeExpectancy'), aggfunc=np.mean)

#Test if everything works
dataset_pivot

#Create Heatmap using Seaborn Python Library
heat_map = sb.heatmap(dataset_pivot, annot=True)


# In[ ]:





# In[ ]:




