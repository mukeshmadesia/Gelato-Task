#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install Faker


# In[2]:


from faker import Faker
class SampleData:
    
    
    def __init__(self,n):
        
        self.m = n
        
        createid(self.m)

    

    def createid(m):
        fake = Faker()
        fake.seed_instance(2)
        datalist = []
        
        for x in range(m):
            firstname = fake.first_name()
            lastname = fake.last_name()
            country = fake.country()
            city  = fake.city()
            email = fake.email()
            Id = fake.random_int(100000000, 999999999)

            data = firstname+ ',' +lastname+',' + country+','+ city+','+ email+','+ str(Id)
            datalist.append(data)
        return datalist


# In[3]:


data = SampleData.createid(3)


# In[4]:


data


# In[ ]:




