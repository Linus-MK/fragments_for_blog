#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

pd.options.display.notebook_repr_html = False # DataFrameの表を綺麗にHTMLで表示されるとブログに貼り付けづらい。テキストにする


# In[2]:


pd.__version__


# In[3]:


df = pd.DataFrame({
    'float_col'  : [1.1, 2.2, 3.3, 4.4, 5.5, 6.6],
    'int_col'    : [0, 2, 4, 1, 3, 5]    
})


# In[4]:


df


# In[5]:


arr = list(range(10, 61, 10))
arr


# In[6]:


idx = df.loc[2]["int_col"]
arr[idx]


# In[7]:


idx


# ## 仕組み、理由

# In[8]:


idx


# In[9]:


df.dtypes


# In[10]:


df.loc[2]


# ## 同様の事例

# In[ ]:




