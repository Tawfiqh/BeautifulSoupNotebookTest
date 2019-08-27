# BeautifulSoupNotebookTest
An example notebook and output of Beautiful soup running in a juypter notebook to quickly and easily manipulate a web page and extract some data.


## 1. Mozilla
The mozilla example extracts all the code snippets from the chosen mozilla web page.

Use case: we wanted to be able to see how to call websockets from a client application, the mozilla
documentation provides a good walktrhough with code snippets. All the code-blocks however are split 
up across the web-page though. 

Naturally all the code-blocks are nicely wrapped with `<pre>` tags. So we can extract them easily 
with BeautifulSoup

## 2. School of life.

Extract all the headings from this school of life article. 

We first observed that all the headings are wrapped in `<b>` or `<strong>` tags and begin with 
numbers.


Exported using:

``` fish
jupyter nbconvert Extract_heading_names_school_of_life.ipynb --to markdown; jupyter nbconvert Extract_heading_names_school_of_life.ipynb --to html; jupyter nbconvert Extract_heading_names_school_of_life.ipynb --to python
```
