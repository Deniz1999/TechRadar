#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


pwd


# In[3]:


df = pd.read_excel('/Users/denizkazdal/Desktop/TechnologyRadar.xlsm')


# In[4]:


df.head(5)


# In[5]:


type(df['Use Case'])


# In[6]:


df['Status/Maturity']


# In[7]:


df['isNew']= 'TRUE'


# In[8]:


df_new = df[['Use Case', 'Description', 'Technology', 'Status/Maturity', 'isNew']]


# In[9]:


df_new.dropna(inplace = True)


# In[10]:


df_new.rename(columns={'Use Case': 'name', 'Technology': 'quadrant', 'Status/Maturity': 'ring', 'Description': 'description'},inplace = True)



# In[11]:


df_new


# In[12]:


df_new['quadrant'].value_counts()


# In[13]:


df_new.quadrant.unique()


# In[14]:


df_new.quadrant = df_new.quadrant.str.lower()


# In[15]:


df_new.quadrant = df_new.quadrant.str.strip()


# In[16]:


df_new['quadrant'].value_counts()


# In[17]:


df_new = df_new[df_new.quadrant.isin(i.lower() for i in ["Artificial Intelligence (Machine Learning; Computer Vision, NLP)","Geographical Information Systems (GIS)","Big data","Blockchain"])]

# df_new[df_new.quadrant == "Artificial Intelligence (Machine Learning; Computer Vision, NLP)" | df_new.quadrant == "Geographical Information Systems (GIS)" | df_new.quadrant == "Big data" | df_new.quadrant == "Blockchain"]




# In[18]:


df_new.ring.unique()


# In[19]:


df_new.shape


# In[ ]:





# In[20]:


df_new.ring = df_new.ring.str.strip()


# In[21]:


df_new.quadrant.value_counts()


# In[28]:


df_new = df_new[df_new.ring != 'Prototype, Idea']


# In[29]:


df_new.ring.unique()


# In[23]:


df_new.quadrant.unique()


# In[24]:


df_new.to_csv('/Users/denizkazdal/Desktop/technologyradarfiltered_last.csv')


# In[ ]:




