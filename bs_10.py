from bs4 import BeautifulSoup
import requests

url = 'https://www.walmart.com/grocery/browse/Cereal-&-Breakfast-Food?aisle=1255027787111_1255027787501'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html')
product_list = soup.find_all('div')
# product_list = soup.find_all('div', class_='productListTile')
print(soup)