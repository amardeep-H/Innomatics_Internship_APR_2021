#!/usr/bin/env python
# coding: utf-8

# In[1]:


#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    mylist=[[i,j,k] for i in range(0,x+1) for j in range(0, y+1) for k in range(0,z+1)if     i+j+k!=n]
    print(mylist)


# In[ ]:




