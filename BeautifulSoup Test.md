
Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/


```python
from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.theschooloflife.com/thebookoflife/cultural-consolation/")

soup = BeautifulSoup(page.content)

print(soup.prettify()[:950])

```

    <!DOCTYPE html>
    <html>
     <head>
      <title>
       Cultural Consolation - The Book of LifeThe Book of Life
      </title>
      <!-- Google Tag Manager -->
      <script>
       (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
                    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
                j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
                'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
            })(window,document,'script','dataLayer','GTM-W4M4CVQ');
      </script>
      <!-- End Google Tag Manager -->
      <meta content="Cultural Consolation - The Book of Life is the 'brain' of The School of Life, a gathering of the best ideas around wisdom and emotional intelligence.
    " name="description"/>
      <meta charset="utf-8"/>
      <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
      <meta content="true" http-equiv="ClearType"/>
      <meta content="Phil



```python
print(soup.title.string)
```

    
            Cultural Consolation - The Book of LifeThe Book of Life    



```python
def begins_with_number(x):
    numbers = ["1","2","3","4","5","6","7","8","9","10"];
    return x[0] in numbers

for link in soup.find_all(['b', 'strong']):
    x= link.string
    
    if(x and begins_with_number(x)):
        print(x)

    
```

    1. Introduction
    2. Companionship
    3.
    4. Balance
    5. Compassion
    6. Knowledge
    7. Encouragement
    8. Appreciation
    9. Perspective
    10. Conclusion



```python
for link in soup.find_all('a'):
    print(link.get('href'))
```

    https://www.theschooloflife.com
    https://www.theschooloflife.com/events
    https://www.theschooloflife.com/business
    https://www.theschooloflife.com/therapy
    https://www.theschooloflife.com/about-us
    https://www.youtube.com/theschooloflifetv
    https://www.theschooloflife.com/shop/
    https://www.theschooloflife.com/thebookoflife/
    https://www.theschooloflife.com/thebookoflife/what-is-the-book-of-life/
    https://www.facebook.com/theschooloflifelondon/
    https://twitter.com/TheSchoolOfLife
    https://www.theschooloflife.com/thebookoflife/category/relationships/
    https://www.theschooloflife.com/thebookoflife/category/work/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/
    https://www.theschooloflife.com/thebookoflife/category/sociability/
    https://www.theschooloflife.com/thebookoflife/category/calm/
    https://www.theschooloflife.com/thebookoflife/category/leisure/
    https://www.theschooloflife.com/thebookoflife/category/relationships/?index
    https://www.theschooloflife.com/thebookoflife/category/relationships/romanticism/
    https://www.theschooloflife.com/thebookoflife/category/relationships/finding-love/
    https://www.theschooloflife.com/thebookoflife/category/relationships/dating/
    https://www.theschooloflife.com/thebookoflife/category/relationships/compatibility/
    https://www.theschooloflife.com/thebookoflife/category/relationships/sex/
    https://www.theschooloflife.com/thebookoflife/category/relationships/conflicts/
    https://www.theschooloflife.com/thebookoflife/category/relationships/mature-love/
    https://www.theschooloflife.com/thebookoflife/category/relationships/breaking-up-heartbreak/
    https://www.theschooloflife.com/thebookoflife/category/relationships/marriage/
    https://www.theschooloflife.com/thebookoflife/category/relationships/affairs/
    https://www.theschooloflife.com/thebookoflife/category/relationships/parenting/
    https://www.theschooloflife.com/thebookoflife/category/work/?index
    https://www.theschooloflife.com/thebookoflife/category/work/meaning/
    https://www.theschooloflife.com/thebookoflife/category/work/purpose/
    https://www.theschooloflife.com/thebookoflife/category/work/good-work/
    https://www.theschooloflife.com/thebookoflife/category/work/business-skills/
    https://www.theschooloflife.com/thebookoflife/category/work/sorrows-of-work/
    https://www.theschooloflife.com/thebookoflife/category/work/consumption-and-need/
    https://www.theschooloflife.com/thebookoflife/category/work/status-and-success/
    https://www.theschooloflife.com/thebookoflife/category/work/capitalism/
    https://www.theschooloflife.com/thebookoflife/category/work/media-and-technology/
    https://www.theschooloflife.com/thebookoflife/category/work/politics-government/
    https://www.theschooloflife.com/thebookoflife/category/work/utopia/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/?index
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/know-yourself/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/mood/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/behaviours/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/emotional-skills/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/fulfilment/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/growth-maturity/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/fear-insecurity/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/trauma-childhood/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/questionnaires/
    https://www.theschooloflife.com/thebookoflife/category/sociability/?index
    https://www.theschooloflife.com/thebookoflife/category/sociability/social-virtues/
    https://www.theschooloflife.com/thebookoflife/category/sociability/confidence/
    https://www.theschooloflife.com/thebookoflife/category/sociability/friendship/
    https://www.theschooloflife.com/thebookoflife/category/sociability/communication/
    https://www.theschooloflife.com/thebookoflife/category/calm/?index
    https://www.theschooloflife.com/thebookoflife/category/calm/anxiety/
    https://www.theschooloflife.com/thebookoflife/category/calm/serenity/
    https://www.theschooloflife.com/thebookoflife/category/calm/perspective/
    https://www.theschooloflife.com/thebookoflife/category/leisure/?index
    https://www.theschooloflife.com/thebookoflife/category/leisure/travel/
    https://www.theschooloflife.com/thebookoflife/category/leisure/food/
    https://www.theschooloflife.com/thebookoflife/category/leisure/culture/
    https://www.theschooloflife.com/thebookoflife/category/leisure/western-philosophy/
    https://www.theschooloflife.com/thebookoflife/category/leisure/eastern-philosophy/
    https://www.theschooloflife.com/thebookoflife/category/leisure/psychotherapy/
    https://www.theschooloflife.com/thebookoflife/category/leisure/political-theory/
    https://www.theschooloflife.com/thebookoflife/category/leisure/literature/
    https://www.theschooloflife.com/thebookoflife/category/leisure/sociology/
    https://www.theschooloflife.com/thebookoflife/category/leisure/artarchitecture/
    https://www.theschooloflife.com/thebookoflife/category/leisure/small-pleasures/
    https://www.theschooloflife.com/thebookoflife/
    https://www.theschooloflife.com/thebookoflife/
    https://www.theschooloflife.com/thebookoflife/category/relationships/
    https://www.theschooloflife.com/thebookoflife/category/relationships/?index
    https://www.theschooloflife.com/thebookoflife/category/relationships/romanticism/
    https://www.theschooloflife.com/thebookoflife/category/relationships/finding-love/
    https://www.theschooloflife.com/thebookoflife/category/relationships/dating/
    https://www.theschooloflife.com/thebookoflife/category/relationships/compatibility/
    https://www.theschooloflife.com/thebookoflife/category/relationships/sex/
    https://www.theschooloflife.com/thebookoflife/category/relationships/conflicts/
    https://www.theschooloflife.com/thebookoflife/category/relationships/mature-love/
    https://www.theschooloflife.com/thebookoflife/category/relationships/breaking-up-heartbreak/
    https://www.theschooloflife.com/thebookoflife/category/relationships/marriage/
    https://www.theschooloflife.com/thebookoflife/category/relationships/affairs/
    https://www.theschooloflife.com/thebookoflife/category/relationships/parenting/
    https://www.theschooloflife.com/thebookoflife/category/work/
    https://www.theschooloflife.com/thebookoflife/category/work/?index
    https://www.theschooloflife.com/thebookoflife/category/work/meaning/
    https://www.theschooloflife.com/thebookoflife/category/work/purpose/
    https://www.theschooloflife.com/thebookoflife/category/work/good-work/
    https://www.theschooloflife.com/thebookoflife/category/work/business-skills/
    https://www.theschooloflife.com/thebookoflife/category/work/sorrows-of-work/
    https://www.theschooloflife.com/thebookoflife/category/work/consumption-and-need/
    https://www.theschooloflife.com/thebookoflife/category/work/status-and-success/
    https://www.theschooloflife.com/thebookoflife/category/work/capitalism/
    https://www.theschooloflife.com/thebookoflife/category/work/media-and-technology/
    https://www.theschooloflife.com/thebookoflife/category/work/politics-government/
    https://www.theschooloflife.com/thebookoflife/category/work/utopia/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/?index
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/know-yourself/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/mood/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/behaviours/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/emotional-skills/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/fulfilment/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/growth-maturity/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/fear-insecurity/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/trauma-childhood/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/questionnaires/
    https://www.theschooloflife.com/thebookoflife/category/sociability/
    https://www.theschooloflife.com/thebookoflife/category/sociability/?index
    https://www.theschooloflife.com/thebookoflife/category/sociability/social-virtues/
    https://www.theschooloflife.com/thebookoflife/category/sociability/confidence/
    https://www.theschooloflife.com/thebookoflife/category/sociability/friendship/
    https://www.theschooloflife.com/thebookoflife/category/sociability/communication/
    https://www.theschooloflife.com/thebookoflife/category/calm/
    https://www.theschooloflife.com/thebookoflife/category/calm/?index
    https://www.theschooloflife.com/thebookoflife/category/calm/anxiety/
    https://www.theschooloflife.com/thebookoflife/category/calm/serenity/
    https://www.theschooloflife.com/thebookoflife/category/calm/perspective/
    https://www.theschooloflife.com/thebookoflife/category/leisure/
    https://www.theschooloflife.com/thebookoflife/category/leisure/?index
    https://www.theschooloflife.com/thebookoflife/category/leisure/travel/
    https://www.theschooloflife.com/thebookoflife/category/leisure/food/
    https://www.theschooloflife.com/thebookoflife/category/leisure/culture/
    https://www.theschooloflife.com/thebookoflife/category/leisure/western-philosophy/
    https://www.theschooloflife.com/thebookoflife/category/leisure/eastern-philosophy/
    https://www.theschooloflife.com/thebookoflife/category/leisure/psychotherapy/
    https://www.theschooloflife.com/thebookoflife/category/leisure/political-theory/
    https://www.theschooloflife.com/thebookoflife/category/leisure/literature/
    https://www.theschooloflife.com/thebookoflife/category/leisure/sociology/
    https://www.theschooloflife.com/thebookoflife/category/leisure/artarchitecture/
    https://www.theschooloflife.com/thebookoflife/category/leisure/small-pleasures/
    https://www.theschooloflife.com/thebookoflife/?s=
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/emotional-skills/
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image29.jpg
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image151.jpg
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image21.jpg
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image24.png
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image01.jpg
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image18.jpg
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image10.png
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image051.jpg
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image13.jpg
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image19.png
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image04.jpg
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image23.jpg
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image17.png
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image141.jpg
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image061.jpg
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image22.jpg
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image02-15.41.17.png
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image091.png
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image20.png
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image12.png
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image25.png
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image11.jpg
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image28.png
    http://www.thebookoflife.org/wp-content/uploads/2016/12/image001.png
    http://www.thebookoflife.org/wp-content/uploads/2016/12/image051.png
    http://www.thebookoflife.org/wp-content/uploads/2016/12/image01.png
    http://www.thebookoflife.org/wp-content/uploads/2016/12/image02.png
    http://www.thebookoflife.org/wp-content/uploads/2016/12/image04.jpg
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image26.jpg
    http://www.thebookoflife.org/wp-content/uploads/2014/03/image031.png
    https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.theschooloflife.com%2Fthebookoflife%2Fcultural-consolation%2F&linkname=Cultural%20Consolation
    https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.theschooloflife.com%2Fthebookoflife%2Fcultural-consolation%2F&linkname=Cultural%20Consolation
    https://www.addtoany.com/add_to/email?linkurl=https%3A%2F%2Fwww.theschooloflife.com%2Fthebookoflife%2Fcultural-consolation%2F&linkname=Cultural%20Consolation
    https://www.addtoany.com/add_to/print?linkurl=https%3A%2F%2Fwww.theschooloflife.com%2Fthebookoflife%2Fcultural-consolation%2F&linkname=Cultural%20Consolation
    #top
    https://www.theschooloflife.com/thebookoflife/helping-our-partners/
    https://www.theschooloflife.com/thebookoflife/helping-our-partners/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/
    https://www.theschooloflife.com/thebookoflife/whats-wrong-with-needy-people/
    https://www.theschooloflife.com/thebookoflife/whats-wrong-with-needy-people/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/
    https://www.theschooloflife.com/thebookoflife/self-love/
    https://www.theschooloflife.com/thebookoflife/self-love/
    https://www.theschooloflife.com/thebookoflife/category/self-knowledge/
    /
    https://theschooloflife.us5.list-manage.com/subscribe/post?u=ac2881538168a724cf44bca81&id=717e06d46b&SIGNUP=tbol
    http://www.theschooloflife.com/
    https://theschooloflife.us5.list-manage.com/subscribe/post?u=ac2881538168a724cf44bca81&id=717e06d46b&SIGNUP=tbol
    https://www.theschooloflife.com/thebookoflife/what-is-the-book-of-life/
    https://www.theschooloflife.com/thebookoflife/newsletter/
    https://twitter.com/TheSchoolOfLife
    https://theschooloflife.com/shop
    https://www.theschooloflife.com

