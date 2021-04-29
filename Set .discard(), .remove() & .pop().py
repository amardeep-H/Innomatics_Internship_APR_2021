#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
noOfcommands=int(input())

for i in range(noOfcommands):
    k= []
    k=input().split()
    if k[0]=='pop':
        s.pop()
        
    elif k[0]=='remove':
        s.remove(int(k[1]))
        
    elif k[0]=='discard':
        s.discard(int(k[1]))
        
    else:
        print("not a command")
        
print(sum(s))


# In[ ]:




