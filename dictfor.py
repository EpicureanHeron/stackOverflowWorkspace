# https://stackoverflow.com/questions/67432748/python-for-loop-prints-horizontal-line

import pandas as pd

df = pd.read_csv('climate_data_Dec2017.csv')

col = ['State','9am relative humidity (%)']

hum = df[col]

grouped_by_state = hum.groupby('State')

max_hum = grouped_by_state.max()

dictionary = max_hum.to_dict()

# dictionary = {'NSW': 100, 'NT': 70, 'QLD': 99, 'SA': 84, 'VIC': 98, 'WA': 89}

for key in dictionary:
  print(key, ": ", dictionary[key])