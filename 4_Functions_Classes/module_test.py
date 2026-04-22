#!/usr/bin/env python
# coding: utf-8

# In[9]:


def course(subjects):
    for course in subjects:
        print(course)


# In[6]:


def mfunc(friends):
    for name in friends:
        print(name.title()+" is my best friend!")


# In[7]:


def my_function(food):
    for x in food:
        print(x)


# In[8]:


def namecity(first_name,last_name,country,gender):
    full_name=first_name +" " + last_name
    personai_info={'full_name':first_name +" " + last_name,'place':country,'M_or_W':gender}
    return personai_info

