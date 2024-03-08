#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd
import sqlite3


# ### Creando el archivo de la base de datos

# In[3]:


try:
    mi_conexion = sqlite3.connect('..\\DataBase/CampoProject_database')
    cursor = mi_conexion.cursor()
except Exception as ex:
    print(ex)


# ### Creando tabla

# In[ ]:




