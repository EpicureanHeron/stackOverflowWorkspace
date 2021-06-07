import re
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import datetime
import time
import random

linksfinal = []

for url in linksfinal: 
    
    results = requests.get(url)

    comms = []
    notes = []
    dates = []
    


    soup = BeautifulSoup(results.text, "html.parser")

    name = soup.find('h1', class_= '_1mTlpMC3').text.strip()

    commentary = soup.find_all('div', class_='_2wrUUKlw _3hFEdNs8')

    for container in commentary:

        comm  = container.find('q', class_ = 'IRsGHoPm').text.strip()
        comms.append(comm)


        comm1 = str(container.find("div", class_="nf9vGX55").find('span'))
        rat = re.findall(r'\d+', str(comm1))
        rat1 = (str(rat))[2]
        notes.append(rat1)

        time.sleep(3) 


    data = pd.DataFrame({
    'comms' : comms,
    'notes' : notes
    })


    data.to_csv(f"{name}.csv", sep=';', index=False)

    time.sleep(3)