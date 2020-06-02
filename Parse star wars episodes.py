#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.starwars.com/news/star-wars-the-clone-wars-chronological-episodeorder/")

soup = BeautifulSoup(page.content)

# Print the first 950 chars of the page.
print(soup.prettify()[:950])


# In[2]:



print(soup.title.string)


# In[26]:



def begins_with_number(x):
    numbers = ["1","2","3","4","5","6","7","8","9","10"];
    return x[0] in numbers


headers = ["episode_code", "season","episode_number", "episode_name", "episode_detail_page_link"]

all_episodes = []

# for row in soup.find_all('td', class_="xl65")[0:3]:
for row in soup.find_all('td', class_="xl65"):
    if(row.string and begins_with_number(row.string)):
        ep_code = row.string
        season = ep_code[0]
        ep_number = int(ep_code[1:])
        
        a_link = row.parent.find("a")
        episode_name = a_link.text
        episode_detail_page_link = a_link['href']
                        
        print(ep_code,":", season, "-", ep_number)


        print(episode_name)
        print(episode_detail_page_link)

        episode = [ep_code,season, ep_number, episode_name, episode_detail_page_link]
        all_episodes.append(episode)
        print(" ")

        
        


# In[27]:


import pandas as pd

df = pd.DataFrame(all_episodes, columns=headers)
df.head()


# In[5]:


def clean(text):
    if(not text):
        return text

    cleaned = text.strip().replace('\n', ' ').replace('\r', '')
    return cleaned
    

def parse_detailed_info_page(url):
    
    #     request the page
    detail_page = requests.get(url)
    detail_soup = BeautifulSoup(detail_page.content)

    #description div has a quote and a description.
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
            
    if((not start_quote) and (not description)):
        description = description_div.text.strip()
       
    #print((start_quote, str(description)))
    return (clean(start_quote), clean(description))


# Test the function works on a few examples
df["episode_detail_page_link"].sample(n=3).map(parse_detailed_info_page)


# In[6]:


# Multi-thread it to apply it quickly across the dataframe and run requests in parallel.
import multiprocessing as mp
with mp.Pool(mp.cpu_count()) as pool:
    quotes_and_description = pool.map(parse_detailed_info_page, df["episode_detail_page_link"])


# In[28]:


df2 = df
df2['quote'], df2['description'] = zip(*quotes_and_description)
df2.head()


# In[29]:


display(df2)
df2.to_csv("clone_wars_episode_guide.csv")


# In[14]:


ep_code = "201"


# In[15]:


season = ep_code[0]


# In[22]:


print(season)
print(int(ep_code[1:]))


# In[ ]:




