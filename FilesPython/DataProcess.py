#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


from DataCollection import df
df


# ## Tablas
# ### <p>Las tablas son la informacion de los departamentos de cada provincia</p>
# <p>Provincias --> Departamentos --> Tablas</p>

# <p>Codigo en una linea</p>

# In[3]:


# En una sola linea
estructura = {key1: {key2: df[df['provincia'] == key1][df['departamento'] == key2].drop(['id_provincia', 'provincia', 'id_departamento', 'departamento', 'id_cultivo'], axis=1) for key2 in set(df[df['provincia'] == key1]['departamento'])} for key1 in set(df['provincia'])}
estructura


# <p>Codigo en varias lineas. Paso a paso</p>

# In[4]:


# Paso a paso

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


# ---

# ### Transformando a Data Frames

# In[5]:


provincias = estructura.keys()
count = 0
try:
    for prov in provincias:
        departamentos = estructura[i].keys()
        for dep in departamentos:
            estructura[prov][dep] = pd.DataFrame(estructura[prov][dep])
except KeyError:
    count += 1
    prov_error = prov
    dep_error = dep
    pass

print(count, '\n', prov_error, dep_error)


# ## Coronel Suarez y alrededores

# In[6]:


list_area = ['Coronel Suarez', 'Adolfo Alsina', 'Guamini', 'Daireaux', 'General La Madrid', 'General la Madrid' , 'Saavedra', 'Coronel Pringles', 'Tornquist']
Suarez_alrededores = {dep: estructura['Buenos Aires'][dep] for dep in list_area}


# <p>Combinando los dos <b>General La Madrid</b></p>

# In[7]:


Suarez_alrededores['General La Madrid'] = pd.concat([Suarez_alrededores['General La Madrid'], Suarez_alrededores['General la Madrid']], ignore_index=True)

