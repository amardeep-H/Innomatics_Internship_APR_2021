#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Q-1: Pista House selling Hyderabadi Chicken Dum biryani claims that each parcel packet has 500 grams of biryani 
#(also mentioned on the label of packet). You are sceptic of their claims and
#believe that on average each packet does not contain 500 grams of biryani. How do you prove your claim? 
#(Given that the population std is 50)


import matplotlib.pyplot  as plt
import numpy as np
from scipy.stats import norm
from scipy.stats import t
import math


# In[ ]:


# Step 1: 

# Plan the hypothesis statements  
# Null Hypothesis (H0) :  Avg. mean of weight of packet = 500 gms
# Alternate hypothesis (H1): Avg. mean of weight of packet != 500 gms


# In[3]:


# if population variation is known we will use z_score
# if population varience is not given then we will use t_score method 


# In[13]:


#Step 2:

# Collect the sample set
# Calculate the samples' mean, samples' standard deviation, samples' size, etc


sample = [490,420,470,500,495,496,496,498,508,480]
mean_pop = 500
N = len(sample)
mean_sample = sum(sample)/len(sample)
print("the mean of sample is : " ,mean_sample)


# In[15]:


# Step 3:
# Calculate the test statistic values
# As sample size is less than 30 and we have not provided with population varience we will be using t_score mehtod

# Function to calculate t_score
def t_score(sample_size, sample_mean, pop_mean, sample_std):
    numerator = mean_sample - mean_pop
    denomenator = sample_std / sample_size**0.5
    return numerator / denomenator

# Standard deviation of the sample (s) is :

std_sample = np.std(sample)
print("The standard deviation s of the sample of size N is : ", std_sample)





# In[16]:


t_score = t_score(N,mean_sample,mean_pop,std_sample)
print("The t score value for the given case is : ",t_score)


# In[17]:


# Step 4:
# Set the significance level of our hypothesis which is denoted by alpha symbol which refers to the likelihood
# that the random sample you choose is not representative of the population. The lower the significance level, the
# more confident you can be in replicating your results.


#Lets assume the confidence level is 95% 
# 𝛼 = 1 - confidence level
# 𝛼 = 0.05

confidence_interval = 0.95
alpha = 1 - confidence_interval


# In[18]:


# Step 5: Deciding the type of test.
# We have to decide the type of test depending on the context of hypothesis. The tests are,
# Two-tailed test
# One-tailed test
# You can decide the type of the test and the position of the critical region on the basis of the ‘sign’ in the
# alternate hypothesis.
# If there is != sign in H₁ then we can use Two-tailed test where Rejection region is present on both the sides of distribution.
# If there is < sign in H₁ then we can use Left-tailed test where Rejection region is present on left side of disgtribution.
# If there is > sign in H₁ then we can use Right-tailed test where Rejection region is present on Riht side of disgtribution.
#From step 1, the alternate hypothesis has a and we should perform a two tailed test.

# To find the t_critical value of a two tailed test,
t_critical = t.ppf(1-alpha/2,df = N-1)
print("The t critical value for the given data is : ", t_critical)


# In[20]:


# interpret via critical value
if abs(t_score) >= t_critical:
    print("Reject the Null hypothesis.")
else:
    print('Fail to Reject the Null hypothesis.')


# In[71]:


# Plot the sampling distribution with rejection regions
# Defining the x minimum and x maximum

x_min = 400
x_max = 600

#diversity factor
df = N-1

# Defining the sampling distribution mean and sampling distribution std

mean = mean_pop
std = std_sample

# Ploting the graph and setting the x limits

x = np.linspace(x_min, x_max, 100)
y = t.pdf(x, df,mean, std)
plt.figure(figsize = (15,10))


# Computing the left and right critical values (Two tailed Test)

t_critical_left = mean_pop - (t_critical * std)
t_critical_right = mean_pop + (t_critical * std)


# Shading the left rejection region

