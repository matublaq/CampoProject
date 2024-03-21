#!/usr/bin/env python
# coding: utf-8

# In[13]:


from DataProcess import Area_dep


# In[14]:


Area_dep.keys()


# ## Graficas
#  - ### Rendimientos

# In[15]:


import matplotlib.pyplot as plt


# In[16]:


Suarez_trigo = Area_dep['Coronel Suarez'][Area_dep['Coronel Suarez']['cultivo'] == 'Trigo total']
LaMadrid_trigo = Area_dep['General La Madrid'][Area_dep['General La Madrid']['cultivo'] == 'Trigo total']


# - <p>Rendimiento trigo</p>

# In[17]:


plt.figure(figsize=(80, 10))
plt.xlabel('capana')
plt.ylabel('kilos/hectarea')

plt.bar(Suarez_trigo['campaña'], Suarez_trigo['rendimiento'])

plt.show()


# In[20]:


plt.figure(figsize=(80, 10))
plt.xlabel('campana')
plt.ylabel('kilos/hectarea')

plt.bar(LaMadrid_trigo['campaña'], LaMadrid_trigo['rendimiento'])

plt.show()


# In[21]:


print('Coronel Suarez trigo rendimiento promedio: ', Suarez_trigo['rendimiento'].mean())
print('General La Madrid trigo rendimiento promedio: ', LaMadrid_trigo['rendimiento'].mean())


# <p>Rendimiento general</p>

# In[18]:


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


# In[19]:


print(Area_dep['Coronel Suarez']['rendimiento'].mean())
print(Area_dep['General La Madrid']['rendimiento'].mean())


# In[ ]:




