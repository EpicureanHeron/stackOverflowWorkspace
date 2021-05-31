import os
import requests
from bs4 import BeautifulSoup

url_lst = [    'https://leg.mt.gov/bills/mca/title_0250/chapter_0190/part_0010/section_0010/0250-0190-0010-0010.html',
'https://leg.mt.gov/bills/mca/title_0250/chapter_0190/part_0010/section_0020/0250-0190-0010-0020.html',
'https://leg.mt.gov/bills/mca/title_0250/chapter_0190/part_0010/section_0030/0250-0190-0010-0030.html',
'https://leg.mt.gov/bills/mca/title_0250/chapter_0190/part_0010/section_0040/0250-0190-0010-0040.html',
'https://leg.mt.gov/bills/mca/title_0250/chapter_0190/part_0010/section_0050/0250-0190-0010-0050.html',
'https://leg.mt.gov/bills/mca/title_0250/chapter_0190/part_0010/section_0060/0250-0190-0010-0060.html',
'https://leg.mt.gov/bills/mca/title_0250/chapter_0190/part_0010/section_0070/0250-0190-0010-0070.html',
'https://leg.mt.gov/bills/mca/title_0250/chapter_0190/part_0010/section_0080/0250-0190-0010-0080.html',
'https://leg.mt.gov/bills/mca/title_0250/chapter_0190/part_0010/section_0090/0250-0190-0010-0090.html',
'https://leg.mt.gov/bills/mca/title_0250/chapter_0190/part_0010/section_0100/0250-0190-0010-0100.html',
'https://leg.mt.gov/bills/mca/title_0250/chapter_0190/part_0010/section_0110/0250-0190-0010-0110.html',
'https://leg.mt.gov/bills/mca/title_0250/chapter_0190/part_0010/section_0120/0250-0190-0010-0120.html',
'https://leg.mt.gov/bills/mca/title_0250/chapter_0190/part_0010/section_0130/0250-0190-0010-0130.html',
'https://leg.mt.gov/bills/mca/title_0250/chapter_0190/part_0010/section_0140/0250-0190-0010-0140.html',
'https://leg.mt.gov/bills/mca/title_0250/chapter_0190/part_0010/section_0150/0250-0190-0010-0150.html',
'https://leg.mt.gov/bills/mca/title_0250/chapter_0190/part_0010/section_0160/0250-0190-0010-0160.html'
    ]

new_url_list = []

for link in url_lst:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    href_elem = soup.find('div', class_='mca-content mca-toc')
    
    new_url_list.append(href_elem.text)
MyFile=open('output.txt','w', encoding='utf-8')

for link in new_url_list:
     MyFile.write(link)
MyFile.close()