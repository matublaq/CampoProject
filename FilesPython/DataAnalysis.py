#!/usr/bin/env python
# coding: utf-8

# In[1]:


from DataProcess import Area_dep


# In[2]:


Area_dep.keys()


# ## Grafica

# In[3]:


import matplotlib.pyplot as plt


# In[4]:


Suarez_soja = Area_dep['Coronel Suarez'][Area_dep['Coronel Suarez']['cultivo'] == 'Soja total']


# In[5]:


LaMadrid_soja = Area_dep['General La Madrid'][Area_dep['General La Madrid']['cultivo'] == 'Soja total']


# In[8]:





# - <p>Rendimiento</p>

# In[7]:


#plt.figure(figsize=(25, 10))
plt.subplot()
plt.bar(Suarez_soja['campaña'], Suarez_soja['rendimiento'])
 
plt.show()


# In[ ]:




