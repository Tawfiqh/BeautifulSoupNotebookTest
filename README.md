# BeautifulSoupNotebookTest
Some example notebooks and output of Beautiful soup running in juypter notebooks to quickly and 
easily manipulate web pages and extract data.

## 1. Wikipedia table 
Parsing a table from wikipedia - https://www.youtube.com/watch?v=Eoq8pTzNCsQ
The script automatically follows links in the source table to scrape extra details about each film in the table. 

Parses data from multiple Wikipedia pages into a Pandas dataframe and then outputs it to CSV. 

We use the example from wikipedia of Worldwide Top Grossing Films (https://en.wikipedia.org/wiki/List_of...) 📽💰 

The script automatically follows links in the source table to scrape extra details about each film in the table. 

The process uses some super simple and easy to set-up multi-threaded(using multiprocessing) to increase performance by about 5x.

The same process could be applied to any wikipedia table to both parse it and to also join extra data from linked data-sources.

## 2. Clone Wars

Same as above but parsing a table with TV-episodes of clone-wars, recursively follows links to the episode's detailed-page and pulls in extra episode info.



## 3. Mozilla
The mozilla example extracts all the code snippets from the chosen mozilla web page.

Use case: we wanted to be able to see how to call websockets from a client application, the mozilla
documentation provides a good walktrhough with code snippets. All the code-blocks however are split 
up across the web-page though. 

Naturally all the code-blocks are nicely wrapped with `<pre>` tags. So we can extract them easily 
with BeautifulSoup

## 4. School of life.

Extract all the headings from this school of life article. 

We first observed that all the headings are wrapped in `<b>` or `<strong>` tags and begin with 
numbers.


Exported using:

``` fish
jupyter nbconvert Extract_heading_names_school_of_life.ipynb --to markdown; jupyter nbconvert Extract_heading_names_school_of_life.ipynb --to html; jupyter nbconvert Extract_heading_names_school_of_life.ipynb --to python
```
