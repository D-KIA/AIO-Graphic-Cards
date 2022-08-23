#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv
from bs4 import BeautifulSoup
import lxml
import requests


# ## Page count

# In[5]:


def no_of_pages():
    url = 'https://www.vedantcomputers.com/pc-components/graphics-card'
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    page_tag = soup.find('ul', class_='pagination')
    max_pages = len(page_tag.find_all('li'))-2
    return max_pages


# ## Prototype

# In[ ]:


def VedantComputers():
    f = open('GPU Prices in India.csv', 'a', encoding='utf8')
    thewriter = csv.writer(f)
    url = 'https://www.vedantcomputers.com/pc-components/graphics-card?page={}'
    try:
        for n in range(1,no_of_pages()+1):
            page = url.format(n)
            re = requests.get(page)
            soup = BeautifulSoup(re.content, 'lxml')
            product_list = soup.find_all('div', class_='caption')
            price_list = []
            for item in product_list:
                try:
                    name = item.find('div', class_='name').text
                    if item.find('span', class_='price-new') != None:
                        price = int(item.find('span', class_='price-new').text[1:].replace(',', ''))                    
                    else:
                        price = int(item.find('span', class_='price-normal').text[1:].replace(',', ''))
                    link = item.find('a').get('href')
                    content = [name, price, link, 'Vedant Computers']
                    thewriter.writerow(content)
                except Exception as e:
                    print(item,'\n',e)
    except Exception as e:
        print('VedantComputers ', e)

