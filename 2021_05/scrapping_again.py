from urllib.request import urlopen
import re

allpages = ["https://www.metrolyrics.com/bob-dylan-alpage-1.html", "https://www.metrolyrics.com/bob-dylan-alpage-2.html", "https://www.metrolyrics.com/bob-dylan-alpage-3.html", "https://www.metrolyrics.com/bob-dylan-alpage-4.html", "https://www.metrolyrics.com/bob-dylan-alpage-5.html", "https://www.metrolyrics.com/bob-dylan-alpage-6.html", "https://www.metrolyrics.com/bob-dylan-alpage-7.html", "https://www.metrolyrics.com/bob-dylan-alpage-8.html", "https://www.metrolyrics.com/bob-dylan-alpage-9.html", "https://www.metrolyrics.com/bob-dylan-alpage-10.html", "https://www.metrolyrics.com/bob-dylan-alpage-11.html"]

scrapped_list = []

for i in allpages:
     print(i)
     page = urlopen(i)
     html_bytes = page.read()
     html = html_bytes.decode("utf-8")
     start_index = html.find("</div><!-- END: Top Songs -->")
     end_index = html.find("</div><!-- END: lyrics -->")
     clean = html[start_index:end_index]
     scrapped_list.append(clean)

MyFile=open('output.txt','w', encoding='utf-8')
for lyrics in scrapped_list:
    print(lyrics)
    MyFile.write(lyrics)
MyFile.close()