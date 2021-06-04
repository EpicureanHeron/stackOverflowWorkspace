from bs4 import BeautifulSoup
import requests

# r = requests.get('https://www.milkround.com/jobs/graduate-software-engineer', headers = headers)
r = requests.get('https://www.milkround.com/jobs/graduate-software-engineer', headers={"content-type":"text"})

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'class':'col-xs-12 job-results clearfix'})

print(table)