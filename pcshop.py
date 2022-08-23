#!/usr/bin/env python
# coding: utf-8

# In[10]:


from csv import writer
import lxml
from bs4 import BeautifulSoup
import requests


# In[11]:


# No. of pages
def no_of_pages():
    url = 'https://www.pcshop.in/product-category/graphic-card/'
    try:
        re = requests.get(url)
        soup = BeautifulSoup(re.content, 'lxml')
        page_tag = soup.find('ul', class_="page-numbers")
        no_of_pages = page_tag.find_all('a', class_="page-numbers" )
        return int(no_of_pages[-2].text)
    except Exception as e:
        print(e)


# ## Scraping pcshop.in

# In[19]:


def pcshop():
    f = open('GPU Prices in India.csv', 'a', encoding='utf8')
    thewriter = writer(f)
    url = 'https://www.pcshop.in/product-category/graphic-card/page/{}/'
    for n in range(1, no_of_pages()+1):
        page = url.format(n)
        try:
            re = requests.get(page)
            soup = BeautifulSoup(re.content, 'lxml')
            product_list = soup.find_all('div', class_="product-inner product-item__inner")
            for item in product_list:
                try:
                    name = item.find('h2', class_="woocommerce-loop-product__title").text
                    if item.find('ins') != None:
                        price = int(item.find('ins').text[1:].replace(',',''))
                    else:
                        price = int(item.find('bdi').text[1:].replace(',',''))
                    link = item.find('a').get('href')
                    content = [name, price, link, 'pcshop']
                    thewriter.writerow(content)
                except Exception as e:
                    print(item, '\n', e)
        except Exception as e:
            print(e)


# In[ ]:





# In[ ]:




