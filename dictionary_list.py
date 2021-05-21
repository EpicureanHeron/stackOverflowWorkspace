# https://stackoverflow.com/questions/67629619/sum-values-of-duplicatecommon-keys-in-list-python/67629744#67629744
# https://stackoverflow.com/questions/67613336/aggregating-dicts-within-a-list-based-on-key-value
tax = [{'taxType': 'T1', 'amount': 140},{'taxType': 'T1', 'amount': 10}]


aggregated_data = {}

for dictionary in tax:
    key = (dictionary['taxType'])
   
    aggregated_data[key] = aggregated_data.get(key, 0) + dictionary['amount']
    

    tax = [{'taxType': key, 'amount': value} for key, value in aggregated_data.items()]

print(tax)