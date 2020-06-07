#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
import requests

page = requests.get("https://en.wikipedia.org/wiki/List_of_highest-grossing_films")

soup = BeautifulSoup(page.content)

# Print the first 950 chars of the page.
print(soup.prettify()[:950])


# In[5]:


print(soup.title.string)


# In[7]:


film_table = soup.find("table", class_="wikitable")

def clean_string(string):
    if(string):
        cleaned_string = string.replace('\n', ' ').replace('\r', '').strip();
        return cleaned_string;

    return string;


all_results = [] #add at end


for row in film_table.find_all("tr"):
    columns = row.find_all(["td", "th"])
    if(columns[0].get("scope")):
        continue
    rank = clean_string(columns[0].text)
    
    
    title = clean_string(columns[2].text)

    link_to_detail = columns[2].find("a")['href']
    
    gross = clean_string(columns[3].text)
    
    year = clean_string(columns[4].text)
    
    result = (rank, title, link_to_detail, gross, year)
    all_results.append(result)

    
print(all_results)


# In[8]:


import pandas as pd

df = pd.DataFrame(all_results, columns=['Rank', 'Film', 'link', 'Worldwide gross ($USD)', "Year"])

df.head() # can remove rank here.


# In[9]:



def from_details_get_description(soup):
    main_content = soup.find(class_="mw-parser-output")
    description = ""
    for child in main_content.children:
        if(child.name == "p"):
            description+= "\n" + child.text
        if(child.name == "h2"):
            break
    description = description.strip()
    return description



def from_details_get_director(soup):
    main_content = soup.find(class_="infobox")
    table_rows = main_content.find_all("tr")

    for row in table_rows:
        header = row.find('th')
        if(header and header.text == "Directed by"):
            column  = row.find('td')
            director = clean_string(column.text)
            return director
    



def get_film_details(film_url):
    
    page = requests.get("https://en.wikipedia.org/" + film_url)

    soup = BeautifulSoup(page.content)
    
    description = from_details_get_description(soup);
#     print(description)

    director = from_details_get_director(soup);
#     print(director)
    return (description, director)
    
        
        

    
result = df['link'].sample(2).map(get_film_details)


# In[10]:


from time import perf_counter 


# In[11]:


time1 = perf_counter()

result = df['link'].map(get_film_details)
df['description'], df['director'] = zip(*result) 

display(df)

time2 = perf_counter()

print("Method1 time_taken: ", time2-time1)


# In[12]:


import multiprocessing as mp


time1 = perf_counter()


with mp.Pool(mp.cpu_count()) as pool:
    result = pool.map(get_film_details, df['link'])

df['description'], df['director'] = zip(*result) 

display(df)

time2 = perf_counter()

print("Method2 time_taken: ", time2-time1)


# In[14]:


df.to_csv("Top_grossing_films.csv", columns = ['Film', "Worldwide gross ($USD)", "Year", "description", "director" ])


# In[16]:


# How many cpu's does this machine actually have
print(mp.cpu_count())

