#!/usr/bin/env python
# coding: utf-8

# Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# In[35]:


from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.theschooloflife.com/thebookoflife/cultural-consolation/")

soup = BeautifulSoup(page.content)

print(soup.prettify()[:950])


# In[13]:


print(soup.title.string)


# In[39]:


def begins_with_number(x):
    numbers = ["1","2","3","4","5","6","7","8","9","10"];
    return x[0] in numbers

for link in soup.find_all(['b', 'strong']):
    x= link.string
    
    if(x and begins_with_number(x)):
        print(x)

    


# In[14]:


for link in soup.find_all('a'):
    print(link.get('href'))

