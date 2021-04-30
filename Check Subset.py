#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Check Subset
#we can use .subset() function too

n= int(input())
i=1
while(i<=n):
    numA = int(input())
    eleOfA = set(map(int, input().split()))
    numB=int(input())
    eleOfB= set(map(int, input().split()))
    
    if (eleOfA.intersection(eleOfB) == eleOfA):
        print("True")
    else:
        print("False")
    i+=1


# In[ ]:




