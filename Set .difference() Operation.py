#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Set .difference() Operation

numEng = int(input())
engRoll = set(map(int, input().split()))
numfre = int(input())
freRoll = set(map(int, input().split()))

engOnly = engRoll - freRoll
print(len(engOnly))


# In[ ]:




