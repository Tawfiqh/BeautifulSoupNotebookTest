#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.starwars.com/news/star-wars-the-clone-wars-chronological-episodeorder/")

soup = BeautifulSoup(page.content)

# Print the first 950 chars of the page.
print(soup.prettify()[:950])


# In[3]:



print(soup.title.string)


# In[15]:



def begins_with_number(x):
    numbers = ["1","2","3","4","5","6","7","8","9","10"];
    return x[0] in numbers


def parse_detailed_info_page(url):
    
    #     request the page
    detail_page = requests.get(episode_detail_page_link)
    detail_soup = BeautifulSoup(detail_page.content)

#     description div has a quote and a description.
    description_div = detail_soup.find('div', class_="desc")
    
    
    start_quote_span = description_div.find('span', 'quote')
    if(start_quote_span):
        start_quote = start_quote_span.text
    else:
        start_quote = ""
        
    description = ""
    
#   first child is empty
#   2nd child is the quote
#   3rd child (index 2) is the description text. but it has some leading white-space.
    for index, child in enumerate(description_div.children):
        if(index==2):
            description = child.strip() 
            
    return (start_quote, str(description))



headers = ["ep_number", "episode_name", "episode_detail_page_link", "start_quote", "description"]

all_episodes = []

# for row in soup.find_all('td', class_="xl65")[0:3]:
for row in soup.find_all('td', class_="xl65"):
    if(row.string and begins_with_number(row.string)):
        ep_number = row.string
        a_link = row.parent.find("a")
        episode_name = a_link.text
        episode_detail_page_link = a_link['href']
        
        detail_page = requests.get(episode_detail_page_link)
        detail_soup = BeautifulSoup(detail_page.content)
        
        start_quote, description = parse_detailed_info_page(episode_detail_page_link)
                
        print(ep_number)
        print(episode_name)
        print(episode_detail_page_link)
        print(start_quote)
        print(description)

        episode = [ep_number, episode_name, episode_detail_page_link, start_quote, description]
        all_episodes.append(episode)
        print(" ")

    



# In[12]:


import pandas as pd

df = pd.DataFrame(all_episodes, columns=headers)
df.head()


# In[66]:





# In[ ]:




