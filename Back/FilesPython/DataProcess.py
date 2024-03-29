#!/usr/bin/env python
# coding: utf-8

# In[108]:


import pandas as pd
import numpy as np


# In[109]:


from DataCollection import df
df


# ---

# ## Tablas
# ### <p>Cada tabla tiene la informacion de cada departamento de las provincias</p>
# <p>Argentina --> Provincias --> Departamentos</p>

# - <p>Codigo en una linea</p>

# In[110]:


# En una sola linea
estructura = {key1: {key2: df[df['provincia'] == key1][df['departamento'] == key2].drop(['id_provincia', 'provincia', 'id_departamento', 'departamento', 'id_cultivo'], axis=1) for key2 in set(df[df['provincia'] == key1]['departamento'])} for key1 in set(df['provincia'])}
estructura


# - <p>Codigo en varias lineas. Paso a paso</p>

# In[111]:


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


# ### Transformando a Data Frames y acomodando tipos de datos

# In[122]:


provincias = estructura.keys()
count = 0
prov_error = None
dep_error = None
try:
    for prov in provincias:
        departamentos = estructura[prov].keys()
        for dep in departamentos:
            estructura[prov][dep] = pd.DataFrame(estructura[prov][dep])
            # Convierte todos los valores a integer y los que no puede se los pone como NaN
            estructura[prov][dep][['id_campaña', 'sup_sembrada', 'sup_cosechada', 'rendimiento']] = estructura[prov][dep][['id_campaña', 'sup_sembrada', 'sup_cosechada', 'rendimiento']].apply(pd.to_numeric, errors='coerce')
            #
except KeyError:
    count += 1
    prov_error = prov
    dep_error = dep
    pass

print(count, '\n', prov_error, dep_error)


# ---

# ## Coronel Suarez, General La Madrid y alrededores

# In[113]:


estructura['Buenos Aires'].keys()


# In[114]:


list_area = ['Coronel Suarez', 'Adolfo Alsina', 'Guamini', 'Daireaux', 'General La Madrid', 'General la Madrid' , 'Saavedra', 'Coronel Pringles', 'Tornquist', 'Olavarria', 'Laprida']
Area_dep = {dep: estructura['Buenos Aires'][dep] for dep in list_area}


# <p>Combinando los dos <b>General La Madrid</b></p>

# In[115]:


Area_dep['General La Madrid'] = pd.concat([Area_dep['General La Madrid'], Area_dep['General la Madrid']], ignore_index=True)
del Area_dep['General la Madrid']

