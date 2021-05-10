# https://stackoverflow.com/questions/67471386/how-to-filter-values-in-nested-dicts-which-are-in-list/67471581#67471581

content = [
{'@type': 'ListItem', 'position': 1, 
   'item': 
    {'@type': 'Product', 'url': 'TestSample', 'sku': 'HO6096863EAD7E0PH', 'mpn': 'HO6096863EAD7E0PH', '@id': 'HO6096863EAD7E0PH'}},
 {'@type': 'ListItem', 'position': 2, 
   'item': 
    {'@type': 'Product', 'url': 'TestSample', 'sku': 'HO5FFFA64882401PH', 'mpn': 'HO5FFFA64882401PH', '@id': 'HO5FFFA64882401PH'}}
]

for d in content:
    for key, value in d.items():
        if key == "item":
            for key1, value1 in value.items():
                if key1 == 'url':
                    print(value1)