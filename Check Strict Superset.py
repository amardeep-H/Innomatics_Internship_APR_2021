#!/usr/bin/env python
# coding: utf-8

# In[1]:


eleOfA = set(map(int, input().split()))
numN = int(input())
k =True
i=1
while(i<= numN):
    eleOfSets=set(map(int, input().split()))
    if not eleOfSets.issubset(eleOfA):
        k = False
    if len(eleOfSets)>= len(eleOfA):
        k=False
    i+=1
    
print(k)


# In[ ]:




