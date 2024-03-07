#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import sqlite3


# ### Creando el archivo de la base de datos

# In[2]:


try:
    mi_conexion = sqlite3.connect('DataBase/CampoProject_database')
    cursor = mi_conexion.cursor()
except Exception as ex:
    print(ex)


# ### Creando tabla

# In[ ]:





# ---

# In[1]:


import nbconvert #No poner --execute. Tarda mucho
get_ipython().system('jupyter nbconvert --to script --output-dir="../" 3_sqlite3.ipynb')

