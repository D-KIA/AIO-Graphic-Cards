#!/usr/bin/env python
# coding: utf-8

# ## Scraping from MD Computers

# In[1]:


import requests
from bs4 import BeautifulSoup
import lxml
import csv


# In[2]:


# No of pages
def no_of_pages():
    l = []
    url = 'https://mdcomputers.in/graphics-card?page=1'
    re = requests.get(url)
    soup = BeautifulSoup(re.content,'lxml')
    pages_class = soup.find('ul', class_='pagination')
    pages = pages_class.find_all('li')
    for x in pages:
        l.append(pages)
    return len(l)-2


# In[5]:


def MD_Scraping():
    f = open('GPU Prices in India.csv', 'a', encoding='utf8')
    thewriter = csv.writer(f)
    url = 'https://mdcomputers.in/graphics-card?page={}'
    for n in range(1, no_of_pages()+1):
        page = url.format(n)
        try:
            re = requests.get(page)
            soup = BeautifulSoup(re.text,'lxml')
            all_product = soup.find_all('div',attrs= {'class' : "product-item-container"})
            for product in all_product:
                name = product.find('h4').text
                price = int(product.find('span', attrs = {'class' : 'price-new'}).text[1:].replace(',',''))
                for link in product.find_all('a'):
                    source = link.get('href')
                try:
                    content = [name, price, source, 'MD Computers']
                    thewriter.writerow(content)
                except Exception as e:
                    print(product,"\n",e)
        except Exception as e:
            print(e)


# In[ ]:




