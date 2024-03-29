#!/usr/bin/env python
# coding: utf-8

# In[1]:


from DataProcess import Area_dep


# In[2]:


Area_dep.keys()


# ---

# ### Mapa

# In[3]:


import folium
import json


# In[4]:


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


# ---

# ## Graficas
# 
# * ### Rendimientos

# In[5]:


import matplotlib.pyplot as plt


# In[6]:


Suarez_trigo = Area_dep['Coronel Suarez'][Area_dep['Coronel Suarez']['cultivo'] == 'Trigo total']
LaMadrid_trigo = Area_dep['General La Madrid'][Area_dep['General La Madrid']['cultivo'] == 'Trigo total']


# - * Trigo Coronel Suarez

# In[7]:


plt.figure(figsize=(80, 10))
plt.xlabel('capana')
plt.ylabel('kilos/hectarea')

plt.bar(Suarez_trigo['campaña'], Suarez_trigo['rendimiento'])

plt.show()


# -  - Trigo General La Madrid

# In[8]:


plt.figure(figsize=(80, 10))
plt.xlabel('campana')
plt.ylabel('kilos/hectarea')

plt.bar(LaMadrid_trigo['campaña'], LaMadrid_trigo['rendimiento'])

plt.show()


# In[9]:


print('Coronel Suarez trigo rendimiento promedio: ', Suarez_trigo['rendimiento'].mean())
print('General La Madrid trigo rendimiento promedio: ', LaMadrid_trigo['rendimiento'].mean())


# -   - Rendimiento general

# In[10]:


plt.figure(figsize=(80, 10))
plt.xlabel('campanas', fontsize=16)
plt.ylabel('kilos/hectarea', fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.bar(Area_dep['Coronel Suarez']['campaña'], Area_dep['Coronel Suarez']['rendimiento'])
'''
for i in Area_dep.keys():
    plt.plot(Area_dep[i]['campaña'], Area_dep[i]['rendimiento'], label=f'{i}')
'''
plt.show()


# In[11]:


print(Area_dep['Coronel Suarez']['rendimiento'].mean())
print(Area_dep['General La Madrid']['rendimiento'].mean())


# In[ ]:




