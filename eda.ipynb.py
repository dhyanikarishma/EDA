#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


# Get the Data
uber_drives=pd.read_csv("uber.csv")
uber_drives


# ## 1. Show the last 10 records of the dataset. 

# In[4]:


uber_drives.tail(10)


# ## 2. Show the first 10 records of the dataset. 

# In[5]:


uber_drives.head(10)


# ## 3. Show the dimension(number of rows and columns) of the dataset. 

# In[6]:


uber_drives.shape


# ## 4. Show the size (Total number of elements) of the dataset. 

# In[7]:


uber_drives.size


# ## 5. Display the information about all the variables of the data set. What can you infer from the output?
# 
# #### Hint: Information includes - Total number of columns,variable data-types, number of non-null values in a variable, and usage

# In[8]:


uber_drives.info()


# ## 6. Check for missing values.
# 
# ####  Note: Output contains only one boolean value

# In[9]:


uber_drives.isnull()


# ## 7. Missing values are present in the entire dataset.
# 

# In[10]:


uber_drives.isnull().sum().sum()


# ## 8. Getting the summary of the original data. 
# 
# #### Summary includes- Count,Mean, Std, Min, 25%,50%,75% and max

# In[11]:


uber_drives.describe()


# 
# 
# ## 9. Dropping the missing values and store the data in a new dataframe (name it"df") .
# 
# #### Note: Dataframe "df" does not contain any missing value

# In[12]:


df=uber_drives.dropna()
df


# ## 10. Checking the information of the dataframe(df). 
# 
# #### Hint: Information includes - Total number of columns,variable data-types, number of non-null values in a variable, and usage

# In[13]:


df.info()


# ##  11. Getting the unique start locations. 
# #### Note: This question is based on the dataframe with no 'NA' values

# In[14]:


pd.unique(df["START*"])


# ## 12. Total number of unique start locations?
# #### Note: Using the original dataframe without dropping 'NA' values

# In[15]:


n=len(pd.unique(uber_drives["START*"]))
n


# ## Q13. What is the total number of unique stop locations. (2 points)
# #### Note: Use the original dataframe without dropping 'NA' values.

# In[16]:


n=len(pd.unique(uber_drives["STOP*"]))
n


# ## Q14. Display all Uber trips that has the starting point as San Francisco. 
# #### Note: Use the original dataframe without dropping the 'NA' values.
# 

# In[18]:


df1=uber_drives[uber_drives["START*"]=="San Francisco"]
df1


# ## Q15. What is the most popular starting point for the Uber drivers? 
# #### Note: Use the original dataframe without dropping the 'NA' values.
# 
# #### Hint:Popular means the place that is visited the most

# In[ ]:


ser1 = df["START*"].value_counts()
ser1.index[0]


# ## Q16. What is the most popular dropping point for the Uber drivers? 
# #### Note: Use the original dataframe without dropping the 'NA' values.
# 
# #### Hint: Popular means the place that is visited the most

# In[ ]:


ser1 = df["STOP*"].value_counts()
ser1.index[0]


# ## Q17. What is the most frequent route taken by Uber drivers. 
# #### Note: This question is based on the new dataframe with no 'na' values.
# #### Hint-Print the most frequent route taken by Uber drivers (Route= combination of START & END points present in the Data set).

# In[ ]:


ser2=(uber_drives["START*"] + "->" + uber_drives["STOP*"]).value_counts()
ser2.index[0]


# ## Q18. Display all types of purposes for the trip in an array. 
# #### Note: This question is based on the new dataframe with no 'NA' values.

# In[ ]:


arr1=df["PURPOSE*"].unique()
arr1


# ## Q19. Plot a bar graph of Purpose vs Miles(Distance). What can you infer from the plot(2 +2 points)
# #### Note: Use the original dataframe without dropping the 'NA' values.
# #### Hint:You have to plot total/sum miles per purpose

# In[ ]:


fig = plt.figure(figsize = (15, 5))
total=df["MILES*"].sum(axis=0)
sumperpurpose=total/(df['PURPOSE*'].value_counts())
list2=list(sumperpurpose)
list1=list(sumperpurpose.index)
plt.bar(list1,list2)



# INFERENCE: MOST OF THE TRIPS WERE FOR COMMUTATION, AIRPORT TRAVEL AND CHARITY
# 

# ## Q20. Display a dataframe of Purpose and the total distance travelled for that particular Purpose. 
# #### Note: Use the original dataframe without dropping "NA" values

# In[ ]:


df1=df.groupby(["PURPOSE*"]).sum()
df1["MILES*"]


# ## Q21. Generate a plot showing count of trips vs category of trips. What can you infer from the plot.
# #### Note: Use the original dataframe without dropping the 'NA' values.

# In[ ]:


df1=df.groupby(["CATEGORY*"]).count()
df1
plt.bar(df1.index, df1["START_DATE*"])


# INFERENCE: MOST OF THE TRIPS ARE BUSINESS TRIPS
# 

# ## Q22. What percentage of Miles were clocked under Business Category and what percentage of Miles were clocked under Personal Category ? 
# 
# ### Note:Use the original dataframe without dropping the 'NA' values. 
# 

# In[ ]:


df1=df[df["CATEGORY*"]=="Business"]

print(df1)
k=df1["MILES*"].sum()
print(k)

l=df["MILES*"].sum()


per=( k/l )*100
print("BUSINESS CATEGORY PERCENTAGE MILES",per)

df2=df[df["CATEGORY*"]=="Personal"]
m=df2["MILES*"].sum()
print(m)
per1= m/l *100
print("PERSONAL CATEGORY PERCENTAGE MILES",per1)


