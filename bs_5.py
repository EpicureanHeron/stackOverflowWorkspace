from bs4 import BeautifulSoup
import requests

url = 'https://www.econjobrumors.com/topic/supreme-court-to-%e2%80%9cconsider%e2%80%9d-taking-up-harvard-affirmative-action-case-on-june-10'  

r = requests.get(url, allow_redirects=False) 

soup = BeautifulSoup(r.content, 'lxml')  

print(soup)