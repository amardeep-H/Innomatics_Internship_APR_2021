#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Set .symmetric_difference() Operation
numEng = int(input())
engRoll = set(map(int, input().split()))
numFre = int(input())
freRoll = set(map(int, input().split()))

eitherEngOrFre = engRoll ^ freRoll
print(len(eitherEngOrFre))


# In[ ]:




