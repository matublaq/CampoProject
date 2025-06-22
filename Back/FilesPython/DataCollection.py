#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import requests


# ## Estimaciones agricolas 69 - 23
# [Datos agricultura, ganaderia y pesca de Argentina](https://datos.magyp.gob.ar/)

# In[ ]:


url = 'https://datos.magyp.gob.ar/dataset/9e1e77ba-267e-4eaa-a59f-3296e86b5f36/resource/95d066e6-8a0f-4a80-b59d-6f28f88eacd5/download/estimaciones-agricolas-2023-10.csv'
local_path = '../archivos_csv/estimaciones_agricolas_69_23.csv'

try: 
    response = requests.get(url)
    if(response.status_code == 200):
        with open(local_path, 'wb') as file:
            file.write(response.content)
        print(f'Download success, status code {response.status_code}')
    else:
        print(f'Download error, status code {response.status_code}')

except: 
    pass
path = '../archivos_csv/estimaciones_agricolas_69_23.csv'


# In[7]:


df = pd.read_csv(path, encoding='ISO-8859-1')
df = pd.DataFrame(df)
print(df.shape)
df.head()
print('Sembrado y cosechado: hectareas \n Produccino: toneladas \n Rendimiento: kilogramos')


# In[8]:


df


# ---

# ## CBOT (Chicago Board of trade)

# In[9]:


url = "https://news.agrofy.com.ar/8a423a00-08bc-4f54-861a-0e3d67ed02e8"
local_path = "../archivos_csv/series_historicas_futuros_Soja_CBOT.csv"

try: 
    response = requests.get(url)
    if(response.status_code == 200):
        with open(local_path, 'wb') as file:
            file.write(response.content)
        print(f"Download success. Status conde {response.status_code}")
    else:
        print(f"Download error. Status code {response.status_code}")
        
except: 
    pass

path = '../archivos_csv/series_historicas_futuros_Soja_CBOT.csv'


# In[ ]:


#df = pd.read_csv(path, encoding='ISO-8859-1')


# In[ ]:




