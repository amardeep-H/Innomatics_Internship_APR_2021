#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings('ignore')


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats


# In[3]:


uniform_100 = np.random.uniform(low=10, high=40, size=(100))
sns.distplot(uniform_100)


# In[4]:


uniform_1000 = np.random.uniform(low=10, high=40, size=(1000))
sns.distplot(uniform_1000)


# In[5]:


uniform_10000 = np.random.uniform(low=10, high=40, size=(10000))
sns.distplot(uniform_10000)


# In[6]:


normal_100 = np.random.normal(loc=20, scale=5, size=100)
sns.distplot(normal_100)


# In[7]:


normal_10000 = np.random.normal(loc=20, scale=5, size=10000)
sns.distplot(normal_10000)


# In[8]:


mu_normal_10000 = normal_10000.mean()
sigma_normal_10000 = normal_10000.std()
print(mu_normal_10000, sigma_normal_10000)


# In[9]:


one_std_right = mu_normal_10000 + (1 * sigma_normal_10000)
one_std_left = mu_normal_10000 - (1 * sigma_normal_10000)
two_std_right = mu_normal_10000 + (2 * sigma_normal_10000)
two_std_left = mu_normal_10000 - (2 * sigma_normal_10000)
three_std_right = mu_normal_10000 + (3 * sigma_normal_10000)
three_std_left = mu_normal_10000 - (3 * sigma_normal_10000)


# In[13]:


plt.figure(figsize = (20,10))
sns.set_style("darkgrid")
sns.distplot(normal_10000)

plt.axvline(mu_normal_10000, color='coral', label = 'Mean')

plt.axvline(one_std_right, color='yellow', label = 'Mean + 1SD')
plt.axvline(one_std_left, color='yellow', label = 'Mean - 1SD')
plt.axvline(two_std_right, color='green', label = 'Mean + 2SD')
plt.axvline(two_std_left, color='green', label = 'Mean - 2SD')
plt.axvline(three_std_right, color='blue', label = 'Mean + 3SD')
plt.axvline(three_std_left, color='blue', label = 'Mean - 3SD')
plt.legend();


# In[14]:


# 68,95,99.7 RULE
type(normal_10000)


# In[15]:


normal_10000 < one_std_right


# In[16]:


(normal_10000 < one_std_right).sum()


# In[18]:


((one_std_left < normal_10000) &(normal_10000 < one_std_right)).sum()


# In[20]:


((one_std_left < normal_10000) & (normal_10000 < one_std_right)).sum()/normal_10000.size


# In[21]:


((two_std_left < normal_10000) & (normal_10000 < two_std_right)).sum()/normal_10000.size


# In[22]:


((three_std_left < normal_10000) & (normal_10000 < three_std_right)).sum()/normal_10000.size


# In[25]:


pareto_rv = np.random.pareto(a=2, size=1000)
sns.distplot(pareto_rv)


# In[26]:


stats.probplot(pareto_rv, dist = "norm", plot = plt)
plt.grid()


# In[37]:


#x_t = transformed by box_cox, 1=lambada
stats.boxcox(pareto_rv)
x_t,a1 = stats.boxcox(pareto_rv)
print(a1)


# In[38]:


stats.probplot(x_t, dist= "norm", plot=plt)
plt.grid()


# In[ ]:




