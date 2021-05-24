import csv

url_variables = [93939, 493943, 344454]

def change(var_data):
    var_data = str(var_data)
    url = 'https://www.example.com/api/index.php?pin='
    key = 'key=113494'
    new_url = f'{url}{var_data}&{key}'  
    return(new_url)

url_list = [change(x) for x in url_variables]

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for val in url_list:
        writer.writerow([val])