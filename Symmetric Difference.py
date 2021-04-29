#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Symmetric difference
m=input()
m1=input()
mlis=m1.split()
mnewlis=set(map(int, mlis))

n=input()
n1=input()
nlis=n1.split()
nnewlis=set(map(int, nlis))

prefinalset = (mnewlis.difference(nnewlis)).union(nnewlis.difference(mnewlis))
for i in sorted(list(prefinalset)):
    print(i)


# In[ ]:





# In[ ]:




