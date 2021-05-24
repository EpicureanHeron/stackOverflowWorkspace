import csv
import requests 
comuni_URL = "https://raw.githubusercontent.com/FloraMarSS/Python/main/comuni_m.csv"
with requests.Session() as s:
    download = s.get(comuni_URL)
    comuni_m = [line.decode('utf-8') for line in download.iter_lines()]
    lettore = csv.reader(comuni_m, delimiter = ";")
    for row in lettore:
        if row != []:
            print(row[0])