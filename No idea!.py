#!/usr/bin/env python
# coding: utf-8

# In[1]:


#No Idea!

m =input().split()
m=map(int, m)
n=map(int,input().split())
a=set(map(int,input().split()))
b=set(map(int,input().split()))

counter = 0
for i in n:
    if i in a:
        counter=counter+1
    elif i in b:
        counter=counter-1
        
print(counter)


# In[ ]:




