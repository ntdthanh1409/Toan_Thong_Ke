#!/usr/bin/env python
# coding: utf-8

# In[36]:


import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp


# In[37]:


def results(p, vals=['mean1', 'mean2'], alpha=0.05):
    cols=['score', 'p_value', 'KetLuan']
    if p['p_value'] < alpha:
        p['KetLuan'] = f"Chấp nhận H1 với mức ý nghĩa {alpha}"
    if p['p_value'] >= alpha:
        p['KetLuan'] = f"Chấp nhận H0 với mức ý nghĩa {alpha}"
    df = pd.DataFrame(p, index=[''])
    if vals: cols = vals + cols
    return df[cols]


# In[38]:


df = pd.read_csv('C:\\Users\\PC\\Desktop\\PTDL-Python-Anova-7.5.2021\\gia_nha_dat_us.csv')
data = df['SalePrice']
data = np.log1p(data)
my_mean = 150000
my_log_mean = np.log1p(my_mean)
print(my_log_mean)


# Giả thiết thống kê:
# 
# H0: μ = 11.918397239722838
# 
# H1: μ ≠ 11.918397239722838

# In[39]:


sample = data.sample(n=200)
p = {}
p['mean1'] = np.mean(sample)
p['mean2'] = my_log_mean
p['score'], p['p_value'] = ttest_1samp(sample, my_log_mean)
results(p)


# # Kiểm định 1 phía

# In[40]:


p = {}
p['mean1'] = np.mean(sample)
p['mean2'] = my_log_mean
p['score'], p['p_value'] = ttest_1samp(sample, my_log_mean, alternative='less')
results(p)


# In[ ]:




