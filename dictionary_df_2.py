import pandas as pd

df = pd.DataFrame({'Zoekterm':['met ballen'],'Mogelijke Bias': ['Vrouwen']})

dictionary = {"Zoekterm":['met ballen']}


df['Zoekterm_nieuw(New column)'] = df['Zoekterm'].map(dictionary).fillna(df['Zoekterm'])



print(df)