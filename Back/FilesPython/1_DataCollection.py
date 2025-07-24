#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import requests
import zipfile
import os


# ## <b>Producción</b> cultivos y productos de ganadería
# [Organización de las Naciones Unidas para la Alimentación y la Agricultura](https://www.fao.org/faostat/es/#data/QCL)

# In[2]:


url = "https://bulks-faostat.fao.org/production/Producción_Cultivos_ProductosGanaderia_S_Todos_los_Datos.zip"
local_path = "../archivos_csv/Producción_Cultivos_Ganaderia_Countries.zip"

try: 
    response = requests.get(url) 
    if(response.status_code == 200):
        with open(local_path, "wb") as file:
            file.write(response.content)
        print(f"Archivo descargado correctamente. {response.status_code}")
    else: 
        print(f"Error al descargar el archivo. Código de estado: {response.status_code}")

except: 
    pass

zip_path = "../archivos_csv/Producción_Cultivos_Ganaderia_Countries.zip"
file_tu_extract = "Producción_Cultivos_ProductosGanaderia_S_Todos_los_Datos.csv"

# Extract the zip file and delete it after extraction
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    print("Archivos en el zip:")
    for name in zip_ref.namelist():
        print(name)
    
    #Extract the specific file
    if file_tu_extract in zip_ref.namelist():
        zip_ref.extract(file_tu_extract, "../archivos_csv/")
        print(f"Archivo {file_tu_extract} extraído correctamente.")
    else:
        print(f"El archivo {file_tu_extract} no se encuentra en el zip.")

#os.rename("../archivos_csv/Producción_Cultivos_ProductosGanaderia_S_Todos_los_Datos.csv", "../archivos_csv/Producción_Cultivos_Ganaderia_countries.csv")
os.remove(zip_path)


# In[16]:


df = pd.read_csv("../archivos_csv/Producción_Cultivos_ProductosGanaderia_S_Todos_los_Datos.csv", encoding='utf-8')
print(df.shape)
df[df["Área"] == "Argentina"]["Producto"].unique().tolist()


# ---

# ## <b>Comercio</b> cultivos y productos de ganadería
# [Organización de las Naciones Unidas para la Alimentación y la Agricultura](https://www.fao.org/faostat/es/#data/TCL)

# In[3]:


url = "https://bulks-faostat.fao.org/production/Comercio_CultivosProductosGanaderia_S_Todos_los_Datos_(Normalizado).zip"
local_path = "../archivos_csv/Comercio_Cultivos_Ganaderia_Countries.zip"

try: 
    response = requests.get(url)
    if(response.status_code == 200):
        with open(local_path, "wb") as file:
            file.write(response.content)
        print(f"Archivo descargado correctamente. {response.status_code}")
    else: 
        print(f"Error al descargar el archivo. Código de estado: {response.status_code}")

except: 
    pass

zip_path = "../archivos_csv/Comercio_Cultivos_Ganaderia_Countries.zip"
file_tu_extract = "Comercio_CultivosProductosGanaderia_S_Todos_los_Datos_(Normalizado).csv"

# Extract the zip file and delete it after extraction
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    print("Archivos en el zip:")
    for name in zip_ref.namelist():
        print(name)
    
    #Extract the specific file
    if file_tu_extract in zip_ref.namelist():
        zip_ref.extract(file_tu_extract, "../archivos_csv/")
        print(f"Archivo {file_tu_extract} extraído correctamente.")
    else:
        print(f"El archivo {file_tu_extract} no se encuentra en el zip.")

#os.rename("../archivos_csv/Comercio_Cultivos_ProductosGanaderia_S_Todos_los_Datos.csv", "../archivos_csv/Comercio_Cultivos_Ganaderia_countries.csv")
os.remove(zip_path)


# ---

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


# In[ ]:


df = pd.read_csv(path, encoding='ISO-8859-1')
df = pd.DataFrame(df)
print(df.shape)
df.head()
print('Sembrado y cosechado: hectareas \n Produccino: toneladas \n Rendimiento: kilogramos')


# In[6]:


df


# ---

# ## CBOT (Chicago Board of trade)

# In[7]:


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


# In[8]:


#df = pd.read_csv(path, encoding='ISO-8859-1')


# In[ ]:




