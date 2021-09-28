#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import stats
from scipy.stats import norm


# In[2]:


# Mean profits from two different divisions of a company = Mean1 + Mean2
Mean = 5+7
print('Mean Profit is Rs', Mean*45,'Million')


# In[3]:


# Variance of profits from two different divisions of a company = SD^2 = SD1^2 + SD2^2
SD = (3^2)+(4^2)
print('Standard Deviation is Rs', SD*45, 'Million')


# In[5]:


# A. Specify a Rupee range (centered on the mean) such that it contains 95% probability for the annual profit of the company.
print('Range is Rs',(stats.norm.interval(0.95,540,315)),'in Millions')


# In[6]:


# B. Specify the 5th percentile of profit (in Rupees) for the company
# To compute 5th Percentile, we use the formula X=μ + Zσ; wherein from z table, 5 percentile = -1.64
X= 540+(-1.64)*(315)
print('5th percentile of profit (in Million Rupees) is',np.round(X,2))


# In[7]:


# C. Which of the two divisions has a larger probability of making a loss in a given year?


# In[8]:


# Probability of Division 1 making a loss P(X<0)
stats.norm.cdf(0,5,3)


# In[9]:


# Probability of Division 2 making a loss P(X<0)
stats.norm.cdf(0,7,4)


# Inference: Probability of Division 1 making a loss in a given year is more than Division 2.

# In[ ]:




