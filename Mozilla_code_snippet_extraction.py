#!/usr/bin/env python
# coding: utf-8

# # Get Code Snippets from Mozilla page
# 
# We want to be able to see how to call websockets from a client application but all the code blocks are split up on the web-page itself.
# 
# This simple script just extracts all the JS code from the page and outputs it here so that it can easily be copied to some JS source code and run.

# In[13]:


from bs4 import BeautifulSoup

import requests

url = "https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications"

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('pre'):
    print(link.string)


# In[ ]:




