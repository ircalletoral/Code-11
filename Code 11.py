#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Checking working directory
import os 
import pandas as pd 

current_directory = os.getcwd()
print(current_directory)


# In[4]:


#change working directory
new_directory_path = r'C:\Users\Isaac\OneDrive\Desktop\USF\Fall 23\Python'
os.chdir(new_directory_path)


# In[6]:


updated_dir = os.getcwd()
print(updated_dir)


# In[8]:


file_path = 'Week13Assignment.txt'

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"file '{file_path}' not foung.")
except IOError:
    print("An error occurred while reading the file. ")


# In[12]:


#Average Age of Patients 
df = pd.read_csv(file_path)


# In[13]:


print(df)


# In[14]:


print(df.columns)


# In[15]:


#Average Age
average_age = df[' Age'].mean()
print(average_age)


# In[17]:


#Number of Male and Female Patients 
male = (df[" Gender"] == ' Male').sum()
female = (df[" Gender"]== ' Female').sum()
print(f"The number of male patients is: {male}. The number of female patients is {female}.")


# In[20]:


#Highest Blood Pressure 
max_bp = max(df[" BloodPressure"])
print(f"The highest Blood Pressure is: {max_bp}.")


# In[22]:


#Lowest Blood Pressure 
min_bp = min(df[" BloodPressure"])
print(f"The Lowestr Blood Pressure is {min_bp}.")


# In[24]:


#Average Body Temperature of Patients
av_temp = df[" Temperature"].mean()
print(f"The average temperature of the patients is: {av_temp} degrees Celcius.")


# In[ ]:




