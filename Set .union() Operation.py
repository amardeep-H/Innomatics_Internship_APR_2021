#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Set .union() Operation
numEng=int(input())
engRoll=set(map(int,input().split()))
numfre=int(input())
freRoll=set(map(int,input().split()))
numostu1newspap=engRoll.union(freRoll)
print(len(numostu1newspap))


# In[ ]:




