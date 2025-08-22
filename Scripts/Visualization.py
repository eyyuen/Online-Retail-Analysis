#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[35]:


df = pd.read_csv("Total_Revenue_by_Product_by_Month.csv")
print(df.head())


# In[36]:


df['Month'] = pd.to_datetime(df['Month'])


# In[37]:


top_products = df.groupby('Product')['TotalRevenue'].sum().nlargest(5).index


# In[38]:


filtered_df = df[df['Product'].isin(top_products)]


# In[39]:


plt.figure(figsize=(12, 6))
sns.lineplot(data=filtered_df, x='Month', y='TotalRevenue', hue='Product', marker='o')

plt.title('Monthly Revenue Trend of Top 10 Products')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[8]:





# In[10]:


df_quarter = pd.read_csv('Top_Products_by_Quarter.csv')
print(df_quarter.head())


# In[11]:


top_products = df_quarter.groupby('Product')['TotalRevenue'].sum().nlargest(10).index
filtered_df = df_quarter[df_quarter['Product'].isin(top_products)]


# In[17]:


plt.figure(figsize=(12, 6))
sns.barplot(
    data=filtered_df,
    x='Quarter',
    y='TotalRevenue',
    hue='Product'
)

plt.title('Top 10 Products by Revenue per Quarter')
plt.xlabel('Quarter')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.legend(title='Product', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('top_products_by_quarter.png', dpi=300, bbox_inches='tight')
plt.show()


# In[16]:


plt.savefig('top_products_by_quarter.png', dpi=300, bbox_inches='tight')
plt.show()


# In[18]:


df = pd.read_csv('Top_Products_Overall.csv')


# In[19]:


df = df.sort_values(by='TotalRevenue', ascending=False)
print(df.head())


# In[20]:


plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='TotalRevenue', y='Product', palette='Blues_d')

plt.title('Top 10 Products by Revenue')
plt.xlabel('Total Revenue')
plt.ylabel('Product')
plt.tight_layout()
plt.savefig('top_10_products_by_revenue.png', dpi=300)
plt.show()


# In[21]:



df_quantity = df.sort_values(by='TotalQuantity', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(data=df_quantity, x='TotalQuantity', y='Product', palette='Greens_d')

plt.title('Top 10 Products by Quantity Sold')
plt.xlabel('Total Quantity')
plt.ylabel('Product')
plt.tight_layout()
plt.savefig('top_10_products_by_quantity.png', dpi=300)
plt.show()


# In[23]:


df = pd.read_csv("Top_Products_by_Country.csv")
print(df.head())


# In[24]:


top_countries = df.groupby('Country')['TotalRevenue'].sum().nlargest(5).index
filtered_df = df[df['Country'].isin(top_countries)]


# In[25]:


top_products_per_country = (
    filtered_df
    .sort_values(['Country', 'TotalRevenue'], ascending=[True, False])
    .groupby('Country')
    .head(3)
)


# In[26]:


plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_products_per_country,
    x='Country',
    y='TotalRevenue',
    hue='Product',
    palette='Set2'
)

plt.title('Top 3 Products by Revenue in Top 5 Countries')
plt.ylabel('Total Revenue')
plt.xlabel('Country')
plt.xticks(rotation=45)
plt.legend(title='Product', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('top_products_by_country.png', dpi=300)
plt.show()


# In[27]:


num_products = top_products_per_country['Product'].nunique()
custom_palette = sns.color_palette("tab20", num_products)


# In[28]:


unique_products = top_products_per_country['Product'].unique()
product_color_map = dict(zip(unique_products, custom_palette))


# In[29]:


plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_products_per_country,
    x='Country',
    y='TotalRevenue',
    hue='Product',
    palette=product_color_map 
)

plt.title('Top 3 Products by Revenue in Top 5 Countries')
plt.xlabel('Country')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.legend(title='Product', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('top_products_by_country_distinct_colors.png', dpi=300)
plt.show()


# In[ ]:




