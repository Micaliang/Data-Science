#!/usr/bin/env python
# coding: utf-8

# In[2]:


def make_car(manufacturer,model,**car_infos):
    car_dict={}
    car_dict['manufacturer']=manufacturer
    car_dict['model']=model

    for key,value in car_infos.items():
        car_dict[key]=value
    return car_dict


# In[3]:


def sandwich(*toppings):
    print("\n Making a andwich witn the following toppings:")
    for topping in toppings:
        print("- " + topping)


# In[4]:


def make_pizza(size,*toppings):
    print("\nMaking a " + str(size) + "-inch pizza witn the following toppings:")
    for topping in toppings:
        print("- " + topping)


# In[6]:


def show_magicians(names):
    for name in names:
        print(name.title())

def make_great(names):
    great_magicians = []
    
    while names:
        current_magician = names.pop()
        great_magician = "the Great " + current_magician
        great_magicians.append(great_magician)
    
    # 倒序放回去，保持原来顺序
    while great_magicians:
        names.append(great_magicians.pop())


# In[ ]:




