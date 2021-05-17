#!/usr/bin/env python
# coding: utf-8

# # @mean
# || mean is nothing but an average of given values.
# || mean = sum of elements / number of elements.
# || mean is dependent on outliers

# In[62]:


import numpy as np
import pandas as pd
import csv
data = pd.read_csv("C:/Users/maheshkatte/Desktop/AD/vs  code py/data.csv")
m_inc_arr = np.array(data["Mthly_HH_Income"])
print("array of monthly income : \n",m_inc_arr)
print("MEAN of Mthly_HH_Income is : ", m_inc_arr.mean())

a_inc_arr = np.array(data["Annual_HH_Income"])
print("Array of Annual_HH_Income is : \n", a_inc_arr )
print("MEAN of Annual_HH_Income is :", a_inc_arr.mean() )


# In[27]:


# Mean without using mean function

n_of_ele_MI = len(m_inc_arr)
print(n_of_ele_MI)
sum_ele_MI = sum(m_inc_arr)
print(sum_ele_MI)

mean_MI = sum_ele_MI/n_of_ele_MI
print(mean_MI)


#look both means are same 


# # @Median 
# || median is the middle-most value if the number of given elements is odd else its a average of two middle-most elements.
# 
# || median is independent of outliers. 
# 
# || sort the elements

# In[17]:


print("Median of Annual_HH_Income is :", np.median(a_inc_arr))
print("Median of Mthly_HH_Income is :", np.median(m_inc_arr))


# In[29]:


#without using median function


m_inc_arr.sort()
  
if n_of_ele_MI % 2 == 0:
    median1 = m_inc_arr[n_of_ele_MI//2]
    median2 = m_inc_arr[n_of_ele_MI//2 - 1]
    median = (median1 + median2)/2
else:
    median = m_inc_arr[n_of_ele_MI//2]
print("Median is: " + str(median))

#both medians are same


# # @Mode
# 
# || Mode is the most frequent value among the given elements.
# 
# 

# In[30]:


import statistics as st

print("Median of Annual_HH_Income is :", st.mode(a_inc_arr))
print("Median of Mthly_HH_Income is :", st.mode(m_inc_arr))


# In[32]:


print("Median of No_of_Fly_Members : " , st.mode(data["No_of_Fly_Members"]))


# In[ ]:





# In[34]:


# without using mode function

from collections import Counter
n_of_ele_MI = len(m_inc_arr)
  
data1 = Counter(m_inc_arr)
get_mode = dict(data1)
mode = [k for k, v in get_mode.items() if v == max(list(data1.values()))]
  
if len(mode) == n_of_ele_MI:
    get_mode = "No mode found"
else:
    get_mode = "Mode is : " + ', '.join(map(str, mode))
      
print(get_mode)


# # Variance
# 
# || Variance is the variability of an element from its mean.
# 
# || Variance is the average of squares of differnce between mean and the values.
# 
# || Var(X) = E[(x-mu)^2]
# https://stackabuse.com/calculating-variance-and-standard-deviation-in-python/

# In[45]:


print("Variance of sample set is : " ,(st.variance(m_inc_arr, mean_MI)))


# In[55]:



st.variance(data["Mthly_HH_Income"], mean_MI)


# # Standard Deviation
# 
# || Standard deviation is a number that describes how spread out the values are.
# 
# || Low standard deviation means that most of the numbers are close to the mean (average) value.
# 
# || A high standard deviation means that the values are spread out over a wider range.
# 
# || Std is a square root of variance.

# In[57]:


std_m_inc_arr = np.std(m_inc_arr)
print("Standard deviation of elements of Mthly_HH_Income column from its mean is : ",std_m_inc_arr)


# In[61]:


#without using library functions

import math  
var  = sum(pow(x-mean_MI,2) for x in m_inc_arr ) / len(m_inc_arr)  # variance
std  = math.sqrt(var)
print(std)


# # Correlation
# 
# || It is always between -1(perfect anti corelation) and +1(perfect corelation)
# 
# || here, the relation between Mthly_hh_income and Annual_HH_Income is appr. completely positive

# In[63]:


data.corr(method = "pearson")


# # Normal Distribution
# 
# || It is very commonly found distribution in nature.
# 
# || The most of the elements are gathered near the average value and least near both the ends.
# 
# || In ND the mean, median, mode are same and it is symmetric around the mean or avg.
# 
# https://www.statisticshowto.com/probability-and-statistics/normal-distributions/#:~:text=Properties%20of%20a%20normal%20distribution,under%20the%20curve%20is%201.

# In[66]:


import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# In[76]:


normal = np.random.normal(loc =mean_MI ,scale =std_m_inc_arr,size =len(m_inc_arr))
sns.displot(normal)


# In[77]:


normal = np.random.normal(loc =mean_MI ,scale =std_m_inc_arr,size =len(m_inc_arr)+10000000)
sns.displot(normal)


# # Positively Skewed & Negatively Skewed Normal Distribution
# 
# || If skewness is less than -1 or greater than 1, the distribution is highly skewed.
# 
# || If skewness is between -1 and -0.5 or between 0.5 and 1, the distribution is moderately skewed.
# 
# || If skewness is between -0.5 and 0.5, the distribution is approximately symmetric.
# 
# || If skewness is 0, the data are perfectly symmetrical, ver rare.
# 
# || Negative skew value represents left skewness and positive skew value represents right skewness

# In[73]:


data["Mthly_HH_Income"].skew() #0.92 it means it is moderately right skewed


# # Kurtosis
# || kurtosis tells you the height and sharpness of the central peak, relative to that of a standard bell curve.
# 
# || if kurt = 0 ...Normal distribution
# || if kurt > 0 ...Relatively peaked distribution
# || if kurt < 0 ...Relatively flat distribution

# In[78]:


data["Mthly_HH_Income"].kurt()


# # Effect on Mean, Median and Mode due to Skewness
# 
# To summarize, generally if the distribution of data is skewed to the left, the mean is less than the median, which is often less than the mode. If the distribution of data is skewed to the right, the mode is often less than the median, which is less than the mean.

# # Explain QQ Plot and show the implementation of the same
# 
# 
# 

# In[86]:


stats.probplot(data['Mthly_HH_Income'], dist="norm", plot=plt)

plt.grid()


# In[87]:


plt.figure(figsize=(12, 8))



plt.subplot(2, 3, 1)
stats.probplot(normal, dist="norm", plot=plt) #normal having 1cr values, so it forms perfect normal distribution


plt.show()


# # Explain Box Cox and show the implementation of the same
# 
# || box cox transform a abnormal distribution plot to normal distribution

# In[96]:



pareto_rv = np.random.pareto(data["Mthly_HH_Income"], len(data["Mthly_HH_Income"]))

sns.displot(pareto_rv)


# In[97]:



stats.probplot(pareto_rv, dist="norm", plot=plt)

plt.grid()


# In[98]:



x_t, l = stats.boxcox(pareto_rv)

print(l)


# In[99]:



stats.probplot(x_t, dist="norm", plot=plt)

plt.grid()


# In[ ]:




