#!/usr/bin/env python
# coding: utf-8

# In[1]:


#The Captain's Room
from collections import Counter
n=int(input())
roomNOList = input().split()

k = Counter(roomNOList)

d= dict(k)

print(min(d, key=lambda k: d[k]))


# In[ ]:




