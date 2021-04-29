#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Set .intersection() Operation

numEng=int(input())
engRoll = set(map(int,input().split()))
numFre=int(input())
freRoll = set(map(int,input().split()))

stuBothSub = engRoll.intersection(freRoll)
print(len(stuBothSub))


# In[ ]:




