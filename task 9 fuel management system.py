#!/usr/bin/env python
# coding: utf-8

# In[18]:


#TATA has developed a better fuel management system for the SUV segment. They claim that with this system,
#on average the SUV's mileage is at least 15 km/litre?


import matplotlib.pyplot  as plt
import numpy as np
from scipy.stats import norm
from scipy.stats import t
import math

# Step 1 :

# Plan the hypothesis statements  
# Null Hypothesis (H0) :  Avg. mean of mileage < 15
# Alternate hypothesis (H1): Avg. mean of mileage > 15 km/litre


#Step 2 :
# collect the sample set 
# calculate the sample mean, sample standard deviation, size of the sample, etc.

pop_mean = 15
sample = [14.1, 14.2, 14.3, 15.1, 15.2, 15.3, 16.1, 16.2, 16.3, 17.1, 17.2, 17.3, 18.1, 18.2, 18.3, 19.1, 19.2, 19.3, 20.1, 20.2, 20.3]
N = len(sample)
sample_mean = sum(sample)/len(sample)
print("sample_mean {}".format(sample_mean))
print("Size of sample {}".format(N))


# In[19]:


# Step 3:
# Calculate the test statistic values
# As sample size is less than 30 and we have not provided with population varience we will be using t_score mehtod

def t_value(sample_size, sample_mean, pop_mean, sample_std):
    numerator = sample_mean - pop_mean
    denomenator = sample_std / sample_size**0.5
    return numerator / denomenator


# In[20]:


# Let us find the standard deviation of the sample s.
sample_std = np.std(sample)
print("The standard deviation (s) of the sample of size {} is {}". format(N,sample_std))


# In[21]:


t_val = t_value(N,sample_mean,pop_mean,sample_std)
print("The T value for the given data is {}".format(t_val))


# In[49]:


# Step 4:
# Set the significance level of our hypothesis which is denoted by alpha symbol which refers to the likelihood
# that the random sample you choose is not representative of the population. The lower the significance level, the
# more confident you can be in replicating your results.


confidence_interval = 0.68
alpha = 1 - confidence_interval
print(alpha)


# In[50]:


## Step 5: Deciding the type of test.
# We have to decide the type of test depending on the context of hypothesis. The tests are,
# Two-tailed test
# One-tailed test
# You can decide the type of the test and the position of the critical region on the basis of the ‘sign’ in the
# alternate hypothesis.
# If there is != sign in H₁ then we can use Two-tailed test where Rejection region is present on both the sides of distribution.
# If there is < sign in H₁ then we can use Left-tailed test where Rejection region is present on left side of disgtribution.
# If there is > sign in H₁ then we can use Right-tailed test where Rejection region is present on Right side of disgtribution.
#From step 1, the alternate hypothesis has a and we should perform a two tailed test.
# To find the t value of a two tailed test,
t_critical = t.ppf(1-alpha,df = N-1)
print("The t critical value for the given data is {}".format(t_critical))


# In[51]:


# interpret via critical value
if abs(t_val) >= t_critical:
 print("Reject the null hypothesis.")
else:
 print('Fail to Reject the null hypothesis.')


# In[52]:


# Ploting the sampling distribution with rejection regions
# Defining the x minimum and x maximum
x_min = 10
x_max = 20
df = N-1
# Defining the sampling distribution mean and sampling distribution std
mean = pop_mean
std = sample_std
# Ploting the graph and setting the x limits
x = np.linspace(x_min, x_max, 100)
y = t.pdf(x,df, mean, std)
plt.figure(figsize = (15,10))
# calculating right critical value for the one tailed test
t_critical_right = pop_mean + (t_critical * std)
# Shading the right rejection region
x2 = np.linspace(t_critical_right, x_max, 100)
y2 = t.pdf(x2,df, mean, std)
plt.fill_between(x2, y2, color='yellow')

plt.annotate("Rejection Region",(17.5,0.025))
plt.scatter(sample_mean, 0)
plt.annotate("Sample_mean", (sample_mean, 0.01))
plt.axvline(mean, color='green')
plt.annotate("pop_mean", (mean+0.1, 0.2))
plt.plot(x, y)
plt.show()
# Ploting the sample mean and concluding the results 


# In[ ]:


# here we reject null hypothesis

