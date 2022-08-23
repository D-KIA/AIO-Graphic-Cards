#!/usr/bin/env python
# coding: utf-8

# ## Using selenium instead of requests as Amazon has bot set up

# In[1]:


import lxml
from csv import writer
from bs4 import BeautifulSoup
from selenium import webdriver


# ## Starting WebDriver

# In[2]:


driver = webdriver.Chrome()


# ## Page Number

# In[3]:


def no_of_pages():
    url = 'https://www.amazon.in/s?k=graphics+cards&i=computers&rh=n%3A1375354031&qid=1659451434&ref=sr_pg_1'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    page_no = soup.find('span', class_="s-pagination-item s-pagination-disabled").text
    return int(page_no)


# ## Scraping Amazon

# In[4]:


def Amazon():
    f = open('GPU Prices in India.csv', 'a', encoding='utf8')
    thewriter = writer(f)
    url = 'https://www.amazon.in/s?k=graphics+cards&i=computers&rh=n%3A1375354031&page={}&qid=1659451700&ref=sr_pg_2'
    for n in range(1, no_of_pages()+1):
        page = url.format(n)
        try:
            driver.get(page)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            product_list = soup.find_all('div', class_="a-section a-spacing-small a-spacing-top-small")
            for item in product_list:
                try:
                    if item.find('span', class_="a-size-medium a-color-base a-text-normal") != None:  
                        name = item.find('span', class_="a-size-medium a-color-base a-text-normal").text
                    else:
                        continue
                    if item.find('span', class_="a-price-whole") != None:
                        price = int(item.find('span', class_="a-price-whole").text.replace(',',''))
                    else:
                        price = None
                    link = 'https://www.amazon.in/'+item.find('a', class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal").get('href')
                    content = [name, price, link, 'Amazon']
                    thewriter.writerow(content)
                except Exception as e:
                        print(item,'\n',e)
        except Exception as e:
            print('Amazon', e)
    driver.close()
Amazon()


# In[ ]:




