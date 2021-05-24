# https://stackoverflow.com/questions/67524027/df-column-values-replace-fxn/67524081#67524081

import pandas as pd

df_d = {'Element':['customer full name','full name','name','religion','account number','lgbt','lgbt identity']}
df = pd.DataFrame(data=df_d)

d = {'name':'Contact', 'religion':'Behavioral', 'lgbt':'Identity'}

keys = [*d.keys()]

# df['Match'] = df['Element'].apply(lambda x: d[x] if x in keys else '' )

df = df.replace(to_replace = ['customer fdaf name'], value = 'BALLS')

print(df)