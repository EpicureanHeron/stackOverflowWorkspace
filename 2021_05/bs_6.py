from bs4 import BeautifulSoup
import requests

page = requests.get('https://podcasts.apple.com/us/podcast/id979020229')
soup = BeautifulSoup(page.text, "html.parser")
eps = soup.find_all(class_ = 'tracks__track__link--block')
for a in eps:
    print(a.text)
    print(a['href'])