x1 = np.linspace(x_min, t_critical_left, 100)
y1 = t.pdf(x1,df, mean, std)
plt.fill_between(x1, y1, color='yellow')



# Shading the right rejection region

x2 = np.linspace(t_critical_right, x_max, 100)
y2 = t.pdf(x2,df, mean, std)
plt.fill_between(x2, y2, color='yellow')

plt.scatter(mean_sample, 0)
plt.annotate("Sample_mean", (mean_sample-20, 0.0007))
plt.axvline(mean, color='green')
plt.annotate("pop_mean", (mean+1, 0.01))
plt.plot(x, y)
plt.show()
# Ploting the sample mean and concluding the results


# @@ According to the plot and the analysis we have done so far we conclude that ...
#                    we failed to reject Null Hypothesis

# In[34]:


#Q.4 : You have developed a new Machine Learning Application and claim that on average it takes less than 100 ms
#to predict for any future datapoint. How do you convince your client about this claim?

# Step 1: 

# Plan the hypothesis statements  
# Null Hypothesis (H0) :  Avg. mean of > 100 ms
# Alternate hypothesis (H1): Avg. mean of < 100 ms


#Step 2:

# Collect the sample set
# Calculate the samples' mean, samples' standard deviation, samples' size, etc.


pop_mean = 100 #Given
sample = [112,85,95,91,103,96,104,100,102,90]
N = len(sample)
sample_mean = sum(sample)/N
print("The mean of the sample is {}".format(sample_mean))


# In[35]:


# Step 3:
# Calculate the test statistic values
# As sample size is less than 30 and we have not provided with population varience we will be using t_score mehtod


# let us define a function for calculating t value
def t_value(sample_size, sample_mean, pop_mean, sample_std):
    numerator = sample_mean - pop_mean
    denomenator = sample_std / sample_size**0.5
    return numerator / denomenator


# In[36]:


# Let us find the standard deviation of the sample s.
sample_std = np.std(sample)
print("The standard deviation s of the sample of size N is {}". format(sample_std))


# In[37]:


t_val = t_value(N,sample_mean,pop_mean,sample_std)
print("The t static value for the given case is {}".format(t_val))


# In[76]:


# Step 4:
# Set the significance level of our hypothesis which is denoted by alpha symbol which refers to the likelihood
# that the random sample you choose is not representative of the population. The lower the significance level, the
# more confident you can be in replicating your results.

confidence_interval = 0.95
alpha = 1 - confidence_interval


# In[77]:


# Step 5: Deciding the type of test.
# We have to decide the type of test depending on the context of hypothesis.
# here we will go for left tailed test


# To find the t value of a one tailed test,
t_critical = t.ppf(1-alpha,df = N-1)
print("The t critical value for the given data is {}".format(t_critical))


# In[83]:


# interpret via critical value
if abs(t_val) < t_critical:
 print("Reject the null hypothesis.")
else:
 print('Fail to Reject the null hypothesis.')


# In[82]:


# Ploting the sampling distribution with rejection regions
# Defining the x minimum and x maximum
x_min = 75
x_max = 125
df = N-1
# Defining the sampling distribution mean and sampling distribution std
mean = pop_mean
std = sample_std
# Ploting the graph and setting the x limits
x = np.linspace(x_min, x_max, 1000)
y = t.pdf(x, df,mean, std)
plt.figure(figsize = (15,10))
# Computing the left critical value (one tailed Test)
t_critical_left = pop_mean - (t_critical * std)
# Shading the left rejection region
x1 = np.linspace(x_min, t_critical_left,10)
y1 = t.pdf(x1,df, mean, std)
plt.fill_between(x1, y1, color='yellow')
plt.scatter(x1,y1)
plt.scatter(sample_mean, 0)
plt.annotate("Sample_mean", (sample_mean-5, 0.0007))
plt.axvline(mean, color='green')
plt.annotate("pop_mean", (mean+1, 0.02))
plt.plot(x, y)
plt.show()
# Ploting the sample mean and concluding the results


# In[ ]:


# here we have failed to reject null hypothesis.

