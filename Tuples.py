#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print (hash(integer_list))

