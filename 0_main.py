#!/usr/bin/env python
# coding: utf-8

# ## Run program

# In[1]:


get_ipython().run_line_magic('run', '1_DataCollection.ipynb')


# In[2]:


get_ipython().run_line_magic('run', '2_DataProcess.ipynb')


# In[3]:


get_ipython().run_line_magic('run', '3_sqlite3.ipynb')


# ---

# In[1]:


import nbconvert #No poner --execute. Tarda mucho
get_ipython().system('jupyter nbconvert --to script --output-dir="../" 0_main.ipynb')

