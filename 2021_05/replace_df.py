# https://stackoverflow.com/questions/67570399/for-a-dataframe-column-how-to-replace-all-the-unnormal-values-to-nan/67570540#67570540

import pandas as pd
import numpy as np

df_d = {'workclass':['@','Private','?','Fedra-gov','_','-','lgbt identity']}
df = pd.DataFrame(data=df_d)

d = {'name':'Contact', 'religion':'Behavioral', 'lgbt':'Identity'}

keys = [*d.keys()]

print(df)

df['workclass'] = df['workclass'].replace(to_replace = '\@|\?' , value=np.NaN, regex = True)

print(df)