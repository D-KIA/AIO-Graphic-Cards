#!/usr/bin/env python
# coding: utf-8

# ## Main Program

# In[ ]:


import csv
from MDComputers import MD_Scraping
from Easyshoppi import Easyshoppi
from AmazonScraping import Amazon
from VedantComputers import VedantComputers
from pcshop import pcshop


# ## Creating New CSV File

# In[ ]:


def new_csv():
    f = open('GPU Prices in India.csv', 'w', encoding='utf8')            ## opening file in write mode
    thewriter = csv.writer(f)
    headers = ['Name', 'Price', 'Link', 'Site']                          ## Adding Headers
    thewriter.writerow(headers)
new_csv()


# ## Scraping Data 

# In[ ]:


MD_Scraping()                        #from MD Computers
Easyshoppi()                         #from Easyshoppi
Amazon()                             #from Amazon
VedantComputers()                    #from Vedant Computers
pcshop()                             #from pcshop


# ## Search GPU

# In[ ]:


graphic_card = input('Enter Graphic Card Name: ')
f = open('GPU Prices in India.csv', 'r', encoding='utf8')
search_results = []
text = csv.reader(f)
dataset = list(text)
for x in dataset:
    if x != []:
        if graphic_card in x[0]:
            search_results.append(x)
for a in search_results:
    print(a)

