#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Required packages are to be installed first

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


import numpy as np
import csv

from scipy import stats
from scipy.stats import norm


# In[3]:



from pandas import ExcelWriter
from pandas import ExcelFile

data = pd.read_excel("C:\\Users\\maheshkatte\\Desktop\\AD\\vs  code py\\aspiring_minds_employability_outcomes_2015.xlsx")

print(data.head(2))


# In[4]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


# In[5]:


data.head(15)


# In[6]:


#Initial shape of data

data.shape


# In[7]:


data.info()


# In[8]:


data.describe()


# In[9]:


#Lets CLEAN the data with null values or inappropriate values like outliers, etc.

data.isnull().sum()


# In[10]:


#lets provide some proper designation so that we will easily handle the data

l=[]
for i in data['Designation']:
    if ('senior' in i and 'engineer' not in i):
        l.append('senior')
    elif('trainee'in i and 'engineer' not in i):
        l.append('trainee')
    elif('engineer' in i and 'senior' not in i):
        l.append('engineer')
    elif('associate' in i and 'senior' not in i):
        l.append('associate')
    elif('developer' in i and 'senior' not in i):
        l.append('developer')
    elif('manager' in i and 'senior' not in i):
        l.append('manager')
    elif('analyst' in i):
        l.append('analyst')
    elif('consultant' in i):
        l.append('consultant')
    elif('executive' in i):
        l.append('executive')
    elif('designer' in i):
        l.append('designer')
    else:
        l.append('others')


# In[11]:


print(l)


# In[12]:


data['Designation']=l
data['Designation'].value_counts()


# In[13]:


print(data['Designation'])


# In[14]:


data['12board'].unique()


# In[15]:


#change the name of the boards

data.loc[data['12board']=="central board of secondary education",'12board'] = "cbse"


# In[16]:


se = pd.Series(["cbse","icse"])
data.loc[-data['12board'].isin(se), '12board'] = 'state board'#those which are not in se are to be tagged by state board


# In[17]:


data['12board'].value_counts()


# In[18]:


#change the name of the degrees

data['Degree'].value_counts()


# In[19]:


data['Specialization'].value_counts()


# In[20]:


sw= pd.Series(data['Specialization'].unique())
print(sw)


# In[21]:


specialization_map = {'electronics and communication engineering' : 'EC',
'computer science & engineering' : 'CS',
'information technology' : 'CS' ,
'computer engineering' : 'CS',
'computer application' : 'CS',
'mechanical engineering' : 'ME',
'electronics and electrical engineering' : 'EC',
'electronics & telecommunications' : 'EC',
'electrical engineering' : 'EL',
'electronics & instrumentation eng' : 'EC',
'civil engineering' : 'CE',
'electronics and instrumentation engineering' : 'EC',
'information science engineering' : 'CS',
'instrumentation and control engineering' : 'EC',
'electronics engineering' : 'EC',
'biotechnology' : 'other',
'other' : 'other',
'industrial & production engineering' : 'other',
'chemical engineering' : 'other',
'applied electronics and instrumentation' : 'EC',
'computer science and technology' : 'CS',
'telecommunication engineering' : 'EC',
'mechanical and automation' : 'ME',
'automobile/automotive engineering' : 'ME',
'instrumentation engineering' : 'EC',
'mechatronics' : 'ME',
'electronics and computer engineering' : 'CS',
'aeronautical engineering' : 'ME',
'computer science' : 'CS',
'metallurgical engineering' : 'other',
'biomedical engineering' : 'other',
'industrial engineering' : 'other',
'information & communication technology' : 'EC',
'electrical and power engineering' : 'EL',
'industrial & management engineering' : 'other',
'computer networking' : 'CS',
'embedded systems technology' : 'EC',
'power systems and automation' : 'EL',
'computer and communication engineering' : 'CS',
 'information science' : 'CS',
'internal combustion engine' : 'ME',
'ceramic engineering' : 'other',
'mechanical & production engineering' : 'ME',
'control and instrumentation engineering' : 'EC',
'polymer technology' : 'other',
'electronics' : 'EC'}


# In[22]:


data['Specialization'] = data['Specialization'].map(specialization_map)


# In[23]:


data['Specialization'].value_counts()


# In[24]:


#lets fix the outliers

fig_dims = (20,4)
fig, ax = plt.subplots(figsize=fig_dims)
sns.set_theme(style="whitegrid")
plt.subplot(1,2,1)
sns.boxplot(data['Salary'], color = 'pink')
plt.subplot(1,2,2)
sns.boxplot(data['10percentage'], color ='lightgreen')


# In[25]:


def no_outt(data,ft):
    q1=data[ft].quantile(.25)
    q3=data[ft].quantile(.75)
    IQR=q3-q1
    lower_limit=q1-(1.5*IQR)
    upper_limit=q3+1.5*IQR
    lst=data.index[(data[ft]<lower_limit)|(data[ft]>upper_limit)]
    return lst


# In[26]:


index_list=[]
for f in ['10percentage','12percentage','Salary']:
    index_list.extend(no_outt(data,f))


# In[27]:


def remove(df1,ft): #defining function to remove outlier in columns
    df1=df1.drop(ft)
    return df1


# In[28]:


df2=remove(data,index_list)
df2.shape


# In[29]:


df2.describe()


# In[30]:


df2.corr()


# In[31]:


plt.subplots(figsize=(20,15))
sns.heatmap(df2.corr(method='pearson'), annot = True, linewidth =0.5 , linecolor="white", cmap="YlGnBu")


# In[32]:


df2.columns


# In[33]:


df2.shape


# In[34]:


df2.drop(columns=[ 'DOL', 'Designation', 'JobCity','CollegeTier',
'CollegeCityTier', '10board','CollegeState','ElectronicsAndSemicon',
'MechanicalEngg', 'ElectricalEngg', 'TelecomEngg',
'CivilEngg'],axis=1,inplace=True)


# In[35]:


df2.shape


# In[36]:


df2=df2.drop(columns=['Unnamed: 0',])


# In[37]:


df2.shape


# In[38]:


df2.info()


# In[39]:


df2['GraduationYear'].value_counts()


# In[40]:


df2.to_csv("cleaned.csv")


# In[41]:


import os
exe = 'cleaned.csv'
#if the exe just in current dir
print (os.path.abspath(exe))
# output
# D:\python\note\something.exe

#if we need find it first
for root, dirs, files in os.walk(r'D:\python'):
    for name in files:
        if name == exe:
            print (os.path.abspath(os.path.join(root, name)))


# In[42]:


import warnings
warnings.filterwarnings("ignore")


# In[43]:


plt.figure(figsize=(20,4))
plt.subplot(1,2,1)
sns.boxplot(data['Salary'], color="pink")
plt.subplot(1,2,2)
sns.boxplot(df2['Salary'])


# In[ ]:





# In[44]:


plt.figure(figsize=(10,9))
plt.subplot(1,2,1)
stats.probplot(data['Salary'],dist='norm',plot=plt)
plt.title("Before removing outliers")
plt.grid()
plt.subplot(1,2,2)
stats.probplot(df2['Salary'],dist='norm',plot=plt)
plt.title("After removing outliers")
plt.grid()


# In[45]:


df2['Salary'].mode()


# In[46]:


df2['Gender'].value_counts()


# In[47]:


# Number of females is much less than males 

fig_dims = (6,6)
fig, ax = plt.subplots(figsize=fig_dims)
sns.countplot(x='Gender',data=df2,palette='RdBu_r')


# In[48]:


#Salaries of males are quite higher than females

sns.barplot(x='Gender', y = 'Salary', data=df2,palette='rainbow_r')


# In[49]:




sns.countplot(x='Specialization',data=df2,palette='viridis')


# In[50]:


#here, we can see that there are outliers in  CE, OTHER, EL, ME

sns.barplot(x='Specialization',y='Salary',data=df2, palette='YlGnBu')


# In[51]:


sns.boxplot(x='Salary', y = 'Specialization', data=df2,palette='summer_r')
plt.suptitle('Salary levels by specialization')


# In[52]:



sns.barplot(x='CollegeCityTier',y='Salary',data=data,palette='BuGn')


# In[53]:


sns.regplot(x='ComputerProgramming', y='Salary', data=df2, scatter_kws={'color':"purple", 'alpha':0.1},line_kws={"color": "black"})


# In[54]:


#graph shows the a positive relation between salary and 12th board

sns.factorplot(x='12board', y='Salary', kind='point', data=df2, ci=None , size=5,aspect=2)
plt.suptitle('Salary vs 12Board')


# In[56]:


#lets check out the relation between degree and salary

sns.factorplot(x='Degree', y='Salary', kind='violin', data=df2, ci=None , size=5,aspect=2, palette="YlGnBu")
plt.suptitle('Salary vs Degree')


# In[57]:


sns.pairplot(data = df2, diag_kind='kde')
print("aa")


# In[ ]:


# Conclusion : i. The people with higher degrees have higher salaries 
#             ii. Normally males have higher salaries and have high number of heads. 


# In[ ]:




