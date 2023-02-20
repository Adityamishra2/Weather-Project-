#!/usr/bin/env python
# coding: utf-8

# # Inserting Libraries

# In[25]:


import numpy as np
import pandas as pd
from datetime import datetime


# In[26]:


df = pd.read_csv("weather_dataset_stage1.xls - Sheet 1 - weather_dataset (2).csv")


# In[27]:


df.head(30)


# # Dropping Null Values

# In[28]:


df.dropna(inplace=True)
df.head()


# # Renaming All Collumns

# In[29]:


df.rename( columns={'weather_dataset':'Date',
                    'Unnamed: 1':'Temperature','Unnamed: 2':'Average_humidity',
                    'Unnamed: 3':'Average_dewpoint','Unnamed: 4':'Average_barometer',
                    'Unnamed: 5':'Average_windspeed','Unnamed: 6':'Average_gustspeed',
                    'Unnamed: 7':'Average_direction','Unnamed: 8':'Rainfall_for_month',
                    'Unnamed: 9':'Rainfall_for_year','Unnamed: 10':'Maximum_rain_per_minute',
                    'Unnamed: 11':'Maximum_temperature','Unnamed: 12':'Minimum_temperature',
                    'Unnamed: 13':'Maximum_humidity','Unnamed: 14':'Minimum_humidity',
                    'Unnamed: 15':'Maximum_pressure','Unnamed: 16':'Minimum_pressure',
                    'Unnamed: 17':'Maximum_windspeed','Unnamed: 18':'Maximum_gust_speed',
                    'Unnamed: 19':'Maximum_heat_index','Unnamed: 20':'Date1',
                    'Unnamed: 21':'Month','Unnamed: 22':'diff_pressure'}, inplace=True )


# In[30]:


df.head()


# In[31]:


df.drop(index=27,axis=0)


# # Resetting Index To 0

# In[32]:


df.reset_index(drop=True,inplace=True)
df.head()


# # Removing Apostrophe from all the data points

# In[33]:


df.drop(0,inplace=True)


# In[34]:


df['Date'] = df['Date'].str.replace(r"'","")
df['Temperature'] = df['Temperature'].str.replace(r"'","")
df['Average_humidity'] = df['Average_humidity'].str.replace(r"'","")
df['Average_dewpoint'] = df['Average_dewpoint'].str.replace(r"'","")
df['Average_barometer'] = df['Average_barometer'].str.replace(r"'","")
df['Average_windspeed'] = df['Average_windspeed'].str.replace(r"'","")
df['Average_gustspeed'] = df['Average_gustspeed'].str.replace(r"'","")
df['Average_direction'] = df['Average_direction'].str.replace(r"'","")
df['Rainfall_for_month'] = df['Rainfall_for_month'].str.replace(r"'","")
df['Rainfall_for_year'] = df['Rainfall_for_year'].str.replace(r"'","")
df['Maximum_rain_per_minute'] = df['Maximum_rain_per_minute'].str.replace(r"'","")
df['Maximum_temperature'] = df['Maximum_temperature'].str.replace(r"'","")
df['Minimum_temperature'] = df['Minimum_temperature'].str.replace(r"'","")
df['Maximum_humidity'] = df['Maximum_humidity'].str.replace(r"'","")
df['Minimum_humidity'] = df['Minimum_humidity'].str.replace(r"'","")
df['Maximum_pressure'] = df['Maximum_pressure'].str.replace(r"'","")
df['Minimum_pressure'] = df['Minimum_pressure'].str.replace(r"'","")
df['Maximum_windspeed'] = df['Maximum_windspeed'].str.replace(r"'","")
df['Maximum_gust_speed'] = df['Maximum_gust_speed'].str.replace(r"'","")
df['Maximum_heat_index'] = df['Maximum_heat_index'].str.replace(r"'","")
df['Date1'] = df['Date1'].str.replace(r"'","")
df['Month'] = df['Month'].str.replace(r"'","")
df['diff_pressure'] = df['diff_pressure'].str.replace(r"'","")
df.head()


# In[35]:


df.columns


# # Changing Data Type Of All Columns

# In[36]:


df['Temperature'] = df['Temperature'].astype(float)
df['Average_humidity'] = df['Average_humidity'].astype(float)
df['Average_dewpoint'] = df['Average_dewpoint'].astype(float)
df['Average_barometer'] = df['Average_barometer'].astype(float)
df['Average_windspeed'] = df['Average_windspeed'].astype(float)
df['Average_gustspeed'] = df['Average_gustspeed'].astype(float)
df['Average_direction'] = df['Average_direction'].astype(float)
df['Rainfall_for_month'] = df['Rainfall_for_month'].astype(float)
df['Rainfall_for_year'] = df['Rainfall_for_year'].astype(float)
df['Maximum_rain_per_minute'] = df['Maximum_rain_per_minute'].astype(float)
df['Maximum_temperature'] = df['Maximum_temperature'].astype(float)
df['Minimum_temperature'] = df['Minimum_temperature'].astype(float)
df['Maximum_humidity'] = df['Maximum_humidity'].astype(float)
df['Minimum_humidity'] = df['Minimum_humidity'].astype(float)
df['Maximum_pressure'] = df['Maximum_pressure'].astype(float)
df['Minimum_pressure'] = df['Minimum_pressure'].astype(float)
df['Maximum_windspeed'] = df['Maximum_windspeed'].astype(float)
df['Maximum_gust_speed'] = df['Maximum_gust_speed'].astype(float)
df['Maximum_heat_index'] = df['Maximum_heat_index'].astype(float)
df['Month'] = df['Month'].astype(int)


# In[37]:


df.drop(columns=['Date1'],axis=1,inplace=True)


# # Removing ';' from data points

# In[38]:


df['diff_pressure'] = df['diff_pressure'].str.replace(r";","")
df['diff_pressure'] = df['diff_pressure'].astype(float)


# In[39]:


df.head()


# # Dropping Duplicates

# In[40]:


df.drop_duplicates()


# # Removing Invalid Date

# In[41]:


indexAge = df[df['Date']=='2022-02-29'].index
df.drop(indexAge , inplace=True)
df.head(30)


# In[42]:


df['Date'] = pd.to_datetime(df['Date'])


# In[43]:


df


# # Making Year Corrections

# In[44]:


from datetime import datetime, timedelta
df['year_offset'] = (df['Date'] == datetime(2022, 1, 1)).cumsum() - 1
df['Date'] = df.apply(lambda x: x['Date'].replace(year=x['Date'].year + x['year_offset']), axis=1)


# In[45]:


df


# # Dropping Duplicate Column

# In[46]:


df.drop('year_offset', axis=1, inplace =True)


# In[47]:


df.info()


# # Exporting Cleaned File as CSV

# In[48]:


df.to_csv(r'C:\Users\Taniya\Downloads\clean_dataset.csv', index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




