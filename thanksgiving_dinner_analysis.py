
# coding: utf-8

# In[27]:


import pandas
data = pandas.read_csv("thanksgiving.csv", encoding="Latin-1")
data.head(5)


# In[16]:


column_names = data.columns
column_names


# In[17]:


celebrating_thanksgiving_cat = data["Do you celebrate Thanksgiving?"].value_counts()
celebrating_thanksgiving_cat


# In[18]:


do_celebrate_thanksgiving = data[data["Do you celebrate Thanksgiving?"] == "Yes"]
do_celebrate_thanksgiving


# In[19]:


data["What is typically the main dish at your Thanksgiving dinner?"].value_counts()


# In[20]:


data[data["What is typically the main dish at your Thanksgiving dinner?"] == "Tofurkey"]["Do you typically have gravy?"]


# In[21]:


apple_isnull = pandas.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"])
pumpkin_isnull = pandas.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"])
pecan_isnull = pandas.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"])

ate_pies = apple_isnull & pumpkin_isnull & pecan_isnull
ate_pies.value_counts()


# In[29]:


def convert_age(age_range):
    if pandas.isnull(age_range):
        return None
    else:
        age_range = age_range.split(" ")[0]
        age_range = age_range.replace("+", "")
        age_range = int(age_range)
        
    return age_range

data["int_age"] = data["Age"].apply(convert_age)
data["int_age"].describe()


# In[ ]:


# Based on the findings, we can see that the data skews downward because we took the very first value in each string


# In[31]:


def convert_income(income_range):
    if pandas.isnull(income_range):
        return None
    else:
        income_range = income_range.split(" ")[0]
        if income_range == "Prefer":
            return None
        income_range = income_range.replace("$","")
        income_range = income_range.replace(",","")
        income_range = int(income_range)
    return income_range

data["int_income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(convert_income)
data["int_income"].describe()


# In[32]:


data[data["int_income"] < 150000]["How far will you travel for Thanksgiving?"].value_counts()


# In[33]:


data[data["int_income"] > 150000]["How far will you travel for Thanksgiving?"].value_counts()


# In[34]:


import numpy as np
data.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", columns='Have you ever attended a "Friendsgiving?"', values = "int_age", aggfunc = np.mean)


# In[35]:


data.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", columns='Have you ever attended a "Friendsgiving?"', values = "int_income", aggfunc = np.mean)

