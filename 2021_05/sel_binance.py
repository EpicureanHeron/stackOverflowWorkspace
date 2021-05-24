import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = "https://www.binance.com/en/markets"

response= requests.get(url)
soup = soup(response.content, "html.parser")


print(soup.text)
