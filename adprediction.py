#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


dataframe = pd.read_csv('d:/Downloads/TADPOLE_D1_D2.csv')


# In[3]:


print(dataframe.head())


# In[28]:


dataframe.dropna(axis=0, how='all', thresh=None, subset=None, inplace=False)
dataframe.head()


# In[4]:


print(dataframe.info())


# In[26]:


dataframe_subset.dropna(axis=0, how='all', thresh=None, subset=None, inplace=False)
dataframe_subset.head()


# In[31]:


dataframe_subset = dataframe[['Ventricles', 'Hippocampus', 'WholeBrain', 'Entorhinal', 'MidTemp' ]]
dataframe_subset.head()


# In[17]:


# Dropping the columns having NaN/NaT values
dataframe_subset = dataframe_subset.dropna(axis=1)

dataframe_subset.head()


# In[23]:


dataframe_subset = dataframe_subset.dropna(axis='columns', how ='all')
dataframe_subset.head()


# In[22]:


# Dropping the columns having NaN/NaT values
dataframe_subset = dataframe_subset.dropna(axis=1)

# Resetting the indices using df.reset_index()
dataframe_subset = dataframe_subset.reset_index(drop=True)

dataframe_subset.head(10)


# In[ ]:





# In[ ]:




