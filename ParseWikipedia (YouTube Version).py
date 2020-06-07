#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests

page = requests.get("https://en.wikipedia.org/wiki/List_of_highest-grossing_films")
soup = BeautifulSoup(page.content)

print(soup.prettify()[:1000])


# In[2]:


print(soup.title.string)


# In[3]:


film_table = soup.find("table", class_="wikitable")

def clean_string(string):
    if string:
        cleaned_string = string.strip().replace('\n', ' ').strip();
        return cleaned_string
    
    return string

all_results = [];

for row in film_table.find_all("tr"):
    columns = row.find_all(["td", "th"])
    if(columns[0].get("scope")):
        continue;
        
    rank = clean_string(columns[0].text)
    title = clean_string(columns[2].text)
    grossing = clean_string(columns[3].text)
    year = clean_string(columns[4].text)
    
    link_anchor = columns[2].find("a")
    if(link_anchor):
        link_detail = clean_string(link_anchor['href'])
    
    result = (rank, title, link_detail, grossing, year)
    all_results.append(result)

print(all_results)


# In[4]:


import pandas as pd

headers = ['rank', 'Title', 'link_detail', "Worldwide gross ($USD)", "Year"]

df = pd.DataFrame(all_results, columns=headers)

df.head(50)


# In[5]:


def from_details_get_film_description(soup):

    main_content = soup.find(class_="mw-parser-output")
    description = ""
    for child in main_content.children:
        if(child.name == "h2"):
            break;
        if(child.name == "p"):
            description += "\n" + child.text

    description = description.strip()
#     print(description)
    return description


def from_details_get_film_director(soup):

    main_content = soup.find("table",  class_="infobox")
    for table_row in main_content.find_all("tr"):
        header = table_row.find('th')
        if(header and header.text == "Directed by"):
            column = table_row.find("td");
            director = clean_string(column.text)
            return director




def get_film_details(detail_url):

    page = requests.get("https://en.wikipedia.org"+detail_url)
    soup = BeautifulSoup(page.content)


    description = from_details_get_film_description(soup)
    director = from_details_get_film_director(soup)
    result = (description, director)
    return result




df["link_detail"].sample(1).map(get_film_details)


# In[6]:


from time import perf_counter

time1 = perf_counter()

result = df["link_detail"].map(get_film_details)

time2 = perf_counter()

print("time taken:", time2-time1)


# In[7]:


df['description'], df['director'] = zip(*result)

df.head()


# In[8]:


import multiprocessing as mp
time1 = perf_counter()

with mp.Pool(mp.cpu_count()) as pool:
    threaded_result = pool.map(get_film_details, df["link_detail"])

time2 = perf_counter()

print("time taken:", time2-time1)

df['description'], df['director'] = zip(*threaded_result)


# In[9]:


df.head(50)


# In[10]:


df.to_csv("Top grossing films.csv", columns=["rank", "Title", "Worldwide gross ($USD)" , "Year","description", "director"])


# In[ ]:




