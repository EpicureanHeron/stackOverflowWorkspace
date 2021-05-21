# https://stackoverflow.com/questions/67527879/python-indexerror-list-index-out-of-range-data-scraping/67528008#67528008

import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

file_name = input("name file: ")
distance = input("distance: ")

for x in range(1):
    url_main = 'https://weedmaps.com/search?entryType=home%20page%20product%20card&filter%5BboundingRadius%5D=' + distance + 'mi&page='
    uClient = uReq(url_main + str(x))
    page_html = uClient.read()
    #uClient.close()
    page_soup = soup(page_html, "html.parser")
   
    filename = file_name + ".csv"
    f = open(filename, "w") git 
    headers = "product \n"
    f.write(headers)
  
    # containers = page_soup.findAll("div", {"data-testid": "serp-item-name"}) 
    containers = page_soup.findAll("div") 
    # containers = page_soup.findAll("div", {"class": "details"}) 
    print(containers)
    contain = containers[0]
    container = containers[0]
    for contain in container:
        product = contain.div.div.div.div.a
        the_product = product.text
        print("product" + " " + the_product)

        f.write(the_product + "," + "\n")