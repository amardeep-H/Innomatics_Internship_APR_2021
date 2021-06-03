#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q-2: You have developed a new Natural Language Processing Algorithms and done a user study.
#You claim that the average rating given by the users is 
#greater than 4 on a scale of 1 to 5. How do you prove this to your client?


import matplotlib.pyplot  as plt
import numpy as np
from scipy.stats import norm
from scipy.stats import t
import math


# In[59]:


# step 1 :
# Plan the hypothesis statements
# Null Hypothesis (H0) will be : Avg. Rating < 4
# Alternate Hypothesis(H1) will be : Avg. Rating > 4


# step 2 : 
# Collect the samples
# calculate the mean, size, sample mean & samples' standard deviation.

pop_mean = 4 #Given
sample = [4, 3, 5, 4, 5, 3, 5, 5, 4, 2, 4, 5, 5, 4, 4, 5, 4, 5, 4, 5]
N = len(sample)
sample_mean = sum(sample)/N
print("The mean of the sample is {}".format(sample_mean))
# calculate the standard deviation of the sample s.

sample_std = np.std(sample)
print("The standard deviation s of the sample of size N is {}". format(sample_std))


# In[58]:


# Step 3 :
# calculate T-Score i.e. test statistics 

# define a function for calculating t value
def t_value(sample_size, sample_mean, pop_mean, sample_std):
    numerator = sample_mean - pop_mean
    denomenator = sample_std / sample_size**0.5
    return numerator / denomenator

print(sample_std)


# In[ ]:





# In[6]:


t_val = t_value(N,sample_mean,pop_mean,sample_std)
print("The t static value for the given case is {}".format(t_val))


# In[7]:


#Step 4 :
# Set a significance level of our hypothesis which is denoted by alpha symbol which refer to the likelihood
# that the random sample you choose is not representative of the population.

confidence_interval = 0.95
alpha = 1 - confidence_interval


# In[8]:


# Step 5 :
# Decide which test you are going to perform based on the sign of H1 statement.
# As the statement uses greater than smybol(>) we will be using right tailed test.
# To find the t_critical value
t_critical = t.ppf(1-alpha,df = N-1)
print("The t critical value for the given data is {}".format(t_critical))


# In[9]:


# interpret via critical value
if abs(t_val) > t_critical:
    print("Reject the Null Hypothesis.")
    else:
    print(' We Failed to Reject the Null Hypothesis.')


# In[61]:


# Ploting the sampling distribution with rejection regions.
# Defining the x minimum and x maximum.
x_min = 0 # see at bottom left it is the min limit of x axis
x_max = 8 # see at bottom right it is the max limit of x axis

df = N-1 # diversity factor

# Defining the sampling distribution mean and sampling distribution std
mean = pop_mean
std = sample_std
# Ploting the graph and setting the x limits

x = np.linspace(x_min, x_max,1000)
y = t.pdf(x,df, mean, std)
plt.figure(figsize = (15,10))


# calculating right critical value for the one tailed test
t_critical_right = pop_mean + (t_critical * std)

# Shading the right rejection region

x2 = np.linspace(t_critical_right, x_max,500) #this line makes the yellow curve smoother
y2 = t.pdf(x2,df, mean, std)
plt.fill_between(x2, y2, color='yellow')
plt.annotate("Rejection Region",(5.5,0.05))

plt.scatter(sample_mean, 0) # it show DOT of sample mean
plt.annotate("Sample_mean", (sample_mean, 0.01)) # name the sample mean 
plt.axvline(mean, color='green') #vertical line
plt.annotate("pop_mean", (mean+0.1, 0.2))# name the vertical line
plt.plot(x, y)
plt.show()
# Ploting the sample mean and concluding the results


# In[ ]:


# here, the sample mean lies out of the rejection region so we can conclude that ...we failed to reject the null hypothesis


# In[ ]:




