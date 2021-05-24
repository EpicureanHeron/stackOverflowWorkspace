# https://stackoverflow.com/questions/67505780/if-column-value-contains-dictionary-key-populate-other-column-value-with-diction/67505969#67505969

import pandas as pd

df_d = {'Element':['customer full name','full name','name','religion','account number','lgbt','lgbt identity']}
df = pd.DataFrame(data=df_d)

d = {'name':'Contact', 'religion':'Behavioral', 'lgbt':'Identity'}

keys = [*d.keys()]

df['Match'] = df['Element'].apply(lambda x: d[x] if x in keys else '' )

print(df)