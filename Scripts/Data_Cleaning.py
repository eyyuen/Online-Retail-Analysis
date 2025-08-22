#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


df = pd.read_excel(r'C:\Users\nijis\Downloads\online+retail\Online Retail.xlsx')


# In[3]:


import os
print(os.getcwd())


# In[7]:


df.head()


# In[8]:


df = df.dropna(subset=['CustomerID'])


# In[9]:


df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
df = df.dropna(subset=['InvoiceDate'])


# In[10]:


df = df[df['Quantity'] > 0]


# In[11]:


df = df[df['UnitPrice'] > 0]


# In[12]:


df = df.drop_duplicates()


# In[13]:


df['Description'] = df['Description'].fillna('No Description')
df['Description'] = df['Description'].str.strip()


# In[14]:


df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]


# In[15]:


df['InvoiceNo'] = df['InvoiceNo'].astype(str)


# In[16]:


df['Country'] = df['Country'].str.strip()


# In[17]:


df['CustomerID'] = df['CustomerID'].astype(int)


# In[18]:


print(df['UnitPrice'].describe())
print(df['Quantity'].describe())


# In[19]:


df = df[df['UnitPrice'] >= 0.01]


# In[20]:


df['Description'] = df['Description'].str.strip().str.upper()


# In[21]:


non_products = ['MANUAL', 'AMAZON FEE', 'ADJUST BAD DEBT', 'POSTAGE', 'DOTCOM POSTAGE']
df = df[~df['Description'].isin(non_products)]


# In[22]:


df['TotalPrice'] = (df['Quantity'] * df['UnitPrice']).round(2)


# In[23]:


df = df.reset_index(drop=True)


# In[28]:


print(df.isnull().sum())


# In[25]:


print(df.dtypes)


# In[26]:


customers = df[['CustomerID', 'Country']].drop_duplicates()
customers.to_csv('customers.csv', index=False)


# In[27]:


products = df[['StockCode', 'Description']].drop_duplicates()
products.to_csv('products.csv', index=False)


# In[29]:


invoices = df[['InvoiceNo', 'InvoiceDate', 'CustomerID']].drop_duplicates()
invoices.to_csv('invoices.csv', index=False)


# In[30]:


orders = df[['InvoiceNo', 'StockCode', 'Quantity', 'UnitPrice', 'TotalPrice']]
orders.to_csv('orders.csv', index=False)


# In[ ]:




