#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


from DataCollection import df
df


# ---

# ## Tablas
# ### <p>Las tablas son la informacion de los departamentos de cada provincia</p>
# <p>Provincias --> Departamentos --> Tablas</p>

# - <p>Codigo en una linea</p>

# In[3]:


# En una sola linea
estructura = {key1: {key2: df[df['provincia'] == key1][df['departamento'] == key2].drop(['id_provincia', 'provincia', 'id_departamento', 'departamento', 'id_cultivo'], axis=1) for key2 in set(df[df['provincia'] == key1]['departamento'])} for key1 in set(df['provincia'])}
estructura


# - <p>Codigo en varias lineas. Paso a paso</p>

# In[4]:


# Paso a paso
'''
# Provincias
estructura2 = {key: 0 for key in set(df['provincia'])}

# Departamentos
for i in estructura2:
    estructura2[i] = {key: None for key in set(df[df['provincia'] == i]['departamento'])}

# Dataframe
for prov in estructura2:
    for depa in estructura2[prov]:
        estructura2[prov][depa] = df[df['provincia'] == prov][df['departamento'] == depa].drop(['id_provincia', 'provincia', 'id_departamento', 'departamento', 'id_cultivo'], axis=1)

estructura2
'''


# ### Transformando a Data Frames

# In[5]:


provincias = estructura.keys()
count = 0
prov_error = None
dep_error = None
try:
    for prov in provincias:
        departamentos = estructura[prov].keys()
        for dep in departamentos:
            estructura[prov][dep] = pd.DataFrame(estructura[prov][dep])
except KeyError:
    count += 1
    prov_error = prov
    dep_error = dep
    pass

print(count, '\n', prov_error, dep_error)


# ---

# In[6]:


estructura['Buenos Aires'].keys()


# ## Coronel Suarez y alrededores

# In[14]:


list_area = ['Coronel Suarez', 'Adolfo Alsina', 'Guamini', 'Daireaux', 'General La Madrid', 'General la Madrid' , 'Saavedra', 'Coronel Pringles', 'Tornquist', 'Olavarria', 'Laprida']
Suarez_alrededores = {dep: estructura['Buenos Aires'][dep] for dep in list_area}


# <p>Combinando los dos <b>General La Madrid</b></p>

# In[17]:


Suarez_alrededores['General La Madrid'] = pd.concat([Suarez_alrededores['General La Madrid'], Suarez_alrededores['General la Madrid']], ignore_index=True)
del Suarez_alrededores['General la Madrid']


# ### Mapa

# In[10]:


import folium
import json


# In[11]:


# Cargando limites geograficos de los departamentos
with open('../visualizacion/geojson/suarez_alrededores.geojson') as f:
    geojson_data = json.load(f)

# mapa object
mapa = folium.Map(location=[-37.45798801348687, -61.93294229940922], zoom_start=8)

# Agrega la capa GEOJSON al mapa y aplica estilos
folium.GeoJson(
    geojson_data,
    style_function=lambda features: {
        'fillColor': 'green',   # Color de relleno verde
        'color': 'black',       # Color del contorno de los departamentos
        'weight': 2,            # Grosor del contorno de los departamentos
        'fillOpacity': 0.5      # Opacidad del relleno de los departamentos
    }
).add_to(mapa)

# Agregar marcadores
folium.Marker([-37.29261188022635, -62.20015596276018], popup='Don Gaston').add_to(mapa)
folium.Marker([-37.31521756433013, -61.49986789793718], popup='La Carola').add_to(mapa)
# Muestra el mapa
mapa


# In[ ]:




