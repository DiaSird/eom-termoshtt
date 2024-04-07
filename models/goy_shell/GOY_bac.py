#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


get_ipython().system(' cargo run --release --example=goy_shell > goy.csv')


# In[4]:


df = pd.read_csv("goy.csv").set_index("time")


# In[5]:


df[["r4", "r8", "r16", "r26"]].plot()


# In[6]:


(df**2).mean().plot()
plt.yscale("log")

