#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Arrays


import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    res = numpy.array(arr[::-1], float)
    return res

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# In[2]:


#Transpose and Flatten

import numpy
n,m = map(int, input().split())

arr = numpy.array([input().strip().split() for _ in range(n)], int)

print(arr.transpose())
print(arr.flatten())


# In[3]:


#Concatenate

import numpy

a, b, c = map(int,input().split())
arr1 = numpy.array([input().split() for _ in range(a)],int)
arr2 = numpy.array([input().split() for _ in range(b)],int)
print(numpy.concatenate((arr1, arr2), axis = 0))



# In[19]:


#Zeros and Ones

import numpy as np

def arrays(arr):
    arr1 = np.array(arr, dtype = int)
    
    arr2 = np.zeros(arr1, dtype = int)
    
    arr3 = np.ones(arr1, dtype = int)
    
    return arr2, arr3

arr = input().strip().split(' ')
arr2, arr3 = arrays(arr)

print(arr2)
print(arr3)


# In[22]:


#Eye and Identity

import numpy
numpy.set_printoptions(legacy = '1.13')

x, y = map(int, input().split())

print(numpy.eye(x , y, k=0))




# In[23]:


#Array Mathematics

import numpy as np
n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')


# In[24]:


#Floor, Ceil and Rint

import numpy
numpy.set_printoptions(legacy='1.13')


arrA = numpy.array(input().split(), float)
print (numpy.floor(arrA))
print (numpy.ceil(arrA))
print (numpy.rint(arrA))


# In[25]:


#Sum and Prod

import numpy
n,m = map(int, input().split()) 

arr = numpy.array([input().split() for _ in range(n)], int)

sum0 = numpy.array(numpy.sum(arr, axis=0))

print(numpy.prod(sum0))


# In[26]:


# Min and Max



import numpy
n,m = map(int, input().split()) 

arr = numpy.array([input().split() for _ in range(n)], int)

sum0 = numpy.array(numpy.min(arr, axis=1))

print(numpy.max(sum0))


# In[27]:


#Mean, Var, and Std

import numpy


N,M = map(int,input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(A.mean(axis=1))
print(A.var(axis=0))
ss=A.std()
print ("{0:.11f}".format(ss))


# In[29]:


#Dot and Cross

import numpy

N = int(input())
A = numpy.array([input().split() for i in range(N)], int)
B = numpy.array([input().split() for i in range(N)], int)
print (numpy.dot(A, B))


# In[30]:


#Inner and Outer

import numpy


A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)

print (numpy.inner(A, B))
print (numpy.outer(A, B))



# In[31]:


#Polynomials

import numpy as np
print(np.polyval(np.array(input().split(),float),int(input())))


# In[32]:



#Linear Algebra



import numpy
print(round(numpy.linalg.det(numpy.array([list(map(float,input().split())) for _ in range(int(input()))])),2))


# In[ ]:




