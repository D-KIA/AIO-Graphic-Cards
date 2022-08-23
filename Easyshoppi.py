#!/usr/bin/env python
# coding: utf-8

# In[2]:


import lxml
from csv import writer
from bs4 import BeautifulSoup
import requests


# ## Number Of pages

# In[4]:


def no_of_pages():
    url = 'https://www.easyshoppi.com/product-category/graphics-card/'
    re = requests.get(url)
    soup = BeautifulSoup(re.content,'lxml')
    
    #tags goes nav->input->max
    page_tag = soup.find('nav', class_='electro-advanced-pagination')      # has all page related info 
    page_no = page_tag.find('input')                                       # can enter page no here with a limit to max page
    max_page = page_no.get('max')                                         # gives us the maximum page number
    return int(max_page)


# ## Scraping From Easyshoppi

# In[12]:


def Easyshoppi():
    f = open('GPU Prices in India.csv', 'a', encoding='utf-8')
    thewriter = writer(f)
    url = 'https://www.easyshoppi.com/product-category/graphics-card/page/{}/'
    for n in range(1, no_of_pages()+1):
        page = url.format(n)
        try:
            re = requests.get(page)
            soup = BeautifulSoup(re.content, 'lxml')
            product_data_list = soup.find_all('div', class_="product-outer product-item__outer")
            for a in product_data_list:
                try:
                    if a.find('span', class_="wcosm_soldout onsale") == None:
                        product_name = a.find('h2', class_="woocommerce-loop-product__title").text
                        product_price = int(a.find('bdi').text[1:].replace(',',''))
                        for b in a.find_all('a', class_='woocommerce-LoopProduct-link woocommerce-loop-product__link'):
                            product_link = b.get('href')
                        content = [product_name, product_price, product_link, 'easyshoppi']
                        thewriter.writerow(content)
                except Exception as e:
                    print(a,'\n',e)
        except Exception as e:
            print('Easyshoppi',e)


# In[ ]:




