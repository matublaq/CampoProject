#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

import requests


# In[3]:


url = 'https://datos.magyp.gob.ar/dataset/9e1e77ba-267e-4eaa-a59f-3296e86b5f36/resource/95d066e6-8a0f-4a80-b59d-6f28f88eacd5/download/estimaciones-agricolas-2023-10.csv'
local_path = '..\\archivos_csv\\estimaciones_agricolas_69_23.csv'

response = requests.get(url)

if(response.status_code == 200):
    with open(local_path, 'wb') as file:
        file.write(response.content)
    print(f'Download success, status code {response.status_code}')
else:
    print(f'Download error, status code {response.status_code}')

path = '..\\archivos_csv\\estimaciones_agricolas_69_23.csv'


# In[4]:


df = pd.read_csv('..\\archivos_csv/estimaciones_agricolas_69_23.csv', encoding='ISO-8859-1')
df = pd.DataFrame(df)
print(df.shape)
df.head()
print('Sembrado y cosechado: hectareas \n Produccino: toneladas \n Rendimiento: kilogramos')

