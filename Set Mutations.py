#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Set Mutations
n = int(input())
numEle = set(map(int, input().split()))
for i in range(int(input())):
    s, b = input().split()
    if s == 'intersection_update':
        numEle &= set(map(int, input().split()))
    elif s == 'update':
        numEle |= set(map(int, input().split()))
    elif s == 'symmetric_difference_update':
        numEle ^= set(map(int, input().split()))
    else:
        numEle -= set(map(int,input().split()))
print(sum(numEle))


# In[ ]:




