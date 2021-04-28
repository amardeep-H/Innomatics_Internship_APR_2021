#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Introduction to Sets

def average(array):
    # your code goes here
    sum_a = sum(set(array))
    len_a =len(set(array))
    op = sum_a/len_a
    return op

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# In[ ]:




